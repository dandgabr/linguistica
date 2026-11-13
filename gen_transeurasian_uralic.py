#!/usr/bin/env python3
"""
Generator for Northeast Asian (Transeurasian/Altaic Areal), Uralic and Caucasian Protolanguages.
Explicit Proto-languages at all roots.
"""

from tree_builder import (
    TreeBuilder, S_LIVING, S_EXTINCT, S_BRANCH,
    S_FAMILY, S_SUBFAMILY, S_GROUP, S_EDGE, S_EDGE_TOPDOWN, S_EDGE_GUTTER, S_LEGEND
)

def build_transeurasian_uralic_page():
    tb = TreeBuilder("trans_uralic", "3. Transeurasiáticas, Urálicas & Caucásicas", width=4200, height=2400)
    tb.add_legend(40, 40)
    
    # Title
    tb.add_node(
        "<b>ÁRVORE FILOGENÉTICA DAS PROTOLÍNGUAS TRANSEURASIÁTICAS, URÁLICAS &amp; CAUCÁSICAS</b><br>"
        "<i>Reconstruções: Proto-Túrquico, Proto-Mongólico, Proto-Tungúsico, Proto-Japônico, Proto-Coreano, Proto-Urálico e Proto-Kartveliano</i><br>"
        "<span style='font-size:10px;'>Baseado em Cole (2026), Robbeets (Transeurasian phylogenetics), Johanson &amp; Csató, Janhunen &amp; Campbell</span>",
        S_FAMILY, 340, 40, 880, 65
    )
    
    # ==========================================
    # 1. PROTO-TÚRQUICO
    # ==========================================
    f_turk = tb.add_node(
        "<b>PROTO-TÚRQUICO</b><br>"
        "<i>c. 500 a.C. — Montes Altai / Sibéria Meridional / Mongólia Ocidental</i>",
        S_FAMILY, 50, 140, 940, 52
    )
    
    b_common = tb.add_node("<b>Proto-Túrquico Comum (Shaz Turkic)</b>", S_SUBFAMILY, 50, 225, 700, 34)
    tb.add_edge(f_turk, b_common, style=S_EDGE_TOPDOWN)
    
    old_turk = tb.add_node("Antigo Túrquico † (Orkhon - 𐰋𐰃𐱅𐰃𐰏)", S_EXTINCT, 50, 275, 700, 30)
    tb.add_edge(b_common, old_turk, style=S_EDGE_TOPDOWN)
    
    # 1.1 Oghuz
    b_oghuz = tb.add_node("<b>Proto-Oguz (Sudoeste)</b>", S_GROUP, 50, 325, 220, 30)
    tb.add_edge(old_turk, b_oghuz, style=S_EDGE_TOPDOWN)
    oghuz_langs = [
        ("Turco Otomano †", S_EXTINCT),
        ("Turco (Türkçe) ~85M", S_LIVING),
        ("Azerbaijano ~30M", S_LIVING),
        ("Turcomeno", S_LIVING),
        ("Gagauz / Qashqai", S_LIVING)
    ]
    tb.add_vertical_children(b_oghuz, oghuz_langs, 50, start_y=370, col_w=220, child_h=30, y_step=38, indent=20)

    # 1.2 Kipchak
    b_kipchak = tb.add_node("<b>Proto-Quiptchaco (Noroeste)</b>", S_GROUP, 290, 325, 220, 30)
    tb.add_edge(old_turk, b_kipchak, style=S_EDGE_TOPDOWN)
    kipchak_langs = [
        ("Cumano †", S_EXTINCT),
        ("Cazaque (Қазақ) ~15M", S_LIVING),
        ("Quirguiz (Кыргыз)", S_LIVING),
        ("Tártaro (Татар) ~5M", S_LIVING),
        ("Bashkir / Karakalpak", S_LIVING),
        ("Tártaro da Crimeia", S_LIVING)
    ]
    tb.add_vertical_children(b_kipchak, kipchak_langs, 290, start_y=370, col_w=220, child_h=30, y_step=38, indent=20)

    # 1.3 Karluk & Siberian
    b_karluk = tb.add_node("<b>Proto-Karluk &amp; Siberiano</b>", S_GROUP, 530, 325, 220, 30)
    tb.add_edge(old_turk, b_karluk, style=S_EDGE_TOPDOWN)
    karluk_langs = [
        ("Chagatai †", S_EXTINCT),
        ("Uzbeque (O'zbek) ~34M", S_LIVING),
        ("Uigur (ئۇيغۇر) ~12M", S_LIVING),
        ("Iacuta / Sakha ~450k", S_LIVING),
        ("Tuvan / Khakas", S_LIVING)
    ]
    tb.add_vertical_children(b_karluk, karluk_langs, 530, start_y=370, col_w=220, child_h=30, y_step=38, indent=20)

    # 1.4 Oghur
    b_oghur = tb.add_node("<b>Proto-Ogúrico (Lir-Turkic)</b>", S_SUBFAMILY, 770, 225, 220, 34)
    tb.add_edge(f_turk, b_oghur, style=S_EDGE_TOPDOWN)
    oghur_langs = [
        ("Búlgaro do Volga †", S_EXTINCT),
        ("Khazar †", S_EXTINCT),
        ("Chuvash (Чӑвашла) ~1M", S_LIVING)
    ]
    tb.add_vertical_children(b_oghur, oghur_langs, 770, start_y=275, col_w=220, child_h=30, y_step=38, indent=20)

    # ==========================================
    # 2. PROTO-MONGÓLICO
    # ==========================================
    f_mong = tb.add_node(
        "<b>PROTO-MONGÓLICO</b><br>"
        "<i>c. séc. IV–VI d.C. — Bacia dos Rios Amur e Shilka (Mongólia/Manchúria)</i>",
        S_FAMILY, 1010, 140, 240, 52
    )
    
    b_mong_sub = tb.add_node("<b>Proto-Mongólico Central</b>", S_SUBFAMILY, 1010, 225, 240, 34)
    tb.add_edge(f_mong, b_mong_sub, style=S_EDGE_TOPDOWN)
    
    mid_mong = tb.add_node("Mongol Médio † (Império de Genghis Khan)", S_EXTINCT, 1032, 275, 218, 30)
    tb.add_edge(b_mong_sub, mid_mong, style=S_EDGE_GUTTER)
    
    mong_langs = [
        ("Mongol Khalkha (Монгол) ~3M", S_LIVING),
        ("Buriato (Буряад - Sibéria)", S_LIVING),
        ("Kalmyk (Хальмг - Europa)", S_LIVING),
        ("Santa / Dongxiang", S_LIVING),
        ("Daur (Arcaico)", S_LIVING)
    ]
    tb.add_vertical_children(mid_mong, mong_langs, 1010, start_y=320, col_w=240, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 3. PROTO-TUNGÚSICO
    # ==========================================
    f_tung = tb.add_node(
        "<b>PROTO-TUNGÚSICO</b><br>"
        "<i>c. 500 a.C. — Bacia do Rio Amur / Sibéria Oriental</i>",
        S_FAMILY, 1270, 140, 230, 52
    )
    
    b_tung_sub = tb.add_node("<b>Ramo Tungúsico</b>", S_SUBFAMILY, 1270, 225, 230, 34)
    tb.add_edge(f_tung, b_tung_sub, style=S_EDGE_TOPDOWN)
    
    jurchen = tb.add_node("Jurchen † (Dinastia Jin)", S_EXTINCT, 1292, 275, 208, 30)
    tb.add_edge(b_tung_sub, jurchen, style=S_EDGE_GUTTER)
    
    tung_langs = [
        ("Manchu (ᠮᠠᠨᠵᡠ)", S_LIVING),
        ("Xibe / Sibe ~30k", S_LIVING),
        ("Evenki (Sibéria/China)", S_LIVING),
        ("Even (Sibéria)", S_LIVING),
        ("Nanai (Rio Amur)", S_LIVING)
    ]
    tb.add_vertical_children(jurchen, tung_langs, 1270, start_y=320, col_w=230, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 4. PROTO-JAPÔNICO
    # ==========================================
    f_jap = tb.add_node(
        "<b>PROTO-JAPÔNICO</b><br>"
        "<i>c. séc. IV–III a.C. (Período Yayoi) — Ilhas Japonesas / Kyūshū</i>",
        S_FAMILY, 1520, 140, 240, 52
    )
    
    old_jap = tb.add_node("Japonês Antigo † (Período Nara)", S_EXTINCT, 1542, 225, 218, 30)
    tb.add_edge(f_jap, old_jap, style=S_EDGE_GUTTER)
    
    mid_jap = tb.add_node("Japonês Médio †", S_EXTINCT, 1542, 270, 218, 30)
    tb.add_edge(old_jap, mid_jap, style=S_EDGE_TOPDOWN)
    
    mod_jap = tb.add_node("<b>Japonês Moderno (日本語)</b><br><i>~125M de falantes</i>", S_LIVING, 1542, 315, 218, 36)
    tb.add_edge(mid_jap, mod_jap, style=S_EDGE_TOPDOWN)
    
    b_ryu = tb.add_node("<b>Proto-Ryukyuano</b>", S_SUBFAMILY, 1520, 375, 240, 30)
    tb.add_edge(old_jap, b_ryu, style=S_EDGE_GUTTER)
    ryu_langs = [
        ("Okinawano (Uchināguchi)", S_LIVING),
        ("Amami / Miyako", S_LIVING),
        ("Yaeyama / Yonaguni", S_LIVING)
    ]
    tb.add_vertical_children(b_ryu, ryu_langs, 1520, start_y=420, col_w=240, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 5. PROTO-COREANO
    # ==========================================
    f_kor = tb.add_node(
        "<b>PROTO-COREANO</b><br>"
        "<i>c. séc. I a.C.–séc. IV d.C. — Península Coreana e Manchúria</i>",
        S_FAMILY, 1780, 140, 240, 52
    )
    
    old_kor = tb.add_node("Coreano Antigo † (Três Reinos)", S_EXTINCT, 1802, 225, 218, 30)
    tb.add_edge(f_kor, old_kor, style=S_EDGE_GUTTER)
    
    mid_kor = tb.add_node("Coreano Médio † (Hangul)", S_EXTINCT, 1802, 270, 218, 30)
    tb.add_edge(old_kor, mid_kor, style=S_EDGE_TOPDOWN)
    
    kor_langs = [
        ("<b>Coreano (한국어 / 조선말)</b> ~80M", S_LIVING),
        ("Jeju (제주말 - Ilha de Jeju)", S_LIVING),
        ("Língua de Goguryeo †", S_EXTINCT),
        ("Baekje † / Silla †", S_EXTINCT)
    ]
    tb.add_vertical_children(mid_kor, kor_langs, 1780, start_y=315, col_w=240, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 6. PROTO-URÁLICO
    # ==========================================
    f_ural = tb.add_node(
        "<b>PROTO-URÁLICO</b><br>"
        "<i>c. 2500–2000 a.C. — Montes Urais / Bacia dos Rios Volga e Kama</i>",
        S_FAMILY, 2040, 140, 1260, 52
    )
    
    proto_ural = tb.add_node("Proto-Fino-Úgrico &amp; Proto-Samoiedo", S_BRANCH, 2040, 225, 1260, 30)
    tb.add_edge(f_ural, proto_ural, style=S_EDGE_TOPDOWN)
    
    # 6.1 Ugric
    b_ugric = tb.add_node("<b>Proto-Úgrico</b>", S_GROUP, 2040, 280, 230, 30)
    tb.add_edge(proto_ural, b_ugric, style=S_EDGE_TOPDOWN)
    ugric_langs = [
        ("<b>Húngaro / Magyar</b> ~13M", S_LIVING),
        ("Khanty / Ostyak (Sibéria)", S_LIVING),
        ("Mansi / Vogul (Urais)", S_LIVING)
    ]
    tb.add_vertical_children(b_ugric, ugric_langs, 2040, start_y=325, col_w=230, child_h=30, y_step=38, indent=20)

    # 6.2 Finnic
    b_finnic = tb.add_node("<b>Proto-Bálto-Fínico</b>", S_GROUP, 2295, 280, 230, 30)
    tb.add_edge(proto_ural, b_finnic, style=S_EDGE_TOPDOWN)
    finnic_langs = [
        ("<b>Finlandês (Suomi)</b> ~5,4M", S_LIVING),
        ("<b>Estoniano (Eesti)</b> ~1,1M", S_LIVING),
        ("Carélio (Karjala)", S_LIVING),
        ("Vepse / Íngrio", S_LIVING),
        ("Livoniano † (Revivido)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_finnic, finnic_langs, 2295, start_y=325, col_w=230, child_h=30, y_step=38, indent=20)

    # 6.3 Sámi
    b_sami = tb.add_node("<b>Proto-Sámi (Lapão)</b>", S_GROUP, 2550, 280, 230, 30)
    tb.add_edge(proto_ural, b_sami, style=S_EDGE_TOPDOWN)
    sami_langs = [
        ("Sámi Setentrional", S_LIVING),
        ("Sámi de Lule / Inari", S_LIVING),
        ("Sámi Skolt", S_LIVING),
        ("Sámi Meridional", S_LIVING)
    ]
    tb.add_vertical_children(b_sami, sami_langs, 2550, start_y=325, col_w=230, child_h=30, y_step=38, indent=20)

    # 6.4 Permic & Volgaic
    b_perm = tb.add_node("<b>Proto-Pérmico &amp; Volgaico</b>", S_GROUP, 2805, 280, 230, 30)
    tb.add_edge(proto_ural, b_perm, style=S_EDGE_TOPDOWN)
    perm_langs = [
        ("Komi (Коми кыв)", S_LIVING),
        ("Udmurt (Удмурт)", S_LIVING),
        ("Mari (Олык марий)", S_LIVING),
        ("Erzya / Moksha (Mordóvia)", S_LIVING)
    ]
    tb.add_vertical_children(b_perm, perm_langs, 2805, start_y=325, col_w=230, child_h=30, y_step=38, indent=20)

    # 6.5 Samoyedic
    b_samo = tb.add_node("<b>Proto-Samoiedo (Sibéria)</b>", S_GROUP, 3060, 280, 240, 30)
    tb.add_edge(proto_ural, b_samo, style=S_EDGE_TOPDOWN)
    samo_langs = [
        ("Nenets (Ненэцяʼ вада)", S_LIVING),
        ("Enets / Nganasan", S_LIVING),
        ("Selkup (Шӧльӄумыт)", S_LIVING),
        ("Kamas † / Mator †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_samo, samo_langs, 3060, start_y=325, col_w=240, child_h=30, y_step=38, indent=20)

    # ==========================================
    # 7. PROTO-KARTVELIANO (Cáucaso Sul)
    # ==========================================
    f_kart = tb.add_node(
        "<b>PROTO-KARTVELIANO</b><br>"
        "<i>c. 2500–2000 a.C. — Região Sul da Transcaucásia</i>",
        S_FAMILY, 3320, 140, 260, 52
    )
    b_kart_sub = tb.add_node("<b>Proto-Georgiano-Zan &amp; Svano</b>", S_SUBFAMILY, 3320, 225, 260, 34)
    tb.add_edge(f_kart, b_kart_sub, style=S_EDGE_TOPDOWN)
    kart_langs = [
        ("<b>Georgiano (ქართული)</b> ~4M", S_LIVING),
        ("Mingrélio (მარგალური)", S_LIVING),
        ("Laz (ლაზური)", S_LIVING),
        ("Svano (ლუშნუ ნინ)", S_LIVING)
    ]
    tb.add_vertical_children(b_kart_sub, kart_langs, 3320, start_y=280, col_w=260, child_h=30, y_step=38, indent=22)

    return tb

if __name__ == "__main__":
    build_transeurasian_uralic_page()
    print("Transeurasian & Uralic updated with explicit Proto-languages.")
