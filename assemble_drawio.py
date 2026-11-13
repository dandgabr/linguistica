#!/usr/bin/env python3
"""
Assemble the complete multi-page .drawio file and generate standalone views.
"""

import os
from gen_pages import build_overview_page
from gen_indoeuropean import build_indoeuropean_page
from gen_east_asia import build_east_asia_page
from gen_transeurasian_uralic import build_transeurasian_uralic_page
from gen_afroasiatic_nigercongo import build_afroasiatic_nigercongo_page
from gen_americas import build_americas_page

def main():
    pages = [
        build_overview_page(),
        build_indoeuropean_page(),
        build_east_asia_page(),
        build_transeurasian_uralic_page(),
        build_afroasiatic_nigercongo_page(),
        build_americas_page()
    ]
    
    # Build multi-page drawio XML
    xml_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<mxfile host="app.diagrams.net" modified="2026-11-13T00:00:00.000Z" agent="Mozilla/5.0" version="24.0.0" type="device">'
    ]
    
    for p in pages:
        pname = p.page_name.replace("&", "&amp;")
        xml_parts.append(f'  <diagram id="{p.page_id}" name="{pname}">')
        xml_parts.append(f'    {p.to_xml()}')
        xml_parts.append('  </diagram>')
        
    xml_parts.append('</mxfile>')
    
    output_filename = "arvore_genealogica_linguas_completa.drawio"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_parts))
        
    print(f"Master multi-page file written to {output_filename} ({os.path.getsize(output_filename)} bytes)")

    # Also write individual page XMLs for direct open_drawio_xml inspection
    for p in pages:
        fname = f"{p.page_id}.xml"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(p.to_xml())
        print(f"Saved {fname} ({len(p.cells)} nodes, {len(p.edges)} edges)")

if __name__ == "__main__":
    main()
