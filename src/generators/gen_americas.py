#!/usr/bin/env python3
"""
Generator for Indigenous American Protolanguages:
North America, Mesoamerica, and South America.
Explicit Proto-languages at all roots.
"""

from tree_builder import (
    TreeBuilder, S_LIVING, S_EXTINCT, S_BRANCH,
    S_FAMILY, S_SUBFAMILY, S_GROUP, S_EDGE, S_EDGE_TOPDOWN, S_EDGE_GUTTER, S_LEGEND
)

def build_americas_page():
    tb = TreeBuilder("americas", "5. Protolínguas Indígenas das Américas", width=4200, height=2400)
    tb.add_legend(40, 40)
    
    # Title
    tb.add_node(
        "<b>ÁRVORE FILOGENÉTICA DAS PROTOLÍNGUAS INDÍGENAS DAS AMÉRICAS</b><br>"
        "<i>Reconstruções Comparativas: Proto-Tupi, Proto-Quechua, Proto-Maia, Proto-Na-Dene, Proto-Uto-Asteca e Troncos Autóctones</i><br>"
        "<span style='font-size:10px;'>Baseado em Cole &amp; Siebert-Cole (Parte 2, ResearchGate 2026), Campbell, Rodrigues (Línguas Brasileiras) &amp; Adelaar</span>",
        S_FAMILY, 340, 40, 920, 65
    )
    
    # ==========================================
    # 1. AMÉRICA DO NORTE
    # ==========================================
    f_na = tb.add_node(
        "<b>PROTOLÍNGUAS DA AMÉRICA DO NORTE</b><br>"
        "<i>Radiações do Ártico, Subártico, Grandes Planícies e Costa Oeste</i>",
        S_FAMILY, 50, 140, 1120, 52
    )
    
    # 1.1 Proto-Eskimo-Aleut
    b_ea = tb.add_node("<b>Proto-Esquimó-Aleúte</b><br><i>c. 2500 a.C. — Estreito de Bering</i>", S_SUBFAMILY, 50, 225, 205, 38)
    tb.add_edge(f_na, b_ea, style=S_EDGE_TOPDOWN)
    ea_langs = [
        ("Inuktitut (ᐃᓄᒃᑎᑐᑦ) ~40k", S_LIVING),
        ("Kalaallisut (Groenlândia) ~57k", S_LIVING),
        ("Yupik do Alasca (Yugtun)", S_LIVING),
        ("Aleúte (Unangam Tunuu)", S_LIVING),
        ("Sirenik † (Extinta)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_ea, ea_langs, 50, start_y=280, col_w=205, child_h=30, y_step=38, indent=18)

    # 1.2 Proto-Na-Dene
    b_nd = tb.add_node("<b>Proto-Na-Dene (Athabaskano)</b><br><i>c. 3000 a.C. — Alasca / Yukon</i>", S_SUBFAMILY, 275, 225, 220, 38)
    tb.add_edge(f_na, b_nd, style=S_EDGE_TOPDOWN)
    nd_langs = [
        ("<b>Navajo (Diné bizaad) ~170k</b><br><i>Maior língua nativa dos EUA</i>", S_LIVING),
        ("Apache Ocidental", S_LIVING),
        ("Chipewyan (Dënësųłinë́)", S_LIVING),
        ("Tłı̨chǫ / Dogrib (Canadá)", S_LIVING),
        ("Tlingit (Lingít)", S_LIVING),
        ("Eyak † (Extinta em 2008)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_nd, nd_langs, 275, start_y=280, col_w=220, child_h=32, y_step=40, indent=20)

    # 1.3 Proto-Algic
    b_alg = tb.add_node("<b>Proto-Álgico (Algonquiano)</b><br><i>c. 2000 a.C. — Rio Columbia</i>", S_SUBFAMILY, 515, 225, 210, 38)
    tb.add_edge(f_na, b_alg, style=S_EDGE_TOPDOWN)
    alg_langs = [
        ("Cree (ᓀᐦᐃᔭᐍᐏᐣ) ~117k", S_LIVING),
        ("Ojibwe (Anishinaabe) ~50k", S_LIVING),
        ("Blackfoot / Pés-Pretos", S_LIVING),
        ("Cheyenne (Tsėhésenėstsestȯtse)", S_LIVING),
        ("Innu / Montagnais", S_LIVING),
        ("Powhatan † (Virgínia)", S_EXTINCT)
    ]
    tb.add_vertical_children(b_alg, alg_langs, 515, start_y=280, col_w=210, child_h=30, y_step=38, indent=18)

    # 1.4 Proto-Iroquoian & Proto-Siouan
    b_iroq_sioux = tb.add_node("<b>Proto-Iroquês &amp; Proto-Sioux</b><br><i>c. 1500–1000 a.C. — Grandes Lagos / Mississippi</i>", S_SUBFAMILY, 745, 225, 205, 38)
    tb.add_edge(f_na, b_iroq_sioux, style=S_EDGE_TOPDOWN)
    is_langs = [
        ("Cherokee (ᏣᎳᎩ / Tsalagi)", S_LIVING),
        ("Mohawk (Kanien'kéha)", S_LIVING),
        ("Seneca / Oneida", S_LIVING),
        ("<b>Lakota / Dakota (Sioux) ~25k</b>", S_LIVING),
        ("Crow / Apsáalooke", S_LIVING),
        ("Mandan †", S_EXTINCT)
    ]
    tb.add_vertical_children(b_iroq_sioux, is_langs, 745, start_y=280, col_w=205, child_h=30, y_step=38, indent=18)

    # 1.5 Northern Uto-Aztecan & Salishan
    b_uto_n = tb.add_node("<b>Proto-Uto-Asteca N. &amp; Salish</b><br><i>Sudoeste dos EUA e Costa Noroeste</i>", S_SUBFAMILY, 970, 225, 200, 38)
    tb.add_edge(f_na, b_uto_n, style=S_EDGE_TOPDOWN)
    un_langs = [
        ("Hopi (Hopílavayi - Arizona)", S_LIVING),
        ("Shoshone (Sosoni')", S_LIVING),
        ("Comanche (Nʉmʉ Tekwapʉ)", S_LIVING),
        ("Paiute / Ute", S_LIVING),
        ("Salish da Costa / Lushootseed", S_LIVING)
    ]
    tb.add_vertical_children(b_uto_n, un_langs, 970, start_y=280, col_w=200, child_h=30, y_step=38, indent=18)

    # ==========================================
    # 2. MESOAMÉRICA
    # ==========================================
    f_meso = tb.add_node(
        "<b>PROTOLÍNGUAS DA MESOAMÉRICA</b><br>"
        "<i>Grandes civilizações: Proto-Maia, Proto-Náuatle, Proto-Oto-Mangue e Olmeca/Mixe-Zoque</i>",
        S_FAMILY, 1190, 140, 890, 52
    )
    
    # 2.1 Proto-Mayan
    b_maya = tb.add_node("<b>Proto-Maia</b><br><i>c. 2200–2000 a.C. — Terras Altas da Guatemala (~6M)</i>", S_SUBFAMILY, 1190, 225, 280, 38)
    tb.add_edge(f_meso, b_maya, style=S_EDGE_TOPDOWN)
    
    classic_maya = tb.add_node("Maia Clássico Hieroglífico †", S_EXTINCT, 1210, 280, 260, 30)
    tb.add_edge(b_maya, classic_maya, style=S_EDGE_GUTTER)
    
    maya_langs = [
        ("<b>K'iche' / Quiché (Guat.) ~2,3M</b><br><i>Texto sagrado Popol Vuh</i>", S_LIVING),
        ("<b>Maia Yucateco ~800k</b><br><i>Península de Yucatán, México</i>", S_LIVING),
        ("Q'eqchi' (Guatemala/Belize) ~800k", S_LIVING),
        ("Kaqchikel ~450k", S_LIVING),
        ("Mam ~500k", S_LIVING),
        ("Tsotsil / Tzotzil (Chiapas) ~500k", S_LIVING),
        ("Tseltal (Chiapas) ~550k", S_LIVING),
        ("Ch'orti' (Herdeiro dos hieróglifos)", S_LIVING)
    ]
    tb.add_vertical_children(classic_maya, maya_langs, 1190, start_y=325, col_w=280, child_h=32, y_step=40, indent=20)

    # 2.2 Proto-Uto-Aztecan South (Nahuatl)
    b_nahuatl = tb.add_node("<b>Proto-Uto-Asteca Meridional</b><br><i>c. 2000 a.C. — Noroeste do México / Altiplano</i>", S_SUBFAMILY, 1490, 225, 280, 38)
    tb.add_edge(f_meso, b_nahuatl, style=S_EDGE_TOPDOWN)
    
    class_nah = tb.add_node("Náuatle Clássico † (Império Asteca)", S_EXTINCT, 1510, 280, 260, 30)
    tb.add_edge(b_nahuatl, class_nah, style=S_EDGE_GUTTER)
    
    nah_langs = [
        ("<b>Náuatle Moderno (Nāhuatl) ~1,7M</b><br><i>Puebla, Hidalgo, Guerrero, Veracruz</i>", S_LIVING),
        ("Huichol (Wixárika - Nayarit)", S_LIVING),
        ("Cora (Naáyarite)", S_LIVING),
        ("Tarahumara (Ralámuli - Chihuahua)", S_LIVING),
        ("Yaqui (Yoeme - Sonora/Arizona)", S_LIVING),
        ("Mayo (Yoreme)", S_LIVING),
        ("Pipil / Nawat (El Salvador)", S_LIVING)
    ]
    tb.add_vertical_children(class_nah, nah_langs, 1490, start_y=325, col_w=280, child_h=32, y_step=40, indent=20)

    # 2.3 Proto-Oto-Manguean & Mixe-Zoque
    b_otomang = tb.add_node("<b>Proto-Oto-Mangue &amp; Mixe-Zoque</b><br><i>c. 3000 a.C. — Vale de Tehuacán / Raiz Olmeca</i>", S_SUBFAMILY, 1790, 225, 290, 38)
    tb.add_edge(f_meso, b_otomang, style=S_EDGE_TOPDOWN)
    om_langs = [
        ("Zapoteca (Diidxazá - Oaxaca) ~450k", S_LIVING),
        ("Mixteco (Tu'un sávi - Oaxaca) ~500k", S_LIVING),
        ("Otomi (Hñähñu - México Central) ~300k", S_LIVING),
        ("Mazahua / Mazateco", S_LIVING),
        ("Totonaca (Puebla/Veracruz) ~250k", S_LIVING),
        ("Mixe (Ayöök - provável raiz Olmeca)", S_LIVING),
        ("Zoque (Ode püt - Chiapas)", S_LIVING),
        ("Purépecha / Tarasco (Isolada)", S_LIVING)
    ]
    tb.add_vertical_children(b_otomang, om_langs, 1790, start_y=280, col_w=290, child_h=30, y_step=38, indent=20)

    # ==========================================
    # 3. AMÉRICA DO SUL
    # ==========================================
    f_sa = tb.add_node(
        "<b>PROTOLÍNGUAS DA AMÉRICA DO SUL</b><br>"
        "<i>Proto-Quechua, Proto-Aimará, Proto-Tupi, Proto-Macro-Jê, Proto-Aruaque, Proto-Caribe e Proto-Pano</i>",
        S_FAMILY, 2100, 140, 1850, 52
    )
    
    # 3.1 Proto-Quechuan
    b_quech = tb.add_node("<b>Proto-Quechua</b><br><i>c. séc. V–VIII d.C. — Andes Centrais (Peru) ~9M</i>", S_SUBFAMILY, 2100, 225, 330, 38)
    tb.add_edge(f_sa, b_quech, style=S_EDGE_TOPDOWN)
    
    class_quech = tb.add_node("Quechua Imperial de Cusco † (Tawantinsuyu)", S_EXTINCT, 2122, 280, 308, 30)
    tb.add_edge(b_quech, class_quech, style=S_EDGE_GUTTER)
    
    quech_langs = [
        ("<b>Quechua Cusco-Collao</b> (Peru) ~1,5M", S_LIVING),
        ("<b>Quechua Ayacuchano / Chanka</b> ~1M", S_LIVING),
        ("<b>Kichwa / Quíchua do Equador</b> ~1,2M", S_LIVING),
        ("Quechua Ancashino / Huaylas", S_LIVING),
        ("Quechua Boliviano Meridional ~1,6M", S_LIVING),
        ("Quechua Santiagueño (Argentina)", S_LIVING)
    ]
    tb.add_vertical_children(class_quech, quech_langs, 2100, start_y=325, col_w=330, child_h=32, y_step=40, indent=22)

    # 3.2 Proto-Aymaran & Mapudungun
    b_aym = tb.add_node("<b>Proto-Aimará (Aru/Jaqi)</b><br><i>c. 500 a.C.–séc. I d.C. — Andes Centro-Sul</i>", S_SUBFAMILY, 2450, 225, 310, 38)
    tb.add_edge(f_sa, b_aym, style=S_EDGE_TOPDOWN)
    aym_langs = [
        ("<b>Aimará (Aymar aru) ~2,8M</b><br><i>Oficial na Bolívia e Peru</i>", S_LIVING),
        ("Jaqaru (Peru) ~700", S_LIVING),
        ("Kawki † (Extinta)", S_EXTINCT),
        ("<b>Mapudungun / Mapuche</b> ~250k<br><i>Chile e Argentina (Isolada)</i>", S_LIVING),
        ("Huilliche (Chile)", S_LIVING)
    ]
    tb.add_vertical_children(b_aym, aym_langs, 2450, start_y=280, col_w=310, child_h=34, y_step=42, indent=22)

    # 3.3 Proto-Tupian
    b_tupi = tb.add_node("<b>Proto-Tupi (Tronco Tupi)</b><br><i>c. 3000–2500 a.C. — Rondônia / Bacia do Guaporé</i>", S_SUBFAMILY, 2780, 225, 360, 38)
    tb.add_edge(f_sa, b_tupi, style=S_EDGE_TOPDOWN)
    
    proto_tupi = tb.add_node("Proto-Tupi-Guarani (Expansão litorânea e meridional)", S_BRANCH, 2802, 280, 338, 30)
    tb.add_edge(b_tupi, proto_tupi, style=S_EDGE_GUTTER)
    
    tupi_langs = [
        ("Tupi Antigo † (Costa do Brasil)", S_EXTINCT),
        ("Língua Geral Paulista †", S_EXTINCT),
        ("<b>Nheengatu (Língua Geral Amazônica)</b><br><i>Cooficial em São Gabriel da Cachoeira (AM)</i>", S_LIVING),
        ("<b>Guarani Paraguaio (Avañe'ẽ) ~6,5M</b><br><i>Oficial no Paraguai (85% da população)</i>", S_LIVING),
        ("Guarani Mbyá (Brasil, Argentina, Paraguai)", S_LIVING),
        ("Guarani Kaiowá / Paï Tavyterã (MS)", S_LIVING),
        ("Tenetehara (Guajajara e Tembé - MA)", S_LIVING),
        ("Ka'apor / Tapirapé", S_LIVING),
        ("Munduruku (Rio Tapajós, PA - Não T-G)", S_LIVING),
        ("Sateré-Mawé (AM/PA - Não T-G)", S_LIVING),
        ("Kamaiurá / Awetí (Alto Xingu)", S_LIVING)
    ]
    tb.add_vertical_children(proto_tupi, tupi_langs, 2780, start_y=325, col_w=360, child_h=32, y_step=40, indent=22)

    # 3.4 Proto-Macro-Jê & Proto-Arawak
    b_je_araw = tb.add_node("<b>Proto-Macro-Jê &amp; Proto-Aruaque</b><br><i>c. 2500–1500 a.C. — Planalto Central / Noroeste Amazônico</i>", S_SUBFAMILY, 3160, 225, 360, 38)
    tb.add_edge(f_sa, b_je_araw, style=S_EDGE_TOPDOWN)
    je_araw_langs = [
        ("Macro-Jê: Xavante (A'uwẽ Uptabi - MT) ~18k", S_LIVING),
        ("Macro-Jê: Kaingang (Sul do Brasil) ~30k", S_LIVING),
        ("Macro-Jê: Kayapó (Mẽbêngôkre - PA/MT) ~12k", S_LIVING),
        ("Macro-Jê: Karajá (Iny rybè - Ilha do Bananal)", S_LIVING),
        ("Macro-Jê: Krenak / Maxakalí", S_LIVING),
        ("Aruaque: Taíno † (Antilhas - Colombo)", S_EXTINCT),
        ("<b>Aruaque: Wayuu / Guajiro ~400k</b>", S_LIVING),
        ("Aruaque: Asháninka (Peru e Acre) ~70k", S_LIVING),
        ("Aruaque: Garifuna (América Central)", S_LIVING),
        ("Aruaque: Pareci / Terêna (MS)", S_LIVING)
    ]
    tb.add_vertical_children(b_je_araw, je_araw_langs, 3160, start_y=280, col_w=360, child_h=30, y_step=38, indent=22)

    # 3.5 Proto-Cariban, Proto-Pano & Yanomami
    b_carib_pano = tb.add_node("<b>Proto-Caribe, Proto-Pano &amp; Yanomami</b><br><i>Planalto das Guianas e Bacia Amazônica Ocidental</i>", S_SUBFAMILY, 3540, 225, 360, 38)
    tb.add_edge(f_sa, b_carib_pano, style=S_EDGE_TOPDOWN)
    cp_langs = [
        ("Caribe: Kari'nja (Caribe continental)", S_LIVING),
        ("Caribe: Ye'kuana / Tiriyó", S_LIVING),
        ("Caribe: Macushi / Wai-Wai", S_LIVING),
        ("Pano: Shipibo-Konibo (Peru) ~35k", S_LIVING),
        ("Pano: Matsés / Kaxinawá (Huni Kuin)", S_LIVING),
        ("Yanomami: Yanomamö / Sanumá", S_LIVING),
        ("Chibcha: Muisca † (Colômbia)", S_EXTINCT),
        ("Chibcha: Bribri (Costa Rica) / Ngäbere", S_LIVING)
    ]
    tb.add_vertical_children(b_carib_pano, cp_langs, 3540, start_y=280, col_w=360, child_h=30, y_step=38, indent=22)

    return tb

if __name__ == "__main__":
    build_americas_page()
    print("Americas updated with explicit Proto-languages.")
