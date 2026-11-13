#!/usr/bin/env python3
import json
import os
import sys

# Garantir importação de módulos locais em src/data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DATA_DIR = os.path.join(BASE_DIR, 'src', 'data')
if SRC_DATA_DIR not in sys.path:
    sys.path.insert(0, SRC_DATA_DIR)

import process_tree
import build_geo_data as geo

def assemble():
    assets_dir = os.path.join(BASE_DIR, 'src', 'assets')
    templates_dir = os.path.join(BASE_DIR, 'src', 'templates')

    print("Reading d3.min.js...")
    with open(os.path.join(assets_dir, 'd3.min.js'), 'r', encoding='utf-8') as f:
        d3_code = f.read()

    print("Reading ne_land_110m_compact.json...")
    with open(os.path.join(assets_dir, 'ne_land_110m_compact.json'), 'r', encoding='utf-8') as f:
        land_geojson = f.read()

    print("Loading tree & geo data...")
    TRUNK_GEO = geo.TRUNK_GEO
    nodes, trunks_meta = process_tree.generate()

    nodes_json = json.dumps(nodes, ensure_ascii=False)
    trunks_json = json.dumps(trunks_meta, ensure_ascii=False)
    geo_json = json.dumps(TRUNK_GEO, ensure_ascii=False)

    with open(os.path.join(templates_dir, 'template_head.html'), 'r', encoding='utf-8') as f:
        head_html = f.read()

    with open(os.path.join(templates_dir, 'template_scripts_d3.js'), 'r', encoding='utf-8') as f:
        scripts_js = f.read()

    scripts_js = scripts_js.replace('__D3_CODE__', d3_code)
    scripts_js = scripts_js.replace('__LAND_GEOJSON__', land_geojson)
    scripts_js = scripts_js.replace('__NODES__', nodes_json)
    scripts_js = scripts_js.replace('__TRUNKS__', trunks_json)
    scripts_js = scripts_js.replace('__GEO__', geo_json)

    final_html = head_html + '\n' + scripts_js

    out_arvore = os.path.join(BASE_DIR, 'arvore_interativa.html')
    out_index = os.path.join(BASE_DIR, 'index.html')

    with open(out_arvore, 'w', encoding='utf-8') as f:
        f.write(final_html)

    with open(out_index, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Assembly complete: arvore_interativa.html & index.html ({len(final_html)} bytes)")

if __name__ == '__main__':
    assemble()
