#!/usr/bin/env python3
import json
import process_tree
import build_geo_data as geo

def assemble():
    with open('landmasses.json', 'r') as f:
        LANDMASSES = json.load(f)

    TRUNK_GEO = geo.TRUNK_GEO
    nodes, trunks_meta = process_tree.generate()

    nodes_json = json.dumps(nodes, ensure_ascii=False)
    trunks_json = json.dumps(trunks_meta, ensure_ascii=False)
    geo_json = json.dumps(TRUNK_GEO, ensure_ascii=False)
    land_json = json.dumps(LANDMASSES, ensure_ascii=False)

    with open('template_head.html', 'r', encoding='utf-8') as f:
        head_html = f.read()

    with open('template_scripts.js', 'r', encoding='utf-8') as f:
        scripts_js = f.read()

    scripts_js = scripts_js.replace('__NODES__', nodes_json)
    scripts_js = scripts_js.replace('__TRUNKS__', trunks_json)
    scripts_js = scripts_js.replace('__GEO__', geo_json)
    scripts_js = scripts_js.replace('__LAND__', land_json)

    final_html = head_html + '\n' + scripts_js

    with open('arvore_interativa.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Assembly complete: arvore_interativa.html ({len(final_html)} bytes)")

if __name__ == '__main__':
    assemble()
