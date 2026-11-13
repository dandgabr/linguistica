#!/usr/bin/env python3
"""
Generates the Organic / Biophilic interactive web application for the
World Languages Phylogenetic Tree.
"""

import json
import xml.etree.ElementTree as ET
import re

def clean_html(text):
    text = re.sub(r'<br\s*/?>', ' — ', text)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def extract_endonym(raw_val):
    # Extracts endonyms in parentheses, e.g. (Português), (العربية), (官话 / 普通话), (Latinum)
    m = re.search(r'\(([^)]+)\)', raw_val)
    if m:
        val = m.group(1).strip()
        if not any(k in val for k in ['a.C.', 'd.C.', 'séc.', 'Sudoeste', 'Ásia', 'Montes', 'Bacia', 'Ilhas', 'Europa', 'África']):
            return val
    return ""

def load_graph():
    tree = ET.parse('arvore_filogenetica_unificada_poster.drawio')
    root = tree.getroot()
    
    nodes = {}
    edges = []
    
    for cell in root.iter('mxCell'):
        cid = cell.attrib.get('id')
        if cell.attrib.get('vertex') == '1' and cid not in ['0', '1', 'node_poster_2', 'node_poster_3']:
            raw_val = cell.attrib.get('value', '')
            style = cell.attrib.get('style', '')
            
            is_extinct = '†' in raw_val or '#f8cecc' in style or '#b85450' in style
            is_proto = 'PROTO-' in raw_val.upper() or 'PROTOLÍNGUA' in raw_val.upper() or 'RADIAÇÃO' in raw_val.upper()
            is_root = cid == 'node_poster_4'
            is_living = '#d5e8d4' in style and not is_extinct
            is_branch = not is_living and not is_extinct and not is_proto
            
            lines = raw_val.split('<br>')
            title = clean_html(lines[0])
            subtitle = clean_html(' '.join(lines[1:])) if len(lines) > 1 else ""
            endonym = extract_endonym(raw_val)
            
            # Clean title of markers
            display_title = title.replace('†', '').strip()
            
            nodes[cid] = {
                "id": cid,
                "title": display_title,
                "raw_title": title,
                "subtitle": subtitle,
                "endonym": endonym,
                "is_extinct": is_extinct,
                "is_proto": is_proto,
                "is_living": is_living,
                "is_branch": is_branch,
                "is_root": is_root,
                "children": [],
                "parents": []
            }
        elif cell.attrib.get('edge') == '1':
            s = cell.attrib.get('source')
            t = cell.attrib.get('target')
            edges.append((s, t))
            
    # Connect north america proto-languages to human radiation root
    edges.append(('node_poster_4', 'node_americas_4'))
    
    for s, t in edges:
        if s in nodes and t in nodes:
            nodes[s]['children'].append(t)
            nodes[t]['parents'].append(s)
            
    return nodes, edges

if __name__ == '__main__':
    nodes, edges = load_graph()
    print(f"Loaded {len(nodes)} nodes, {len(edges)} edges.")
