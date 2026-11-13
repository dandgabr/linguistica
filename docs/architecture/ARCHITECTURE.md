# 🏛️ Arquitetura do Sistema — Herbário Filogenético

> **Documento Normativo de Arquitetura e Engenharia de Software**  
> Projeto: **Linguística** ([linguas.dan.seg.br](https://linguas.dan.seg.br))

---

## 1. Princípios Arquiteturais e Restrições Globais

1. **Autonomia Local e Resiliência Zero-Network:**
   - O aplicativo compilado (`index.html` / `arvore_interativa.html`) funciona com **zero dependências externas em tempo de execução**.
   - Executável diretamente via protocolo `file://` ou em qualquer servidor HTTP estático (GitHub Pages, Cloudflare Pages, Nginx, Apache).
   - Bibliotecas gráficas (D3.js v7) e geometrias topológicas (*Natural Earth 110m*) são embutidas inline no próprio artefato.

2. **Estética "Organic / Biophilic / Solarpunk":**
   - **Superfície e Tonalidade:** Fundo pergaminho/linho cru (`#F7F4EB`), superfícies elevadas em marfim (`#FFFDF9`) e bordas suaves em sépia (`#E2D9C8`).
   - **Identidade Cromática Botânica:**
     - 🟢 *Línguas Vivas:* Verde folha (`#2E7D32` / `#4CAF50`).
     - 🔴 *Línguas Extintas (†):* Vermelho argila/terracota (`#B91C1C` / `#EF4444`).
     - 🔵 *Protolínguas Reconstruídas:* Azul índigo/azurita (`#1D4ED8` / `#3B82F6`).
     - 🟤 *Sub-ramos Taxonômicos:* Marrom casca/tronco (`#4A3B32` / `#8C7A6B`).
     - 🟡 *Seiva Ancestral Ativa:* Âmbar dourado com pulso luminescente (`#D97706`, `rgba(217, 119, 6, 0.4)`).
   - **Tipografia Humanista Clássica:** Títulos em serifas editoriais (*Playfair Display*, *Georgia*, *Baskerville*) e corpo em sans-serif neutra de alta legibilidade.

3. **Rigor Científico e Terminológico:**
   - Erradicação de adjetivos laudatórios e chavões acríticos.
   - Linguagem estritamente filogenética: alinhamento morfossintático (nominativo-acusativo, ergativo-absolutivo clivado, ativo-estativo, alinhamento de foco austronésio), ordem básica de constituintes (SVO, SOV, VSO, VOS), níveis de síntese (aglutinante, fusional, isolante, polissintético) e datações calibradas por glotocronologia e radiocarbono.

---

## 2. Visão Estrutural do Repositório

```
linguistica/
├── index.html                   # Artefato estático de produção (GitHub Pages)
├── arvore_interativa.html       # Cópia compilada de trabalho para visualização local
├── CNAME                        # Apontamento de DNS (linguas.dan.seg.br)
├── LICENSE                      # Licença de código aberto MIT
├── README.md                    # Vitrine principal e documentação geral do projeto
│
├── docs/                        # Documentação Técnica e Acadêmica
│   ├── architecture/            # Decisões e diagramas arquiteturais
│   │   └── ARCHITECTURE.md      # Este documento normativo
│   └── references/              # Corpus bibliográfico e notas metodológicas
│       └── BIBLIOGRAPHY.md      # Bibliografia acadêmica consolidada com DOIs e metadados
│
├── src/                         # Código-Fonte Modular
│   ├── assets/                  # Ativos estáticos compilados inline
│   │   ├── d3.min.js            # Biblioteca D3 v7 para projeção ortográfica e interpolação esférica
│   │   └── ne_land_110m_compact.json # GeoJSON compacto das massas continentais (Natural Earth 110m)
│   ├── data/                    # Modelos de Dados e Parsers
│   │   ├── build_geo_data.py    # Catálogo geolinguístico das 21 macrofamílias e vetores de dispersão
│   │   ├── build_organic_data.py# Extrator e higienizador do XML/Drawio de 580 nós filogenéticos
│   │   ├── process_tree.py      # Construtor do grafo taxonômico e gerador da linhagem ancestral
│   │   └── arvore_filogenetica_unificada_poster.drawio # Grafo original em formato vetorial draw.io
│   ├── generators/              # Geradores setoriais das árvores filogenéticas
│   │   ├── gen_indoeuropean.py
│   │   ├── gen_east_asia.py
│   │   ├── gen_afroasiatic_nigercongo.py
│   │   ├── gen_transeurasian_uralic.py
│   │   ├── gen_americas.py
│   │   ├── gen_pages.py
│   │   └── tree_builder.py
│   └── templates/               # Templates de interface visual
│       ├── template_head.html   # Estrutura HTML, design tokens CSS e regras de responsividade
│       └── template_scripts_d3.js # Lógica reativa do globo 3D, cinemática, filtros e árvore viva
│
├── tools/                       # Ferramentas de Engenharia e Qualidade
│   ├── build.py                 # Compilador que monta o artefato monolítico autônomo
│   └── test_phase2_qa.py        # Suíte de testes automatizados de integridade, geometria e grafos
│
└── legacy/                      # Arquivos históricos preservados de versões e protótipos anteriores
```

---

## 3. Os Três Motores Visuais

### 3.1 🌍 Globo 3D Ortográfico (`d3.geoOrthographic`)
* **Recorte de Visibilidade Frontal:**  
  O bug clássico de projeções cartográficas onde pontos do verso da Terra vazavam para a frente (ex.: línguas da Europa sobrepostas ao Oceano Pacífico) é rigorosamente resolvido através da medição da distância angular euclidiana-esférica:
  $$\text{dist} = \arccos(\sin(\text{lat}_c)\sin(\text{lat}_p) + \cos(\text{lat}_c)\cos(\text{lat}_p)\cos(\text{lon}_p - \text{lon}_c))$$
  Implementado via `d3.geoDistance(center, [lon, lat]) \le \frac{\pi}{2} + 0.002$.
* **Renderização em Camadas no Canvas 2D:**
  1. *Esfera Oceânica Sólida:* Gradiente radial de cor pergaminho/linho que bloqueia transparências indesejadas.
  2. *Graticule Esférico:* Meridianos e paralelos sutis com 10 graus de espaçamento.
  3. *Polígonos Continentais:* Massas terrestres preenchidas em sálvia fosca (`#9AAF8F`) e contorno musgo.
  4. *Arcos Geodésicos de Migração:* Linhas tracejadas conectando o *Urheimat* aos entrepostos de dispersão.
  5. *Marcadores de Urheimat com Halo:* Pinos dourados pulsantes para a família ativa e verdes para as demais.
  6. *Vinheta Atmosférica:* Gradiente radial especular que confere volume e acabamento tridimensional natural.

### 3.2 🏛️ Dossel das Macrofamílias (Macro Canopy Grid)
* Grid responsivo em CSS (auto-fill, minmax 280px).
* Exibição de cards estatísticos com cálculo instantâneo de nós filhos (`countKids()`), destacando a repartição entre vivas, extintas e protolínguas.
* Filtragem síncrona: ao acionar filtros globais, macrofamílias sem representantes têm sua opacidade reduzida (`opacity: 0.25`), filtro em escala de cinza e cliques suspensos (`pointer-events: none`).

### 3.3 🌿 Árvore Filogenética Viva (Living Tree Engine)
* **Algoritmo de Layout Tidy Tree:**  
  Determina recursivamente a posição $X$ de cada nó com base na profundidade taxonômica ($X = \text{depth} \times 240\text{px}$) e a posição $Y$ como a média aritmética da posição vertical de seus nós filhos. Folhas são distribuídas com espaçamento mínimo de $72\text{px}$, eliminando sobreposições.
* **Cipós Orgânicos (Bézier Splines):**  
  As conexões entre línguas progenitoras e filhas são desenhadas em SVG através de curvas cúbicas suaves:
  $$M(x_0, y_0) \;\; C(x_0 + \Delta x \cdot 0.55, y_0), \;\; (x_1 - \Delta x \cdot 0.55, y_1), \;\; (x_1, y_1)$$
* **Condução de Seiva Ancestral (*Sap-Flow*):**  
  Ao clicar em qualquer língua, todo o caminho genealógico do nó atual até a raiz ancestral é destacado com animação de fluxo dourado pontilhado (*SVG stroke-dashoffset loop*), permitindo visualizar visualmente milênios de evolução fonológica e ramificação histórica.

---

## 4. Pipeline de Compilação e Deploy

O pipeline de compilação é estritamente reprodutível:

```bash
# Executa a compilação monolítica que alimenta index.html
python3 tools/build.py

# Executa a suíte de validação formal de QA
python3 tools/test_phase2_qa.py
```

O deploy é automático no GitHub Pages acionado via commits na branch `main`, servido sob SSL gerenciado na Cloudflare com o domínio `linguas.dan.seg.br`.
