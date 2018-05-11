# pandoc-docx-pagebreak-py

Pandoc filter to insert page break or section break in docx file

### install

```sh
pip3 install git+https://github.com/pandocker/pandoc-docx-pagebreak-py
```

### Usage

- Add `\newpage` where preferred to insert a page break
    - Expecting to work like native pandoc behavior for latex output
- Add `\newsection` where preferred to insert a section break
    - Only works for docx output


```sh
pandoc -f markdown -t docx -o docx.docx --filter=pandoc-docx-pagebreakpy
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

\newsection

Contents after **Section Break**
