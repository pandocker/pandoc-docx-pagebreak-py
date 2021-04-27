#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" pandoc-docx-pagebreakpy
Pandoc filter to insert pagebreak as openxml RawBlock
Only for docx output

Trying to port pandoc-doc-pagebreak
- https://github.com/alexstoick/pandoc-docx-pagebreak
"""

import panflute as pf


class DocxPagebreak(object):
    pagebreak = pf.RawBlock("<w:p><w:r><w:br w:type=\"page\" /></w:r></w:p>", format="openxml")
    sectionbreak = pf.RawBlock("<w:p><w:pPr><w:sectPr><w:type w:val=\"nextPage\" /></w:sectPr></w:pPr></w:p>",
                               format="openxml")
    toc = pf.RawBlock(r"""
<w:sdt>
    <w:sdtContent xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
        <w:p>
            <w:r>
                <w:fldChar w:fldCharType="begin" w:dirty="true" />
                <w:instrText xml:space="preserve">TOC \o "1-3" \h \z \u</w:instrText>
                <w:fldChar w:fldCharType="separate" />
                <w:fldChar w:fldCharType="end" />
            </w:r>
        </w:p>
    </w:sdtContent>
</w:sdt>
""", format="openxml")

    def action(self, elem, doc):
        if isinstance(elem, (pf.Para, pf.Plain)):
            for child in elem.content:
                if isinstance(child, pf.Str) and child.text == r"\newpage":
                    if (doc.format == "docx"):
                        pf.debug("Page Break")
                        elem = self.pagebreak
        if isinstance(elem, pf.RawBlock):
            if elem.text == r"\newpage":
                if (doc.format == "docx"):
                    pf.debug("Page Break")
                    elem = self.pagebreak
            # elif elem.text == r"\newsection":
            #     if (doc.format == "docx"):
            #         pf.debug("Section Break")
            #         elem = self.sectionbreak
            #     else:
            #         elem = []
            elif elem.text == r"\toc":
                if (doc.format == "docx"):
                    pf.debug("Table of Contents")
                    para = [pf.Para(pf.Str("Table"), pf.Space(), pf.Str("of"), pf.Space(), pf.Str("Contents"))]
                    div = pf.Div(*para, attributes={"custom-style": "TOC Heading"})
                    elem = [div, self.toc]
                else:
                    elem = []
        return elem


def main(doc=None):
    dp = DocxPagebreak()
    return pf.run_filter(dp.action, doc=doc)


if __name__ == "__main__":
    main()
