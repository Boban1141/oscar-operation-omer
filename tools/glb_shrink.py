#!/usr/bin/env python3
"""Réduit les textures d'un modèle .glb (Sketchfab, etc.) pour le jeu.
Usage : python3 tools/glb_shrink.py source.glb destination.glb [--max 512] [--quality 82]
Chaque image est ramenée à --max pixels de côté. Les images opaques passent en JPEG,
celles qui ont de la transparence restent en PNG. Le reste du fichier n'est pas modifié."""
import argparse, io, json, struct
from PIL import Image

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('dst')
    ap.add_argument('--max', type=int, default=512)
    ap.add_argument('--quality', type=int, default=82)
    a = ap.parse_args()
    d = open(a.src, 'rb').read()
    assert d[:4] == b'glTF', 'pas un fichier .glb'
    jl = struct.unpack_from('<I', d, 12)[0]
    js = json.loads(d[20:20 + jl])
    p = 20 + jl
    bl = struct.unpack_from('<I', d, p)[0]
    binc = d[p + 8:p + 8 + bl]
    views = js['bufferViews']
    img_views = {}
    for im in js.get('images', []):
        if 'bufferView' in im:
            img_views[im['bufferView']] = im
    out = bytearray(); newviews = []
    for i, v in enumerate(views):
        raw = binc[v.get('byteOffset', 0):v.get('byteOffset', 0) + v['byteLength']]
        if i in img_views:
            im = img_views[i]; mime0 = im.get('mimeType')
            try:
                pic = Image.open(io.BytesIO(raw)); pic.load()
                if max(pic.size) > a.max:
                    pic.thumbnail((a.max, a.max), Image.LANCZOS)
                alpha = pic.mode in ('RGBA', 'LA') and pic.getchannel('A').getextrema()[0] < 250
                buf = io.BytesIO()
                if alpha:
                    pic.convert('RGBA').save(buf, 'PNG', optimize=True); im['mimeType'] = 'image/png'
                else:
                    pic.convert('RGB').save(buf, 'JPEG', quality=a.quality, optimize=True); im['mimeType'] = 'image/jpeg'
                big = max(Image.open(io.BytesIO(raw)).size) > a.max
                if big or len(buf.getvalue()) < len(raw):
                    raw = buf.getvalue()
                else:
                    im['mimeType'] = mime0
            except Exception as e:
                print('  image gardée telle quelle :', e)
        while len(out) % 4: out.append(0)
        nv = dict(v); nv['byteOffset'] = len(out); nv['byteLength'] = len(raw)
        out += raw; newviews.append(nv)
    while len(out) % 4: out.append(0)
    js['bufferViews'] = newviews
    js['buffers'][0]['byteLength'] = len(out)
    jb = json.dumps(js, separators=(',', ':')).encode()
    while len(jb) % 4: jb += b' '
    total = 12 + 8 + len(jb) + 8 + len(out)
    res = b'glTF' + struct.pack('<II', 2, total) + struct.pack('<I', len(jb)) + b'JSON' + jb + struct.pack('<I', len(out)) + b'BIN\x00' + bytes(out)
    open(a.dst, 'wb').write(res)
    print('%s : %.1f Mo -> %.1f Mo' % (a.src, len(d) / 1e6, len(res) / 1e6))

if __name__ == '__main__':
    main()
