#!/usr/bin/env bash
# Catena di compilazione dell'Opera, in un solo comando e in quest'ordine.
#   markdown -> html -> pdf (taggato, con segnalibri e numerazione) -> sigillo
# L'ultimo passo fissa le date e scrive l'impronta: senza date fisse
# l'impronta cambierebbe a ogni compilazione e non certificherebbe nulla.
set -euo pipefail
cd "$(dirname "$0")/.."
USCITA="${1:-.}"
MD=aldo-moro-ottanta-anni-senza-pace.md
python3 _monografia/assembla_opera.py
node _verifiche/generatori/p_opera.js "$MD" "$USCITA/opera.html"
node _verifiche/generatori/pdf_opera.js "$USCITA/opera.html" "$USCITA/opera.grezzo.pdf"
python3 _verifiche/generatori/sigilla_pdf.py "$USCITA/opera.grezzo.pdf" "$MD" "$USCITA/${MD%.md}.pdf"
rm -f "$USCITA/opera.grezzo.pdf"
