#!/usr/bin/env python3
"""
Builds an interactive, rich standalone HTML + CSS + JS web application
containing all world language families, with pan/zoom, search, filters,
and detailed linguistic explanations for each language and proto-language.
"""

import json
import xml.etree.ElementTree as ET
import re

def clean_html(text):
    text = re.sub(r'<br\s*/?>', ' — ', text)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

# Comprehensive linguistic knowledge base for node enrichment
LINGUISTIC_DESCRIPTIONS = {
    # Indo-European Branches
    "PROTO-INDO-EUROPEU": {
        "resumo": "Ancestral hipotético comum de mais de 440 línguas indo-europeias faladas por ~3,3 bilhões de pessoas.",
        "data": "c. 4500–3500 a.C. (Calcolítico / Idade do Bronze)",
        "urheimat": "Estepes pôntico-cáspias (Norte do Mar Negro e Mar Cáspio - Teoria dos Kurgans / Marija Gimbutas).",
        "caracteristicas": "Língua altamente flexiva com 8 casos gramaticais (nominativo, vocativo, acusativo, genitivo, dativo, ablativo, instrumental, locativo), três gêneros (masculino, feminino, neutro), três números (singular, dual, plural), apofonia vocálica (*Ablaut*) e teoria das laringais (*h₁, *h₂, *h₃)."
    },
    "ANATOLIANA": {
        "resumo": "Primeiro ramo divergente do Proto-Indo-Europeu. Todas as línguas deste ramo estão extintas.",
        "data": "Séculos XIX a.C. a I a.C.",
        "urheimat": "Anatólia (atual Turquia).",
        "caracteristicas": "Conservou as laringais laringais do PIE (especialmente *h₂ como ḫ em hitita), escrita cuneiforme e hieroglífica anatólica; ausência de gênero feminino gramatical primitivo."
    },
    "Hitita": {
        "resumo": "Língua oficial do Império Hitita, a mais antiga língua indo-europeia registrada em textos escritos.",
        "data": "Textos cuneiformes de c. 1650 a.C. a 1180 a.C. (†)",
        "regiao": "Hattusa, planalto central da Anatólia (Turquia).",
        "caracteristicas": "Decifrada por Bedřich Hrozný em 1915. Registrada em tabuletas de argila em escrita cuneiforme acadiana."
    },
    "Luwiano": {
        "resumo": "Língua intimamente ligada ao hitita, amplamente falada na Anatólia meridional e ocidental.",
        "data": "c. 1400 a.C. a 700 a.C. (†)",
        "caracteristicas": "Utilizava tanto a escrita cuneiforme quanto os Hieróglifos Anatólicos (inscrições em rocha e estelas monumentais)."
    },
    "HELÊNICA": {
        "resumo": "Ramo indo-europeu centrado no Mar Egeu e Bálcãs do Sul com mais de 3.400 anos de registros escritos contínuos.",
        "caracteristicas": "Evoluiu do Grego Micênico (Linear B) para os dialetos arcaicos/clássicos (Ático, Jônico, Dórico), dando origem ao Koiné helenístico, Bizantino e Grego Moderno."
    },
    "Grego Micênico": {
        "resumo": "A mais antiga forma atestada da língua grega, preservada em tabuletas de argila palacianas de Micenas, Pilos e Creta.",
        "data": "c. 1450 a.C. a 1200 a.C. (†)",
        "escrita": "Linear B (silabário decifrado por Michael Ventris em 1952)."
    },
    "Grego Clássico": {
        "resumo": "Idioma da filosofia clássica, tragédias, oratória e ciências da Grécia Antiga (Atenas e colônias).",
        "data": "c. 800 a.C. a 300 a.C. (†)",
        "autores": "Homero, Platão, Aristóteles, Tucídides, Sófocles."
    },
    "Grego Moderno": {
        "resumo": "Língua oficial da Grécia e Chipre e uma das 24 línguas oficiais da União Europeia.",
        "falantes": "~13,5 milhões de falantes.",
        "caracteristicas": "Substituição do sistema tonal clássico por acento de intensidade; simplificação de casos e desinências (Dimotiki)."
    },
    "ITÁLICA": {
        "resumo": "Ramo que floresceu na península itálica antes da unificação romana, originando as línguas românicas.",
        "divisao": "Subdividido em Latino-Falisco e Sabélico (Osco-Úmbrio)."
    },
    "Latim": {
        "resumo": "Língua da Roma Antiga, do Império Romano, do direito ocidental e língua franca da ciência e da Igreja Católica.",
        "data": "c. 700 a.C. até a transição para as línguas românicas (séc. VII-VIII d.C.).",
        "caracteristicas": "Língua com 6 casos gramaticais (nominativo, vocativo, acusativo, genitivo, dativo, ablativo) e três gêneros."
    },
    "Português": {
        "resumo": "Língua românica ocidental originada do Galego-Português no noroeste da Península Ibérica.",
        "falantes": "~260 a 290 milhões de falantes (9ª língua mais falada do mundo).",
        "paises": "Brasil, Portugal, Angola, Moçambique, Cabo Verde, Guiné-Bissau, São Tomé e Príncipe, Timor-Leste, Macau.",
        "caracteristicas": "Preservação de vogais nasais arcaicas, infinitivo pessoal flexionado, mesóclise e rica morfologia verbal."
    },
    "Espanhol": {
        "resumo": "Língua românica ibérica com a segunda maior população de falantes nativos do mundo (~490 milhões).",
        "falantes": "~590 milhões de falantes totais.",
        "distribuicao": "Espanha, América Hispânica (19 países) e forte presença nos EUA."
    },
    "Francês": {
        "resumo": "Língua românica com forte superstrato germânico (frâncico) e substrato gaulês.",
        "falantes": "~320 milhões de falantes totais (Europa, África Ocidental/Central, Canadá)."
    },
    "Italiano": {
        "resumo": "Língua românica direta herdeira do dialeto toscano literário (Dante, Petrarca, Boccaccio).",
        "falantes": "~68 milhões de falantes nativos e secundários."
    },
    "Romeno": {
        "resumo": "Língua românica oriental desenvolvida na antiga província de Dácia.",
        "falantes": "~25 milhões de falantes (Romênia e Moldávia).",
        "caracteristicas": "Artigo definido enclítico (-ul, -a) e conservação de resquícios de declinação genitivo-dativa."
    },
    # Germanic
    "GERMÂNICA": {
        "resumo": "Ramo do PIE marcado pela Primeira Mudança Consonantal Germânica (Lei de Grimm e Lei de Verner).",
        "data": "Proto-Germânico: c. 500 a.C. a 200 d.C. (Cultura Jastorf - Escandinávia e Norte da Alemanha)."
    },
    "Inglês": {
        "resumo": "Língua germânica ocidental do subgrupo anglo-frísio, lingua franca internacional contemporânea.",
        "falantes": "~1,5 bilhão de falantes totais (~400M nativos).",
        "historia": "Evoluiu do Inglês Antigo (Anglo-Saxão, germânico puro) para o Inglês Médio (impactado pelo Francês Normando pós-1066) e Inglês Moderno."
    },
    "Alemão": {
        "resumo": "Língua germânica ocidental marcada pela Segunda Mudança Consonantal Germânica (Alto-Alemão).",
        "falantes": "~135 milhões de falantes (Alemanha, Áustria, Suíça, Liechtenstein, Luxemburgo).",
        "caracteristicas": "Sistema de 4 casos (nominativo, acusativo, genitivo, dativo), ordem frasal V2 em orações principais e verbo no fim em subordinadas."
    },
    "Gótico": {
        "resumo": "Língua do ramo Germânico Oriental falada pelos godos (visigodos e ostrogodos).",
        "data": "Registrada na Bíblia de Wulfila (séc. IV d.C.) no Codex Argenteus (†).",
        "caracteristicas": "O mais antigo testemunho literário substancial de uma língua germânica."
    },
    # Slavic
    "PROTO-BALTO-ESLAVO": {
        "resumo": "Tronco comum que gerou as famílias Báltica e Eslava, caracterizado por inovações fonológicas e acentuais compartilhadas (Lei de Winter, acento móvel).",
        "data": "c. 1500–1000 a.C."
    },
    "Russo": {
        "resumo": "Maior língua eslava e a mais falada na Europa geograficamente.",
        "falantes": "~255 milhões de falantes totais.",
        "caracteristicas": "Alfabeto cirílico, oposição fonêmica entre consoantes palatalizadas ('suaves') e não-palatalizadas ('duras'), 6 casos gramaticais."
    },
    "Polonês": {
        "resumo": "Língua eslava ocidental com rica fonologia sibilante e conservação de vogais nasais (ą, ę).",
        "falantes": "~45 milhões de falantes (Polônia e diáspora)."
    },
    # Indo-Iranian
    "PROTO-INDO-IRANIANO": {
        "resumo": "Maior ramo do Indo-Europeu em extensão geográfica e antiguidade no leste, associado à cultura Sintashta e Andronovo.",
        "data": "c. 2500–2000 a.C. — Estepes da Ásia Central."
    },
    "Sânscrito": {
        "resumo": "Língua clássica e sagrada da Índia (Vedas, Upanixades, Gita), codificada por Pāṇini no século IV a.C.",
        "data": "Védico de c. 1500 a.C.; Sânscrito Clássico († como língua materna; preservada na liturgia)."
    },
    "Hindi": {
        "resumo": "Língua indo-ariana moderna oficial da Índia, intimamente ligada ao Urdu.",
        "falantes": "~600 milhões de falantes totais.",
        "escrita": "Devanagari (हिन्दी)."
    },
    "Persa": {
        "resumo": "Língua iraniana de prestígio literário contínuo por mais de 2.500 anos (Império Aquemênida ao Irã moderno).",
        "falantes": "~120 milhões de falantes (Irã, Afeganistão como Dari, Tajiquistão como Tajique).",
        "escrita": "Perso-árabe (فارسی)."
    },
    # Sino-Tibetan
    "PROTO-SINO-TIBETANO": {
        "resumo": "Segunda maior família do mundo em número de falantes (~1,4 bilhão).",
        "data": "c. 4500–4000 a.C.",
        "urheimat": "Bacia do Rio Amarelo (culturas neolíticas Yangshao e Majiayao) ou leste do planalto tibetano.",
        "caracteristicas": "Línguas tonais (na sua maioria secundárias via tonogênese), morfologia predominantemente isolante com ricas partículas aspectuais."
    },
    "Mandarim": {
        "resumo": "Variedade mais falada da família sínica e a língua com maior número de falantes nativos do planeta.",
        "falantes": "~930 milhões de falantes nativos (~1,1 bilhão totais).",
        "caracteristicas": "4 tons fonêmicos no Mandarim Padrão, ausência de flexão morfológica, sistema de classificadores numerais obrigatórios."
    },
    "Cantonês": {
        "resumo": "Língua sínica tradicional de Guangdong, Hong Kong e Macau.",
        "falantes": "~85 milhões de falantes.",
        "caracteristicas": "Preserva 6 a 9 tons fonêmicos e consoantes finais oclusivas (-p, -t, -k) do Chinês Médio perdidas no Mandarim."
    },
    "Tibetano": {
        "resumo": "Língua do planalto do Tibete, veículo central da filosofia e literatura budista vajrayana.",
        "escrita": "Alfabeto tibetano brâmico criado no século VII por Thonmi Sambhota."
    },
    # Austronesian
    "PROTO-AUSTRONÉSIO": {
        "resumo": "Família de dispersão marítima extraordinária, cobrindo da Ilha de Páscoa (Rapa Nui) a Madagascar.",
        "data": "c. 4000–3500 a.C. — Ilha de Taiwan (Formosa).",
        "caracteristicas": "Sistema de alinhamento austronésio ('foco de voz'), reduplicação morfológica produtiva e ausência de tons primitivos."
    },
    "Indonésio": {
        "resumo": "Forma padronizada do Malaio adotada como língua nacional da Indonésia.",
        "falantes": "~200 a 300 milhões de falantes (nativos e segunda língua).",
        "caracteristicas": "Língua aglutinante com rico sistema de prefixos e sufixos derivacionais (me-, ber-, -kan, -an)."
    },
    "Tagalo": {
        "resumo": "Base do Filipino, língua nacional das Filipinas.",
        "falantes": "~85 milhões de falantes.",
        "caracteristicas": "Complexo sistema de foco verbal em que o prefixo indica o papel temático do argumento topicalizado."
    },
    "Malgaxe": {
        "resumo": "Língua nacional de Madagascar, demonstrando a migração marítima austronésia através do Oceano Índico.",
        "falantes": "~25 milhões de falantes.",
        "origem": "Subgrupo Barito de Bornéu (Indonésia)."
    },
    "Maori": {
        "resumo": "Língua polinésia indígena da Nova Zelândia (Aotearoa).",
        "falantes": "~180 mil falantes.",
        "caracteristicas": "Ordem VSO (verbo-sujeito-objeto), inventário fonêmico estritamente econômico (10 consoantes, 5 vogais)."
    },
    # Afroasiatic
    "PROTO-AFROASIÁTICO": {
        "resumo": "Família demonstrada mais antiga da humanidade (~10.000 a 8.000 a.C.), abrangendo o Norte da África e Oriente Médio.",
        "urheimat": "Chifre da África ou Deserto Oriental/Bacia do Nilo.",
        "caracteristicas": "Morfologia introflexiva de raiz e padrão consonantal (raízes triconsonantais C-C-C intercaladas com vogais de tempo/aspecto)."
    },
    "Árabe": {
        "resumo": "Língua sacra do Islã e idioma oficial de 22 países da Liga Árabe.",
        "falantes": "~380 a 420 milhões de falantes.",
        "caracteristicas": "Diglossia marcada entre o Árabe Padrão Moderno (Fusha) e os dialetos vernáculos regionais; escrita da direita para a esquerda."
    },
    "Hebraico": {
        "resumo": "Língua bíblica milenar revitalizada com sucesso como idioma moderno e nacional em Israel no século XX.",
        "falantes": "~9 milhões de falantes.",
        "revitalizacao": "Liderada por Eliezer Ben-Yehuda a partir de 1881."
    },
    "Acadiano": {
        "resumo": "A mais antiga língua semítica registrada, falada na Babilônia e Assíria (Mesopotâmia).",
        "data": "Textos cuneiformes de c. 2500 a.C. a 100 d.C. (†)."
    },
    "Hauçá": {
        "resumo": "Maior língua chádica e grande língua franca comercial da África Ocidental e Central.",
        "falantes": "~77 milhões de falantes (Nigéria, Níger, Gana)."
    },
    # Niger-Congo
    "PROTO-NÍGER-CONGO": {
        "resumo": "Maior família do mundo em número total de línguas distintas (~1.540 línguas catalogadas).",
        "data": "c. 5000–4000 a.C. — Bacia do Rio Níger (Sahel Ocidental).",
        "caracteristicas": "Sistema extensivo de classes nominais com concordância por prefixos obrigatórios em adjetivos e verbos; línguas tonais."
    },
    "Suaíli": {
        "resumo": "Grande língua franca da África Oriental e língua oficial da União Africana e da Comunidade da África Oriental.",
        "falantes": "~150 a 200 milhões de falantes (Tanzânia, Quênia, R.D. Congo, Uganda).",
        "caracteristicas": "Língua bantu que perdeu os tons ancestrais e incorporou vocabulário do árabe pelo comércio no Oceano Índico."
    },
    "Zulu": {
        "resumo": "Maior língua materna da África do Sul, pertencente ao grupo Nguni do ramo Bantu meridional.",
        "falantes": "~12 milhões nativos.",
        "caracteristicas": "Presença de consoantes com cliques (estalidos c, q, x) absorvidas por contato com línguas Khoisan."
    },
    "Iorubá": {
        "resumo": "Língua volta-níger com forte presença cultural e religiosa na Nigéria e na diáspora atlântica (Candomblé no Brasil).",
        "falantes": "~45 milhões de falantes."
    },
    # Dravidian
    "PROTO-DRAVÍDICO": {
        "resumo": "Família autóctone do Sul da Ásia anterior à expansão indo-ariana.",
        "data": "c. 3000–2500 a.C. — Planalto do Decão / Bacia do Indo.",
        "caracteristicas": "Aglutinante, ordem SOV estrita, distinção sistemática entre consoantes retroflexas e dentais."
    },
    "Tâmil": {
        "resumo": "Uma das mais antigas línguas clássicas vivas do mundo, com literatura ininterrupta desde o Sangam (c. 300 a.C.).",
        "falantes": "~85 milhões de falantes (Índia, Sri Lanka, Cingapura, Malásia)."
    },
    # Turkic & Uralic
    "PROTO-TÚRQUICO": {
        "resumo": "Ancestral das línguas espalhadas das estepes da Ásia Central até o Mediterrâneo e a Sibéria.",
        "data": "c. 500 a.C. — Montes Altai.",
        "caracteristicas": "Harmonia vocálica rigorosa, estrutura aglutinante com sufixação exclusiva, ordem SOV e ausência de gênero gramatical."
    },
    "Turco": {
        "resumo": "Maior língua túrquica, falada na Turquia e Chipre do Norte.",
        "falantes": "~85 milhões de falantes.",
        "reforma": "Substituição do alfabeto perso-árabe pelo latino e purificação lexical na década de 1920 sob Atatürk."
    },
    "PROTO-URÁLICO": {
        "resumo": "Família que se estende da Europa Setentrional e Báltico até a bacia do rio Danúbio e Sibéria.",
        "data": "c. 2500–2000 a.C. — Montes Urais."
    },
    "Finlandês": {
        "resumo": "Língua bálto-fínica com 15 casos gramaticais e rica harmonia vocálica.",
        "falantes": "~5,4 milhões de falantes."
    },
    "Húngaro": {
        "resumo": "Maior língua urálica (ramo úgrico), isolada linguisticamente na Europa Central cercada por línguas indo-europeias.",
        "falantes": "~13 milhões de falantes."
    },
    # Americas
    "PROTO-TUPI": {
        "resumo": "Tronco linguístico de enorme relevância na história indígena sul-americana e na formação do Brasil.",
        "data": "c. 3000–2500 a.C. — Berço em Rondônia (Bacias do Madeira e Guaporé - Rodrigues, 1986).",
        "expansao": "Migrações ao longo do Amazonas e da costa atlântica (Tupinambá e Tupi Antigo) e bacia do Prata (Guarani)."
    },
    "Nheengatu": {
        "resumo": "Língua Geral Amazônica derivada do Tupinambá pelos jesuítas e comerciantes; oficial no município de São Gabriel da Cachoeira (AM).",
        "status": "Língua viva de resistência indígena no Rio Negro."
    },
    "Guarani": {
        "resumo": "Língua oficial do Paraguai, falada por cerca de 85% a 90% da população nacional, e cooficial em Corrientes (Argentina).",
        "falantes": "~6,5 milhões de falantes."
    },
    "PROTO-QUECHUA": {
        "resumo": "Maior família indígena das Américas em população ativa, língua da civilização Inca (Tawantinsuyu).",
        "falantes": "~8 a 10 milhões de falantes (Peru, Bolívia, Equador, Colômbia, Argentina).",
        "caracteristicas": "Rica morfologia sufixal aglutinante, sistema de evidencialidade gramatical obrigatória (testemunhado vs não-testemunhado/inferido)."
    },
    "PROTO-MAIA": {
        "resumo": "Família de alta sofisticação literária e astronômica da Mesoamérica pré-colombiana.",
        "data": "c. 2200–2000 a.C. — Terras Altas da Guatemala.",
        "escrita": "Hieróglifos maias com escrita logosilábica decifrada por Yuri Knorozov.",
        "linguas_vivas": "K'iche', Yucateco, Q'eqchi', Kaqchikel, Mam (~6 milhões de falantes)."
    },
    "Náuatle": {
        "resumo": "Língua do Império Asteca (Mexica) e da literatura lírica clássica de Nezahualcóyotl.",
        "falantes": "~1,7 milhão de falantes nativos no México contemporâneo."
    },
    "Navajo": {
        "resumo": "Maior língua indígena norte-americana nos EUA (família Na-Dene / Athabascana).",
        "falantes": "~170 mil falantes na Nação Navajo (Arizona, Novo México, Utah).",
        "historia": "Usada como código inquebrável pelos Code Talkers na Segunda Guerra Mundial."
    }
}

