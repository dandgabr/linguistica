#!/usr/bin/env python3
"""
Generator for East & Southeast Asian Families with explicit Protolanguages:
Proto-Sino-Tibetan, Proto-Hmong-Mien, Proto-Kra-Dai, Proto-Austroasiatic, Proto-Austronesian.
"""

from tree_builder import (
    TreeBuilder, S_LIVING, S_EXTINCT, S_BRANCH,
    S_FAMILY, S_SUBFAMILY, S_GROUP, S_EDGE, S_EDGE_TOPDOWN, S_EDGE_GUTTER, S_LEGEND
)

def build_east_asia_page():
    tb = TreeBuilder("east_asia", "2. Sino-Tibetana, Kra-Dai, Austroasiática & Austronésia", width=4200, height=2400)
    tb.add_legend(40, 40)
    
    # Title
    tb.add_node(
        "<b>ÁRVORE FILOGENÉTICA DAS PROTOLÍNGUAS DO LESTE E SUDESTE ASIÁTICO &amp; PACÍFICO</b><br>"
        "<i>Reconstruções Comparativas: Proto-Sino-Tibetano, Proto-Austronésio, Proto-Austroasiático, Proto-Kra-Dai e Proto-Hmong-Mien</i><br>"
        "<span style='font-size:10px;'>Baseado em Cole &amp; Siebert-Cole (Parte 2, ResearchGate 2026), Sagart, Matisoff &amp; Blust</span>",
        S_FAMILY, 340, 40, 880, 65
    )
    
    # ==========================================
    # 1. PROTO-SINO-TIBETANO
    # ==========================================
    f_st = tb.add_node(
        "<b>PROTO-SINO-TIBETANO (PST)</b><br>"
        "<i>c. 4500–4000 a.C. — Bacia do Rio Amarelo (Cultura Yangshao) / Leste do Tibete</i>",
        S_FAMILY, 50, 140, 780, 52
    )
    
    # 1.1 Proto-Sínico
    b_sin = tb.add_node("<b>Proto-Sínico (Proto-Sinitic)</b>", S_SUBFAMILY, 50, 225, 370, 36)
    tb.add_edge(f_st, b_sin, style=S_EDGE_TOPDOWN)
    
    ochinese = tb.add_node("Chinês Antigo † (Archaic Chinese - 上古漢語)", S_EXTINCT, 74, 280, 346, 30)
    tb.add_edge(b_sin, ochinese, style=S_EDGE_GUTTER)
    
    mchinese = tb.add_node("Chinês Médio † (Middle Chinese - 中古漢語)", S_EXTINCT, 74, 325, 346, 30)
    tb.add_edge(ochinese, mchinese, style=S_EDGE_TOPDOWN)
    
    sinitic_langs = [
        ("Mandarim Padrão (官话 / 普通话) ~930M", S_LIVING),
        ("Cantonês / Yue (粤语 / 廣東話) ~85M", S_LIVING),
        ("Wu / Xangainês (吴语 / 上海话) ~82M", S_LIVING),
        ("Min Nan / Hokkien / Taiwanês (闽南语) ~50M", S_LIVING),
        ("Hakka / Kejia (客家话) ~44M", S_LIVING),
        ("Xiang / Hunanês (湘语) ~38M", S_LIVING),
        ("Gan / Jiangxinês (赣语) ~22M", S_LIVING),
        ("Jin (晋语) ~47M", S_LIVING),
        ("Dungan (Mandarim em cirílico)", S_LIVING)
    ]
    tb.add_vertical_children(mchinese, sinitic_langs, 50, start_y=370, col_w=370, child_h=30, y_step=38, indent=24)

    # 1.2 Proto-Tibeto-Birmanês
    b_tb = tb.add_node("<b>Proto-Tibeto-Birmanês</b>", S_SUBFAMILY, 440, 225, 390, 36)
    tb.add_edge(f_st, b_tb, style=S_EDGE_TOPDOWN)
    
    b_tib = tb.add_node("Proto-Bódico (Tibético)", S_GROUP, 440, 280, 390, 28)
    tb.add_edge(b_tb, b_tib, style=S_EDGE_TOPDOWN)
    tib_langs = [
        ("Tibetano Clássico † (ཆོས་སྐད)", S_EXTINCT),
        ("Tibetano Lhasa (བོད་སྐད)", S_LIVING),
        ("Dzongkha (Butão - རྫོང་ཁ)", S_LIVING),
        ("Sherpa / Ladakhi", S_LIVING)
    ]
    tb.add_vertical_children(b_tib, tib_langs, 440, start_y=320, col_w=390, child_h=28, y_step=36, indent=24)
    
    b_burm = tb.add_node("Proto-Lolo-Búrmico &amp; Qiangic", S_GROUP, 440, 485, 390, 28)
    tb.add_edge(b_tb, b_burm, style=S_EDGE_GUTTER)
    burm_langs = [
        ("Birmanês Antigo †", S_EXTINCT),
        ("Birmanês (မြန်မာစာ - Mianmar)", S_LIVING),
        ("Yi / Nuosu (ꆈꌠ꒿ - Sichuan)", S_LIVING),
        ("Karen / Kayin", S_LIVING),
        ("Tangut † (Império Xixia)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_burm, burm_langs, 440, start_y=525, col_w=390, child_h=28, y_step=36, indent=24)

    # ==========================================
    # 2. PROTO-HMONG-MIEN
    # ==========================================
    f_hm = tb.add_node(
        "<b>PROTO-HMONG-MIEN</b><br>"
        "<i>c. 2500 a.C. — Bacia dos Rios Yangtzé e Han (China Central)</i>",
        S_FAMILY, 850, 140, 260, 52
    )
    
    b_hmong = tb.add_node("<b>Proto-Hmongico (Miao)</b>", S_SUBFAMILY, 850, 225, 260, 32)
    tb.add_edge(f_hm, b_hmong, style=S_EDGE_TOPDOWN)
    hm_langs = [
        ("Hmong Branco (Hmoob Dawb)", S_LIVING),
        ("Hmong Verde (Hmoob Leeg)", S_LIVING),
        ("Miao Central / Hmu", S_LIVING)
    ]
    tb.add_vertical_children(b_hmong, hm_langs, 850, start_y=270, col_w=260, child_h=28, y_step=36, indent=22)
    
    b_mien = tb.add_node("<b>Proto-Mienico (Yao)</b>", S_SUBFAMILY, 850, 395, 260, 32)
    tb.add_edge(f_hm, b_mien, style=S_EDGE_GUTTER)
    mien_langs = [
        ("Iu Mien (Yao)", S_LIVING),
        ("Kim Mun / Lanten", S_LIVING)
    ]
    tb.add_vertical_children(b_mien, mien_langs, 850, start_y=440, col_w=260, child_h=28, y_step=36, indent=22)

    # ==========================================
    # 3. PROTO-KRA-DAI
    # ==========================================
    f_kd = tb.add_node(
        "<b>PROTO-KRA-DAI (TAI-KADAI)</b><br>"
        "<i>c. 2000–1500 a.C. — Litoral Sul da China (Guangdong / Guangxi)</i>",
        S_FAMILY, 1130, 140, 480, 52
    )
    
    b_tai = tb.add_node("<b>Proto-Tai</b>", S_SUBFAMILY, 1130, 225, 230, 34)
    tb.add_edge(f_kd, b_tai, style=S_EDGE_TOPDOWN)
    tai_langs = [
        ("Tailandês / Siamês (ไทย) ~60M", S_LIVING),
        ("Lao / Laosiano (ພາສາລາວ) ~30M", S_LIVING),
        ("Isan (Tailandês do Nordeste)", S_LIVING),
        ("Shan (လိၵ်ႈတႆး - Mianmar)", S_LIVING),
        ("Zhuang (Vahcuengh - Guangxi) ~16M", S_LIVING),
        ("Bouyei (Guizhou)", S_LIVING),
        ("Ahom † (Índia)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_tai, tai_langs, 1130, start_y=270, col_w=230, child_h=30, y_step=38, indent=22)

    b_non_tai = tb.add_node("<b>Proto-Kam-Sui &amp; Kra</b>", S_SUBFAMILY, 1380, 225, 230, 34)
    tb.add_edge(f_kd, b_non_tai, style=S_EDGE_TOPDOWN)
    non_tai_langs = [
        ("Kam / Dong (Guizhou/Hunan)", S_LIVING),
        ("Sui / Shui (Guizhou)", S_LIVING),
        ("Maonan / Mulam (Guangxi)", S_LIVING),
        ("Gelao (Kra)", S_LIVING),
        ("Hlai (Ilha de Hainan)", S_LIVING)
    ]
    tb.add_vertical_children(b_non_tai, non_tai_langs, 1380, start_y=270, col_w=230, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 4. PROTO-AUSTROASIÁTICO
    # ==========================================
    f_aa = tb.add_node(
        "<b>PROTO-AUSTROASIÁTICO</b><br>"
        "<i>c. 2500–2000 a.C. — Vales dos Rios Yangtzé e Mekong</i>",
        S_FAMILY, 1630, 140, 520, 52
    )
    
    b_mk = tb.add_node("<b>Proto-Mon-Khmer &amp; Viético</b>", S_SUBFAMILY, 1630, 225, 250, 34)
    tb.add_edge(f_aa, b_mk, style=S_EDGE_TOPDOWN)
    mk_langs = [
        ("Vietnamita Antigo †", S_EXTINCT),
        ("Vietnamita (Tiếng Việt) ~85M", S_LIVING),
        ("Muong (Vietnã)", S_LIVING),
        ("Khmer Antigo †", S_EXTINCT),
        ("Khmer Moderno (ភាសាខ្មែរ) ~17M", S_LIVING),
        ("Mon Moderno (Mianmar/Tailândia)", S_LIVING),
        ("Khasi (Meghalaya, Índia)", S_LIVING),
        ("Wa (Estado Wa, Mianmar)", S_LIVING)
    ]
    tb.add_vertical_children(b_mk, mk_langs, 1630, start_y=270, col_w=250, child_h=30, y_step=38, indent=22)

    b_munda = tb.add_node("<b>Proto-Munda (Índia)</b>", S_SUBFAMILY, 1900, 225, 250, 34)
    tb.add_edge(f_aa, b_munda, style=S_EDGE_TOPDOWN)
    munda_langs = [
        ("Santali (ᱥᱟᱱᱛᱟᱲᱤ) ~7,6M", S_LIVING),
        ("Mundari (Jharkhand, Índia)", S_LIVING),
        ("Ho (Warang Chiti)", S_LIVING),
        ("Korku (Madhya Pradesh)", S_LIVING),
        ("Sora (Savara - Odisha)", S_LIVING)
    ]
    tb.add_vertical_children(b_munda, munda_langs, 1900, start_y=270, col_w=250, child_h=30, y_step=38, indent=22)

    # ==========================================
    # 5. PROTO-AUSTRONÉSIO (PAN)
    # ==========================================
    f_an = tb.add_node(
        "<b>PROTO-AUSTRONÉSIO (PAN)</b><br>"
        "<i>c. 4000–3500 a.C. — Ilha de Taiwan (Formosa)</i>",
        S_FAMILY, 2170, 140, 1980, 52
    )
    
    # 5.1 Formosan
    b_form = tb.add_node("<b>Ramos Formosianos</b><br><i>(Troncos primários basais)</i>", S_SUBFAMILY, 2170, 225, 240, 38)
    tb.add_edge(f_an, b_form, style=S_EDGE_TOPDOWN)
    form_langs = [
        ("Atayal (Tayal)", S_LIVING),
        ("Amis ('Amis / Pangcah)", S_LIVING),
        ("Paiwan (Sul de Taiwan)", S_LIVING),
        ("Bunun (Taiwan Central)", S_LIVING),
        ("Siraya † (Extinta)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_form, form_langs, 2170, start_y=280, col_w=240, child_h=30, y_step=38, indent=22)

    # 5.2 Proto-Malayo-Polynesian
    b_mp = tb.add_node("<b>Proto-Malaio-Polinésio (PMP)</b><br><i>(Dispersão marítima c. 2200 a.C.)</i>", S_SUBFAMILY, 2430, 225, 1720, 38)
    tb.add_edge(f_an, b_mp, style=S_EDGE_TOPDOWN)
    
    # Sub-columns:
    b_sunda = tb.add_node("<b>Malaio-Súndico &amp; Barito</b>", S_GROUP, 2430, 280, 410, 30)
    tb.add_edge(b_mp, b_sunda, style=S_EDGE_TOPDOWN)
    sunda_langs = [
        ("Malaio Antigo †", S_EXTINCT),
        ("Malaio (Bahasa Melayu)", S_LIVING),
        ("Indonésio (Bahasa Indonesia) ~200M", S_LIVING),
        ("Javanês (Basa Jawa) ~85M", S_LIVING),
        ("Sudanês (Basa Sunda) ~40M", S_LIVING),
        ("Madurês ~14M / Balinês", S_LIVING),
        ("Malgaxe (Madagascar) ~25M", S_LIVING),
        ("Acehnês / Cham", S_LIVING)
    ]
    tb.add_vertical_children(b_sunda, sunda_langs, 2430, start_y=325, col_w=410, child_h=30, y_step=38, indent=24)

    b_phil = tb.add_node("<b>Proto-Filipino (Filipinas)</b>", S_GROUP, 2860, 280, 390, 30)
    tb.add_edge(b_mp, b_phil, style=S_EDGE_TOPDOWN)
    phil_langs = [
        ("Tagalo / Filipino (Tagalog) ~85M", S_LIVING),
        ("Cebuano / Bisaya ~25M", S_LIVING),
        ("Ilocano ~9M / Hiligaynon ~9M", S_LIVING),
        ("Bikol / Waray-Waray", S_LIVING),
        ("Kapampangan / Pangasinan", S_LIVING),
        ("Tausug / Maranao", S_LIVING)
    ]
    tb.add_vertical_children(b_phil, phil_langs, 2860, start_y=325, col_w=390, child_h=30, y_step=38, indent=24)

    b_sula = tb.add_node("<b>Sulawesi &amp; Timor</b>", S_GROUP, 3270, 280, 380, 30)
    tb.add_edge(b_mp, b_sula, style=S_EDGE_TOPDOWN)
    sula_langs = [
        ("Bugis (Basa Ugi)", S_LIVING),
        ("Macassar (Mangkasara')", S_LIVING),
        ("Toraja-Sa'dan", S_LIVING),
        ("Tetum (Tetun - Timor-Leste)", S_LIVING),
        ("Manggarai (Flores) / Sasak", S_LIVING)
    ]
    tb.add_vertical_children(b_sula, sula_langs, 3270, start_y=325, col_w=380, child_h=30, y_step=38, indent=24)

    b_oce = tb.add_node("<b>Proto-Oceânico &amp; Polinésio</b>", S_GROUP, 3670, 280, 480, 30)
    tb.add_edge(b_mp, b_oce, style=S_EDGE_TOPDOWN)
    oce_langs = [
        ("Fijiano (Vosa Vakaviti - Fiji)", S_LIVING),
        ("Samoano (Gagana Sāmoa - Samoa)", S_LIVING),
        ("Tonganês (Lea Faka-Tonga)", S_LIVING),
        ("Maori (Te Reo Māori - N. Zelândia)", S_LIVING),
        ("Havaiano (ʻŌlelo Hawaiʻi - Havaí)", S_LIVING),
        ("Taitiano (Reo Tahiti)", S_LIVING),
        ("Rapa Nui (Ilha de Páscoa)", S_LIVING),
        ("Chamorro (Guam) / Palauano", S_LIVING)
    ]
    tb.add_vertical_children(b_oce, oce_langs, 3670, start_y=325, col_w=480, child_h=30, y_step=38, indent=24)

    return tb

if __name__ == "__main__":
    build_east_asia_page()
    print("East Asia updated with explicit Proto-languages.")
