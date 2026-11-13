#!/usr/bin/env python3
"""
Generator for Page 0: Global Protolanguages Master Tree.
Directly displays all world proto-languages branching from human linguistic radiation.
"""

from tree_builder import (
    TreeBuilder, S_LIVING, S_EXTINCT, S_BRANCH,
    S_FAMILY, S_SUBFAMILY, S_GROUP, S_EDGE_TOPDOWN, S_EDGE_GUTTER, S_LEGEND
)

def build_overview_page():
    tb = TreeBuilder("overview", "0. Árvore Filogenética das Protolínguas do Mundo", width=4400, height=2200)
    tb.add_legend(40, 40)
    
    # Title
    tb.add_node(
        "<b>ÁRVORE FILOGENÉTICA DAS PROTOLÍNGUAS DO MUNDO</b><br>"
        "<i>Reconstruções Comparativas das Protolínguas Raiz e Sub-Ramos Primários</i><br>"
        "<span style='font-size:10px;'>Classificação: Glottolog, Theodor Cole (Parte 2, 2026), Campbell, Blust, Rodrigues &amp; Greenberg</span>",
        S_FAMILY, 340, 40, 850, 70
    )
    
    # Root
    root = tb.add_node(
        "<b>RADIAÇÃO FILOGENÉTICA DAS LÍNGUAS HUMANAS</b><br>"
        "(Línguas Naturais Atuais e Históricas — ~140 famílias filogeneticamente autônomas)",
        S_FAMILY, 1850, 140, 600, 50
    )
    
    # Macro-columns with explicit Proto-languages:
    proto_families = [
        ("PROTO-INDO-EUROPEU (PIE)", "c. 4500–3500 a.C.<br><i>Estepes Pôntico-Cáspias</i>", [
            ("Proto-Anatólico † (Hitita, Lúvio)", S_EXTINCT),
            ("Proto-Toqueano † (Toqueano A/B)", S_EXTINCT),
            ("Proto-Itálico (Latim → Românicas)", S_LIVING),
            ("Proto-Céltico (Goidélico / Britônico)", S_LIVING),
            ("Proto-Germânico (Nórdico / Ocidental)", S_LIVING),
            ("Proto-Balto-Eslavo (Báltico / Eslavo)", S_LIVING),
            ("Proto-Indo-Iraniano (Ariano / Iraniano)", S_LIVING),
            ("Proto-Helênico (Grego Antigo/Moderno)", S_LIVING),
            ("Proto-Armênio / Proto-Albanês", S_LIVING)
        ]),
        ("PROTO-URÁLICO", "c. 2500–2000 a.C.<br><i>Montes Urais / Bacia Volga-Kama</i>", [
            ("Proto-Fino-Úgrico", S_BRANCH),
            ("→ Proto-Bálto-Fínico (Suomi, Eesti)", S_LIVING),
            ("→ Proto-Úgrico (Húngaro, Mansi)", S_LIVING),
            ("→ Proto-Sámi (Lapão)", S_LIVING),
            ("→ Proto-Pérmico & Volgaico", S_LIVING),
            ("Proto-Samoiedo (Nenets, Selkup)", S_LIVING)
        ]),
        ("PROTO-SINO-TIBETANO", "c. 4500–4000 a.C.<br><i>Bacia do Rio Amarelo</i>", [
            ("Proto-Sínico (上古漢語)", S_BRANCH),
            ("→ Mandarim, Cantonês, Wu, Min", S_LIVING),
            ("Proto-Tibeto-Birmanês", S_BRANCH),
            ("→ Proto-Bódico (Tibetano, Dzongkha)", S_LIVING),
            ("→ Proto-Búrmico (Birmanês, Yi)", S_LIVING),
            ("→ Tangut † (Império Xixia)", S_EXTINCT)
        ]),
        ("PROTO-AUSTRONÉSIO (PAN)", "c. 4000–3500 a.C.<br><i>Ilha de Taiwan (Formosa)</i>", [
            ("Ramos Formosianos (Atayal, Amis, Paiwan)", S_LIVING),
            ("Proto-Malaio-Polinésio (PMP)", S_BRANCH),
            ("→ Malaio, Indonésio, Javanês", S_LIVING),
            ("→ Filipino (Tagalo, Cebuano)", S_LIVING),
            ("→ Malgaxe (Madagascar)", S_LIVING),
            ("→ Proto-Oceânico (Polinésio, Maori)", S_LIVING)
        ]),
        ("PROTO-AFROASIÁTICO (PAA)", "c. 10000–8000 a.C.<br><i>Chifre da África / Nilo</i>", [
            ("Proto-Semítico (Árabe, Hebraico, Aramaico)", S_LIVING),
            ("Egípcio Antigo & Copta †", S_EXTINCT),
            ("Proto-Berbere (Amazigh / Tuaregue)", S_LIVING),
            ("Proto-Cuchítico (Somali, Oromo)", S_LIVING),
            ("Proto-Chádico (Hauçá / Hausa)", S_LIVING),
            ("Proto-Omótico (Wolaytta)", S_LIVING)
        ]),
        ("PROTO-NÍGER-CONGO", "c. 5000–4000 a.C.<br><i>Bacia do Rio Níger (Sahel)</i>", [
            ("Proto-Bantu (Suaíli, Zulu, Quimbundo)", S_LIVING),
            ("Proto-Volta-Níger (Iorubá, Igbo)", S_LIVING),
            ("Proto-Atlântico (Fula, Wolof)", S_LIVING),
            ("Proto-Kwa (Akan/Twi, Ewe)", S_LIVING),
            ("Proto-Mandê (Bambara, Mandinga)", S_LIVING)
        ]),
        ("PROTO-DRAVÍDICO", "c. 3000–2500 a.C.<br><i>Planalto do Decão (Índia)</i>", [
            ("Proto-Dravídico Meridional (Tâmil, Malaiala)", S_LIVING),
            ("Proto-Dravídico Sul-Central (Telugu, Gondi)", S_LIVING),
            ("Proto-Dravídico Central (Kolami)", S_LIVING),
            ("Proto-Dravídico Setentrional (Brahui)", S_LIVING)
        ]),
        ("PROTOLÍNGUAS DO NORDESTE ASIÁTICO*", "500 a.C.–séc. IV d.C.<br><i>Ásia Central/Sibéria (Complexo Areal)</i>", [
            ("Proto-Túrquico (Turco, Cazaque, Uzbeque)", S_LIVING),
            ("Proto-Mongólico (Khalkha, Buriato)", S_LIVING),
            ("Proto-Tungúsico (Manchu, Evenki)", S_LIVING),
            ("Proto-Japônico (Japonês, Ryukyu)", S_LIVING),
            ("Proto-Coreano (Coreano, Jeju)", S_LIVING)
        ]),
        ("PROTOLÍNGUAS DO SUDESTE ASIÁTICO", "2500–1500 a.C.<br><i>Sul da China / Vales Fluviais</i>", [
            ("Proto-Austroasiático (Khmer, Vietnamita)", S_LIVING),
            ("Proto-Munda (Santali, Mundari)", S_LIVING),
            ("Proto-Kra-Dai (Tai, Lao, Zhuang)", S_LIVING),
            ("Proto-Hmong-Mien (Hmong, Iu Mien)", S_LIVING)
        ]),
        ("PROTOLÍNGUAS DA AMÉRICA DO NORTE", "3000–1000 a.C.<br><i>Bering, Subártico e Grandes Planícies</i>", [
            ("Proto-Esquimó-Aleúte (Inuktitut, Kalaallisut)", S_LIVING),
            ("Proto-Na-Dene (Navajo, Apache, Tlingit)", S_LIVING),
            ("Proto-Álgico (Cree, Ojibwe, Blackfoot)", S_LIVING),
            ("Proto-Iroquês (Cherokee, Mohawk)", S_LIVING),
            ("Proto-Sioux (Lakota/Dakota, Crow)", S_LIVING)
        ]),
        ("PROTOLÍNGUAS DA MESOAMÉRICA", "3000–2000 a.C.<br><i>Terras Altas e Vales do México/Am. Central</i>", [
            ("Proto-Maia (K'iche', Yucateco, Q'eqchi')", S_LIVING),
            ("Proto-Uto-Asteca (Náuatle, Hopi, Huichol)", S_LIVING),
            ("Proto-Oto-Mangue (Zapoteca, Mixteco)", S_LIVING),
            ("Proto-Mixe-Zoque & Totonaca", S_LIVING)
        ]),
        ("PROTOLÍNGUAS DA AMÉRICA DO SUL", "3000 a.C.–séc. V d.C.<br><i>Andes, Amazônia e Bacia do Prata</i>", [
            ("Proto-Tupi (Tupi Antigo, Nheengatu, Guarani)", S_LIVING),
            ("Proto-Macro-Jê (Xavante, Kaingang, Kayapó)", S_LIVING),
            ("Proto-Aruaque (Wayuu, Asháninka, Taíno †)", S_LIVING),
            ("Proto-Caribe (Kari'nja, Macushi)", S_LIVING),
            ("Proto-Quechua (Cusco, Ayacucho, Kichwa)", S_LIVING),
            ("Proto-Aimará & Mapudungun", S_LIVING)
        ])
    ]
    
    col_w = 330
    gap_x = 26
    start_x = 50
    header_y = 260
    header_h = 75
    
    for i, (pname, pmeta, pchildren) in enumerate(proto_families):
        cx = start_x + i * (col_w + gap_x)
        fnid = tb.add_node(
            f"<b>{pname}</b><br><span style='font-size:10px;'>{pmeta}</span>",
            S_FAMILY, cx, header_y, col_w, header_h
        )
        tb.add_edge(root, fnid, style=S_EDGE_TOPDOWN)
        tb.add_vertical_children(fnid, pchildren, cx, start_y=365, col_w=col_w, child_h=34, y_step=44, indent=22)

    return tb

if __name__ == "__main__":
    t = build_overview_page()
    print("Page 0 built with explicit Proto-languages.")
