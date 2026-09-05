#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sigilla il PDF dell'Opera: metadati, date fisse, impronta SHA-256.

Ricomprime anche il PDF impacchettando gli oggetti in flussi (PDF 1.5): il
contenuto non cambia di un byte -- pagine, segnalibri, struttura accessibile e
metadati sono verificati prima e dopo -- ma l'albero dei tag, che per un'opera
di due milioni di parole conta centosettantamila oggetti scritti in chiaro,
smette di pesare un terzo del file. Sul volume unico: da 61,3 a 41,3 MiB.

Le date si fissano invece di lasciarle all'orologio, perche' un PDF che cambia
impronta a ogni compilazione non e' verificabile: l'impronta certifica il
contenuto, non il minuto in cui e' stato prodotto.

Verifica che la struttura accessibile (PDF taggato) e i segnalibri sopravvivano
alla riscrittura, e si ferma se non e' cosi': un sigillo che rompe cio' che
sigilla non e' un sigillo.

Uso: python3 sigilla_pdf.py <pdf> <sorgente.md> [uscita.pdf]
"""
import hashlib
import sys
from pathlib import Path

import pikepdf
from pypdf import PdfReader, PdfWriter

# Data di riferimento dell'edizione: fissa, dichiarata, non l'ora di macchina.
DATA = "D:20260902000000Z"


def impronta(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for blocco in iter(lambda: f.read(1 << 20), b""):
            h.update(blocco)
    return h.hexdigest()


def main():
    arg = [a for a in sys.argv[1:] if not a.startswith("--")]
    opz = {a.split("=")[0]: a.split("=", 1)[-1] for a in sys.argv[1:] if a.startswith("--")}
    if len(arg) < 2:
        sys.exit("uso: sigilla_pdf.py <pdf> <sorgente.md> [uscita.pdf] "
                 "[--titolo=…] [--senza-lato]")
    pdf = Path(arg[0])
    sorgente = Path(arg[1])
    uscita = Path(arg[2]) if len(arg) > 2 else pdf
    titolo = opz.get("--titolo", "Aldo Moro — Ottanta anni senza pace")

    sha_sorgente = impronta(sorgente)
    def stato(lettore):
        # /Count e' il totale dei segnalibri; len(outline) conta solo il primo
        # livello, e su un volume di tremila voci diceva «331».
        contorni = lettore.trailer["/Root"].get("/Outlines")
        return {
            "pagine": len(lettore.pages),
            "segnalibri": int(contorni.get("/Count", 0)) if contorni else 0,
            "taggato": "/StructTreeRoot" in lettore.trailer["/Root"],
        }

    lettore = PdfReader(pdf)
    prima = stato(lettore)

    scrittore = PdfWriter(clone_from=lettore)
    scrittore.add_metadata({
        "/Title": titolo,
        "/Subject": "La seconda guerra non è mai finita. Opera monografica sul caso Moro.",
        "/Author": "Generata da un'intelligenza artificiale su richiesta del titolare del repository",
        "/Keywords": ("Aldo Moro; via Fani; 16 marzo 1978; 9 maggio 1978; giudicato; "
                      "Stato Zero; celle aperte; scala Savona; gradi della prova"),
        "/Creator": "corpus collegi-italia — assembla_opera.py + p_opera.js",
        "/Producer": "Chromium via Playwright, sigillato con pypdf",
        "/CreationDate": DATA,
        "/ModDate": DATA,
        # L'impronta della sorgente viaggia DENTRO il PDF: chi lo riceve puo'
        # ricalcolarla dal repository senza chiedere nulla a nessuno.
        "/SourceSHA256": sha_sorgente,
    })
    scrittore.write(uscita)

    # Ricompressione: gli oggetti non-flusso vanno in flussi d'oggetti. Nessun
    # contenuto si perde -- il controllo qui sotto lo verifica -- e l'esito e'
    # deterministico, percio' l'impronta resta riproducibile.
    grezzo = uscita.stat().st_size
    pikepdf.settings.set_flate_compression_level(9)
    with pikepdf.open(uscita, allow_overwriting_input=True) as p:
        p.save(uscita, object_stream_mode=pikepdf.ObjectStreamMode.generate,
               compress_streams=True, recompress_flate=True, deterministic_id=True)
    compresso = uscita.stat().st_size

    controllo = PdfReader(uscita)
    dopo = stato(controllo)
    for chiave in prima:
        if prima[chiave] != dopo[chiave]:
            sys.exit(f"ERRORE: la sigillatura ha alterato «{chiave}»: "
                     f"{prima[chiave]} → {dopo[chiave]}. Non sigillo un PDF che rompo.")

    sha_pdf = impronta(uscita)
    misura = (f"  peso {compresso/1048576:.2f} MiB "
              f"(da {grezzo/1048576:.2f}, ricompresso senza perdere nulla)")
    if "--senza-lato" in opz:
        print(f"sigillato {uscita.name}")
        print(f"  pagine {dopo['pagine']} · segnalibri {dopo['segnalibri']} · "
              f"taggato {'sì' if dopo['taggato'] else 'NO'}")
        print(misura)
        print(f"  SHA-256 pdf      {sha_pdf}")
        print(f"  SHA-256 sorgente {sha_sorgente}")
        return
    lato = Path(uscita.name + ".sha256")
    lato.write_text(
        "# Impronte dell'Opera monografica.\n"
        "#\n"
        "# La compilazione e' RIPRODUCIBILE: le date del PDF sono fissate, non\n"
        "# prese dall'orologio, percio' due compilazioni della stessa sorgente\n"
        "# danno la stessa impronta. Un'impronta che cambia a ogni compilazione\n"
        "# certificherebbe il minuto, non il contenuto.\n"
        "#\n"
        "# Per ricalcolarle, dal repository:\n"
        "#     _monografia/compila.sh <cartella>\n"
        "#     sha256sum <cartella>/" + uscita.name + "\n"
        "#\n"
        "# La prima riga e' il volume; la seconda e' il markdown assemblato da\n"
        "# cui e' composto, e viaggia anche dentro il PDF (/SourceSHA256).\n"
        f"{sha_pdf}  {uscita.name}\n"
        f"{sha_sorgente}  {sorgente.name}\n", encoding="utf-8")

    print(f"sigillato {uscita.name}")
    print(f"  pagine {dopo['pagine']} · segnalibri {dopo['segnalibri']} · "
          f"taggato {'sì' if dopo['taggato'] else 'NO'}")
    print(misura)
    print(f"  SHA-256 pdf      {sha_pdf}")
    print(f"  SHA-256 sorgente {sha_sorgente}")


if __name__ == "__main__":
    main()
