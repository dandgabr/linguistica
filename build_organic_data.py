#!/usr/bin/env python3
import json
import xml.etree.ElementTree as ET
import re

def clean_html(text):
    text = re.sub(r'<br\s*/?>', ' — ', text)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def extract_endonym(raw_val):
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
            
    edges.append(('node_poster_4', 'node_americas_4'))
    
    for s, t in edges:
        if s in nodes and t in nodes:
            nodes[s]['children'].append(t)
            nodes[t]['parents'].append(s)
            
    return nodes, edges

TRUNK_META = {
    "node_ie_4": {"nome": "Indo-Europeia", "era": "~4.500–3.000 a.C.", "urheimat": "Estepes Pôntico-Cáspias", "desc": "Maior família por número de falantes no mundo (~3,3 bilhões), abrange ramos Itálico, Germânico, Indo-Iraniano, Balto-Eslavo, Helênico, Céltico, Armênio, Albanês, Anatólico e Toqueano."},
    "node_east_asia_4": {"nome": "Sino-Tibetana", "era": "~4.500–4.000 a.C.", "urheimat": "Bacia do Rio Amarelo / Tibete", "desc": "Segunda maior família por falantes nativos (~1,4 bilhão), compreende ramos Sínico (Mandarim, Cantonês, Wu, Min) e Tibeto-Birmanês."},
    "node_afro_niger_drav_4": {"nome": "Afroasiática", "era": "~10.000–8.000 a.C.", "urheimat": "Chifre da África / Bacia do Nilo", "desc": "Mais antiga protolíngua com reconstrução aceita. Ramos Semítico (Árabe, Hebraico, Acadiano), Egípcio, Berbere, Cuchítico e Chádico."},
    "node_afro_niger_drav_83": {"nome": "Níger-Congo", "era": "~5.000–4.000 a.C.", "urheimat": "Bacia do Rio Níger (Sahel Ocidental)", "desc": "Maior família do mundo em número total de línguas (~1.540). Inclui a imensa expansão Bantu (Suaíli, Zulu), Volta-Níger (Iorubá, Igbo) e Atlântico."},
    "node_east_asia_128": {"nome": "Austronésia", "era": "~4.000–3.500 a.C.", "urheimat": "Ilha de Taiwan (Formosa)", "desc": "Maior dispersão oceânica pré-moderna (Madagascar à Ilha de Páscoa). Ramos Formosianos, Malaio-Polinésio, Oceânico e línguas das Filipinas e Indonésia."},
    "node_trans_uralic_113": {"nome": "Urálica", "era": "~2.500–2.000 a.C.", "urheimat": "Montes Urais / Bacia Volga-Kama", "desc": "Línguas do norte da Eurásia e Europa Central com rica harmonia vocálica e casos múltiplos. Ramos Fino-Úgrico (Finlandês, Húngaro, Estoniano) e Samoiedo."},
    "node_trans_uralic_4": {"nome": "Túrquica", "era": "c. 500 a.C.", "urheimat": "Montes Altai / Sibéria Meridional", "desc": "Extensa família aglutinante com harmonia vocálica estrita. Ramo Oghuz (Turco, Azerbaijano), Kipchak (Cazaque), Karluk (Uzbeque) e Siberiano."},
    "node_afro_niger_drav_156": {"nome": "Dravídica", "era": "~3.000–2.500 a.C.", "urheimat": "Planalto do Decão / Vale do Indo", "desc": "Família autóctone do Sul da Ásia com literatura milenar e fonologia retroflexa. Tâmil, Telugu, Canará e Malaiala."},
    "node_east_asia_97": {"nome": "Austroasiática", "era": "~2.500–2.000 a.C.", "urheimat": "Vales dos Rios Yangtzé e Mekong", "desc": "Línguas autóctones do Sudeste Asiático continental e leste da Índia. Khmer (Camboja), Vietnamita e família Munda."},
    "node_east_asia_68": {"nome": "Kra-Dai (Tai-Kadai)", "era": "~2.000–1.500 a.C.", "urheimat": "Litoral Sul da China (Guangdong/Guangxi)", "desc": "Línguas tonais isolantes do Sudeste Asiático continental. Tailandês (Siamês), Lao e Zhuang."},
    "node_east_asia_53": {"nome": "Hmong-Mien", "era": "c. 2.500 a.C.", "urheimat": "Bacia dos Rios Yangtzé e Han", "desc": "Família do sul da China e Sudeste Asiático com fonologia tonal de alta complexidade. Hmong, Iu Mien e She."},
    "node_trans_uralic_85": {"nome": "Japônica", "era": "séc. IV–III a.C.", "urheimat": "Arquipélago Japonês / Kyūshū", "desc": "Família do Japão continental e ilhas Ryūkyū. Língua Japonesa e dialetos Okinawanos."},
    "node_trans_uralic_100": {"nome": "Coreânica", "era": "séc. I a.C.–séc. IV d.C.", "urheimat": "Península Coreana e Manchúria", "desc": "Língua Coreana e língua de Jeju, marcadas por sistema fonológico tripartite de oclusivas e escrita Hangeul."},
    "node_trans_uralic_55": {"nome": "Mongólica", "era": "séc. IV–VI d.C.", "urheimat": "Bacias dos Rios Amur e Shilka", "desc": "Família das estepes da Ásia Central. Mongol Khalkha, Buriato, Calmuco e línguas dos impérios nômades."},
    "node_trans_uralic_70": {"nome": "Tungúsica", "era": "c. 500 a.C.", "urheimat": "Bacia do Rio Amur / Sibéria Oriental", "desc": "Línguas da Manchúria e Sibéria. Manchu (dinastia Qing), Evenki e Nanai."},
    "node_trans_uralic_166": {"nome": "Kartveliana (Sul-Caucásica)", "era": "~2.500–2.000 a.C.", "urheimat": "Região Sul da Transcaucásia", "desc": "Línguas do Cáucaso com complexo alinhamento morfossintático split-ergativo e aglomerações consonantais. Georgiano, Mingrélio, Laz e Svan."},
    "node_americas_4": {"nome": "América do Norte (Protolínguas)", "era": "3.000–1.000 a.C.", "urheimat": "Bering, Subártico, Planícies e Costa Oeste", "desc": "Radiações autóctones: Esquimó-Aleúte (Inuktitut), Na-Dene (Navajo, Apache), Álgico (Cree, Ojibwe), Iroquês (Cherokee, Mohawk) e Sioux (Lakota)."},
    "node_americas_71": {"nome": "Mesoamérica (Protolínguas)", "era": "3.000–2.000 a.C.", "urheimat": "Terras Altas e Vales do México e América Central", "desc": "Línguas das grandes civilizações pré-colombianas: Família Maia (K'iche', Yucateco), Uto-Asteca (Náuatle), Oto-Mangue (Zapoteca, Mixteco) e Mixe-Zoque."},
    "node_americas_128": {"nome": "América do Sul (Protolínguas)", "era": "3.000 a.C.–séc. V d.C.", "urheimat": "Andes, Amazônia e Bacia do Prata", "desc": "Rica diversidade autóctone sul-americana: Tronco Tupi (Tupinambá, Nheengatu, Guarani), Família Quechua, Aimará, Macro-Jê, Aruaque e Caribe."}
}

print("Metadata definitions loaded.")
