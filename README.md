# pandoc-docx-pagebreak-py

Pandoc filter to insert page break or section break in docx file

\toc

### install

```bash
pip3 install git+https://github.com/pandocker/pandoc-docx-pagebreak-py
```

### Usage

- Add `\newpage` where preferred to insert a page break
    - Expecting to work like native pandoc behavior for latex output
- Add `\toc` where preferred to insert TOC(Table of Contents)
    - unable to use with `--toc` otherwise TOC appears on head of document also
<!--
- Add `\newsection` where preferred to insert a section break
    - Only works for docx output
    - It resets page header/footer style to _portrait, US-letter_ sized pages with whatever reference file you used,
    except the last section in the file. **_You will have to fix them to your preference._**
-->

```bash
# Try the filter with this file like this:
pandoc -f markdown -t docx -o docx.docx --filter=pandoc-docx-pagebreakpy README.md
```

### Sample

```markdown
Contents before pagebreak

\newpage
Contents after _Page Break_

Contents after **Section Break**
```

Contents before pagebreak

\newpage

Contents after _Page Break_

Contents after **Section Break**
