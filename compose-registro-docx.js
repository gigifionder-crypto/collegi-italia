const fs = require('fs');
const { Document, Packer, Paragraph, Table, TableRow, TableCell, TextRun, WidthType, BorderStyle, HeadingLevel } = require('docx');

// Helper to create table cell
const tableCell = (text, bold = false, width = 50) => {
  return new TableCell({
    width: { size: width, type: WidthType.PERCENTAGE },
    children: [new Paragraph(bold ? { text, bold: true } : text)]
  });
};

// Helper to create table row
const tableRow = (cellsArray) => {
  return new TableRow({
    cells: cellsArray
  })
};

const docElements = [];

// Title
docElements.push(
  new Paragraph({
    text: 'Registro PEC e canali di contatto — agosto 2026',
    heading: HeadingLevel.HEADING_1,
    spacing: { after: 200 }
  })
);

docElements.push(
  new Paragraph({
    text: 'Tutti i destinatari del dossier di diffusione, con tipo di canale, recapito verificato, e grado della verifica dichiarato.',
    spacing: { after: 100 }
  })
);

docElements.push(
  new Paragraph({
    text: 'Compilato il 26 agosto 2026 alle 12:45 CET.',
    spacing: { after: 400 }
  })
);

// Section: Ondata 0
docElements.push(
  new Paragraph({
    text: 'Ondata 0 — invii immediati (non in concorrenza)',
    heading: HeadingLevel.HEADING_2,
    spacing: { after: 200 }
  })
);

// Archivio Flamigni
docElements.push(
  new Paragraph({
    text: 'Centro documentazione Archivio «Flamigni» ETS',
    heading: HeadingLevel.HEADING_3,
    spacing: { after: 100 }
  })
);

const table1 = new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  rows: [
    tableRow([tableCell('Tipo di canale', true, 30), tableCell('Posta elettronica certificata (PEC)', false, 70)]),
    tableRow([tableCell('Indirizzo PEC', true, 30), tableCell('Da ricercare — non ancora accertato', false, 70)]),
    tableRow([tableCell('Metodi di ricerca', true, 30), tableCell('RUNTS; INI-PEC; sito archivioflamigni.org', false, 70)]),
    tableRow([tableCell('Indirizzo cartaceo', true, 30), tableCell('Piazza Bartolomeo Romano 6, 00154 Roma', false, 70)]),
    tableRow([tableCell('Grado di verifica', true, 30), tableCell('Accertato che non è stato accertato', false, 70)])
  ]
});

docElements.push(table1);
docElements.push(new Paragraph({ text: '', spacing: { after: 200 } }));

// Fondazione Aldo Moro
docElements.push(
  new Paragraph({
    text: 'Fondazione Aldo Moro',
    heading: HeadingLevel.HEADING_3,
    spacing: { after: 100 }
  })
);

const table2 = new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  rows: [
    tableRow([tableCell('Tipo di canale', true, 30), tableCell('Posta elettronica ordinaria', false, 70)]),
    tableRow([tableCell('Sede legale', true, 30), tableCell('via dei Gracchi 29/B, 00192 Roma', false, 70)]),
    tableRow([tableCell('Presidente', true, 30), tableCell('prof. Renato Moro', false, 70)]),
    tableRow([tableCell('Segretario-tesoriere', true, 30), tableCell('dott. Luigi Mandolesi', false, 70)]),
    tableRow([tableCell('Indirizzo email', true, 30), tableCell('Da ricercare prima dell\'invio', false, 70)]),
    tableRow([tableCell('Grado di verifica', true, 30), tableCell('Indirizzo sede verificato; email da ricercare', false, 70)])
  ]
});

docElements.push(table2);
docElements.push(new Paragraph({ text: '', spacing: { after: 200 } }));

// Zenodo
docElements.push(
  new Paragraph({
    text: 'Zenodo',
    heading: HeadingLevel.HEADING_3,
    spacing: { after: 100 }
  })
);

const table3 = new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  rows: [
    tableRow([tableCell('Tipo di canale', true, 30), tableCell('Deposito digitale con HTTPS', false, 70)]),
    tableRow([tableCell('URL', true, 30), tableCell('https://zenodo.org', false, 70)]),
    tableRow([tableCell('Grado di verifica', true, 30), tableCell('Verificato', false, 70)])
  ]
});

