#!/usr/bin/env python3
"""Réduit les textures intégrées d'un fichier FBX binaire (Mixamo) sans toucher au modèle ni au squelette.

Usage : python3 tools/fbx_shrink.py entree.fbx sortie.fbx [--max 1024] [--gloss 512] [--quality 85]

Le fichier est lu comme un arbre de nœuds FBX (format binaire 7.x), chaque image intégrée (nœud Video/Content)
est redimensionnée et réencodée en JPEG (PNG si elle a une vraie transparence), les noms de fichiers sont
mis à jour, puis l'arbre est réécrit avec des décalages recalculés et un pied de fichier conforme.
Nécessite : Pillow.
"""
import io, struct, sys, argparse
from PIL import Image

MAGIC = b'Kaydara FBX Binary  \x00'

class Node:
    __slots__ = ('name', 'props', 'children', 'sentinel')
    def __init__(self, name, props, children, sentinel):
        self.name, self.props, self.children, self.sentinel = name, props, children, sentinel

def read_prop(d, p):
    t = chr(d[p]); p += 1
    if t == 'Y': return (t, d[p:p+2]), p + 2
    if t == 'C': return (t, d[p:p+1]), p + 1
    if t in 'IF': return (t, d[p:p+4]), p + 4
    if t in 'DL': return (t, d[p:p+8]), p + 8
    if t in 'fdlib':
        alen, enc, clen = struct.unpack_from('<III', d, p)
        return (t, d[p:p+12+clen]), p + 12 + clen
    if t in 'SR':
        ln, = struct.unpack_from('<I', d, p)
        return (t, bytes(d[p+4:p+4+ln])), p + 4 + ln
    raise ValueError('type de propriété inconnu %r à %d' % (t, p - 1))

def read_node(d, p, wide):
    if wide:
        end, nprops, plen = struct.unpack_from('<QQQ', d, p); p += 24
    else:
        end, nprops, plen = struct.unpack_from('<III', d, p); p += 12
    nlen = d[p]; p += 1
    if end == 0:
        return None, p
    name = bytes(d[p:p+nlen]).decode('latin-1'); p += nlen
    props = []
    for _ in range(nprops):
        pr, p = read_prop(d, p); props.append(pr)
    children, sentinel = [], False
    while p < end:
        ch, p = read_node(d, p, wide)
        if ch is None:
            sentinel = True; break
        children.append(ch)
    if p != end:
        raise ValueError('nœud %s : fin attendue %d, obtenue %d' % (name, end, p))
    return Node(name, props, children, sentinel), p

def enc_prop(pr):
    t, v = pr
    if t in 'SR':
        return t.encode() + struct.pack('<I', len(v)) + v
    return t.encode() + bytes(v)

def write_node(out, n, wide):
    props = b''.join(enc_prop(pr) for pr in n.props)
    name = n.name.encode('latin-1')
    hdr = 25 if wide else 13
    start = len(out)
    head_len = (24 if wide else 12) + 1 + len(name)
    out += b'\0' * head_len
    out += props
    for ch in n.children:
        write_node(out, ch, wide)
    if n.sentinel:
        out += b'\0' * hdr
    end = len(out)
    if wide:
        struct.pack_into('<QQQ', out, start, end, len(n.props), len(props))
    else:
        struct.pack_into('<III', out, start, end, len(n.props), len(props))
    out[start + (24 if wide else 12)] = len(name)
    out[start + (25 if wide else 13): start + head_len] = name

def parse(data):
    if not data.startswith(MAGIC):
        raise ValueError('ce n’est pas un FBX binaire')
    version, = struct.unpack_from('<I', data, 23)
    wide = version >= 7500
    p, nodes = 27, []
    while True:
        n, p = read_node(data, p, wide)
        if n is None:
            break
        nodes.append(n)
    return version, wide, nodes, data[p:]

