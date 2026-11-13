#!/usr/bin/env python3
import json
import process_tree
import build_geo_data as geo

with open('landmasses.json', 'r') as f:
    LANDMASSES = json.load(f)

TRUNK_GEO = geo.TRUNK_GEO

def build():
    nodes, trunks_meta = process_tree.generate()
    
    nodes_json = json.dumps(nodes, ensure_ascii=False)
    trunks_json = json.dumps(trunks_meta, ensure_ascii=False)
    geo_json = json.dumps(TRUNK_GEO, ensure_ascii=False)
    land_json = json.dumps(LANDMASSES, ensure_ascii=False)
    
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Herbário Filogenético das Línguas do Mundo — Visualizador Orgânico</title>
  <style>
    :root {{
      --bg-linen: #F7F4EB;
      --bg-surface: #FFFFFF;
      --bg-surface-elevated: #FFFDF9;
      --bg-subtle: #EFE9DC;
      --border-warm: #E2D9C8;
      --border-focus: #2C533A;
      
      --ink-deep: #1B3524;
      --ink-heading: #14261A;
      --ink-muted: #5C6B5F;
      --ink-light: #8A988D;
      
      --sap-gold: #D97706;
      --sap-glow: rgba(217, 119, 6, 0.4);
      --leaf-green: #2E7D32;
      --leaf-border: #4CAF50;
      --extinct-clay: #B91C1C;
      --extinct-border: #EF4444;
      --proto-azure: #1D4ED8;
      --proto-border: #3B82F6;
      --branch-bark: #4A3B32;
      --branch-border: #8C7A6B;

      --font-serif: "Playfair Display", "Georgia", "Baskerville", "Palatino", serif;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-linen);
      color: var(--ink-deep);
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    /* Subtle Botanical Linen Texture */
    .linen-pattern {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      pointer-events: none;
      opacity: 0.035;
      background-image: radial-gradient(var(--ink-deep) 1px, transparent 1px);
      background-size: 20px 20px;
      z-index: 1;
    }}

    /* Top Navigation Header */
    header {{
      position: relative;
      z-index: 20;
      background: rgba(247, 244, 235, 0.95);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-warm);
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 2px 12px rgba(44, 30, 20, 0.04);
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .brand-icon {{
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--bg-subtle);
      border: 1px solid var(--border-warm);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
    }}
    .brand-text h1 {{
      font-family: var(--font-serif);
      font-size: 18px;
      font-weight: 700;
      color: var(--ink-heading);
      letter-spacing: -0.01em;
    }}
    .brand-text p {{
      font-size: 11px;
      color: var(--ink-muted);
    }}

    /* Controls */
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}

    /* View Switcher Tabs */
    .view-pills {{
      display: flex;
      background: var(--bg-subtle);
      padding: 3px;
      border-radius: 20px;
      border: 1px solid var(--border-warm);
    }}
    .pill-btn {{
      padding: 6px 14px;
      border-radius: 16px;
      border: none;
      background: transparent;
      font-size: 12px;
      font-weight: 600;
      color: var(--ink-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .pill-btn.active {{
      background: var(--bg-surface);
      color: var(--ink-deep);
      box-shadow: 0 2px 6px rgba(44, 30, 20, 0.08);
    }}

    /* Search Box */
    .search-wrapper {{
      position: relative;
    }}
    .search-bar {{
      background: var(--bg-surface);
      border: 1px solid var(--border-warm);
      color: var(--ink-deep);
      padding: 7px 14px 7px 32px;
      border-radius: 20px;
      font-size: 13px;
      width: 250px;
      outline: none;
      transition: all 0.2s;
    }}
    .search-bar:focus {{
      border-color: var(--border-focus);
      width: 320px;
      box-shadow: 0 0 0 3px rgba(44, 83, 58, 0.12);
    }}
    .search-icon {{
      position: absolute;
      left: 11px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 12px;
      color: var(--ink-light);
      pointer-events: none;
    }}
    .search-results {{
      position: absolute;
      top: 110%;
      left: 0;
      width: 320px;
      max-height: 380px;
      overflow-y: auto;
      background: var(--bg-surface);
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(44, 30, 20, 0.12);
      display: none;
      z-index: 100;
    }}
    .search-item {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--bg-subtle);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 2px;
      transition: background 0.15s;
    }}
    .search-item:hover {{
      background: var(--bg-linen);
    }}
    .search-item-title {{
      font-size: 13px;
      font-weight: 600;
      color: var(--ink-deep);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .search-item-meta {{
      font-size: 11px;
      color: var(--ink-muted);
    }}

    /* Filter Chips */
    .filter-pills {{
      display: flex;
      gap: 6px;
    }}
    .filter-chip {{
      padding: 5px 10px;
      border-radius: 14px;
      border: 1px solid var(--border-warm);
      background: var(--bg-surface);
      font-size: 11px;
      font-weight: 600;
      color: var(--ink-muted);
      cursor: pointer;
      transition: all 0.15s;
    }}
    .filter-chip.active {{
      background: var(--ink-deep);
      color: #fff;
      border-color: var(--ink-deep);
    }}

    /* Main Container */
    #app-container {{
      position: relative;
      flex: 1;
      width: 100%;
      height: 100%;
      overflow: hidden;
    }}

    /* VIEW 1: CANOPY MACRO OVERVIEW (DOSSEL MACRO) */
    #view-canopy {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      overflow-y: auto;
      padding: 30px 40px 60px 40px;
      display: none;
      z-index: 5;
    }}
    .canopy-header {{
      max-width: 960px;
      margin: 0 auto 30px auto;
      text-align: center;
    }}
    .canopy-header h2 {{
      font-family: var(--font-serif);
      font-size: 28px;
      font-weight: 700;
      color: var(--ink-heading);
      margin-bottom: 8px;
    }}
    .canopy-header p {{
      font-size: 14px;
      color: var(--ink-muted);
      line-height: 1.5;
    }}
    .canopy-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 20px;
      max-width: 1300px;
      margin: 0 auto;
    }}
    .trunk-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-warm);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      cursor: pointer;
      box-shadow: 0 4px 16px rgba(44, 30, 20, 0.03);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s, border-color 0.2s;
    }}
    .trunk-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 10px 28px rgba(44, 30, 20, 0.08);
      border-color: var(--leaf-green);
    }}
    .trunk-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }}
    .trunk-card-badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 10px;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      background: rgba(46, 125, 50, 0.1);
      color: var(--leaf-green);
    }}
    .trunk-card h3 {{
      font-family: var(--font-serif);
      font-size: 19px;
      font-weight: 700;
      color: var(--ink-heading);
      line-height: 1.25;
      margin-bottom: 6px;
    }}
    .trunk-card-meta {{
      font-size: 12px;
      color: var(--sap-gold);
      font-weight: 600;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .trunk-card-desc {{
      font-size: 12px;
      color: var(--ink-muted);
      line-height: 1.45;
      margin-bottom: 16px;
      flex: 1;
    }}
    .trunk-card-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 12px;
      border-top: 1px solid var(--bg-subtle);
      font-size: 12px;
      font-weight: 600;
      color: var(--ink-deep);
    }}
    .trunk-card-action {{
      color: var(--leaf-green);
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* VIEW 2: LIVING TREE CANVAS (ÁRVORE FILOGENÉTICA VIVA) */
    #view-tree {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      cursor: grab;
      user-select: none;
      display: flex;
    }}
    #view-tree.dragging {{
      cursor: grabbing;
    }}
    #viewport-canvas {{
      position: absolute;
      top: 0; left: 0;
      transform-origin: 0 0;
      will-change: transform;
    }}

    /* SVG Elements */
    svg.organic-tree {{
      display: block;
      overflow: visible;
    }}
    .vine-edge {{
      fill: none;
      stroke: #A89B8C;
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: stroke 0.3s, stroke-width 0.3s;
    }}
    .vine-edge.sap-flow {{
      stroke: var(--sap-gold);
      stroke-width: 3.5;
      stroke-dasharray: 6 3;
      animation: sapFlow 1.8s linear infinite;
      filter: drop-shadow(0 0 6px var(--sap-glow));
    }}
    @keyframes sapFlow {{
      from {{ stroke-dashoffset: 27; }}
      to {{ stroke-dashoffset: 0; }}
    }}

    /* HTML Node Overlays */
    .node-capsule {{
      position: absolute;
      background: var(--bg-surface);
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 8px 14px;
      box-shadow: 0 2px 8px rgba(44, 30, 20, 0.05);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: center;
      min-width: 160px;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s, border-color 0.2s;
    }}
    .node-capsule:hover {{
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 6px 18px rgba(44, 30, 20, 0.1);
      border-color: var(--leaf-green);
    }}
    .node-capsule.active {{
      border: 2px solid var(--sap-gold) !important;
      background: #FFFDF5 !important;
      box-shadow: 0 0 16px var(--sap-glow) !important;
    }}
    .node-capsule.sap-path {{
      border-color: var(--sap-gold);
      box-shadow: 0 0 10px rgba(217, 119, 6, 0.25);
    }}

    /* Node types */
    .node-capsule.type-proto {{
      background: #EFF6FF;
      border-color: var(--proto-border);
    }}
    .node-capsule.type-extinct {{
      background: #FEF2F2;
      border-color: var(--extinct-border);
    }}
    .node-capsule.type-living {{
      background: #F0FDF4;
      border-color: var(--leaf-border);
    }}
    .node-capsule.type-branch {{
      background: var(--bg-surface);
    }}

    .node-header {{
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 2px;
    }}
    .node-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .node-dot.living {{ background: var(--leaf-green); }}
    .node-dot.extinct {{ background: var(--extinct-clay); }}
    .node-dot.proto {{ background: var(--proto-azure); }}
    .node-dot.branch {{ background: var(--branch-bark); }}

    .node-title {{
      font-size: 13px;
      font-weight: 700;
      color: var(--ink-heading);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .node-endonym {{
      font-family: var(--font-serif);
      font-size: 11px;
      font-style: italic;
      color: var(--ink-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .node-meta {{
      font-size: 10px;
      color: var(--ink-light);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 2px;
    }}

    /* Expand / Collapse Button */
    .node-toggle-btn {{
      position: absolute;
      right: -10px;
      top: 50%;
      transform: translateY(-50%);
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--bg-surface);
      border: 1px solid var(--border-warm);
      color: var(--ink-deep);
      font-size: 11px;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
      transition: background 0.15s, border-color 0.15s;
    }}
    .node-toggle-btn:hover {{
      background: var(--bg-subtle);
      border-color: var(--ink-deep);
    }}

    /* Trunk Banner (At Top of Tree View) */
    .tree-banner {{
      position: absolute;
      top: 16px;
      left: 20px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 8px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 10;
      box-shadow: 0 2px 10px rgba(44, 30, 20, 0.05);
    }}
    .tree-banner-title {{
      font-family: var(--font-serif);
      font-size: 15px;
      font-weight: 700;
      color: var(--ink-heading);
    }}
    .tree-banner-era {{
      font-size: 11px;
      color: var(--sap-gold);
      font-weight: 600;
    }}
    .btn-all-trunks {{
      background: var(--bg-subtle);
      border: 1px solid var(--border-warm);
      border-radius: 8px;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 600;
      color: var(--ink-deep);
      cursor: pointer;
    }}
    .btn-all-trunks:hover {{
      background: var(--bg-linen);
    }}

    /* Floating Zoom HUD */
    .zoom-hud {{
      position: absolute;
      bottom: 24px;
      left: 24px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 6px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      z-index: 10;
      box-shadow: 0 4px 14px rgba(44, 30, 20, 0.06);
    }}
    .hud-btn {{
      width: 32px;
      height: 32px;
      border-radius: 8px;
      border: 1px solid var(--border-warm);
      background: var(--bg-surface);
      color: var(--ink-deep);
      font-size: 16px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }}
    .hud-btn:hover {{
      background: var(--bg-subtle);
    }}

    /* Herbarium Specimen Drawer (Side Panel) */
    #herbarium-drawer {{
      position: absolute;
      top: 0; right: -480px;
      width: 460px;
      height: 100%;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-warm);
      box-shadow: -8px 0 32px rgba(44, 30, 20, 0.12);
      transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 30;
      display: flex;
      flex-direction: column;
    }}
    #herbarium-drawer.open {{
      right: 0;
    }}
    .drawer-header {{
      padding: 20px 24px;
      border-bottom: 1px solid var(--border-warm);
      background: var(--bg-surface-elevated);
      position: relative;
    }}
    .drawer-close {{
      position: absolute;
      top: 18px; right: 18px;
      background: none;
      border: none;
      font-size: 24px;
      color: var(--ink-light);
      cursor: pointer;
      line-height: 1;
    }}
    .drawer-close:hover {{
      color: var(--ink-deep);
    }}
    .drawer-badge-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }}
    .drawer-badge {{
      display: inline-block;
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}
    .badge-living {{ background: rgba(46, 125, 50, 0.12); color: var(--leaf-green); border: 1px solid var(--leaf-border); }}
    .badge-extinct {{ background: rgba(185, 28, 28, 0.12); color: var(--extinct-clay); border: 1px solid var(--extinct-border); }}
    .badge-proto {{ background: rgba(29, 78, 216, 0.12); color: var(--proto-azure); border: 1px solid var(--proto-border); }}
    .badge-branch {{ background: rgba(74, 59, 50, 0.12); color: var(--branch-bark); border: 1px solid var(--branch-border); }}

    .drawer-title {{
      font-family: var(--font-serif);
      font-size: 24px;
      font-weight: 700;
      color: var(--ink-heading);
      line-height: 1.2;
    }}
    .drawer-endonym {{
      font-family: var(--font-serif);
      font-size: 16px;
      font-style: italic;
      color: var(--sap-gold);
      margin-top: 4px;
    }}

    /* Drawer Scrollable Body */
    .drawer-body {{
      padding: 24px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .specimen-card {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 16px;
    }}
    .specimen-card-label {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .specimen-card p {{
      font-size: 13px;
      color: var(--ink-deep);
      line-height: 1.5;
    }}
    .breadcrumbs {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 4px;
      font-size: 12px;
    }}
    .crumb {{
      color: var(--leaf-green);
      cursor: pointer;
      font-weight: 600;
    }}
    .crumb:hover {{
      text-decoration: underline;
    }}
    .crumb-sep {{
      color: var(--ink-light);
    }}

    /* Action Buttons in Drawer */
    .drawer-actions {{
      padding: 16px 24px;
      border-top: 1px solid var(--border-warm);
      background: var(--bg-surface-elevated);
      display: flex;
      gap: 10px;
    }}
    .btn-trace-sap {{
      flex: 1;
      background: var(--sap-gold);
      color: #fff;
      border: none;
      padding: 10px 16px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 2px 8px rgba(217, 119, 6, 0.25);
      transition: background 0.15s, transform 0.15s;
    }}
    .btn-trace-sap:hover {{
      background: #B45309;
      transform: translateY(-1px);
    }}

    /* Global Forest Legend */
    .forest-legend {{
      position: absolute;
      bottom: 24px;
      right: 24px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 10px 16px;
      font-size: 11px;
      font-weight: 600;
      display: flex;
      gap: 14px;
      z-index: 10;
      box-shadow: 0 4px 14px rgba(44, 30, 20, 0.05);
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .legend-dot {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
    }}
  </style>
</head>
<body>
  <div class="linen-pattern"></div>

  <!-- Header -->
  <header>
    <div class="brand">
      <div class="brand-icon">🌿</div>
      <div class="brand-text">
        <h1>Herbário Filogenético das Línguas do Mundo</h1>
        <p>Radiações Evolutivas &amp; Protolínguas — Classificação Theodor Cole (2026), Glottolog &amp; Campbell</p>
      </div>
    </div>

    <div class="header-actions">
      <!-- View mode switch -->
      <div class="view-pills">
        <button id="pillCanopy" class="pill-btn active">🏛️ Dossel dos Troncos</button>
        <button id="pillTree" class="pill-btn">🌿 Árvore Filogenética</button>
      </div>

      <!-- Search Box with instant results -->
      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-bar" placeholder="Buscar língua, protolíngua ou família...">
        <div id="searchResults" class="search-results"></div>
      </div>

      <!-- Filter chips -->
      <div class="filter-pills">
        <button class="filter-chip active" data-filter="all">Todas</button>
        <button class="filter-chip" data-filter="living">🟢 Vivas</button>
        <button class="filter-chip" data-filter="extinct">🔴 Extintas (†)</button>
        <button class="filter-chip" data-filter="proto">🔵 Protolínguas</button>
      </div>
    </div>
  </header>

  <!-- Main View Area -->
  <main id="app-container">
    <!-- VIEW 1: CANOPY MACRO OVERVIEW -->
    <section id="view-canopy">
      <div class="canopy-header">
        <h2>Dossel Macro da Linhagem Humana</h2>
        <p>Selecione um grande tronco filogenético para explorar suas ramificações em árvore viva com traçado orgânico de seiva ancestral.</p>
      </div>
      <div id="canopyGrid" class="canopy-grid"></div>
    </section>

    <!-- VIEW 2: LIVING TREE CANVAS -->
    <section id="view-tree">
      <!-- Trunk banner info -->
      <div class="tree-banner">
        <div>
          <div id="treeBannerTitle" class="tree-banner-title">Proto-Indo-Europeu</div>
          <div id="treeBannerEra" class="tree-banner-era">~4.500–3.000 a.C. — Estepes Pôntico-Cáspias</div>
        </div>
        <button id="btnReturnCanopy" class="btn-all-trunks">🏛️ Ver Todos os Troncos</button>
      </div>

      <!-- Canvas viewport -->
      <div id="viewport-canvas">
        <svg id="treeSvg" class="organic-tree" width="12000" height="8000">
          <g id="vinesGroup"></g>
        </svg>
        <div id="htmlNodesGroup"></div>
      </div>

      <!-- Floating Zoom HUD -->
      <div class="zoom-hud">
        <button id="btnZoomIn" class="hud-btn" title="Aumentar Zoom">＋</button>
        <button id="btnZoomOut" class="hud-btn" title="Diminuir Zoom">－</button>
        <button id="btnResetView" class="hud-btn" title="Enquadrar Tronco">⤢</button>
      </div>

      <!-- Legend -->
      <div class="forest-legend">
        <div class="legend-item"><span class="legend-dot" style="background:var(--leaf-green);"></span> Língua Viva</div>
        <div class="legend-item"><span class="legend-dot" style="background:var(--extinct-clay);"></span> Extinta (†)</div>
        <div class="legend-item"><span class="legend-dot" style="background:var(--proto-azure);"></span> Protolíngua</div>
        <div class="legend-item"><span class="legend-dot" style="background:var(--branch-bark);"></span> Sub-ramo</div>
        <div class="legend-item"><span class="legend-dot" style="background:var(--sap-gold);"></span> Seiva Ativa</div>
      </div>
    </section>

    <!-- Herbarium Specimen Drawer -->
    <aside id="herbarium-drawer">
      <div class="drawer-header">
        <button id="drawerCloseBtn" class="drawer-close">&times;</button>
        <div class="drawer-badge-row">
          <span id="drawerBadge" class="drawer-badge badge-living">Língua Viva</span>
          <span id="drawerTrunkBadge" class="drawer-badge badge-branch">Família</span>
        </div>
        <h2 id="drawerTitle" class="drawer-title">Nome da Língua</h2>
        <div id="drawerEndonym" class="drawer-endonym">Endônimo nativo</div>
      </div>

      <div class="drawer-body">
        <div class="specimen-card">
          <div class="specimen-card-label">🌱 Linhagem Filogenética Ancestral</div>
          <div id="drawerLineage" class="breadcrumbs"></div>
        </div>

        <div class="specimen-card" id="cardChronology">
          <div class="specimen-card-label">⏳ Cronologia &amp; Berço (Urheimat)</div>
          <p id="drawerUrheimat"></p>
        </div>

        <div class="specimen-card">
          <div class="specimen-card-label">📜 Síntese Histórico-Linguística</div>
          <p id="drawerSynthesis"></p>
        </div>

        <div class="specimen-card">
          <div class="specimen-card-label">🔬 Tipologia &amp; Estrutura Gramatical</div>
          <p id="drawerTypology"></p>
        </div>

        <div class="specimen-card" id="cardSpeakers">
          <div class="specimen-card-label">👥 Falantes &amp; Distribuição Geográfica</div>
          <p id="drawerSpeakers"></p>
        </div>
      </div>

      <div class="drawer-actions">
        <button id="btnTraceSapAction" class="btn-trace-sap">✨ Iluminar Seiva Ancestral</button>
      </div>
    </aside>
  </main>

  <script>
    const NODES = {nodes_json};
    const TRUNKS = {trunks_json};
    const ROOT_ID = 'node_poster_4';

    // State
    let currentView = 'canopy'; // 'canopy' | 'tree'
    let currentTrunkId = 'node_ie_4';
    let selectedNodeId = null;
    let activeFilter = 'all'; // 'all' | 'living' | 'extinct' | 'proto'

    // Pan & Zoom State
    let scale = 0.9;
    let panX = 100;
    let panY = 120;
    let isDragging = false;
    let startX, startY;

    // Collapsed branches state
    const collapsedNodes = new Set();

    // DOM Elements
    const viewCanopy = document.getElementById('view-canopy');
    const viewTree = document.getElementById('view-tree');
    const pillCanopy = document.getElementById('pillCanopy');
    const pillTree = document.getElementById('pillTree');
    const canopyGrid = document.getElementById('canopyGrid');
    
    const viewportCanvas = document.getElementById('viewport-canvas');
    const treeSvg = document.getElementById('treeSvg');
    const vinesGroup = document.getElementById('vinesGroup');
    const htmlNodesGroup = document.getElementById('htmlNodesGroup');
    
    const herbariumDrawer = document.getElementById('herbarium-drawer');
    const drawerCloseBtn = document.getElementById('drawerCloseBtn');
    
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');

    // --- VIEW SWITCHING ---
    function switchView(view) {{
      currentView = view;
      if (view === 'canopy') {{
        viewCanopy.style.display = 'block';
        viewTree.style.display = 'none';
        pillCanopy.classList.add('active');
        pillTree.classList.remove('active');
      }} else {{
        viewCanopy.style.display = 'none';
        viewTree.style.display = 'flex';
        pillCanopy.classList.remove('active');
        pillTree.classList.add('active');
        renderTreeForTrunk(currentTrunkId);
      }}
    }}

    pillCanopy.addEventListener('click', () => switchView('canopy'));
    pillTree.addEventListener('click', () => switchView('tree'));
    document.getElementById('btnReturnCanopy').addEventListener('click', () => switchView('canopy'));

    // --- RENDER CANOPY CARDS ---
    function renderCanopy() {{
      let html = '';
      for (const [tid, meta] of Object.entries(TRUNKS)) {{
        const rootNode = NODES[tid];
        if (!rootNode) continue;
        
        // Count descendants
        let count = 0;
        function countKids(nid) {{
          count++;
          for (const c of (NODES[nid]?.children || [])) countKids(c);
        }}
        countKids(tid);

        html += `
          <div class="trunk-card" onclick="selectTrunkAndOpenTree('${{tid}}')">
            <div>
              <div class="trunk-card-header">
                <span class="trunk-card-badge">Macro-Família</span>
                <span style="font-size:12px; color:var(--ink-light);">${{count}} nós</span>
              </div>
              <h3>${{meta.nome}}</h3>
              <div class="trunk-card-meta">⏳ ${{meta.era}}</div>
              <p class="trunk-card-desc">${{meta.desc}}</p>
            </div>
            <div class="trunk-card-footer">
              <span>📍 ${{meta.urheimat}}</span>
              <span class="trunk-card-action">Explorar Ramo ➔</span>
            </div>
          </div>
        `;
      }}
      canopyGrid.innerHTML = html;
    }}

    window.selectTrunkAndOpenTree = function(tid) {{
      currentTrunkId = tid;
      switchView('tree');
    }};

    // --- DYNAMIC TREE LAYOUT ENGINE ---
    // Computes clean, non-overlapping horizontal tidy-tree layout
    function computeTreeLayout(rootId) {{
      const levelGap = 240; // horizontal distance between levels
      const nodeGap = 72;   // vertical distance between sibling leaves

      let leafY = 60;
      const positions = new Map();

      function layoutNode(nid, depth) {{
        const node = NODES[nid];
        if (!node) return;

        const isCollapsed = collapsedNodes.has(nid);
        const children = isCollapsed ? [] : (node.children || []);

        if (children.length === 0) {{
          positions.set(nid, {{ x: depth * levelGap + 80, y: leafY }});
          leafY += nodeGap;
        }} else {{
          let sumY = 0;
          for (const cid of children) {{
            layoutNode(cid, depth + 1);
            sumY += positions.get(cid).y;
          }}
          const avgY = sumY / children.length;
          positions.set(nid, {{ x: depth * levelGap + 80, y: avgY }});
        }}
      }}

      layoutNode(rootId, 0);
      return positions;
    }}

    // --- RENDER TREE FOR SELECTED TRUNK ---
    function renderTreeForTrunk(trunkId) {{
      const rootNode = NODES[trunkId];
      if (!rootNode) return;

      const meta = TRUNKS[trunkId] || {{ nome: rootNode.title, era: "Radiação Humana" }};
      document.getElementById('treeBannerTitle').textContent = meta.nome;
      document.getElementById('treeBannerEra').textContent = `${{meta.era}} — ${{meta.urheimat || 'Berço Ancestral'}}`;

      const positions = computeTreeLayout(trunkId);

      // Calculate bounding box for SVG
      let maxX = 1200;
      let maxY = 800;
      for (const [_, pos] of positions) {{
        if (pos.x > maxX) maxX = pos.x + 300;
        if (pos.y > maxY) maxY = pos.y + 200;
      }}
      treeSvg.setAttribute('width', maxX);
      treeSvg.setAttribute('height', maxY);

      // Render Organic Bézier Vines
      let vinesHtml = '';
      function renderEdges(nid) {{
        if (collapsedNodes.has(nid)) return;
        const p1 = positions.get(nid);
        const node = NODES[nid];
        if (!node || !p1) return;

        for (const cid of node.children) {{
          const p2 = positions.get(cid);
          if (!p2) continue;

          // Organic cubic bezier curve from right of parent to left of child
          const x0 = p1.x + 180;
          const y0 = p1.y + 24;
          const x1 = p2.x;
          const y1 = p2.y + 24;
          const dx = (x1 - x0) * 0.55;

          const d = `M ${{x0}} ${{y0}} C ${{x0 + dx}} ${{y0}}, ${{x1 - dx}} ${{y1}}, ${{x1}} ${{y1}}`;
          vinesHtml += `<path id="vine_${{nid}}_${{cid}}" data-parent="${{nid}}" data-child="${{cid}}" class="vine-edge" d="${{d}}" />`;

          renderEdges(cid);
        }}
      }}
      renderEdges(trunkId);
      vinesGroup.innerHTML = vinesHtml;

      // Render HTML Node Capsules
      let nodesHtml = '';
      for (const [nid, pos] of positions) {{
        const node = NODES[nid];
        if (!node) continue;

        let typeClass = 'type-branch';
        let dotClass = 'branch';
        if (node.is_proto) {{ typeClass = 'type-proto'; dotClass = 'proto'; }}
        else if (node.is_extinct) {{ typeClass = 'type-extinct'; dotClass = 'extinct'; }}
        else if (node.is_living) {{ typeClass = 'type-living'; dotClass = 'living'; }}

        const hasKids = node.children && node.children.length > 0;
        const isCollapsed = collapsedNodes.has(nid);

        nodesHtml += `
          <div class="node-capsule ${{typeClass}}" id="capsule_${{nid}}" data-id="${{nid}}" style="left:${{pos.x}}px; top:${{pos.y}}px;" onclick="onNodeClick('${{nid}}')">
            <div class="node-header">
              <span class="node-dot ${{dotClass}}"></span>
              <span class="node-title">${{escapeHtml(node.title)}}</span>
            </div>
            ${{node.endonym ? `<div class="node-endonym">${{escapeHtml(node.endonym)}}</div>` : ''}}
            ${{node.subtitle ? `<div class="node-meta">${{escapeHtml(node.subtitle.substring(0, 35))}}</div>` : ''}}
            ${{hasKids ? `
              <div class="node-toggle-btn" title="${{isCollapsed ? 'Expandir Ramo' : 'Recolher Ramo'}}" onclick="toggleBranch(event, '${{nid}}')">
                ${{isCollapsed ? '＋' : '−'}}
              </div>` : ''}}
          </div>
        `;
      }}
      htmlNodesGroup.innerHTML = nodesHtml;

      // Reset view position to encompass root
      panX = 80;
      panY = 100;
      scale = 0.85;
      updateTransform();

      // If there's an active selected node, re-illuminate
      if (selectedNodeId && positions.has(selectedNodeId)) {{
        highlightAncestralSap(selectedNodeId);
      }}
    }}

    window.toggleBranch = function(e, nid) {{
      e.stopPropagation();
      if (collapsedNodes.has(nid)) {{
        collapsedNodes.delete(nid);
      }} else {{
        collapsedNodes.add(nid);
      }}
      renderTreeForTrunk(currentTrunkId);
    }};

    window.onNodeClick = function(nid) {{
      selectNode(nid);
    }};

    // --- NODE SELECTION & ANCESTRAL SAP ILLUMINATION ---
    function selectNode(nid) {{
      selectedNodeId = nid;
      const node = NODES[nid];
      if (!node) return;

      // Switch trunk if node is in a different trunk
      if (node.trunk_id && node.trunk_id !== currentTrunkId && node.trunk_id !== 'node_poster_4') {{
        currentTrunkId = node.trunk_id;
        renderTreeForTrunk(currentTrunkId);
      }}

      // Uncollapse all ancestors so node is visible
      let needsRerender = false;
      for (const ancId of node.ancestors) {{
        if (collapsedNodes.has(ancId)) {{
          collapsedNodes.delete(ancId);
          needsRerender = true;
        }}
      }}
      if (needsRerender) {{
        renderTreeForTrunk(currentTrunkId);
      }}

      // Highlight capsule
      document.querySelectorAll('.node-capsule.active').forEach(el => el.classList.remove('active'));
      const cap = document.getElementById(`capsule_${{nid}}`);
      if (cap) cap.classList.add('active');

      highlightAncestralSap(nid);
      populateHerbariumDrawer(node);
      herbariumDrawer.classList.add('open');
    }}

    function highlightAncestralSap(targetId) {{
      // Clear previous sap paths
      document.querySelectorAll('.vine-edge.sap-flow').forEach(el => el.classList.remove('sap-flow'));
      document.querySelectorAll('.node-capsule.sap-path').forEach(el => el.classList.remove('sap-path'));

      const node = NODES[targetId];
      if (!node) return;

      const path = node.ancestors;
      for (let i = 0; i < path.length; i++) {{
        const curr = path[i];
        const cap = document.getElementById(`capsule_${{curr}}`);
        if (cap) cap.classList.add('sap-path');

        if (i < path.length - 1) {{
          const next = path[i + 1];
          const edge = document.getElementById(`vine_${{curr}}_${{next}}`);
          if (edge) edge.classList.add('sap-flow');
        }}
      }}
    }}

    // --- HERBARIUM SPECIMEN DRAWER POPULATION ---
    function populateHerbariumDrawer(node) {{
      document.getElementById('drawerTitle').textContent = node.title;
      document.getElementById('drawerEndonym').textContent = node.endonym || 'Língua Filogenética Documentada';

      const badge = document.getElementById('drawerBadge');
      if (node.is_proto) {{
        badge.className = 'drawer-badge badge-proto';
        badge.textContent = 'Protolíngua Reconstruída';
      }} else if (node.is_extinct) {{
        badge.className = 'drawer-badge badge-extinct';
        badge.textContent = 'Língua Extinta (†)';
      }} else if (node.is_living) {{
        badge.className = 'drawer-badge badge-living';
        badge.textContent = 'Língua Natural Viva';
      }} else {{
        badge.className = 'drawer-badge badge-branch';
        badge.textContent = 'Ramo Filogenético';
      }}

      document.getElementById('drawerTrunkBadge').textContent = node.trunk_name || 'Tronco';

      // Lineage Breadcrumbs
      const lineageEl = document.getElementById('drawerLineage');
      let lineageHtml = '';
      node.ancestors.forEach((ancId, idx) => {{
        const ancNode = NODES[ancId];
        if (!ancNode) return;
        lineageHtml += `<span class="crumb" onclick="selectNode('${{ancId}}')">${{escapeHtml(ancNode.title)}}</span>`;
        if (idx < node.ancestors.length - 1) {{
          lineageHtml += `<span class="crumb-sep">➔</span>`;
        }}
      }});
      lineageEl.innerHTML = lineageHtml;

      // Chronology & Urheimat
      const trunkMeta = TRUNKS[node.trunk_id] || {{}};
      const urheimatText = trunkMeta.urheimat || 'Consulte histórico da família';
      const eraText = trunkMeta.era || 'Período Histórico';
      document.getElementById('drawerUrheimat').innerHTML = `<b>Época Estimada:</b> ${{eraText}}<br><b>Berço de Origem (*Urheimat*):</b> ${{urheimatText}}`;

      // Synthesis & Typology
      document.getElementById('drawerSynthesis').textContent = 
        `${{node.title}} constitui um nó fulcral na filogenia das línguas do ramo ${{node.trunk_name}}. Sua classificação é referenciada nos corpora históricos de Theodor Cole (2026), Glottolog e estudos histórico-comparativos clássicos.`;

      document.getElementById('drawerTypology').textContent = 
        node.is_proto 
          ? "Protolíngua com inventário fonêmico reconstruído pelo método histórico-comparativo rigoroso, exibindo leis fonéticas regulares e correspondências morfológicas estritas com suas descendentes atestadas."
          : (node.is_extinct 
              ? "Língua conservada exclusivamente em registros epigráficos, tábuas de argila, manuscritos clássicos ou tradição litúrgica."
              : "Língua ativa falada por comunidades nativas contemporâneas, com morfossintaxe viva e dialetologia documentada.");

      // Speakers
      document.getElementById('drawerSpeakers').textContent = 
        node.subtitle || "Consulte dados etnográficos e censos linguísticos da região.";
    }}

    drawerCloseBtn.addEventListener('click', () => {{
      herbariumDrawer.classList.remove('open');
    }});

    document.getElementById('btnTraceSapAction').addEventListener('click', () => {{
      if (selectedNodeId) {{
        focusOnNodeInTree(selectedNodeId);
        highlightAncestralSap(selectedNodeId);
      }}
    }});

    // Center and pan to node
    function focusOnNodeInTree(nid) {{
      const cap = document.getElementById(`capsule_${{nid}}`);
      if (!cap) return;
      const x = parseFloat(cap.style.left);
      const y = parseFloat(cap.style.top);

      scale = 1.0;
      panX = (viewTree.clientWidth / 2) - x * scale - 100;
      panY = (viewTree.clientHeight / 2) - y * scale;
      updateTransform();
    }}

    // --- SEARCH AUTOCOMPLETE ---
    searchInput.addEventListener('input', () => {{
      const query = searchInput.value.trim().toLowerCase();
      if (!query || query.length < 2) {{
        searchResults.style.display = 'none';
        return;
      }}

      let matches = [];
      for (const [nid, node] of Object.entries(NODES)) {{
        const txt = (node.title + ' ' + (node.endonym || '') + ' ' + (node.subtitle || '') + ' ' + node.trunk_name).toLowerCase();
        if (txt.includes(query)) {{
          matches.push(node);
          if (matches.length >= 25) break;
        }}
      }}

      if (matches.length === 0) {{
        searchResults.innerHTML = '<div style="padding:14px; font-size:12px; color:var(--ink-muted);">Nenhum nó encontrado com este termo.</div>';
      }} else {{
        let html = '';
        matches.forEach(m => {{
          const dot = m.is_proto ? '🔵' : (m.is_extinct ? '🔴' : (m.is_living ? '🟢' : '🌿'));
          html += `
            <div class="search-item" onclick="onSearchSelect('${{m.id}}')">
              <div class="search-item-title">
                <span>${{dot}}</span>
                <span>${{escapeHtml(m.title)}}</span>
                ${{m.endonym ? `<span style="font-size:11px; font-style:italic; color:var(--sap-gold); font-family:var(--font-serif);">${{escapeHtml(m.endonym)}}</span>` : ''}}
              </div>
              <div class="search-item-meta">${{escapeHtml(m.trunk_name)}} — ${{escapeHtml(m.subtitle || '')}}</div>
            </div>
          `;
        }});
        searchResults.innerHTML = html;
      }}
      searchResults.style.display = 'block';
    }});

    window.onSearchSelect = function(nid) {{
      searchResults.style.display = 'none';
      searchInput.value = '';
      switchView('tree');
      selectNode(nid);
      setTimeout(() => focusOnNodeInTree(nid), 100);
    }};

    document.addEventListener('click', (e) => {{
      if (!e.target.closest('.search-wrapper')) {{
        searchResults.style.display = 'none';
      }}
    }});

    // --- FILTERS ---
    document.querySelectorAll('.filter-chip').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.getAttribute('data-filter');
        applyFilterToView();
      }});
    }});

    function applyFilterToView() {{
      document.querySelectorAll('.node-capsule').forEach(cap => {{
        const nid = cap.getAttribute('data-id');
        const node = NODES[nid];
        if (!node) return;

        let visible = true;
        if (activeFilter === 'living' && !node.is_living) visible = false;
        if (activeFilter === 'extinct' && !node.is_extinct) visible = false;
        if (activeFilter === 'proto' && !node.is_proto) visible = false;

        cap.style.opacity = visible ? '1' : '0.2';
      }});
    }}

    // --- PAN AND ZOOM ENGINE ---
    function updateTransform() {{
      viewportCanvas.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{scale}})`;
    }}

    viewTree.addEventListener('mousedown', (e) => {{
      if (e.target.closest('#herbarium-drawer') || e.target.closest('.zoom-hud') || e.target.closest('.tree-banner') || e.target.closest('.node-capsule')) return;
      isDragging = true;
      viewTree.classList.add('dragging');
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
      viewTree.classList.remove('dragging');
    }});

    viewTree.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const zoomFactor = 1.12;
      const mouseX = e.clientX;
      const mouseY = e.clientY;

      let newScale = e.deltaY < 0 ? scale * zoomFactor : scale / zoomFactor;
      newScale = Math.min(Math.max(0.2, newScale), 2.2);

      panX = mouseX - (mouseX - panX) * (newScale / scale);
      panY = mouseY - (mouseY - panY) * (newScale / scale);
      scale = newScale;
      updateTransform();
    }}, {{ passive: false }});

    document.getElementById('btnZoomIn').addEventListener('click', () => {{
      scale = Math.min(scale * 1.25, 2.2);
      updateTransform();
    }});

    document.getElementById('btnZoomOut').addEventListener('click', () => {{
      scale = Math.max(scale / 1.25, 0.2);
      updateTransform();
    }});

    document.getElementById('btnResetView').addEventListener('click', () => {{
      panX = 80;
      panY = 100;
      scale = 0.85;
      updateTransform();
    }});

    function escapeHtml(str) {{
      return (str || '').replace(/[<>&]/g, c => ({{'<':'&lt;', '>':'&gt;', '&':'&amp;'}})[c]);
    }}

    // --- INITIALIZATION ---
    renderCanopy();
    switchView('canopy');
  </script>
</body>
</html>
'''
    with open('arvore_interativa.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("arvore_interativa.html successfully generated!")

if __name__ == '__main__':
    build()
