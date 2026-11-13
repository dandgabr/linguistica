#!/usr/bin/env python3
"""
Generator for Indo-European Family Tree.
Zero-overlap guarantee using cladogram gutter routing and tiered horizontal corridors.
"""

from tree_builder import (
    TreeBuilder, S_LIVING, S_EXTINCT, S_BRANCH,
    S_FAMILY, S_SUBFAMILY, S_GROUP, S_EDGE, S_EDGE_TOPDOWN, S_EDGE_GUTTER, S_LEGEND
)

def build_indoeuropean_page():
    tb = TreeBuilder("ie", "1. Família Indo-Europeia", width=4200, height=2400)
    tb.add_legend(40, 40)
    
    # Title
    tb.add_node(
        "<b>ÁRVORE FILOGENÉTICA DA FAMÍLIA INDO-EUROPEIA</b><br>"
        "<i>Indo-European Language Family Tree — Baseado no modelo comparativo de Cole (2026) e Schleicher</i>",
        S_FAMILY, 340, 40, 700, 60
    )
    
    # Root
    root = tb.add_node(
        "<b>PROTO-INDO-EUROPEU (PIE)</b><br>(~4.500–3.000 a.C. — Estepes Pôntico-Cáspias)",
        S_FAMILY, 1900, 130, 400, 50
    )
    
    branch_y = 230

    # ==========================================
    # 1. ANATOLIANA (Extinta)
    # ==========================================
    b_anat = tb.add_node("<b>ANATOLIANA †</b><br><i>(Ásia Menor)</i>", S_BRANCH, 50, branch_y, 220, 44)
    tb.add_edge(root, b_anat, style=S_EDGE_TOPDOWN)
    anat_langs = [
        ("Hitita (Hittite) †", S_EXTINCT),
        ("Luwiano †", S_EXTINCT),
        ("Lício (Lycian) †", S_EXTINCT),
        ("Lídio (Lydian) †", S_EXTINCT),
        ("Cariano (Carian) †", S_EXTINCT),
        ("Palaico †", S_EXTINCT),
        ("Pisídio †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_anat, anat_langs, 50, start_y=300, col_w=220, child_h=30, y_step=38, indent=24)

    # ==========================================
    # 2. HELÊNICA
    # ==========================================
    b_hell = tb.add_node("<b>HELÊNICA</b>", S_BRANCH, 300, branch_y, 210, 44)
    tb.add_edge(root, b_hell, style=S_EDGE_TOPDOWN)
    
    myc = tb.add_node("Grego Micênico †", S_EXTINCT, 324, 300, 186, 30)
    tb.add_edge(b_hell, myc, style=S_EDGE_GUTTER)
    
    anc_grk = tb.add_node("Grego Clássico †<br>(Ático, Jônico, Dórico)", S_EXTINCT, 324, 345, 186, 36)
    tb.add_edge(myc, anc_grk, style=S_EDGE_TOPDOWN)
    
    koine = tb.add_node("Grego Koiné †", S_EXTINCT, 324, 395, 186, 30)
    tb.add_edge(anc_grk, koine, style=S_EDGE_TOPDOWN)
    
    byz = tb.add_node("Grego Bizantino †", S_EXTINCT, 324, 440, 186, 30)
    tb.add_edge(koine, byz, style=S_EDGE_TOPDOWN)
    
    mod_grk = tb.add_node("Grego Moderno<br>(Ελληνικά)", S_LIVING, 324, 485, 186, 36)
    tb.add_edge(byz, mod_grk, style=S_EDGE_TOPDOWN)
    
    tsak = tb.add_node("Tsakoniano (Dórico)", S_LIVING, 324, 535, 186, 30)
    tb.add_edge(anc_grk, tsak, style=S_EDGE_GUTTER)

    # ==========================================
    # 3. ITÁLICA (Latino-Falisco & Sabélico -> Românica)
    # ==========================================
    b_ital = tb.add_node("<b>ITÁLICA</b>", S_BRANCH, 540, branch_y, 900, 44)
    tb.add_edge(root, b_ital, style=S_EDGE_TOPDOWN)
    
    # 3.1 Sabellic branch
    b_sabel = tb.add_node("<b>Sabélica / Osco-Úmbria</b>", S_BRANCH, 540, 300, 200, 36)
    tb.add_edge(b_ital, b_sabel, style=S_EDGE_TOPDOWN)
    sabel_langs = [
        ("Osco †", S_EXTINCT),
        ("Úmbrio †", S_EXTINCT),
        ("Volsco †", S_EXTINCT),
        ("Piceno Meridional †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_sabel, sabel_langs, 540, start_y=355, col_w=200, child_h=30, y_step=38, indent=24)

    # 3.2 Latino-Faliscan & Romance
    b_latfal = tb.add_node("<b>Latino-Falisca</b>", S_BRANCH, 770, 300, 670, 36)
    tb.add_edge(b_ital, b_latfal, style=S_EDGE_TOPDOWN)
    
    faliscan = tb.add_node("Falisco †", S_EXTINCT, 770, 355, 130, 30)
    tb.add_edge(b_latfal, faliscan, style=S_EDGE_TOPDOWN)
    
    latin = tb.add_node("<b>Latim (Latinum) †</b>", S_EXTINCT, 930, 355, 510, 32)
    tb.add_edge(b_latfal, latin, style=S_EDGE_TOPDOWN)
    
    vulg_lat = tb.add_node("Latim Vulgar †", S_EXTINCT, 930, 405, 510, 30)
    tb.add_edge(latin, vulg_lat, style=S_EDGE_TOPDOWN)
    
    rom_branch = tb.add_node("<b>Línguas Românicas</b>", S_SUBFAMILY, 930, 455, 510, 34)
    tb.add_edge(vulg_lat, rom_branch, style=S_EDGE_TOPDOWN)
    
    # Romance sub-groups: 3 horizontal columns
    # 3.2.1 Ibero-Romance
    ibero = tb.add_node("<b>Ibero-Românicas</b>", S_GROUP, 770, 510, 210, 32)
    tb.add_edge(rom_branch, ibero, style=S_EDGE_TOPDOWN)
    ibero_langs = [
        ("Galego-Português †", S_EXTINCT),
        ("Português (Português)", S_LIVING),
        ("Galego (Galego)", S_LIVING),
        ("Espanhol (Español)", S_LIVING),
        ("Asturiano / Leonês", S_LIVING),
        ("Mirandês", S_LIVING),
        ("Aragonês", S_LIVING),
        ("Ladino (Sefardita)", S_LIVING),
        ("Moçárabe †", S_EXTINCT)
    ]
    tb.add_vertical_children(ibero, ibero_langs, 770, start_y=560, col_w=210, child_h=30, y_step=38, indent=22)

    # 3.2.2 Gallo-Romance & Occitano-Romance
    gallo = tb.add_node("<b>Galo-Românicas</b>", S_GROUP, 1000, 510, 210, 32)
    tb.add_edge(rom_branch, gallo, style=S_EDGE_TOPDOWN)
    gallo_langs = [
        ("Antigo Francês †", S_EXTINCT),
        ("Francês (Français)", S_LIVING),
        ("Occitano (Lenga d'òc)", S_LIVING),
        ("Catalão (Català)", S_LIVING),
        ("Valão (Wallon)", S_LIVING),
        ("Normando", S_LIVING),
        ("Franco-Provençal (Arpitan)", S_LIVING)
    ]
    tb.add_vertical_children(gallo, gallo_langs, 1000, start_y=560, col_w=210, child_h=30, y_step=38, indent=22)

    # 3.2.3 Italo-Dalmatian & Eastern Romance
    italo_east = tb.add_node("<b>Ítalo-Dálmata &amp; Oriental</b>", S_GROUP, 1230, 510, 210, 32)
    tb.add_edge(rom_branch, italo_east, style=S_EDGE_TOPDOWN)
    italo_langs = [
        ("Italiano (Italiano)", S_LIVING),
        ("Napolitano / Siciliano", S_LIVING),
        ("Sardo (Sardu)", S_LIVING),
        ("Corso (Corsu)", S_LIVING),
        ("Veneto / Lombardo", S_LIVING),
        ("Romanche (Rumantsch)", S_LIVING),
        ("Friulano", S_LIVING),
        ("Dálmata †", S_EXTINCT),
        ("Romeno (Română)", S_LIVING),
        ("Aromeno / Megleno", S_LIVING)
    ]
    tb.add_vertical_children(italo_east, italo_langs, 1230, start_y=560, col_w=210, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 4. CÉLTICA
    # ==========================================
    b_celt = tb.add_node("<b>CÉLTICA</b>", S_BRANCH, 1470, branch_y, 450, 44)
    tb.add_edge(root, b_celt, style=S_EDGE_TOPDOWN)
    
    # Continental
    b_cont_celt = tb.add_node("Continental †", S_BRANCH, 1470, 300, 200, 32)
    tb.add_edge(b_celt, b_cont_celt, style=S_EDGE_TOPDOWN)
    cont_langs = [
        ("Gaulês †", S_EXTINCT),
        ("Celtibero †", S_EXTINCT),
        ("Lepôntico †", S_EXTINCT),
        ("Gálata †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_cont_celt, cont_langs, 1470, start_y=350, col_w=200, child_h=30, y_step=38, indent=24)
    
    # Insular
    b_ins_celt = tb.add_node("<b>Insular</b>", S_BRANCH, 1690, 300, 230, 32)
    tb.add_edge(b_celt, b_ins_celt, style=S_EDGE_TOPDOWN)
    
    b_goid = tb.add_node("Goidélica (Gaélica)", S_GROUP, 1690, 350, 230, 30)
    tb.add_edge(b_ins_celt, b_goid, style=S_EDGE_TOPDOWN)
    goid_langs = [
        ("Irlandês Antigo †", S_EXTINCT),
        ("Irlandês (Gaeilge)", S_LIVING),
        ("Gaélico Escocês (Gàidhlig)", S_LIVING),
        ("Manx (Gaelg)", S_LIVING)
    ]
    tb.add_vertical_children(b_goid, goid_langs, 1690, start_y=395, col_w=230, child_h=30, y_step=38, indent=22)
    
    b_bryt = tb.add_node("Britônica", S_GROUP, 1690, 565, 230, 30)
    tb.add_edge(b_ins_celt, b_bryt, style=S_EDGE_GUTTER)
    bryt_langs = [
        ("Galês (Cymraeg)", S_LIVING),
        ("Bretão (Brezhoneg)", S_LIVING),
        ("Córnico (Kernewek)", S_LIVING),
        ("Cúmbrico † / Picto †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_bryt, bryt_langs, 1690, start_y=610, col_w=230, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 5. GERMÂNICA
    # ==========================================
    b_germ = tb.add_node("<b>GERMÂNICA</b>", S_BRANCH, 1950, branch_y, 560, 44)
    tb.add_edge(root, b_germ, style=S_EDGE_TOPDOWN)
    
    # East Germanic
    b_egerm = tb.add_node("Oriental †", S_BRANCH, 1950, 300, 160, 32)
    tb.add_edge(b_germ, b_egerm, style=S_EDGE_TOPDOWN)
    egerm_langs = [
        ("Gótico †", S_EXTINCT),
        ("Vandálico †", S_EXTINCT),
        ("Burgúndio †", S_EXTINCT),
        ("Gótico da Crimeia †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_egerm, egerm_langs, 1950, start_y=350, col_w=160, child_h=30, y_step=38, indent=20)
    
    # North Germanic
    b_ngerm = tb.add_node("<b>Nórdica (Setentrional)</b>", S_BRANCH, 2130, 300, 180, 32)
    tb.add_edge(b_germ, b_ngerm, style=S_EDGE_TOPDOWN)
    onorse = tb.add_node("Nórdico Antigo †", S_EXTINCT, 2152, 350, 158, 30)
    tb.add_edge(b_ngerm, onorse, style=S_EDGE_GUTTER)
    norse_langs = [
        ("Islandês (Íslenska)", S_LIVING),
        ("Feroês (Føroyskt)", S_LIVING),
        ("Norueguês (Norsk)", S_LIVING),
        ("Sueco (Svenska)", S_LIVING),
        ("Dinamarquês (Dansk)", S_LIVING),
        ("Elfdaliano (Övdalsk)", S_LIVING),
        ("Norn †", S_EXTINCT)
    ]
    tb.add_vertical_children(onorse, norse_langs, 2130, start_y=395, col_w=180, child_h=30, y_step=38, indent=22)

    # West Germanic
    b_wgerm = tb.add_node("<b>Ocidental</b>", S_BRANCH, 2330, 300, 180, 32)
    tb.add_edge(b_germ, b_wgerm, style=S_EDGE_TOPDOWN)
    
    b_anglo = tb.add_node("Anglo-Frísio", S_GROUP, 2330, 350, 180, 28)
    tb.add_edge(b_wgerm, b_anglo, style=S_EDGE_TOPDOWN)
    anglo_langs = [
        ("Inglês Antigo †", S_EXTINCT),
        ("Inglês (English)", S_LIVING),
        ("Escocês (Scots)", S_LIVING),
        ("Frísio (Frysk)", S_LIVING)
    ]
    tb.add_vertical_children(b_anglo, anglo_langs, 2330, start_y=390, col_w=180, child_h=28, y_step=36, indent=20)
    
    b_low = tb.add_node("Baixo-Francônio", S_GROUP, 2330, 545, 180, 28)
    tb.add_edge(b_wgerm, b_low, style=S_EDGE_GUTTER)
    low_langs = [
        ("Holandês (Nederlands)", S_LIVING),
        ("Africâner (Afrikaans)", S_LIVING),
        ("Baixo-Alemão (Platt)", S_LIVING)
    ]
    tb.add_vertical_children(b_low, low_langs, 2330, start_y=585, col_w=180, child_h=28, y_step=36, indent=20)
    
    b_high = tb.add_node("Alto-Alemão", S_GROUP, 2330, 710, 180, 28)
    tb.add_edge(b_wgerm, b_high, style=S_EDGE_GUTTER)
    high_langs = [
        ("Alemão (Deutsch)", S_LIVING),
        ("Iídiche (ייִדיש)", S_LIVING),
        ("Luxemburguês", S_LIVING),
        ("Suíço-Alemão", S_LIVING)
    ]
    tb.add_vertical_children(b_high, high_langs, 2330, start_y=750, col_w=180, child_h=28, y_step=36, indent=20)

    # ==========================================
    # 6. BALTO-ESLAVA
    # ==========================================
    b_baltoslav = tb.add_node("<b>BALTO-ESLAVA</b>", S_BRANCH, 2540, branch_y, 490, 44)
    tb.add_edge(root, b_baltoslav, style=S_EDGE_TOPDOWN)
    
    # Baltic
    b_balt = tb.add_node("<b>Báltica</b>", S_BRANCH, 2540, 300, 170, 32)
    tb.add_edge(b_baltoslav, b_balt, style=S_EDGE_TOPDOWN)
    balt_langs = [
        ("Lituano (Lietuvių)", S_LIVING),
        ("Letão (Latviešu)", S_LIVING),
        ("Prussiano Antigo †", S_EXTINCT),
        ("Jatvíngio / Curônio †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_balt, balt_langs, 2540, start_y=350, col_w=170, child_h=30, y_step=38, indent=22)
    
    # Slavic
    b_slav = tb.add_node("<b>Eslava</b>", S_BRANCH, 2730, 300, 300, 32)
    tb.add_edge(b_baltoslav, b_slav, style=S_EDGE_TOPDOWN)
    
    proto_slav = tb.add_node("Proto-Eslavo †", S_EXTINCT, 2730, 345, 300, 28)
    tb.add_edge(b_slav, proto_slav, style=S_EDGE_TOPDOWN)
    
    # East Slavic
    b_eslav = tb.add_node("Oriental", S_GROUP, 2730, 390, 140, 26)
    tb.add_edge(proto_slav, b_eslav, style=S_EDGE_TOPDOWN)
    eslav_langs = [
        ("Russo (Русский)", S_LIVING),
        ("Ucraniano (Українська)", S_LIVING),
        ("Bielorrusso (Беларуская)", S_LIVING),
        ("Rusyn", S_LIVING)
    ]
    tb.add_vertical_children(b_eslav, eslav_langs, 2730, start_y=430, col_w=140, child_h=28, y_step=36, indent=18)
    
    # West Slavic
    b_wslav = tb.add_node("Ocidental", S_GROUP, 2890, 390, 140, 26)
    tb.add_edge(proto_slav, b_wslav, style=S_EDGE_TOPDOWN)
    wslav_langs = [
        ("Polonês (Polski)", S_LIVING),
        ("Tcheco (Čeština)", S_LIVING),
        ("Eslovaco (Slovenčina)", S_LIVING),
        ("Sórbio / Cassúbio", S_LIVING)
    ]
    tb.add_vertical_children(b_wslav, wslav_langs, 2890, start_y=430, col_w=140, child_h=28, y_step=36, indent=18)
    
    # South Slavic
    b_sslav = tb.add_node("Meridional", S_GROUP, 2810, 590, 220, 26)
    tb.add_edge(proto_slav, b_sslav, style=S_EDGE_GUTTER)
    sslav_langs = [
        ("Antigo Eslavo Ecles. †", S_EXTINCT),
        ("Búlgaro / Macedônio", S_LIVING),
        ("Sérvio / Croata / Bósnio", S_LIVING),
        ("Esloveno (Slovenščina)", S_LIVING)
    ]
    tb.add_vertical_children(b_sslav, sslav_langs, 2810, start_y=630, col_w=220, child_h=28, y_step=36, indent=20)

    # ==========================================
    # 7. INDO-IRANIANA
    # ==========================================
    b_indoiran = tb.add_node("<b>INDO-IRANIANA</b>", S_BRANCH, 3060, branch_y, 480, 44)
    tb.add_edge(root, b_indoiran, style=S_EDGE_TOPDOWN)
    
    # Indo-Aryan
    b_aryan = tb.add_node("<b>Indo-Ariana (Índica)</b>", S_BRANCH, 3060, 300, 230, 32)
    tb.add_edge(b_indoiran, b_aryan, style=S_EDGE_TOPDOWN)
    
    sanskrit = tb.add_node("Sânscrito Védico / Clássico †", S_EXTINCT, 3082, 345, 208, 28)
    tb.add_edge(b_aryan, sanskrit, style=S_EDGE_GUTTER)
    
    prakrit = tb.add_node("Prácritos †", S_EXTINCT, 3082, 385, 208, 26)
    tb.add_edge(sanskrit, prakrit, style=S_EDGE_TOPDOWN)
    
    aryan_langs = [
        ("Hindi (हिन्दी) & Urdu (اردو)", S_LIVING),
        ("Bengali (বাংলা)", S_LIVING),
        ("Panjabi (ਪੰਜਾਬੀ)", S_LIVING),
        ("Marata (मराठी)", S_LIVING),
        ("Guzerate (ગુજરાતી)", S_LIVING),
        ("Bhojpuri / Maithili", S_LIVING),
        ("Odia / Assamês", S_LIVING),
        ("Sindi / Nepali", S_LIVING),
        ("Cingalês (සිංහල)", S_LIVING),
        ("Romani (Cigano)", S_LIVING)
    ]
    tb.add_vertical_children(prakrit, aryan_langs, 3060, start_y=425, col_w=230, child_h=28, y_step=36, indent=22)
    
    # Iranian
    b_iran = tb.add_node("<b>Iraniana</b>", S_BRANCH, 3310, 300, 230, 32)
    tb.add_edge(b_indoiran, b_iran, style=S_EDGE_TOPDOWN)
    
    old_iran = tb.add_node("Avéstico † &amp; Persa Antigo †", S_EXTINCT, 3332, 345, 208, 28)
    tb.add_edge(b_iran, old_iran, style=S_EDGE_GUTTER)
    
    iran_langs = [
        ("Persa / Farsi (فارسی)", S_LIVING),
        ("Dari / Tajique", S_LIVING),
        ("Pashto (پښتو)", S_LIVING),
        ("Curdo (Kurdî)", S_LIVING),
        ("Balúchi (بلوچی)", S_LIVING),
        ("Osseta (Ирон)", S_LIVING),
        ("Sogdiano † / Pártio †", S_EXTINCT)
    ]
    tb.add_vertical_children(old_iran, iran_langs, 3310, start_y=385, col_w=230, child_h=28, y_step=36, indent=22)

    # ==========================================
    # 8. TOCARIANA (Extinta)
    # ==========================================
    b_toch = tb.add_node("<b>TOCARIANA †</b>", S_BRANCH, 3560, branch_y, 180, 44)
    tb.add_edge(root, b_toch, style=S_EDGE_TOPDOWN)
    toch_langs = [
        ("Tocariano A †", S_EXTINCT),
        ("Tocariano B †", S_EXTINCT),
        ("Tocariano C †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_toch, toch_langs, 3560, start_y=300, col_w=180, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 9. ARMÊNIA
    # ==========================================
    b_arm = tb.add_node("<b>ARMÊNIA</b>", S_BRANCH, 3760, branch_y, 180, 44)
    tb.add_edge(root, b_arm, style=S_EDGE_TOPDOWN)
    arm_langs = [
        ("Armênio Clássico †", S_EXTINCT),
        ("Armênio Oriental (Հայերեն)", S_LIVING),
        ("Armênio Ocidental", S_LIVING)
    ]
    tb.add_vertical_children(b_arm, arm_langs, 3760, start_y=300, col_w=180, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 10. ALBANESA
    # ==========================================
    b_alb = tb.add_node("<b>ALBANESA</b>", S_BRANCH, 3960, branch_y, 180, 44)
    tb.add_edge(root, b_alb, style=S_EDGE_TOPDOWN)
    alb_langs = [
        ("Proto-Albanês †", S_EXTINCT),
        ("Albanês Tosk (Shqip)", S_LIVING),
        ("Albanês Gheg", S_LIVING),
        ("Arbëresh", S_LIVING)
    ]
    tb.add_vertical_children(b_alb, alb_langs, 3960, start_y=300, col_w=180, child_h=30, y_step=38, indent=22)

    return tb

print("Indo-European generator ready with zero-overlap routing.")
