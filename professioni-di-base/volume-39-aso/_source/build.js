const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  Header, Footer, PageNumber, FootnoteReferenceRun, PageBreak,
  convertInchesToTwip, VerticalAlign
} = require("docx");

const content = JSON.parse(fs.readFileSync(path.join(__dirname, "content.json"), "utf8"));

const NAVY = "16264B";
const GOLD = "C49A48";
const CREAM = "FDFBF7";
const FONT = "Barlow Semicondensed";

// footnotes: build docx-js footnotes map, and a text-splitter that emits FootnoteReferenceRun
const footnoteIndexByMarker = {}; // "1" -> docx footnote id key
const footnotesForDocx = {};
content.footnotes.forEach((text, i) => {
  const key = i + 1;
  footnotesForDocx[key] = {
    children: [new Paragraph({ children: [new TextRun({ text, font: FONT, size: 18 })] })]
  };
  footnoteIndexByMarker[String(i + 1)] = key;
});

function runsFromText(str, opts = {}) {
  // splits "text [^1] more text [^2]" into TextRun + FootnoteReferenceRun sequence
  const parts = str.split(/\[\^(\d+)\]/g);
  const runs = [];
  for (let i = 0; i < parts.length; i++) {
    if (i % 2 === 0) {
      if (parts[i]) runs.push(new TextRun({ text: parts[i], font: FONT, size: 22, ...opts }));
    } else {
      const key = footnoteIndexByMarker[parts[i]];
      if (key) runs.push(new FootnoteReferenceRun(key));
    }
  }
  if (runs.length === 0) runs.push(new TextRun({ text: "", font: FONT, size: 22, ...opts }));
  return runs;
}

function bodyPara(str, opts = {}) {
  return new Paragraph({
    children: runsFromText(str, opts),
    spacing: { after: 200, line: 300 },
    alignment: AlignmentType.JUSTIFIED
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 480, after: 240 },
    children: [new TextRun({ text, font: FONT, bold: true, color: NAVY, size: 32 })]
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 360, after: 200 },
    children: [new TextRun({ text, font: FONT, bold: true, color: NAVY, size: 26 })]
  });
}
function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 280, after: 160 },
    children: [new TextRun({ text, font: FONT, bold: true, color: GOLD, size: 24 })]
  });
}

function cellShaded(text, { header = false, width = 2000, bold = false } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: header ? { type: ShadingType.CLEAR, color: "auto", fill: NAVY } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 100, bottom: 100, left: 120, right: 120 },
    children: [new Paragraph({
      children: [new TextRun({
        text, font: FONT, size: 20, bold: header || bold,
        color: header ? "FFFFFF" : "1A1A1A"
      })]
    })]
  });
}

function buildDashboard() {
  const widths = [4200, 2600, 2600];
  const headerRow = new TableRow({
    tableHeader: true,
    children: [
      cellShaded("Indicatore", { header: true, width: widths[0] }),
      cellShaded("Valore", { header: true, width: widths[1] }),
      cellShaded("Fonte", { header: true, width: widths[2] })
    ]
  });
  const rows = content.dashboard.map(d => new TableRow({
    children: [
      cellShaded(d.label, { width: widths[0] }),
      cellShaded(d.value, { width: widths[1], bold: true }),
      cellShaded(d.fonte, { width: widths[2] })
    ]
  }));
  return new Table({
    width: { size: 9400, type: WidthType.DXA },
    columnWidths: widths,
    rows: [headerRow, ...rows]
  });
}

function buildResultsTable(t) {
  const n = t.colonne.length;
  const totalWidth = 9400;
  const widths = n === 3 ? [3400, 3000, 3000] : Array(n).fill(Math.floor(totalWidth / n));
  const headerRow = new TableRow({
    tableHeader: true,
    children: t.colonne.map((c, i) => cellShaded(c, { header: true, width: widths[i] }))
  });
  const rows = t.righe.map(r => new TableRow({
    children: r.map((c, i) => cellShaded(c, { width: widths[i] }))
  }));
  const elements = [
    new Paragraph({ spacing: { before: 200, after: 120 }, children: [new TextRun({ text: t.titolo, font: FONT, bold: true, color: NAVY, size: 22 })] }),
    new Table({ width: { size: totalWidth, type: WidthType.DXA }, columnWidths: widths, rows: [headerRow, ...rows] })
  ];
  if (t.nota) {
    elements.push(new Paragraph({
      spacing: { before: 120, after: 240 },
      children: [new TextRun({ text: t.nota, font: FONT, italics: true, size: 18, color: "555555" })]
    }));
  }
  return elements;
}

