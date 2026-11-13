#!/usr/bin/env python3
import json
import process_tree
import build_geo_data as geo

def assemble():
    print("Reading d3.min.js...")
    with open('d3.min.js', 'r', encoding='utf-8') as f:
        d3_code = f.read()

    print("Reading ne_land_110m_compact.json...")
    with open('ne_land_110m_compact.json', 'r', encoding='utf-8') as f:
        land_geojson = f.read()

    print("Loading tree & geo data...")
    TRUNK_GEO = geo.TRUNK_GEO
    nodes, trunks_meta = process_tree.generate()

    nodes_json = json.dumps(nodes, ensure_ascii=False)
    trunks_json = json.dumps(trunks_meta, ensure_ascii=False)
    geo_json = json.dumps(TRUNK_GEO, ensure_ascii=False)

    with open('template_head.html', 'r', encoding='utf-8') as f:
        head_html = f.read()

    with open('template_scripts_d3.js', 'r', encoding='utf-8') as f:
        scripts_js = f.read()

    scripts_js = scripts_js.replace('__D3_CODE__', d3_code)
    scripts_js = scripts_js.replace('__LAND_GEOJSON__', land_geojson)
    scripts_js = scripts_js.replace('__NODES__', nodes_json)
    scripts_js = scripts_js.replace('__TRUNKS__', trunks_json)
    scripts_js = scripts_js.replace('__GEO__', geo_json)

    final_html = head_html + '\n' + scripts_js

    with open('arvore_interativa.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Assembly complete: arvore_interativa.html ({len(final_html)} bytes)")

if __name__ == '__main__':
    assemble()
