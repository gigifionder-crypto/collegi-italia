#!/usr/bin/env bash
# Compila l'OPERA INTEGRALE E OMNICOMPRENSIVA in tomi.
# Uso: compila_integrale.sh <cartella_uscita>
set -euo pipefail
cd "$(dirname "$0")/.."
U="${1:?serve la cartella di uscita}"; mkdir -p "$U"
python3 _monografia/assembla_integrale.py
python3 - "$U" <<'PY'
import json, subprocess, sys, hashlib
from pathlib import Path
U = Path(sys.argv[1]); INT = Path("_integrale")
man = json.loads((INT / "manifesto-tomi.json").read_text(encoding="utf-8"))["tomi"]
righe, tot = [], 0
for t in man:
    md = INT / t["file"]
    base = md.stem
    html, grezzo, pdf = U / f"{base}.html", U / f"{base}.grezzo.pdf", U / f"{base}.pdf"
    subprocess.run(["node", "_verifiche/generatori/p_opera.js", str(md), str(html)], check=True)
    subprocess.run(["node", "_verifiche/generatori/pdf_opera.js", str(html), str(grezzo)], check=True)
    subprocess.run(["python3", "_verifiche/generatori/sigilla_pdf.py", str(grezzo), str(md), str(pdf),
                    f"--titolo=Opera Nera — Tomo {t['tomo']}: {t['titolo']}",
                    "--senza-lato"], check=True)
    grezzo.unlink(); html.unlink()
    from pypdf import PdfReader
    pag = len(PdfReader(pdf).pages)
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    t["pagine"] = pag; tot += pag
    righe += [f"{sha(pdf)}  {pdf.name}", f"{sha(md)}  {md.name}"]
    print(f"  tomo {t['tomo']:2d}: {pag:5d} pagine  {pdf.stat().st_size/1048576:6.2f} MiB  {t['titolo']}")
(INT / "manifesto-tomi.json").write_text(json.dumps({"tomi": man, "pagine_totali": tot}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
Path("_integrale/IMPRONTE.sha256").write_text(
    "# Impronte dell'Opera integrale e omnicomprensiva, tomo per tomo.\n#\n"
    "# La compilazione e' RIPRODUCIBILE: le date dei PDF sono fissate, non\n"
    "# prese dall'orologio. Per ricalcolarle, dal repository:\n"
    "#     _monografia/compila_integrale.sh <cartella>\n"
    "#     sha256sum <cartella>/*.pdf\n#\n"
    "# Per ogni tomo: prima il PDF, poi il markdown da cui e' composto.\n"
    + "\n".join(righe) + "\n", encoding="utf-8")
print(f"\nTOTALE {tot} pagine in {len(man)} tomi")
PY
