#!/usr/bin/env python3
"""
Generator for Afroasiatic, Niger-Congo, and Dravidian Protolanguages.
Explicit Proto-languages at all roots.
"""

from tree_builder import (
    TreeBuilder, S_LIVING, S_EXTINCT, S_BRANCH,
    S_FAMILY, S_SUBFAMILY, S_GROUP, S_EDGE, S_EDGE_TOPDOWN, S_EDGE_GUTTER, S_LEGEND
)

def build_afroasiatic_nigercongo_page():
    tb = TreeBuilder("afro_niger_drav", "4. Afroasiática, Níger-Congo & Dravídica", width=3800, height=2300)
    tb.add_legend(40, 40)
    
    # Title
    tb.add_node(
        "<b>ÁRVORE FILOGENÉTICA DAS PROTOLÍNGUAS AFROASIÁTICA, NÍGER-CONGO &amp; DRAVÍDICA</b><br>"
        "<i>Reconstruções: Proto-Afroasiático (PAA), Proto-Níger-Congo (PNC) e Proto-Dravídico</i><br>"
        "<span style='font-size:10px;'>Baseado em Cole &amp; Siebert-Cole, Greenberg (Languages of Africa), Hetzron &amp; Krishnamurti</span>",
        S_FAMILY, 340, 40, 880, 65
    )
    
    # ==========================================
    # 1. PROTO-AFROASIÁTICO (PAA)
    # ==========================================
    f_afro = tb.add_node(
        "<b>PROTO-AFROASIÁTICO (PAA)</b><br>"
        "<i>c. 10000–8000 a.C. — Chifre da África / Deserto Oriental / Bacia do Nilo (Mais antiga reconstrução)</i>",
        S_FAMILY, 50, 140, 1310, 52
    )
    
    # 1.1 Proto-Semítico
    b_sem = tb.add_node("<b>Proto-Semítico (c. 3750 a.C. — Levante / Arábia)</b>", S_SUBFAMILY, 50, 225, 580, 34)
    tb.add_edge(f_afro, b_sem, style=S_EDGE_TOPDOWN)
    
    # East Semitic
    b_esem = tb.add_node("Semítico Oriental †", S_GROUP, 50, 280, 175, 30)
    tb.add_edge(b_sem, b_esem, style=S_EDGE_TOPDOWN)
    esem_langs = [
        ("Acadiano †", S_EXTINCT),
        ("Babilônico †", S_EXTINCT),
        ("Assírio Antigo †", S_EXTINCT),
        ("Eblaíta †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_esem, esem_langs, 50, start_y=325, col_w=175, child_h=30, y_step=38, indent=18)

    # Northwest Semitic
    b_nwsem = tb.add_node("Proto-Noroeste Semítico", S_GROUP, 245, 280, 195, 30)
    tb.add_edge(b_sem, b_nwsem, style=S_EDGE_TOPDOWN)
    nwsem_langs = [
        ("Ugarítico †", S_EXTINCT),
        ("Fenício / Púnico †", S_EXTINCT),
        ("Hebraico Bíblico †", S_EXTINCT),
        ("<b>Hebraico Moderno (עברית)</b> ~9M", S_LIVING),
        ("Aramaico Antigo †", S_EXTINCT),
        ("Siríaco Clássico †", S_EXTINCT),
        ("Neo-Aramaico Assírio", S_LIVING)
    ]
    tb.add_vertical_children(b_nwsem, nwsem_langs, 245, start_y=325, col_w=195, child_h=30, y_step=38, indent=18)

    # Arabic & South Semitic
    b_arab_eth = tb.add_node("Árabe &amp; Semítico Etíope", S_GROUP, 460, 280, 170, 30)
    tb.add_edge(b_sem, b_arab_eth, style=S_EDGE_TOPDOWN)
    arab_eth_langs = [
        ("Árabe Clássico †", S_EXTINCT),
        ("<b>Árabe Moderno (العربية)</b> ~380M", S_LIVING),
        ("Maltês (Malti - UE)", S_LIVING),
        ("Ge'ez † (Litúrgico)", S_EXTINCT),
        ("<b>Amárico (አማርኛ)</b> ~32M", S_LIVING),
        ("Tigrínia (ትግርኛ)", S_LIVING)
    ]
    tb.add_vertical_children(b_arab_eth, arab_eth_langs, 460, start_y=325, col_w=170, child_h=30, y_step=38, indent=18)

    # 1.2 Egyptian, Berber, Chadic, Cushitic
    b_egypt = tb.add_node("<b>Egípcio Antigo †</b>", S_SUBFAMILY, 650, 225, 160, 34)
    tb.add_edge(f_afro, b_egypt, style=S_EDGE_TOPDOWN)
    egypt_langs = [
        ("Egípcio Arcaico †", S_EXTINCT),
        ("Demótico †", S_EXTINCT),
        ("Copta (ⲘⲉⲧⲢⲉⲙⲛ̀ⲭⲏⲙⲓ) †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_egypt, egypt_langs, 650, start_y=275, col_w=160, child_h=30, y_step=38, indent=18)

    b_berber = tb.add_node("<b>Proto-Berbere (Amazigh)</b>", S_SUBFAMILY, 830, 225, 170, 34)
    tb.add_edge(f_afro, b_berber, style=S_EDGE_TOPDOWN)
    berber_langs = [
        ("Tamazight (ⵜⴰⵎⴰⵣⵉⵖⵜ)", S_LIVING),
        ("Shilha / Tashelhit ~5M", S_LIVING),
        ("Cabila (Taqbaylit) ~5M", S_LIVING),
        ("Tuaregue (Tamasheq)", S_LIVING),
        ("Guanche † (Canárias)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_berber, berber_langs, 830, start_y=275, col_w=170, child_h=30, y_step=38, indent=18)

    b_chadic = tb.add_node("<b>Proto-Chádico</b>", S_SUBFAMILY, 1020, 225, 165, 34)
    tb.add_edge(f_afro, b_chadic, style=S_EDGE_TOPDOWN)
    chadic_langs = [
        ("<b>Hauçá (Hausa) ~77M</b>", S_LIVING),
        ("Bade / Bole", S_LIVING),
        ("Kotoko (Lago Chade)", S_LIVING)
    ]
    tb.add_vertical_children(b_chadic, chadic_langs, 1020, start_y=275, col_w=165, child_h=32, y_step=40, indent=18)

    b_cush = tb.add_node("<b>Proto-Cuxítico</b>", S_SUBFAMILY, 1205, 225, 155, 34)
    tb.add_edge(f_afro, b_cush, style=S_EDGE_TOPDOWN)
    cush_langs = [
        ("<b>Somali (Af-Soomaali)</b> ~22M", S_LIVING),
        ("<b>Oromo (Afaan Oromoo)</b> ~37M", S_LIVING),
        ("Afar / Sidamo", S_LIVING)
    ]
    tb.add_vertical_children(b_cush, cush_langs, 1205, start_y=275, col_w=155, child_h=32, y_step=40, indent=18)

    # ==========================================
    # 2. PROTO-NÍGER-CONGO
    # ==========================================
    f_nc = tb.add_node(
        "<b>PROTO-NÍGER-CONGO</b><br>"
        "<i>c. 5000–4000 a.C. — África Ocidental (Bacia do Rio Níger / Transição Sahel-Floresta)</i>",
        S_FAMILY, 1380, 140, 1370, 52
    )
    
    # 2.1 Bantu
    b_bantu = tb.add_node("<b>Proto-Bantu (c. 1500 a.C. — Camarões/Nigéria) ~350M</b>", S_SUBFAMILY, 1380, 225, 520, 36)
    tb.add_edge(f_nc, b_bantu, style=S_EDGE_TOPDOWN)
    
    # Bantu East & Central
    b_bantu_ec = tb.add_node("Bantu Oriental &amp; Central", S_GROUP, 1380, 280, 250, 30)
    tb.add_edge(b_bantu, b_bantu_ec, style=S_EDGE_TOPDOWN)
    bantu_ec_langs = [
        ("<b>Suaíli / Swahili</b> ~150M total", S_LIVING),
        ("Lingala (R.D. Congo) ~15M", S_LIVING),
        ("Quicongo (Kikongo)", S_LIVING),
        ("Luganda (Uganda) ~10M", S_LIVING),
        ("Kinyarwanda ~12M", S_LIVING),
        ("Kirundi ~11M", S_LIVING),
        ("Quimbundo (Angola)", S_LIVING),
        ("Umbundu (Angola) ~6M", S_LIVING)
    ]
    tb.add_vertical_children(b_bantu_ec, bantu_ec_langs, 1380, start_y=325, col_w=250, child_h=30, y_step=38, indent=22)

    # Bantu Southern
    b_bantu_s = tb.add_node("Bantu Meridional (Nguni/Sotho)", S_GROUP, 1650, 280, 250, 30)
    tb.add_edge(b_bantu, b_bantu_s, style=S_EDGE_TOPDOWN)
    bantu_s_langs = [
        ("<b>Zulu (isiZulu)</b> ~12M", S_LIVING),
        ("<b>Xhosa (isiXhosa)</b> ~8M", S_LIVING),
        ("Shona (chiShona) ~11M", S_LIVING),
        ("Sesotho / Setswana", S_LIVING),
        ("Sepedi / Changāna", S_LIVING),
        ("Macua (Moçambique) ~5M", S_LIVING),
        ("Chichewa (Malawi) ~12M", S_LIVING)
    ]
    tb.add_vertical_children(b_bantu_s, bantu_s_langs, 1650, start_y=325, col_w=250, child_h=30, y_step=38, indent=22)

    # 2.2 Volta-Niger
    b_vn = tb.add_node("<b>Proto-Volta-Níger</b>", S_SUBFAMILY, 1920, 225, 260, 34)
    tb.add_edge(f_nc, b_vn, style=S_EDGE_TOPDOWN)
    vn_langs = [
        ("<b>Iorubá (Èdè Yorùbá)</b> ~45M", S_LIVING),
        ("<b>Igbo (Asụsụ Igbo)</b> ~30M", S_LIVING),
        ("Edo / Bini", S_LIVING),
        ("Igala / Idoma", S_LIVING),
        ("Nupe / Urhobo", S_LIVING)
    ]
    tb.add_vertical_children(b_vn, vn_langs, 1920, start_y=275, col_w=260, child_h=30, y_step=38, indent=20)

    # 2.3 Atlantic
    b_atl = tb.add_node("<b>Proto-Atlântico Ocidental</b>", S_SUBFAMILY, 2200, 225, 260, 34)
    tb.add_edge(f_nc, b_atl, style=S_EDGE_TOPDOWN)
    atl_langs = [
        ("<b>Fula / Fulani (Pulaar)</b> ~35M", S_LIVING),
        ("<b>Wolof (Senegal)</b> ~12M", S_LIVING),
        ("Serer / Jola", S_LIVING),
        ("Temne (Serra Leoa)", S_LIVING)
    ]
    tb.add_vertical_children(b_atl, atl_langs, 2200, start_y=275, col_w=260, child_h=30, y_step=38, indent=20)

    # 2.4 Kwa & Mande
    b_kwa_mande = tb.add_node("<b>Proto-Kwa &amp; Proto-Mandê</b>", S_SUBFAMILY, 2480, 225, 270, 34)
    tb.add_edge(f_nc, b_kwa_mande, style=S_EDGE_TOPDOWN)
    km_langs = [
        ("Akan (Twi/Fante - Gana) ~11M", S_LIVING),
        ("Ewe (Èʋegbe - Gana/Togo)", S_LIVING),
        ("Baoulé (Costa do Marfim)", S_LIVING),
        ("Bambara (Mali) ~14M", S_LIVING),
        ("Mandinka / Maninka", S_LIVING),
        ("Mossi (Burkina Faso) ~9M", S_LIVING)
    ]
    tb.add_vertical_children(b_kwa_mande, km_langs, 2480, start_y=275, col_w=270, child_h=30, y_step=38, indent=20)

    # ==========================================
    # 3. PROTO-DRAVÍDICO
    # ==========================================
    f_drav = tb.add_node(
        "<b>PROTO-DRAVÍDICO</b><br>"
        "<i>c. 3000–2500 a.C. — Planalto do Decão / Vale do Rio Indo (Índia)</i>",
        S_FAMILY, 2770, 140, 970, 52
    )
    
    # 3.1 South Dravidian
    b_sdrav = tb.add_node("<b>Proto-Dravídico Meridional</b>", S_SUBFAMILY, 2770, 225, 310, 34)
    tb.add_edge(f_drav, b_sdrav, style=S_EDGE_TOPDOWN)
    sdrav_langs = [
        ("Tâmil Antigo †", S_EXTINCT),
        ("<b>Tâmil (தமிழ்)</b> ~85M", S_LIVING),
        ("<b>Malaiala (മലയാളം)</b> ~38M", S_LIVING),
        ("<b>Canarês (ಕನ್ನಡ)</b> ~45M", S_LIVING),
        ("Tulu (ತುಳು) ~2M", S_LIVING),
        ("Badaga / Toda / Kota", S_LIVING)
    ]
    tb.add_vertical_children(b_sdrav, sdrav_langs, 2770, start_y=275, col_w=310, child_h=30, y_step=38, indent=22)

    # 3.2 South-Central Dravidian
    b_scdrav = tb.add_node("<b>Proto-Dravídico Sul-Central</b>", S_SUBFAMILY, 3100, 225, 310, 34)
    tb.add_edge(f_drav, b_scdrav, style=S_EDGE_TOPDOWN)
    scdrav_langs = [
        ("Telugu Antigo †", S_EXTINCT),
        ("<b>Télugo / Telugu (తెలుగు)</b> ~86M", S_LIVING),
        ("Gondi (Gōndi) ~3M", S_LIVING),
        ("Kui / Kuvi / Konda", S_LIVING),
        ("Kolami (Dravídico Central)", S_LIVING)
    ]
    tb.add_vertical_children(b_scdrav, scdrav_langs, 3100, start_y=275, col_w=310, child_h=30, y_step=38, indent=22)

    # 3.3 North Dravidian
    b_ndrav = tb.add_node("<b>Proto-Dravídico Setentrional</b>", S_SUBFAMILY, 3430, 225, 310, 34)
    tb.add_edge(f_drav, b_ndrav, style=S_EDGE_TOPDOWN)
    ndrav_langs = [
        ("<b>Brahui (براهوئی)</b> ~2,5M<br><i>Ilha linguística no Baluchistão</i>", S_LIVING),
        ("Kurukh / Oraon ~2M", S_LIVING),
        ("Malto / Sauria Paharia", S_LIVING)
    ]
    tb.add_vertical_children(b_ndrav, ndrav_langs, 3430, start_y=275, col_w=310, child_h=34, y_step=42, indent=22)

    return tb

if __name__ == "__main__":
    build_afroasiatic_nigercongo_page()
    print("Afroasiatic, Niger-Congo & Dravidian updated with explicit Proto-languages.")