docElements.push(table3);
docElements.push(new Paragraph({ text: '', spacing: { after: 400 } }));

// Ondata 1
docElements.push(
  new Paragraph({
    text: 'Ondata 1 — editori generici (modulo online o email)',
    heading: HeadingLevel.HEADING_2,
    spacing: { after: 200 }
  })
);

const editors1 = [
  { name: 'il Mulino', channel: 'Modulo web', contact: 'sito editore' },
  { name: 'Chiarelettere', channel: 'Email ordinaria o modulo', contact: 'proposte.editoriali@chiarelettere.it' },
  { name: 'Carocci', channel: 'Modulo web', contact: 'sito editore' }
];

for (const ed of editors1) {
  docElements.push(
    new Paragraph({
      text: ed.name,
      heading: HeadingLevel.HEADING_3,
      spacing: { after: 100 }
    })
  );

  const edTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      tableRow([tableCell('Tipo di canale', true, 30), tableCell(ed.channel, false, 70)]),
      tableRow([tableCell('Contatto', true, 30), tableCell(ed.contact, false, 70)]),
      tableRow([tableCell('Grado', true, 30), tableCell('Verificato', false, 70)])
    ]
  });

  docElements.push(edTable);
  docElements.push(new Paragraph({ text: '', spacing: { after: 200 } }));
}

// Ondata 2
docElements.push(
  new Paragraph({
    text: 'Ondata 2 — editori con tempi lunghi',
    heading: HeadingLevel.HEADING_2,
    spacing: { after: 200 }
  })
);

docElements.push(
  new Paragraph({
    text: 'Laterza',
    heading: HeadingLevel.HEADING_3,
    spacing: { after: 100 }
  })
);

const tableL = new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  rows: [
    tableRow([tableCell('Tipo di canale', true, 30), tableCell('Posta cartacea', false, 70)]),
    tableRow([tableCell('Indirizzo Roma', true, 30), tableCell('via di Villa Sacchetti 17, 00197 Roma', false, 70)]),
    tableRow([tableCell('Indirizzo Bari', true, 30), tableCell('piazza Umberto I 54, 70121 Bari', false, 70)]),
    tableRow([tableCell('Grado', true, 30), tableCell('Verificato', false, 70)])
  ]
});

docElements.push(tableL);
docElements.push(new Paragraph({ text: '', spacing: { after: 400 } }));

// Ondata 3
docElements.push(
  new Paragraph({
    text: 'Ondata 3 — editori che valutano l\'opera',
    heading: HeadingLevel.HEADING_2,
    spacing: { after: 200 }
  })
);

const editors3 = [
  { name: 'Bompiani', channel: 'Modulo web', contact: 'manoscritti.bompiani.it' },
  { name: 'Einaudi', channel: 'Email ordinaria', contact: 'einaudi@einaudi.it' }
];

for (const ed of editors3) {
  docElements.push(
    new Paragraph({
      text: ed.name,
      heading: HeadingLevel.HEADING_3,
      spacing: { after: 100 }
    })
  );

  const edTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      tableRow([tableCell('Tipo di canale', true, 30), tableCell(ed.channel, false, 70)]),
      tableRow([tableCell('Contatto', true, 30), tableCell(ed.contact, false, 70)]),
      tableRow([tableCell('Grado', true, 30), tableCell('Verificato', false, 70)])
    ]
  });

  docElements.push(edTable);
  docElements.push(new Paragraph({ text: '', spacing: { after: 200 } }));
}

// Summary table
docElements.push(
  new Paragraph({
    text: 'Tabella sinottica dei destinatari',
    heading: HeadingLevel.HEADING_2,
    spacing: { after: 200 }
  })
);

