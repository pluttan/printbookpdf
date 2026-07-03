<div align="center">

# printbookpdf

**PDF booklet formatter for double-sided printing**

</div>

Rearranges PDF pages into booklet (signature) order for double-sided printing. Takes any PDF, pads it to a multiple of 4 pages, reorders pages so that when printed double-sided and folded, they form a properly sequenced booklet. Pages on the back of each sheet are rotated 180 degrees so both sides line up correctly.

## ■ Features

- ❖ **Booklet reordering** — pairs the last page with the first, next-to-last with the second, and so on into signature order
- ❖ **Auto-padding** — appends blank Letter-size pages (612×792 pt) to reach a multiple of 4
- ❖ **Page rotation** — rotates two of every four pages 180° so the reverse side prints the right way up
- ❖ **Any input PDF** — works with documents of any page count

## ■ Stack

<div align="center">

| Component | Technology |
|-----------|------------|
| Language | Python |
| PDF | PyPDF2 (`<3.0`, legacy `PdfFileReader` / `PdfFileWriter` API) |

</div>

## ■ How It Works

```
1. Load the input PDF with PyPDF2.
2. Append blank Letter-size pages (612×792 pt) until the page count is a multiple of 4.
3. Reorder pages into signature order: pair the last page with the first, next-to-last with the second, etc.
4. Rotate every second page in each pair 180° so the reverse side of a printed sheet reads correctly.
5. Write the result to the books/ directory as <input-name>.pdf.
```

## ■ Screenshots

<div align="center">

![Screenshot](screenshots/main.png)

*Booklet page reordering result*

</div>

## ■ Usage

```bash
pip install "PyPDF2<3.0"
python printBookPDF.py input.pdf
```

> Note: the output directory is hard-coded in `printBookPDF.py` (`DIR = '/Users/pluttan/Desktop/проекты/printbookpdf/books/'`). Edit that line to point at your own `books/` folder before running — the result is written there as `<input-name>.pdf`.

## ■ License

MIT © [pluttan](https://github.com/pluttan)
