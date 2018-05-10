# pandoc-docx-pagebreak-py

Pandoc filter to insert pagebreak in docx file

### install

```sh
pip3 install git+https://github.com/pandocker/pandoc-docx-pagebreak-py
```

### Usage

Add `\newpage` where preferred to insert a page break

Expecting to work like native pandoc behavior for latex output

```sh
pandoc -f markdown -t docx -o docx.docx --filter=pandoc-docx-pagebreakpy
```

### Sample

```markdown
Contents before pagebreak

\\newpage

Contents after pagebreak
```