def get_linguistic_info(title, raw_val, region, is_proto, is_extinct):
    # Lookup in dictionary
    for k, info in LINGUISTIC_DESCRIPTIONS.items():
        if k.lower() in title.lower() or k.lower() in raw_val.lower():
            return info
            
    # Fallback contextual synthesis
    status_str = "Língua extinta (†), preservada em registros históricos, inscrições ou reconstrução comparativa." if is_extinct else "Língua natural viva, em uso comunitário ativo ou oficial."
    if is_proto:
        return {
            "resumo": f"Protolíngua reconstruída pelo método histórico-comparativo, ancestral do ramo {title}.",
            "status": "Protolíngua Reconstruída",
            "regiao": region,
            "caracteristicas": "Raiz filogenética ancestral identificada através de correspondências fonéticas e morfológicas regulares entre as línguas filhas."
        }
    else:
        return {
            "resumo": f"Membro da família e ramo filogenético {region}. {status_str}",
            "status": "Extinta (†)" if is_extinct else "Ativa / Viva",
            "regiao": region,
            "caracteristicas": "Classificada segundo a taxonomia comparativa de Theodor Cole (2026), Glottolog e fontes linguísticas especializadas."
        }

def build_app():
    tree = ET.parse('arvore_filogenetica_unificada_poster.drawio')
    root = tree.getroot()
    
    nodes_data = []
    edges_data = []
    
    id_map = {}
    
    for cell in root.iter('mxCell'):
        cid = cell.attrib.get('id')
        if cell.attrib.get('vertex') == '1' and cid not in ['0', '1', 'node_poster_2', 'node_poster_3']:
            g = cell.find('mxGeometry')
            if g is not None:
                x = float(g.attrib.get('x', 0))
                y = float(g.attrib.get('y', 0))
                w = float(g.attrib.get('width', 0))
                h = float(g.attrib.get('height', 0))
                raw_val = cell.attrib.get('value', '')
                style = cell.attrib.get('style', '')
                
                is_extinct = '†' in raw_val or '#f8cecc' in style
                is_proto = 'PROTO-' in raw_val.upper() or 'PROTOLÍNGUA' in raw_val.upper() or 'RADIAÇÃO' in raw_val.upper()
                is_family = '#1a365d' in style
                is_subfamily = '#2b6cb0' in style
                is_living = '#d5e8d4' in style and not is_extinct
                
                # Region
                if x < 4300:
                    region = "Indo-Europeia"
                elif x < 8400:
                    region = "Transeurasiática / Urálica / Caucásica"
                elif x < 12300:
                    region = "Afroasiática / Níger-Congo / Dravídica"
                elif x < 16600:
                    region = "Sino-Tibetana / Austronésia / Sudeste Asiático"
                else:
                    region = "Línguas Indígenas das Américas"
                    
                lines = raw_val.split('<br>')
                title = clean_html(lines[0])
                meta = clean_html(' '.join(lines[1:])) if len(lines) > 1 else ""
                
                info = get_linguistic_info(title, raw_val, region, is_proto, is_extinct)
                
                node_obj = {
                    "id": cid,
                    "title": title,
                    "meta": meta,
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "is_extinct": is_extinct,
                    "is_proto": is_proto,
                    "is_living": is_living,
                    "is_family": is_family,
                    "region": region,
                    "info": info
                }
                nodes_data.append(node_obj)
                id_map[cid] = node_obj
                
        elif cell.attrib.get('edge') == '1':
            src = cell.attrib.get('source')
            tgt = cell.attrib.get('target')
            style = cell.attrib.get('style', '')
            edges_data.append({"src": src, "tgt": tgt, "style": style})

    print(f"Loaded {len(nodes_data)} nodes and {len(edges_data)} edges for web app.")
    
    # Generate HTML App
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Árvore Filogenética das Línguas do Mundo — Visualizador Interativo</title>
  <style>
    :root {{
      --bg: #0b0f19;
      --surface: #111827;
      --surface-border: #1f2937;
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --accent: #38bdf8;
      --accent-hover: #0284c7;
      --node-living: #166534;
      --node-living-border: #22c55e;
      --node-extinct: #991b1b;
      --node-extinct-border: #ef4444;
      --node-proto: #1e3a8a;
      --node-proto-border: #3b82f6;
      --node-branch: #1e293b;
      --node-branch-border: #475569;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    
    /* Top Bar */
    header {{
      background: rgba(17, 24, 39, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--surface-border);
      padding: 10px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      z-index: 20;
    }}
    .title-box h1 {{
      font-size: 16px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .title-box p {{
      font-size: 11px;
      color: var(--text-muted);
    }}
    
    /* Controls Bar */
    .controls {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .search-input {{
      background: #1f2937;
      border: 1px solid #374151;
      color: #fff;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      width: 260px;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--accent);
    }}
    select, button {{
      background: #1f2937;
      border: 1px solid #374151;
      color: #fff;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      cursor: pointer;
      outline: none;
      transition: background 0.2s, border-color 0.2s;
    }}
    select:hover, button:hover {{
      background: #374151;
      border-color: #4b5563;
    }}
    button.primary {{
      background: #0284c7;
      border-color: #38bdf8;
      font-weight: 600;
    }}
    button.primary:hover {{
      background: #0369a1;
    }}
    
    /* Main Layout */
    #viewport {{
      flex: 1;
      position: relative;
      overflow: hidden;
      cursor: grab;
      user-select: none;
    }}
    #viewport.dragging {{
      cursor: grabbing;
    }}
    #canvas-container {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      will-change: transform;
    }}
    
    /* SVG Canvas */
    svg.tree-canvas {{
      display: block;
    }}
    .edge-line {{
      fill: none;
      stroke: #475569;
      stroke-width: 1.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: stroke 0.2s, stroke-width 0.2s;
    }}
    .edge-line.highlight {{
      stroke: #38bdf8;
      stroke-width: 3;
    }}
    
    /* HTML / SVG Nodes */
    .node-group {{
      cursor: pointer;
      transition: filter 0.2s;
    }}
    .node-group:hover {{
      filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.6));
    }}
    .node-group.active rect {{
      stroke: #facc15 !important;
      stroke-width: 3 !important;
    }}
    .node-group.match rect {{
      stroke: #a855f7 !important;
      stroke-width: 3 !important;
      animation: pulse 1.5s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ filter: drop-shadow(0 0 4px #a855f7); }}
      50% {{ filter: drop-shadow(0 0 12px #c084fc); }}
    }}
    
    /* Side Drawer */
    #sidebar {{
      position: absolute;
      top: 0;
      right: -460px;
      width: 440px;
      height: 100%;
      background: rgba(17, 24, 39, 0.98);
      backdrop-filter: blur(12px);
      border-left: 1px solid var(--surface-border);
      box-shadow: -10px 0 30px rgba(0, 0, 0, 0.7);
      transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 30;
      display: flex;
      flex-direction: column;
    }}
    #sidebar.open {{
      right: 0;
    }}
    .sidebar-header {{
      padding: 18px 20px;
      border-bottom: 1px solid var(--surface-border);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
    }}
    .sidebar-header h2 {{
      font-size: 18px;
      font-weight: 700;
      color: #fff;
      line-height: 1.3;
    }}
    .badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
      margin-top: 6px;
    }}
    .badge-living {{ background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }}
    .badge-extinct {{ background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; }}
    .badge-proto {{ background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid #3b82f6; }}
    .close-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 24px;
      cursor: pointer;
      line-height: 1;
      padding: 0 4px;
    }}
    .close-btn:hover {{
      color: #fff;
    }}
    .sidebar-content {{
      padding: 20px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .info-card {{
      background: #1f2937;
      border: 1px solid #374151;
      border-radius: 8px;
      padding: 14px;
    }}
    .info-card h4 {{
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent);
      margin-bottom: 6px;
    }}
    .info-card p, .info-card ul {{
      font-size: 13px;
      color: #e5e7eb;
      line-height: 1.5;
    }}
    .info-card ul {{
      padding-left: 18px;
    }}
    
    /* Minimap & HUD Controls */
    .hud {{
      position: absolute;
      bottom: 20px;
      left: 20px;
      background: rgba(17, 24, 39, 0.9);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      z-index: 10;
    }}
    .legend-hud {{
      position: absolute;
      bottom: 20px;
      right: 20px;
      background: rgba(17, 24, 39, 0.9);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 12px;
      display: flex;
      gap: 14px;
      z-index: 10;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .legend-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }}
  </style>
</head>
<body>

  <header>
    <div class="title-box">
      <h1>🌍 Árvore Filogenética das Línguas do Mundo</h1>
      <p>Explorador Interativo de Protolínguas e Linhagens Históricas — Cole (2026), Glottolog &amp; Campbell</p>
    </div>
    
    <div class="controls">
      <input type="text" id="searchInput" class="search-input" placeholder="Buscar língua, família ou país...">
      
      <select id="regionFilter">
        <option value="all">Todas as Macro-Regiões</option>
        <option value="Indo-Europeia">Eurásia: Indo-Europeia</option>
        <option value="Transeurasiática / Urálica / Caucásica">Norte da Eurásia &amp; Urais</option>
        <option value="Afroasiática / Níger-Congo / Dravídica">África, Oriente Médio &amp; Índia Sul</option>
        <option value="Sino-Tibetana / Austronésia / Sudeste Asiático">Leste, Sudeste Asiático &amp; Pacífico</option>
        <option value="Línguas Indígenas das Américas">Américas (Norte, Meso &amp; Sul)</option>
      </select>
      
      <select id="statusFilter">
        <option value="all">Todos os Status</option>
        <option value="living">🟢 Línguas Vivas</option>
        <option value="extinct">🔴 Línguas Extintas (†)</option>
        <option value="proto">🔵 Protolínguas &amp; Troncos</option>
      </select>
      
      <button id="btnZoomIn">＋</button>
      <button id="btnZoomOut">－</button>
      <button id="btnResetView" class="primary">Visão Geral</button>
    </div>
  </header>

  <div id="viewport">
    <div id="canvas-container">
      <svg id="treeSvg" class="tree-canvas" width="22000" height="3000">
        <g id="edgesGroup"></g>
        <g id="nodesGroup"></g>
      </svg>
    </div>

    <!-- HUD zoom controls -->
    <div class="hud">
      <button id="hudZoomIn" title="Aumentar Zoom">＋</button>
      <button id="hudZoomOut" title="Diminuir Zoom">－</button>
      <button id="hudReset" title="Enquadrar">⤢</button>
    </div>

    <!-- Quick Legend -->
    <div class="legend-hud">
      <div class="legend-item"><span class="legend-dot" style="background:#22c55e;"></span> Língua Viva</div>
      <div class="legend-item"><span class="legend-dot" style="background:#ef4444;"></span> Extinta (†)</div>
      <div class="legend-item"><span class="legend-dot" style="background:#3b82f6;"></span> Protolíngua</div>
      <div class="legend-item"><span class="legend-dot" style="background:#475569;"></span> Nó de Ramificação</div>
    </div>

    <!-- Side Drawer -->
    <aside id="sidebar">
      <div class="sidebar-header">
        <div>
          <h2 id="sideTitle">Detalhes da Língua</h2>
          <span id="sideBadge" class="badge">Status</span>
        </div>
        <button id="closeSidebar" class="close-btn">&times;</button>
      </div>
      
      <div class="sidebar-content">
        <div class="info-card">
          <h4>Classificação Filogenética</h4>
          <p id="sideFamily">Família</p>
          <p id="sidePath" style="font-size:12px; color:var(--text-muted); margin-top:4px;"></p>
        </div>

        <div class="info-card" id="cardData" style="display:none;">
          <h4>Época &amp; Berço (Urheimat)</h4>
          <p id="sideUrheimat"></p>
        </div>

        <div class="info-card">
          <h4>Síntese Histórico-Linguística</h4>
          <p id="sideDescription"></p>
        </div>

        <div class="info-card" id="cardDetails">
          <h4>Características &amp; Relevância</h4>
          <p id="sideFeatures"></p>
        </div>

        <div class="info-card" id="cardSpeakers" style="display:none;">
          <h4>Falantes &amp; Distribuição</h4>
          <p id="sideSpeakers"></p>
        </div>
      </div>
    </aside>
  </div>

  <script>
    const NODES = {json.dumps(nodes_data, ensure_ascii=False)};
    const EDGES = {json.dumps(edges_data, ensure_ascii=False)};
    const NODES_MAP = new Map(NODES.map(n => [n.id, n]));

    // Viewport state
    let scale = 0.35;
    let panX = 100;
    let panY = 50;
    let isDragging = false;
    let startX, startY;

    const viewport = document.getElementById('viewport');
    const container = document.getElementById('canvas-container');
    const edgesGroup = document.getElementById('edgesGroup');
    const nodesGroup = document.getElementById('nodesGroup');
    const sidebar = document.getElementById('sidebar');

    function updateTransform() {{
      container.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{scale}})`;
    }}

    // Render Edges
    function renderEdges() {{
      let html = '';
      for (const e of EDGES) {{
        const s = NODES_MAP.get(e.src);
        const t = NODES_MAP.get(e.tgt);
        if (!s || !t) continue;

        let d = '';
        const style = e.style || '';

        if (style.includes('exitX=0') && style.includes('entryX=0')) {{
          // Gutter routing: drops on left margin of parent
          const x0 = s.x;
          const y0 = s.y + s.h;
          const x1 = t.x;
          const y1 = t.y + t.h / 2;
          d = `M ${{x0}} ${{y0}} L ${{x0}} ${{y1}} L ${{x1}} ${{y1}}`;
        }} else {{
          // Top-down bus routing
          const x0 = s.x + s.w / 2;
          const y0 = s.y + s.h;
          const x1 = t.x + t.w / 2;
          const y1 = t.y;
          const midY = (y0 + y1) / 2;
          d = `M ${{x0}} ${{y0}} L ${{x0}} ${{midY}} L ${{x1}} ${{midY}} L ${{x1}} ${{y1}}`;
        }}

        html += `<path id="edge_${{e.src}}_${{e.tgt}}" class="edge-line" d="${{d}}" />`;
      }}
      edgesGroup.innerHTML = html;
    }}

    // Render Nodes
    function renderNodes() {{
      let html = '';
      for (const n of NODES) {{
        let fill = '#1e293b';
        let stroke = '#475569';
        let textFill = '#f8fafc';

        if (n.is_proto || n.is_family) {{
          fill = '#1e3a8a';
          stroke = '#3b82f6';
        }} else if (n.is_extinct) {{
          fill = '#450a0a';
          stroke = '#ef4444';
          textFill = '#fca5a5';
        }} else if (n.is_living) {{
          fill = '#052e16';
          stroke = '#22c55e';
          textFill = '#86efac';
        }}

        const fontSize = (n.is_proto || n.is_family) ? 14 : 11;
        const fontWeight = (n.is_proto || n.is_family || n.title.includes('PROTO')) ? 'bold' : 'normal';

        html += `
          <g class="node-group" id="node_${{n.id}}" data-id="${{n.id}}" transform="translate(${{n.x}}, ${{n.y}})">
            <rect width="${{n.w}}" height="${{n.h}}" rx="6" fill="${{fill}}" stroke="${{stroke}}" stroke-width="1.5" />
            <text x="${{n.w / 2}}" y="${{n.meta ? n.h / 2 - 4 : n.h / 2 + 4}}" fill="${{textFill}}" font-size="${{fontSize}}" font-weight="${{fontWeight}}" text-anchor="middle" dominant-baseline="central">
              ${{escapeXml(n.title)}}
            </text>
            ${{n.meta ? `
            <text x="${{n.w / 2}}" y="${{n.h / 2 + 10}}" fill="#94a3b8" font-size="9" text-anchor="middle" dominant-baseline="central">
              ${{escapeXml(n.meta.substring(0, 45))}}${{n.meta.length > 45 ? '...' : ''}}
            </text>` : ''}}
          </g>
        `;
      }}
      nodesGroup.innerHTML = html;
    }}

    function escapeXml(str) {{
      return (str || '').replace(/[<>&]/g, c => ({{'<':'&lt;', '>':'&gt;', '&':'&amp;'}})[c]);
    }}

    // Node Click -> Open Side Drawer
    nodesGroup.addEventListener('click', (e) => {{
      const g = e.target.closest('.node-group');
      if (!g) return;
      const id = g.getAttribute('data-id');
      const n = NODES_MAP.get(id);
      if (!n) return;

      selectNode(n);
    }});

    function selectNode(n) {{
      // Update UI selection
      document.querySelectorAll('.node-group.active').forEach(el => el.classList.remove('active'));
      const el = document.getElementById(`node_${{n.id}}`);
      if (el) el.classList.add('active');

      // Populate Sidebar
      document.getElementById('sideTitle').textContent = n.title;
      const badge = document.getElementById('sideBadge');
      if (n.is_extinct) {{
        badge.className = 'badge badge-extinct';
        badge.textContent = 'Língua Extinta (†)';
      }} else if (n.is_proto) {{
        badge.className = 'badge badge-proto';
        badge.textContent = 'Protolíngua / Reconstrução';
      }} else {{
        badge.className = 'badge badge-living';
        badge.textContent = 'Língua Viva / Ativa';
      }}

      document.getElementById('sideFamily').textContent = n.region;
      document.getElementById('sidePath').textContent = n.meta || 'Filogenia direta documentada';

      const info = n.info || {{}};
      document.getElementById('sideDescription').textContent = info.resumo || 'Membro do inventário comparativo filogenético.';

      if (info.data || info.urheimat) {{
        document.getElementById('cardData').style.display = 'block';
        document.getElementById('sideUrheimat').innerHTML = `<b>Época:</b> ${{info.data || 'Histórica'}}<br><b>Urheimat:</b> ${{info.urheimat || 'Ver macro-região'}}`;
      }} else {{
        document.getElementById('cardData').style.display = 'none';
      }}

      document.getElementById('sideFeatures').textContent = info.caracteristicas || info.divisao || 'Estrutura gramatical e fonológica em conformidade com o ramo filogenético.';

      if (info.falantes || info.paises) {{
        document.getElementById('cardSpeakers').style.display = 'block';
        document.getElementById('sideSpeakers').innerHTML = `<b>Falantes:</b> ${{info.falantes || 'Consulte censo local'}}<br><b>Países:</b> ${{info.paises || info.regiao || ''}}`;
      }} else {{
        document.getElementById('cardSpeakers').style.display = 'none';
      }}

      sidebar.classList.add('open');
    }}

    document.getElementById('closeSidebar').addEventListener('click', () => {{
      sidebar.classList.remove('open');
    }});

    // Search and Highlight
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', () => {{
      const q = searchInput.value.trim().toLowerCase();
      document.querySelectorAll('.node-group.match').forEach(el => el.classList.remove('match'));

      if (!q) return;

      let firstMatch = null;
      for (const n of NODES) {{
        const txt = (n.title + ' ' + n.meta + ' ' + n.region).toLowerCase();
        if (txt.includes(q)) {{
          const el = document.getElementById(`node_${{n.id}}`);
          if (el) {{
            el.classList.add('match');
            if (!firstMatch) firstMatch = n;
          }}
        }}
      }}

      if (firstMatch) {{
        focusOnNode(firstMatch);
      }}
    }});

    function focusOnNode(n) {{
      scale = 0.85;
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      panX = vw / 2 - (n.x + n.w / 2) * scale;
      panY = vh / 2 - (n.y + n.h / 2) * scale;
      updateTransform();
    }}

    // Filters
    const regionFilter = document.getElementById('regionFilter');
    const statusFilter = document.getElementById('statusFilter');

    function applyFilters() {{
      const reg = regionFilter.value;
      const st = statusFilter.value;

      for (const n of NODES) {{
        const el = document.getElementById(`node_${{n.id}}`);
        if (!el) continue;

        let visible = true;
        if (reg !== 'all' && n.region !== reg) visible = false;
        if (st === 'living' && !n.is_living) visible = false;
        if (st === 'extinct' && !n.is_extinct) visible = false;
        if (st === 'proto' && !n.is_proto) visible = false;

        el.style.display = visible ? 'block' : 'none';
      }}
    }}

    regionFilter.addEventListener('change', applyFilters);
    statusFilter.addEventListener('change', applyFilters);

    // Pan & Zoom Interaction
    viewport.addEventListener('mousedown', (e) => {{
      if (e.target.closest('#sidebar') || e.target.closest('.hud')) return;
      isDragging = true;
      viewport.classList.add('dragging');
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
      viewport.classList.remove('dragging');
    }});

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const zoomFactor = 1.15;
      const mouseX = e.clientX;
      const mouseY = e.clientY;

      let newScale = e.deltaY < 0 ? scale * zoomFactor : scale / zoomFactor;
      newScale = Math.min(Math.max(0.08, newScale), 2.5);

      panX = mouseX - (mouseX - panX) * (newScale / scale);
      panY = mouseY - (mouseY - panY) * (newScale / scale);
      scale = newScale;
      updateTransform();
    }}, {{ passive: false }});

    // Zoom buttons
    function zoomBy(factor) {{
      const vw = viewport.clientWidth / 2;
      const vh = viewport.clientHeight / 2;
      const newScale = Math.min(Math.max(0.08, scale * factor), 2.5);
      panX = vw - (vw - panX) * (newScale / scale);
      panY = vh - (vh - panY) * (newScale / scale);
      scale = newScale;
      updateTransform();
    }}

    document.getElementById('btnZoomIn').addEventListener('click', () => zoomBy(1.3));
    document.getElementById('btnZoomOut').addEventListener('click', () => zoomBy(0.7));
    document.getElementById('hudZoomIn').addEventListener('click', () => zoomBy(1.3));
    document.getElementById('hudZoomOut').addEventListener('click', () => zoomBy(0.7));

    function resetView() {{
      const vw = viewport.clientWidth;
      scale = Math.min(vw / 22000, 0.28);
      panX = 20;
      panY = 60;
      updateTransform();
      document.querySelectorAll('.node-group.active').forEach(el => el.classList.remove('active'));
    }}

    document.getElementById('btnResetView').addEventListener('click', resetView);
    document.getElementById('hudReset').addEventListener('click', resetView);

    // Initial load
    renderEdges();
    renderNodes();
    resetView();
  </script>
</body>
</html>
'''
    with open('arvore_interativa.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Application built successfully: arvore_interativa.html")

if __name__ == '__main__':
    build_app()