function numberedList(items, startAfter = "") {
  return items.map((item, i) => new Paragraph({
    spacing: { after: 160, line: 300 },
    alignment: AlignmentType.JUSTIFIED,
    children: [
      new TextRun({ text: `${i + 1}. `, font: FONT, bold: true, color: GOLD, size: 22 }),
      ...runsFromText(item)
    ]
  }));
}

const children = [];

// --- Cover ---
children.push(
  new Paragraph({ spacing: { before: 1600, after: 200 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: content.meta.opera, font: FONT, color: NAVY, bold: true, size: 44 })] }),
  new Paragraph({ spacing: { after: 400 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: content.meta.volume + " — " + content.meta.figura, font: FONT, color: GOLD, bold: true, size: 32 })] }),
  new Paragraph({ spacing: { after: 1600 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: content.meta.sottotitolo, font: FONT, italics: true, size: 24, color: "333333" })] }),
  new Paragraph({ spacing: { after: 120 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: content.meta.autore, font: FONT, size: 22, color: NAVY })] }),
  new Paragraph({ spacing: { after: 1200 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: content.meta.data, font: FONT, size: 20, color: "555555" })] }),
  new Paragraph({ children: [new PageBreak()] })
);

// --- Nota editoriale ---
children.push(h1("Nota editoriale"));
children.push(bodyPara(content.notaEditoriale));
children.push(new Paragraph({ children: [new PageBreak()] }));

// --- Funnel: Dashboard ---
children.push(h1("Dashboard"));
children.push(buildDashboard());
children.push(new Paragraph({ text: "", spacing: { after: 300 } }));

// --- Executive summary ---
children.push(h1("Executive summary"));
children.push(bodyPara(content.executiveSummary));

// --- 5 key findings ---
children.push(h2("Cinque risultati chiave"));
children.push(...numberedList(content.keyFindings));

// --- Raccomandazioni ---
children.push(h2("Raccomandazioni"));
children.push(...numberedList(content.raccomandazioni));
children.push(new Paragraph({ children: [new PageBreak()] }));

// --- Chapters ---
content.capitoli.forEach(cap => {
  children.push(h1(`Capitolo ${cap.numero}. ${cap.titolo}`));
  if (cap.tabelle) {
    cap.tabelle.forEach(t => { children.push(...buildResultsTable(t)); });
  }
  cap.paragrafi.forEach(p => {
    children.push(h3(p.heading));
    p.testo.forEach(par => children.push(bodyPara(par)));
  });
});

// --- Appendici ---
children.push(h1("Appendici registrate"));
content.appendici.forEach(a => {
  children.push(h2(`Appendice ${a.lettera}. ${a.titolo}`));
  children.push(bodyPara(a.testo));
});

const doc = new Document({
  creator: content.meta.autore,
  title: `${content.meta.opera} — ${content.meta.volume} — ${content.meta.figura}`,
  description: content.meta.sottotitolo,
  footnotes: footnotesForDocx,
  styles: {
    default: {
      document: { run: { font: FONT, size: 22, color: "1A1A1A" } }
    }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4 in DXA
        margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ text: content.meta.header, font: FONT, size: 16, color: GOLD, bold: true })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Pagina ", font: FONT, size: 16, color: NAVY }),
            new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: NAVY }),
            new TextRun({ text: " di ", font: FONT, size: 16, color: NAVY }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 16, color: NAVY })
          ]
        })]
      })
    },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(path.join(__dirname, "volume-39-aso.docx"), buf);
  console.log("Written volume-39-aso.docx", buf.length, "bytes");
});
