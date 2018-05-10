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

    def action(self, elem, doc):
        if (doc.format == "docx"):
            if isinstance(elem, pf.RawBlock) and elem.text == r"\newpage":
                pf.debug("Page Break")
                elem = self.pagebreak
        return elem


def main(doc=None):
    dp = DocxPagebreak()
    return pf.run_filter(dp.action, doc=doc)


if __name__ == "__main__":
    main()