def serialize(version, wide, nodes, footer_src):
    out = bytearray(data_header(version))
    for n in nodes:
        write_node(out, n, wide)
    out += b'\0' * (25 if wide else 13)
    # pied de fichier : identifiant (16 o), 4 octets nuls, alignement sur 16, version, 120 octets nuls, signature (16 o)
    fid = footer_src[:16] if len(footer_src) >= 16 else b'\xfa\xbc\xab\x09\xd0\xc8\xd4\x66\xb1\x76\xfb\x83\x1c\xf7\x26\x7e'
    tail = footer_src[-16:] if len(footer_src) >= 16 else b'\xf8\x5a\x8c\x6a\xde\xf5\xd9\x7e\xec\xe9\x0c\xe3\x75\x8f\x29\x0b'
    out += fid + b'\0' * 4
    pad = (16 - len(out) % 16) % 16 or 16
    out += b'\0' * pad
    out += struct.pack('<I', version) + b'\0' * 120 + tail
    return bytes(out)

def data_header(version):
    return MAGIC + b'\x1a\x00' + struct.pack('<I', version)

def walk(nodes):
    for n in nodes:
        yield n
        yield from walk(n.children)

def child(n, name):
    for c in n.children:
        if c.name == name:
            return c
    return None

def shrink_image(raw, fname, mx, gloss, quality):
    im = Image.open(io.BytesIO(raw)); im.load()
    lim = gloss if any(k in fname.lower() for k in ('gloss', 'specular', 'rough', 'metal')) else mx
    if max(im.size) > lim:
        im = im.resize((lim, lim) if im.size[0] == im.size[1] else
                       (lim, int(im.size[1] * lim / im.size[0])) if im.size[0] >= im.size[1] else
                       (int(im.size[0] * lim / im.size[1]), lim), Image.LANCZOS)
    has_alpha = im.mode in ('RGBA', 'LA') and im.getchannel('A').getextrema()[0] < 250
    buf = io.BytesIO()
    if has_alpha:
        im.save(buf, 'PNG', optimize=True); ext = '.png'
    else:
        im.convert('RGB').save(buf, 'JPEG', quality=quality, optimize=True); ext = '.jpg'
    return buf.getvalue(), ext

def rename(s, ext):
    for old in ('.png', '.PNG', '.jpeg', '.JPEG', '.jpg', '.JPG', '.tga', '.TGA'):
        if s.endswith(old.encode()):
            return s[:-len(old)] + ext.encode()
    return s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('dst')
    ap.add_argument('--max', type=int, default=1024)
    ap.add_argument('--gloss', type=int, default=512)
    ap.add_argument('--quality', type=int, default=85)
    a = ap.parse_args()
    data = open(a.src, 'rb').read()
    version, wide, nodes, footer = parse(data)
    renames = {}
    for n in walk(nodes):
        if n.name != 'Video':
            continue
        content = child(n, 'Content')
        fnode = child(n, 'RelativeFilename') or child(n, 'Filename')
        fname = fnode.props[0][1].decode('latin-1', 'replace') if fnode and fnode.props else ''
        if not content or not content.props or content.props[0][0] != 'R' or len(content.props[0][1]) < 64:
            continue
        try:
            img, ext = shrink_image(content.props[0][1], fname, a.max, a.gloss, a.quality)
        except Exception as e:
            print('  image ignorée', fname, e); continue
        print('  %-40s %8.1f Mo -> %6.2f Mo %s' % (fname[-40:], len(content.props[0][1]) / 1e6, len(img) / 1e6, ext))
        content.props[0] = ('R', img)
        base = fname.rsplit('.', 1)[0] if '.' in fname else fname
        renames[base] = ext
    if renames:
        for n in walk(nodes):
            if n.name in ('Video', 'Texture'):
                for c in n.children:
                    if c.name in ('FileName', 'Filename', 'RelativeFilename') and c.props and c.props[0][0] == 'S':
                        s = c.props[0][1]
                        for base, ext in renames.items():
                            if base.encode('latin-1', 'replace') and base.encode('latin-1', 'replace') in s:
                                c.props[0] = ('S', rename(s, ext))
    out = serialize(version, wide, nodes, footer)
    open(a.dst, 'wb').write(out)
    # contrôle : relecture complète
    v2, w2, n2, f2 = parse(out)
    assert len(n2) == len(nodes)
    print('%s : %.1f Mo -> %.1f Mo (version FBX %d, relu sans erreur)' % (a.src, len(data) / 1e6, len(out) / 1e6, version))

if __name__ == '__main__':
    main()
