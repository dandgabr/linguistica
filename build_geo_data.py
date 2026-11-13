#!/usr/bin/env python3
"""
Base de dados geolinguística rigorosa para as 19 macrofamílias filogenéticas.
Fontes: Anthony (2007), Sagart et al. (2019), Blust (1999), Ehret (1995),
Bendor-Samuel (1989), Kallio (2014), Johanson & Csató (1998), Krishnamurti (2003),
Rodrigues (1986), Kaufman (1976), Goddard (1994), Fortescue (2010),
Sidwell & Blench (2011), Ostapirat (2000), Ratliff (2010), Vovin (2010),
Lee & Ramsey (2011), Janhunen (2003, 2012), Klimov (1998).
"""

TRUNK_GEO = {
    "node_ie_4": {
        "nome": "Proto-Indo-Europeu",
        "lat": 53.20, "lon": 50.15,
        "era": "c. 4500–3000 a.C.",
        "urheimat": "Estepes Pôntico-Cáspias (Cultura Yamnaya / Vale do Médio Volga)",
        "ecologia": "Estepe temperada e bacia fluvial; economia pastoril e equina",
        "desc": "Radiação de mais de 440 línguas em direção à Europa, Anatólia, Planalto Iraniano e Ásia Meridional através das estepes e corredores fluviais eurasiáticos.",
        "alinhamento": "Nominativo-Acusativo; flexão fusional sintética; apofonia (Ablaut)",
        "ordem": "SOV arcaico -> SVO / VSO nos ramos filhotes",
        "referencia": "Anthony, David W. (2007). The Horse, the Wheel, and Language. Princeton University Press.",
        "dispersions": [
            {"nome": "Ramo Itálico (Latim)", "lat": 41.90, "lon": 12.50},
            {"nome": "Ramo Germânico (Proto-Germânico)", "lat": 55.00, "lon": 10.00},
            {"nome": "Ramo Indo-Ariano (Sânscrito Védico)", "lat": 31.50, "lon": 74.35},
            {"nome": "Ramo Iraniano (Avéstico / Persa Antigo)", "lat": 32.00, "lon": 53.00},
            {"nome": "Ramo Céltico (Gálico / Britônico)", "lat": 47.00, "lon": 2.00},
            {"nome": "Ramo Balto-Eslavo (Eslavo Antigo)", "lat": 53.00, "lon": 28.00},
            {"nome": "Ramo Helênico (Grego Micênico)", "lat": 38.00, "lon": 22.50},
            {"nome": "Ramo Anatólico (Hitita † / Hattusa)", "lat": 39.82, "lon": 34.61},
            {"nome": "Ramo Toqueano (Toqueano A/B † / Bacia de Tarim)", "lat": 41.70, "lon": 82.95}
        ]
    },
    "node_east_asia_4": {
        "nome": "Proto-Sino-Tibetano",
        "lat": 34.50, "lon": 105.70,
        "era": "c. 5200–4000 a.C.",
        "urheimat": "Bacia do Médio e Alto Rio Amarelo (Cultura Yangshao / Majiayao)",
        "ecologia": "Vales de loess e terraços fluviais do Rio Amarelo e Wei; agricultura de milhete",
        "desc": "Radiação ancestral dividida entre o ramo Sínico na planície central chinesa e os ramos Tibeto-Birmaneses pelo planalto tibetano e vales himalaios.",
        "alinhamento": "Ergativo-Absolutivo e Nominativo-Acusativo cindido; línguas tonais monossilábicas",
        "ordem": "SOV (Tibeto-Birmanês) e SVO (Sínico arcaico/moderno)",
        "referencia": "Sagart, L. et al. (2019). Dated language phylogenies shed light on the ancestry of Sino-Tibetan. PNAS, 116(21):10317–10322.",
        "dispersions": [
            {"nome": "Ramo Sínico Norte (Mandarim / Planície Central)", "lat": 34.75, "lon": 113.66},
            {"nome": "Ramo Sínico Sul (Cantonês / Min / Wu)", "lat": 23.13, "lon": 113.26},
            {"nome": "Ramo Bódico (Tibetano Clássico / Lhasa)", "lat": 29.65, "lon": 91.13},
            {"nome": "Ramo Búrmico (Birmanês / Rio Irrawaddy)", "lat": 21.97, "lon": 95.98},
            {"nome": "Ramo Himalaico (Kiranti / Nepal)", "lat": 27.70, "lon": 85.32},
            {"nome": "Império Tangut † (Xixia / Rio Amarelo)", "lat": 38.50, "lon": 106.20}
        ]
    },
    "node_east_asia_128": {
        "nome": "Proto-Austronésio",
        "lat": 23.70, "lon": 120.95,
        "era": "c. 3500–2500 a.C.",
        "urheimat": "Ilha de Taiwan (Culturas Neolíticas Ta-pen-k'eng e Yuanshan)",
        "ecologia": "Ambiente insular marítimo subtropical com navegação de canoas de balancim",
        "desc": "Maior expansão marítima da pré-história humana, cobrindo mais de 200 graus de longitude, desde Madagascar no Oceano Índico até a Ilha de Páscoa no Pacífico Oriental.",
        "alinhamento": "Sistema de alinhamento austronésio (foco no agente/paciente/locativo/instrumento)",
        "ordem": "VSO / VOS inicial preservada nos ramos formosanos e filipinos",
        "referencia": "Blust, Robert (1999). Subgrouping, circularity and extinction in Austronesian. Academia Sinica.",
        "dispersions": [
            {"nome": "Filipinas (Tagalo / Cebuano / Ilokano)", "lat": 17.57, "lon": 120.38},
            {"nome": "Indonésia & Malásia (Malaio / Javanês)", "lat": -6.20, "lon": 106.81},
            {"nome": "Madagascar (Malgaxe / Oceano Índico)", "lat": -18.76, "lon": 46.86},
            {"nome": "Melanésia (Cultura Lapita / Bismarck)", "lat": -2.00, "lon": 147.00},
            {"nome": "Polinésia Central (Samoa / Tonga / Taiti)", "lat": -13.83, "lon": -171.76},
            {"nome": "Aotearoa / Nova Zelândia (Maori)", "lat": -38.50, "lon": 175.50},
            {"nome": "Rapa Nui (Ilha de Páscoa)", "lat": -27.11, "lon": -109.35}
        ]
    },
    "node_afro_niger_drav_4": {
        "nome": "Proto-Afroasiático",
        "lat": 15.50, "lon": 37.50,
        "era": "c. 12000–9000 a.C.",
        "urheimat": "Corredor do Mar Vermelho / Chifre da África Setentrional e Alto Nilo",
        "ecologia": "Savana pré-holocênica e zonas ripárias do Nilo e Mar Vermelho",
        "desc": "Tronco linguístico de maior profundidade temporal comprovada; deu origem aos grandes ramos Semítico, Egípcio, Berbere, Chádico, Cuchítico e Omótico.",
        "alinhamento": "Nominativo-Acusativo; morfologia de raiz consonantal triconsonântica com introflexão",
        "ordem": "VSO arcaico característico",
        "referencia": "Ehret, Christopher (1995). Reconstructing Proto-Afroasiatic. University of California Press.",
        "dispersions": [
            {"nome": "Ramo Semítico (Árabe / Aramaico / Hebraico)", "lat": 31.50, "lon": 35.50},
            {"nome": "Mesopotâmia (Acadiano / Assírio-Babilônico †)", "lat": 33.30, "lon": 44.40},
            {"nome": "Vale do Nilo (Egípcio Antigo & Copta †)", "lat": 26.00, "lon": 32.00},
            {"nome": "Norte da África (Berbere / Amazigh)", "lat": 28.00, "lon": 10.00},
            {"nome": "Bacia do Chade (Hauçá / Chádico)", "lat": 12.50, "lon": 14.50},
            {"nome": "Chifre da África (Cuchítico - Somali / Oromo)", "lat": 9.00, "lon": 40.00}
        ]
    },
    "node_afro_niger_drav_83": {
        "nome": "Proto-Níger-Congo",
        "lat": 8.50, "lon": 7.50,
        "era": "c. 6000–4000 a.C.",
        "urheimat": "Bacia dos Rios Níger e Benue / Linha de Camarões",
        "ecologia": "Mosaico de savana e floresta tropical úmida guineense",
        "desc": "Maior família linguística da África em número de línguas e falantes, centro propulsor da monumental expansão Banto que povoou o centro, leste e sul do continente.",
        "alinhamento": "Nominativo-Acusativo; sistema elaborado de classes nominais com concordância por prefixos",
        "ordem": "SVO predominante com núcleo inicial",
        "referencia": "Bendor-Samuel, John (1989). The Niger-Congo Languages. University Press of America.",
        "dispersions": [
            {"nome": "África Ocidental (Iorubá / Igbo / Kwa)", "lat": 6.50, "lon": 3.40},
            {"nome": "Senegâmbia (Fula / Wolof / Atlântico)", "lat": 14.50, "lon": -17.40},
            {"nome": "Berço Banto (Fronteira Nigéria-Camarões)", "lat": 5.50, "lon": 9.50},
            {"nome": "Bacia do Congo (Quimbundo / Lingala)", "lat": -4.30, "lon": 15.30},
            {"nome": "Costa Leste Africana (Suaíli)", "lat": -6.80, "lon": 39.30},
            {"nome": "África Austral (Zulu / Xhosa)", "lat": -26.20, "lon": 28.04}
        ]
    },
    "node_trans_uralic_113": {
        "nome": "Proto-Urálico",
        "lat": 56.50, "lon": 50.00,
        "era": "c. 3000–2000 a.C.",
        "urheimat": "Bacia do Médio Volga / Encostas Ocidentais dos Montes Urais",
        "ecologia": "Floresta boreal de taiga mista e bacias hidrográficas do Volga e Kama",
        "desc": "Dispersão pelas florestas boreais do norte europeu e sibéria ocidental, alcançando o Báltico, a Escandinávia e a planície panônica da bacia do Danúbio.",
        "alinhamento": "Nominativo-Acusativo com marcação diferencial de objeto; aglutinante estrito com harmonia vocálica",
        "ordem": "SOV arcaico rígido com posposições",
        "referencia": "Kallio, Petri (2014). The Stratigraphy of Uralic Prehistoric Loanwords. Rodopi.",
        "dispersions": [
            {"nome": "Mar Báltico & Finlândia (Suomi / Estoniano)", "lat": 58.50, "lon": 25.00},
            {"nome": "Bacia dos Cárpatos (Húngaro / Magyar)", "lat": 47.50, "lon": 19.04},
            {"nome": "Lapônia Ártica (Línguas Sámi)", "lat": 68.00, "lon": 25.00},
            {"nome": "Sibéria Ocidental (Samoiédico - Nenets / Khanty)", "lat": 61.00, "lon": 69.00},
            {"nome": "Região Volga-Kama (Mari / Udmurte / Komi)", "lat": 56.00, "lon": 48.00}
        ]
    },
    "node_trans_uralic_4": {
        "nome": "Proto-Túrquico",
        "lat": 49.50, "lon": 89.00,
        "era": "c. 1000 a.C.–200 d.C.",
        "urheimat": "Montes Altai / Sibéria Meridional e Noroeste da Mongólia",
        "ecologia": "Estepes de altitude e taiga montanhosa siberiana",
        "desc": "Expansão pastoril nômade pelas estepes da Ásia Central até o Cáucaso, Bacia do Volga, Anatólia e extremo norte da Sibéria.",
        "alinhamento": "Nominativo-Acusativo; aglutinante regular sem prefixos; harmonia vocálica palatal e labial",
        "ordem": "SOV núcleo-final estrito",
        "referencia": "Johanson, Lars & Csató, Éva Á. (1998). The Turkic Languages. Routledge.",
        "dispersions": [
            {"nome": "Estepe Central (Canato de Orkhon)", "lat": 47.55, "lon": 102.83},
            {"nome": "Ásia Central (Cazaque / Quirguiz / Uzbeque)", "lat": 43.00, "lon": 68.00},
            {"nome": "Anatólia (Turco Otomano & Moderno)", "lat": 39.92, "lon": 32.85},
            {"nome": "Cáspio & Cáucaso (Azeri / Turcomeno)", "lat": 40.40, "lon": 49.80},
            {"nome": "Bacia do Volga (Chuvache / Tártaro)", "lat": 55.80, "lon": 49.10},
            {"nome": "Sibéria Setentrional (Yakut / Sakha)", "lat": 62.03, "lon": 129.73}
        ]
    },
    "node_afro_niger_drav_156": {
        "nome": "Proto-Dravídico",
        "lat": 21.50, "lon": 74.00,
        "era": "c. 3500–2500 a.C.",
        "urheimat": "Noroeste do Planalto do Decão / Gujarat e Bacia do Rio Narmada",
        "ecologia": "Florestas decíduas tropicais e planalto basáltico do Decão",
        "desc": "Família autóctone primordial do subcontinente indiano, outrora mais dispersa pelo norte e agora concentrada nos grandes estados do sul da Índia.",
        "alinhamento": "Nominativo-Acusativo; rica morfologia aglutinante com sufixação; distinção retroflexa fonêmica",
        "ordem": "SOV estrito com posposições",
        "referencia": "Krishnamurti, Bhadriraju (2003). The Dravidian Languages. Cambridge University Press.",
        "dispersions": [
            {"nome": "Tamil Nadu (Tâmil Clássico & Sangam)", "lat": 11.00, "lon": 78.50},
            {"nome": "Karnataka (Canará / Kannada)", "lat": 12.97, "lon": 77.59},
            {"nome": "Andhra Pradesh & Telangana (Telugu)", "lat": 16.50, "lon": 80.50},
            {"nome": "Kerala (Malaiala / Malayalam)", "lat": 10.00, "lon": 76.50},
            {"nome": "Baluchistão (Brahui / Paquistão Ocidental)", "lat": 28.50, "lon": 66.50},
            {"nome": "Índia Central (Gondi / Kolami)", "lat": 20.00, "lon": 81.50}
        ]
    },
    "node_americas_128": {
        "nome": "Protolínguas da América do Sul",
        "lat": -11.50, "lon": -62.50,
        "era": "c. 3000–1500 a.C.",
        "urheimat": "Bacias dos Rios Madeira, Guaporé e Mamoré (Rondônia, Brasil)",
        "ecologia": "Transição biogeográfica entre floresta amazônica de terra firme e campos sul-amazônicos",
        "desc": "Berço de alta diversidade interna comprovada para o Tronco Tupi e irradiações para as bacias do Madeira, Paraná, Paraguai e litoral atlântico, complementado pelos troncos Aruaque, Macro-Jê e Quechua.",
        "alinhamento": "Cisão ativo-estativo / ergativo-absolutivo nos ramos amazônicos",
        "ordem": "SOV e SVO com marcação de posse por prefixos relacionais",
        "referencia": "Rodrigues, Aryon D. (1986). Línguas Brasileiras. Ed. Loyola.",
        "dispersions": [
            {"nome": "Litoral Atlântico (Tupinambá & Tupi Antigo †)", "lat": -23.00, "lon": -44.00},
            {"nome": "Bacia do Prata (Guarani / Paraguai)", "lat": -25.00, "lon": -56.00},
            {"nome": "Alto Rio Negro (Nheengatu / Língua Geral)", "lat": -0.10, "lon": -67.00},
            {"nome": "Andes Centrais (Quechua / Cusco)", "lat": -13.52, "lon": -71.97},
            {"nome": "Planalto Andino (Aimará / Lago Titicaca)", "lat": -16.50, "lon": -68.15},
            {"nome": "Brasil Central (Macro-Jê - Xavante / Kaingang)", "lat": -14.00, "lon": -52.00}
        ]
    },
    "node_americas_71": {
        "nome": "Protolínguas da Mesoamérica",
        "lat": 15.32, "lon": -91.47,
        "era": "c. 2200–1500 a.C.",
        "urheimat": "Terras Altas da Guatemala (Cordilheira dos Cuchumatanes)",
        "ecologia": "Florestas montanas de pinheiro-carvalho e vales intramontanos mesoamericanos",
        "desc": "Berço ancestral da família Maia, integrado na área de convergência linguística da Mesoamérica junto aos troncos Otomangueano (Oaxaca) e Uto-Asteca.",
        "alinhamento": "Ergativo-Absolutivo estrito com marcação na raiz verbal; consoantes ejetivas/glotalizadas",
        "ordem": "VSO e VOS predominantes",
        "referencia": "Kaufman, Terrence (1976). Archaeological and Linguistic Correlations in Mayaland. World Archaeology.",
        "dispersions": [
            {"nome": "Costa do Golfo (Huasteco / San Luis Potosí)", "lat": 22.00, "lon": -98.50},
            {"nome": "Terras Baixas do Petén (Iucateco / Cholano / Tikal)", "lat": 17.00, "lon": -89.90},
            {"nome": "Península de Iucatã (Maia Yucateco)", "lat": 20.50, "lon": -89.00},
            {"nome": "Planalto Mexicano (Náuatle / Mexica)", "lat": 19.43, "lon": -99.13},
            {"nome": "Vales de Oaxaca (Zapoteca & Mixteco)", "lat": 17.06, "lon": -96.72}
        ]
    },
    "node_americas_4": {
        "nome": "Protolínguas da América do Norte",
        "lat": 64.00, "lon": -145.00,
        "era": "c. 3500–1500 a.C.",
        "urheimat": "Bacia do Rio Yukon / Interior do Alasca e Subártico Canadense",
        "ecologia": "Taiga boreal subártica com redes lacustres e fluviais de drenagem para o Pacífico",
        "desc": "Berço do tronco Na-Dene (Eyak-Atabascano), com dispersões pela Costa Noroeste e pela migração interior até o Sudoeste árido norte-americano (Navajo/Apache).",
        "alinhamento": "Polissintético extremo com estrutura de prefixos posicionais em fendas no verbo",
        "ordem": "SOV núcleo-final",
        "referencia": "Krauss, Michael E. (1973). Na-Dene. Current Trends in Linguistics, Mouton.",
        "dispersions": [
            {"nome": "Sudoeste dos EUA (Navajo / Diné & Apache)", "lat": 36.00, "lon": -109.50},
            {"nome": "Grandes Planícies (Cree & Ojibwe / Algonguiano)", "lat": 46.50, "lon": -84.35},
            {"nome": "Costa Atlântica Leste (Powhatan & Iroquês)", "lat": 37.50, "lon": -76.50},
            {"nome": "Ártico & Groenlândia (Inuit / Inuktitut)", "lat": 65.50, "lon": -168.00},
            {"nome": "Grandes Planícies Centrais (Sioux / Lakota)", "lat": 44.00, "lon": -102.00}
        ]
    },
    "node_east_asia_97": {
        "nome": "Proto-Austroasiático",
        "lat": 21.50, "lon": 101.50,
        "era": "c. 3000–2000 a.C.",
        "urheimat": "Bacia do Médio Rio Mekong e Yunnan Meridional",
        "ecologia": "Vales fluviais tropicais e subtropicais de cultivo inicial de arroz úmido",
        "desc": "Tronco autóctone arcaico do Sudeste Asiático continental, outrora contínuo desde o Leste da Índia até o litoral do Vietnã e Península Malaia.",
        "alinhamento": "Nominativo-Acusativo; línguas isolantes com afixação não concatenativa; ricos inventários vocálicos",
        "ordem": "SVO predominante (exceto ramos Munda que adotaram SOV na Índia)",
        "referencia": "Sidwell, Paul & Blench, Roger (2011). The Austroasiatic Urheimat. Pacific Linguistics.",
        "dispersions": [
            {"nome": "Camboja (Khmer / Angkor)", "lat": 11.56, "lon": 104.92},
            {"nome": "Vietnã (Vietnamita / Tiếng Việt)", "lat": 21.03, "lon": 105.85},
            {"nome": "Birmânia & Tailândia (Línguas Mon)", "lat": 16.50, "lon": 97.50},
            {"nome": "Índia Oriental (Ramo Munda - Santali / Chota Nagpur)", "lat": 23.00, "lon": 85.50},
            {"nome": "Ilhas Nicobar (Ramo Nicobarês)", "lat": 7.00, "lon": 93.80}
        ]
    },
    "node_east_asia_68": {
        "nome": "Proto-Kra-Dai (Tai-Kadai)",
        "lat": 23.00, "lon": 108.50,
        "era": "c. 2000–1200 a.C.",
        "urheimat": "Litoral Sul da China (Guangxi Oriental e Guangdong Ocidental)",
        "ecologia": "Planícies aluviais costeiras e bacia do Rio das Pérolas",
        "desc": "Migração em direção ao sul em direção às férteis bacias fluviais da Indochina e Tailândia impulsionada pela expansão agrária.",
        "alinhamento": "Línguas tonais analíticas isolantes com classificadores numerais obrigatórios",
        "ordem": "SVO estrito",
        "referencia": "Ostapirat, Weera (2000). Proto-Kra. Linguistics of the Tibeto-Burman Area, 23(1):1–251.",
        "dispersions": [
            {"nome": "Planície Central da Tailândia (Tailandês / Siamês)", "lat": 14.50, "lon": 100.50},
            {"nome": "Bacia do Médio Mekong (Lao / Vientiane)", "lat": 17.97, "lon": 102.63},
            {"nome": "Guangxi (Línguas Zhuang)", "lat": 22.80, "lon": 108.30},
            {"nome": "Ilha de Hainan (Línguas Hlai / Kadai)", "lat": 19.00, "lon": 109.50},
            {"nome": "Nordeste da Índia (Ahom / Vale do Brahmaputra)", "lat": 26.98, "lon": 94.63}
        ]
    },
    "node_east_asia_53": {
        "nome": "Proto-Hmong-Mien",
        "lat": 28.50, "lon": 112.50,
        "era": "c. 2500–1800 a.C.",
        "urheimat": "Bacia Central do Rio Yangtzé (Entre os Lagos Dongting e Poyang)",
        "ecologia": "Zonas úmidas de várzea do Yangtzé e sopés montanhosos de Hunan e Hubei",
        "desc": "Povos Hmong e Mien ancestralmente ligados às culturas arrozeiras do Médio Yangtzé, progressivamente empurrados para as terras altas da China meridional e Indochina.",
        "alinhamento": "Línguas isolantes monossilábicas com sistemas tonais hiperdesenvolvidos (até 8-12 tons)",
        "ordem": "SVO",
        "referencia": "Ratliff, Martha (2010). Hmong-Mien Language History. Pacific Linguistics.",
        "dispersions": [
            {"nome": "Planalto de Guizhou (Hmong de Guizhou)", "lat": 26.50, "lon": 106.70},
            {"nome": "Montanhas Nanling (Iu Mien / Guangxi)", "lat": 24.50, "lon": 110.00},
            {"nome": "Yunnan & Indochina (Hmong Branco e Verde)", "lat": 23.50, "lon": 103.50},
            {"nome": "Terras Altas do Laos e Vietnã (Miao-Yao)", "lat": 19.50, "lon": 103.00}
        ]
    },
    "node_trans_uralic_85": {
        "nome": "Proto-Japônico",
        "lat": 33.60, "lon": 130.40,
        "era": "c. 900–300 a.C.",
        "urheimat": "Norte de Kyushu / Península Coreana Meridional (Cultura Arqueológica Yayoi Inicial)",
        "ecologia": "Planícies litorâneas e vales férteis propícios à orizicultura inundada irrigada",
        "desc": "Introduzido no arquipélago japonês pelos migrantes Yayoi trazendo agricultura e metalurgia, substituindo e assimilando as línguas da cultura Jomon original.",
        "alinhamento": "Nominativo-Acusativo; morfologia aglutinante sufixal com partícula de tópico dedicada (wa)",
        "ordem": "SOV núcleo-final estrito",
        "referencia": "Vovin, Alexander (2010). Koreo-Japonica. University of Hawai'i Press.",
        "dispersions": [
            {"nome": "Região de Kansai / Kinki (Yamato / Quioto / Nara)", "lat": 34.68, "lon": 135.80},
            {"nome": "Planície de Kanto (Tóquio / Honshu Oriental)", "lat": 35.68, "lon": 139.75},
            {"nome": "Honshu Setentrional (Tohoku)", "lat": 39.70, "lon": 141.15},
            {"nome": "Ilhas Ryukyu (Okinawano / Naha)", "lat": 26.21, "lon": 127.68},
            {"nome": "Kyushu Meridional (Kagoshima)", "lat": 31.60, "lon": 130.55}
        ]
    },
    "node_trans_uralic_100": {
        "nome": "Proto-Coreânico",
        "lat": 41.00, "lon": 123.00,
        "era": "c. 500 a.C.–300 d.C.",
        "urheimat": "Bacia do Rio Liao Meridional (Manchúria) e Península de Liaodong",
        "ecologia": "Planície aluvial temperada da Manchúria com transição para vales montanhosos",
        "desc": "Formado na bacia do Liao e expandido pela península coreana, consolidando-se através dos reinos de Goguryeo, Baekje e Silla.",
        "alinhamento": "Nominativo-Acusativo com sistema honorífico altamente estratificado no verbo",
        "ordem": "SOV núcleo-final rigoroso",
        "referencia": "Lee, Ki-Moon & Ramsey, S. Robert (2011). A History of the Korean Language. Cambridge University Press.",
        "dispersions": [
            {"nome": "Bacia do Rio Taedong (Gojoseon / Pyongyang)", "lat": 39.02, "lon": 125.75},
            {"nome": "Península Central (Vale do Rio Han / Seul)", "lat": 37.56, "lon": 126.97},
            {"nome": "Sudeste Peninsular (Reino de Silla / Gyeongju)", "lat": 35.83, "lon": 129.21},
            {"nome": "Manchúria e Bacia do Yalu (Reino de Goguryeo)", "lat": 41.12, "lon": 126.18},
            {"nome": "Ilha de Jeju (Língua de Jeju)", "lat": 33.50, "lon": 126.52}
        ]
    },
    "node_trans_uralic_55": {
        "nome": "Proto-Mongólico",
        "lat": 49.00, "lon": 111.00,
        "era": "c. 300–800 d.C.",
        "urheimat": "Bacia dos Rios Shilka e Onon / Montanhas Khentii (Trans-Baikal / Mongólia)",
        "ecologia": "Estepe-floresta da Sibéria meridional e planalto mongol",
        "desc": "Desenvolvido a partir das tribos montanhesas do norte, expandiu-se espetacularmente por toda a Eurásia durante o Império Mongol a partir do século XIII.",
        "alinhamento": "Nominativo-Acusativo; aglutinante com harmonia vocálica e rica declinação de casos",
        "ordem": "SOV núcleo-final",
        "referencia": "Janhunen, Juha (2003). The Mongolic Languages. Routledge.",
        "dispersions": [
            {"nome": "Planalto Central Mongol (Khalkha / Rio Orkhon)", "lat": 47.20, "lon": 102.84},
            {"nome": "Bacia do Lago Baikal (Buriato / Buriácia)", "lat": 52.00, "lon": 107.50},
            {"nome": "Manchúria Ocidental (Ramo Dagur)", "lat": 48.50, "lon": 123.50},
            {"nome": "Planalto de Qinghai (Monguor / Santa)", "lat": 36.50, "lon": 101.50},
            {"nome": "Bacia do Baixo Volga (Calmuco / Elista)", "lat": 46.30, "lon": 44.25}
        ]
    },
    "node_trans_uralic_70": {
        "nome": "Proto-Tungúsico",
        "lat": 48.00, "lon": 134.00,
        "era": "c. 500 a.C.–500 d.C.",
        "urheimat": "Bacia do Médio e Baixo Rio Amur e Bacia do Rio Ussuri (Manchúria Exterior)",
        "ecologia": "Florestas temperadas e taiga úmida do Amur; economia mista de caça, pesca e criação de renas/suínos",
        "desc": "Radiação de povos caçadores e pastores que ocuparam a vasta taiga siberiana oriental até o Oceano Ártico e fundaram a dinastia Qing na China (Manchu).",
        "alinhamento": "Nominativo-Acusativo; morfologia aglutinante com harmonia vocálica palatal",
        "ordem": "SOV núcleo-final",
        "referencia": "Janhunen, Juha (2012). The Expansion of the Tungusic Languages. Folia Orientalia, 49.",
        "dispersions": [
            {"nome": "Manchúria Central (Jurchen / Manchu - Dinastia Qing)", "lat": 43.85, "lon": 126.55},
            {"nome": "Taiga da Sibéria Oriental (Evenki / Tunguska)", "lat": 60.00, "lon": 100.00},
            {"nome": "Costa de Okhotsk (Língua Even)", "lat": 62.00, "lon": 145.00},
            {"nome": "Foz do Amur & Sacalina (Nanai / Ulch / Orok)", "lat": 52.00, "lon": 141.00},
            {"nome": "Noroeste da China / Xinjiang (Xibe)", "lat": 43.80, "lon": 81.30}
        ]
    },
    "node_trans_uralic_166": {
        "nome": "Proto-Kartveliano",
        "lat": 42.00, "lon": 43.00,
        "era": "c. 3000–2000 a.C.",
        "urheimat": "Sul da Transcaucásia / Cáucaso Menor e Geórgia Ocidental",
        "ecologia": "Vales montanhosos de altitude e sopés florestados entre o Mar Negro e a cordilheira do Cáucaso",
        "desc": "Família autóctone isolada do Cáucaso meridional, caracterizada pela separação precoce do Svan nas terras altas e cisão posterior entre Georgiano e Zan (Megrelo-Laz).",
        "alinhamento": "Ergatividade cindida complexa (alinhamento nominativo no presente, ergativo no aoristo, dativo no perfeito)",
        "ordem": "SOV arcaico, atualmente flexível orientada a foco",
        "referencia": "Klimov, Georgy A. (1998). Etymological Dictionary of the Kartvelian Languages. Mouton de Gruyter.",
        "dispersions": [
            {"nome": "Terras Altas da Suanécia (Svan / Monte Elbrus)", "lat": 43.04, "lon": 42.72},
            {"nome": "Costa do Mar Negro / Cólquida (Megrelo / Samegrelo)", "lat": 42.50, "lon": 41.87},
            {"nome": "Costa Pontina da Anatólia (Laz / Rize-Hopa)", "lat": 41.20, "lon": 41.30},
            {"nome": "Geórgia Oriental (Georgiano / Tbilisi / Vale do Kura)", "lat": 41.72, "lon": 44.79}
        ]
    }
}
print("Geographic, chronological and linguistic metadata updated for all 19 trunks.")
