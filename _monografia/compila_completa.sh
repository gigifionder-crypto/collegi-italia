#!/usr/bin/env bash
# Compila la MONOGRAFIA COMPLETA: il volume unico seguito dagli undici tomi.
# Uso: compila_completa.sh <cartella_uscita>
set -euo pipefail
cd "$(dirname "$0")/.."
U="${1:?serve la cartella di uscita}"; mkdir -p "$U"
MD=_integrale/opera-nera-monografia-completa.md
python3 _monografia/assembla_integrale.py            # i tomi
python3 _monografia/assembla_integrale.py --unico    # il volume
python3 _monografia/assembla_integrale.py --completa # i due insieme
node _verifiche/generatori/p_opera.js "$MD" "$U/completa.html"
node _verifiche/generatori/pdf_opera.js "$U/completa.html" "$U/completa.grezzo.pdf"
python3 _verifiche/generatori/sigilla_pdf.py "$U/completa.grezzo.pdf" "$MD" \
  "$U/OPERA-NERA-monografia-completa.pdf" \
  "--titolo=Opera Nera — monografia completa: il volume unico e gli undici tomi" --senza-lato
rm -f "$U/completa.grezzo.pdf" "$U/completa.html"
{ echo "# Impronte della monografia completa (volume unico + undici tomi)."
  echo "# Riproducibile: date fisse, ricompressione deterministica."
  echo "#     _monografia/compila_completa.sh <cartella>"
  echo "# Prima il PDF, poi il markdown da cui e' composto."
  sha256sum "$U/OPERA-NERA-monografia-completa.pdf" | sed 's#  .*/#  #'
  sha256sum "$MD" | sed 's#  .*/#  #'
} > _integrale/IMPRONTA-COMPLETA.sha256