const summaryTable = new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  rows: [
    tableRow([
      tableCell('#', true, 8),
      tableCell('Destinatario', true, 22),
      tableCell('Canale', true, 22),
      tableCell('Contatto', true, 25),
      tableCell('Grado', true, 23)
    ]),
    tableRow([tableCell('0', false, 8), tableCell('Archivio Flamigni', false, 22), tableCell('PEC', false, 22), tableCell('da ricercare', false, 25), tableCell('incerto', false, 23)]),
    tableRow([tableCell('0-bis', false, 8), tableCell('Fondazione Aldo Moro', false, 22), tableCell('Email', false, 22), tableCell('da ricercare', false, 25), tableCell('parziale', false, 23)]),
    tableRow([tableCell('1', false, 8), tableCell('il Mulino', false, 22), tableCell('Modulo web', false, 22), tableCell('sito editore', false, 25), tableCell('verificato', false, 23)]),
    tableRow([tableCell('2', false, 8), tableCell('Chiarelettere', false, 22), tableCell('Email', false, 22), tableCell('proposte.editoriali@', false, 25), tableCell('verificato', false, 23)]),
    tableRow([tableCell('3', false, 8), tableCell('Carocci', false, 22), tableCell('Modulo web', false, 22), tableCell('sito editore', false, 25), tableCell('verificato', false, 23)]),
    tableRow([tableCell('4', false, 8), tableCell('Laterza', false, 22), tableCell('Posta', false, 22), tableCell('Roma / Bari', false, 25), tableCell('verificato', false, 23)]),
    tableRow([tableCell('5', false, 8), tableCell('Bompiani', false, 22), tableCell('Modulo web', false, 22), tableCell('sito editore', false, 25), tableCell('verificato', false, 23)]),
    tableRow([tableCell('6', false, 8), tableCell('Einaudi', false, 22), tableCell('Email', false, 22), tableCell('einaudi@einaudi.it', false, 25), tableCell('verificato', false, 23)]),
    tableRow([tableCell('10', false, 8), tableCell('Zenodo', false, 22), tableCell('HTTPS', false, 22), tableCell('zenodo.org', false, 25), tableCell('verificato', false, 23)])
  ]
});

docElements.push(summaryTable);
docElements.push(new Paragraph({ text: '', spacing: { after: 400 } }));

// Verifiche
docElements.push(
  new Paragraph({
    text: 'Verifiche ancora da completare — prima dell\'invio',
    heading: HeadingLevel.HEADING_2,
    spacing: { after: 200 }
  })
);

const checks = [
  'Archivio Flamigni: ricerca PEC su RUNTS, INI-PEC, sito archivioflamigni.org',
  'Fondazione Aldo Moro: ricerca email istituzionale',
  'Feltrinelli: verifica dello stato attuale',
  'Bollati Boringhieri: conferma assenza canale diretto',
  'Italia contemporanea: identificazione redazione',
  'Edizione Nazionale Moro: ricerca indirizzo email presso Università Bologna'
];

for (const check of checks) {
  docElements.push(
    new Paragraph({
      text: `• ${check}`,
      spacing: { before: 50, after: 50 }
    })
  );
}

// Final grado
docElements.push(new Paragraph({ text: '', spacing: { after: 300 } }));
docElements.push(
  new Paragraph({
    text: 'Grado della verifica complessiva',
    heading: HeadingLevel.HEADING_2,
    spacing: { after: 200 }
  })
);

docElements.push(
  new Paragraph({
    text: '26 agosto 2026, 12:45 CET',
    spacing: { after: 100 },
    bold: true
  })
);

docElements.push(
  new Paragraph({
    text: 'Verificati: il Mulino, Carocci, Bompiani, Chiarelettere, Laterza, Einaudi, Zenodo.',
    spacing: { after: 100 }
  })
);

docElements.push(
  new Paragraph({
    text: 'Parzialmente verificati: Archivio Flamigni (esiste, PEC non accertato); Fondazione Aldo Moro (indirizzo sede legale noto, email da ricercare).',
    spacing: { after: 100 }
  })
);

docElements.push(
  new Paragraph({
    text: 'Incerti: Feltrinelli e Bollati Boringhieri (siti non raggiungibili dall\'ambiente di ricerca).',
    spacing: { after: 200 }
  })
);

docElements.push(
  new Paragraph({
    text: 'Nessuna informazione è "silenziosamente" scaduta. Si verifichi il giorno dell\'invio.',
    spacing: { after: 200 },
    italics: true
  })
);

// Create and save document
const doc = new Document({
  sections: [{
    properties: {},
    children: docElements
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad/REGISTRO_PEC_E_CANALI.docx', buffer);
  console.log('DOCX saved: REGISTRO_PEC_E_CANALI.docx');
});
