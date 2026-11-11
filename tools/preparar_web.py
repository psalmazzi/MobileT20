#!/usr/bin/env python3
"""Copia o index.html do app para web/ e injeta o manifesto (PWA) e o registro do service worker.
Uso: python3 tools/preparar_web.py caminho/para/index.html"""
import sys, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
html = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
cab = ('<link rel="manifest" href="manifest.webmanifest">\n'
       '<link rel="apple-touch-icon" href="icons/icon-192.png">\n</head>')
reg = ('<script>if("serviceWorker" in navigator && /github\\.io$/.test(location.hostname))'
       'navigator.serviceWorker.register("sw.js").catch(function(){});</script>\n</body>')
assert "</head>" in html and "</body>" in html
html = html.replace("</head>", cab, 1)
html = html[::-1].replace("</body>"[::-1], reg[::-1], 1)[::-1]
(raiz / "web" / "index.html").write_text(html, encoding="utf-8")
print("web/index.html atualizado", len(html.encode()) // 1024, "KB")
