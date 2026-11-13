#!/usr/bin/env python3
"""
Generates a Unified Single-Canvas Poster Diagram:
'arvore_filogenetica_unificada_poster.drawio'
Combines all world protolanguages and their phylogenetic trees on one giant continuous canvas.
"""

from tree_builder import (
    TreeBuilder, S_LIVING, S_EXTINCT, S_BRANCH,
    S_FAMILY, S_SUBFAMILY, S_GROUP, S_EDGE_TOPDOWN, S_EDGE_GUTTER, S_LEGEND
)
from gen_indoeuropean import build_indoeuropean_page
from gen_east_asia import build_east_asia_page
from gen_transeurasian_uralic import build_transeurasian_uralic_page
from gen_afroasiatic_nigercongo import build_afroasiatic_nigercongo_page
from gen_americas import build_americas_page

def generate_unified_poster():
    poster = TreeBuilder("poster", "Árvore Filogenética Unificada Mundial", width=21000, height=2800)
    poster.add_legend(60, 50)
    
    # Title Banner
    poster.add_node(
        "<b>ÁRVORE GENEALÓGICA E FILOGENÉTICA DAS LÍNGUAS DO MUNDO (PÔSTER COMPLETO)</b><br>"
        "<i>Classificação Comparativa Global de Todas as Protolínguas e Linhagens Vivas e Históricas</i><br>"
        "<span style='font-size:11px;'>Referência: Theodor Cole &amp; Siebert-Cole (Parte 2, ResearchGate 2026), Glottolog, Campbell, Blust, Rodrigues &amp; Greenberg</span>",
        S_FAMILY, 380, 50, 1100, 75
    )
    
    # Global Root
    master_root = poster.add_node(
        "<b>RADIAÇÃO FILOGENÉTICA DAS LÍNGUAS HUMANAS</b><br>"
        "(Línguas Naturais — Reconstruções de Protolínguas e Famílias Independentes Reconhecidas)",
        S_FAMILY, 9800, 150, 800, 55
    )
    
    pages = [
        ("Indo-Europeia", build_indoeuropean_page(), 100),
        ("Transeurasiática / Urálica", build_transeurasian_uralic_page(), 4400),
        ("Afroasiática / Níger-Congo / Dravídica", build_afroasiatic_nigercongo_page(), 8500),
        ("Leste / Sudeste Asiático & Pacífico", build_east_asia_page(), 12400),
        ("Américas", build_americas_page(), 16700),
    ]
    
    for section_name, tb, offset_x in pages:
        # Transfer all cells with offset_x, skipping original title and legend
        for cell in tb.cells:
            # Skip page-specific title banner and legend
            if cell["x"] < 1100 and cell["y"] < 130:
                continue
            new_cell = dict(cell)
            new_cell["x"] += offset_x
            new_cell["y"] += 120  # shift down slightly to accommodate master root
            poster.cells.append(new_cell)
            
            # If this is a primary family / proto-language root node (y was ~130-140):
            if cell["y"] <= 145 and "PROTO-" in cell["value"].upper():
                poster.add_edge(master_root, cell["id"], style=S_EDGE_TOPDOWN)
                
        # Transfer all edges
        for edge in tb.edges:
            poster.edges.append(dict(edge))
            
    xml = poster.to_xml()
    wrapped_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2026-11-13T00:00:00.000Z" agent="Mozilla/5.0" version="24.0.0" type="device">
  <diagram id="poster" name="Árvore Filogenética Unificada Mundial">
    {xml}
  </diagram>
</mxfile>'''
    with open("arvore_filogenetica_unificada_poster.drawio", "w", encoding="utf-8") as f:
        f.write(wrapped_xml)
        
    print(f"Unified single-canvas poster generated: {len(poster.cells)} nodes, {len(poster.edges)} edges.")

if __name__ == "__main__":
    generate_unified_poster()
