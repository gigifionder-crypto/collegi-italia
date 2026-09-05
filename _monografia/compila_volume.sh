#!/usr/bin/env bash
# Compila l'OPERA in UN SOLO VOLUME: la guida e poi tutte le 154 parti.
# Uso: compila_volume.sh <cartella_uscita>
set -euo pipefail
cd "$(dirname "$0")/.."
U="${1:?serve la cartella di uscita}"; mkdir -p "$U"
MD=_integrale/opera-nera-volume-unico.md
python3 _monografia/assembla_integrale.py --unico
node _verifiche/generatori/p_opera.js "$MD" "$U/volume.html"
node _verifiche/generatori/pdf_opera.js "$U/volume.html" "$U/volume.grezzo.pdf"
python3 _verifiche/generatori/sigilla_pdf.py "$U/volume.grezzo.pdf" "$MD" \
  "$U/OPERA-NERA-volume-unico.pdf" \
  "--titolo=Opera Nera — Il Secolo Nero della Bella Europa (volume unico)" --senza-lato
rm -f "$U/volume.grezzo.pdf" "$U/volume.html"
{ echo "# Impronte del volume unico. La compilazione e' RIPRODUCIBILE:"
  echo "# le date del PDF sono fissate, non prese dall'orologio."
  echo "#     _monografia/compila_volume.sh <cartella>"
  echo "#     sha256sum <cartella>/OPERA-NERA-volume-unico.pdf"
  echo "# Prima il PDF, poi il markdown da cui e' composto."
  sha256sum "$U/OPERA-NERA-volume-unico.pdf" | sed 's#  .*/#  #'
  sha256sum "$MD" | sed 's#  .*/#  #'
} > _integrale/IMPRONTA-VOLUME.sha256
python3 - "$U/OPERA-NERA-volume-unico.pdf" <<'PY'
import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
o = r.trailer["/Root"].get("/Outlines")
print(f"volume unico: {len(r.pages)} pagine · {o.get('/Count') if o else 0} segnalibri")
PY
