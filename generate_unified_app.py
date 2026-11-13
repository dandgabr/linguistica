#!/usr/bin/env python3
"""
Builds the unified arvore_interativa.html integrating:
1. 3D Botanical Parchment Globe with interactive Urheimat pins and migration arcs
2. Canopy Macro Overview (19 Trunks)
3. Living Phylogenetic Tree with organic Bézier vines and golden sap illumination
4. Herbarium Specimen Drawer
"""

import json
import process_tree
import build_geo_data as geo

with open('landmasses.json', 'r') as f:
    LANDMASSES = json.load(f)

TRUNK_GEO = geo.TRUNK_GEO
nodes, trunks_meta = process_tree.generate()

nodes_json = json.dumps(nodes, ensure_ascii=False)
trunks_json = json.dumps(trunks_meta, ensure_ascii=False)
geo_json = json.dumps(TRUNK_GEO, ensure_ascii=False)
land_json = json.dumps(LANDMASSES, ensure_ascii=False)

with open('template_head.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Herbário Filogenético das Línguas do Mundo — Globo & Árvore Viva</title>
  <style>
    :root {
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
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg-linen);
      color: var(--ink-deep);
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    .linen-pattern {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      pointer-events: none;
      opacity: 0.035;
      background-image: radial-gradient(var(--ink-deep) 1px, transparent 1px);
      background-size: 20px 20px;
      z-index: 1;
    }

    header {
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
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .brand-icon {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--bg-subtle);
      border: 1px solid var(--border-warm);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
    }
    .brand-text h1 {
      font-family: var(--font-serif);
      font-size: 18px;
      font-weight: 700;
      color: var(--ink-heading);
      letter-spacing: -0.01em;
    }
    .brand-text p {
      font-size: 11px;
      color: var(--ink-muted);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .view-pills {
      display: flex;
      background: var(--bg-subtle);
      padding: 3px;
      border-radius: 20px;
      border: 1px solid var(--border-warm);
    }
    .pill-btn {
      padding: 6px 14px;
      border-radius: 16px;
      border: none;
      background: transparent;
      font-size: 12px;
      font-weight: 600;
      color: var(--ink-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .pill-btn.active {
      background: var(--bg-surface);
      color: var(--ink-deep);
      box-shadow: 0 2px 6px rgba(44, 30, 20, 0.08);
    }

    .search-wrapper {
      position: relative;
    }
    .search-bar {
      background: var(--bg-surface);
      border: 1px solid var(--border-warm);
      color: var(--ink-deep);
      padding: 7px 14px 7px 32px;
      border-radius: 20px;
      font-size: 13px;
      width: 250px;
      outline: none;
      transition: all 0.2s;
    }
    .search-bar:focus {
      border-color: var(--border-focus);
      width: 320px;
      box-shadow: 0 0 0 3px rgba(44, 83, 58, 0.12);
    }
    .search-icon {
      position: absolute;
      left: 11px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 12px;
      color: var(--ink-light);
      pointer-events: none;
    }
    .search-results {
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
    }
    .search-item {
      padding: 10px 14px;
      border-bottom: 1px solid var(--bg-subtle);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 2px;
      transition: background 0.15s;
    }
    .search-item:hover {
      background: var(--bg-linen);
    }
    .search-item-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--ink-deep);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .search-item-meta {
      font-size: 11px;
      color: var(--ink-muted);
    }

    .filter-pills {
      display: flex;
      gap: 6px;
    }
    .filter-chip {
      padding: 5px 10px;
      border-radius: 14px;
      border: 1px solid var(--border-warm);
      background: var(--bg-surface);
      font-size: 11px;
      font-weight: 600;
      color: var(--ink-muted);
      cursor: pointer;
      transition: all 0.15s;
    }
    .filter-chip.active {
      background: var(--ink-deep);
      color: #fff;
      border-color: var(--ink-deep);
    }

    #app-container {
      position: relative;
      flex: 1;
      width: 100%;
      height: 100%;
      overflow: hidden;
    }

    /* VIEW 1: 3D GLOBE & GEOGRAPHY (SPLIT SCREEN) */
    #view-globe {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      display: grid;
      grid-template-columns: minmax(420px, 55%) 1fr;
      overflow: hidden;
      z-index: 5;
    }
    #globeCanvasWrapper {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(ellipse at center, #FFFDF8 0%, #F5EFE0 70%, #EFE8D6 100%);
      border-right: 1px solid var(--border-warm);
      overflow: hidden;
    }
    #globeCanvas {
      width: min(92%, 620px);
      aspect-ratio: 1;
      touch-action: none;
      cursor: grab;
    }
    #globeCanvas.dragging {
      cursor: grabbing;
    }
    .globe-caption {
      position: absolute;
      left: 20px;
      bottom: 16px;
      font-size: 12px;
      font-style: italic;
      color: var(--ink-muted);
    }
    .globe-controls {
      position: absolute;
      top: 20px;
      left: 20px;
      display: flex;
      gap: 6px;
    }
    .globe-btn {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      border: 1px solid var(--border-warm);
      background: var(--bg-surface);
      color: var(--ink-deep);
      font-size: 15px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    .globe-btn:hover {
      background: var(--bg-subtle);
    }

    /* Right Side of Globe View: Geo Dossier */
    #globeTrunkInfo {
      padding: 30px 36px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
      background: var(--bg-linen);
    }
    .geo-trunk-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-warm);
      border-radius: 18px;
      padding: 24px;
      box-shadow: 0 4px 16px rgba(44, 30, 20, 0.04);
    }
    .geo-trunk-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      background: rgba(46, 125, 50, 0.12);
      color: var(--leaf-green);
      margin-bottom: 10px;
    }
    .geo-trunk-title {
      font-family: var(--font-serif);
      font-size: 26px;
      font-weight: 700;
      color: var(--ink-heading);
      margin-bottom: 6px;
    }
    .geo-trunk-era {
      font-size: 13px;
      color: var(--sap-gold);
      font-weight: 600;
      margin-bottom: 14px;
    }
    .geo-trunk-urheimat {
      font-size: 14px;
      line-height: 1.5;
      color: var(--ink-deep);
      background: var(--bg-subtle);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 18px;
    }
    .geo-dispersion-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 8px;
    }
    .dispersion-pill {
      background: #FFFDF9;
      border: 1px solid var(--border-warm);
      border-radius: 14px;
      padding: 5px 12px;
      font-size: 12px;
      font-weight: 600;
      color: var(--leaf-green);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .dispersion-pill:hover {
      border-color: var(--leaf-green);
      background: #F0FDF4;
      transform: translateY(-1px);
    }

    .btn-dive-tree {
      background: var(--leaf-green);
      color: #fff;
      border: none;
      padding: 12px 20px;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(46, 125, 50, 0.25);
      transition: background 0.15s, transform 0.15s;
      margin-top: 10px;
    }
    .btn-dive-tree:hover {
      background: #1B5E20;
      transform: translateY(-2px);
    }

    /* VIEW 2: CANOPY MACRO OVERVIEW (DOSSEL MACRO) */
    #view-canopy {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      overflow-y: auto;
      padding: 30px 40px 60px 40px;
      display: none;
      z-index: 5;
    }
    .canopy-header {
      max-width: 960px;
      margin: 0 auto 30px auto;
      text-align: center;
    }
    .canopy-header h2 {
      font-family: var(--font-serif);
      font-size: 28px;
      font-weight: 700;
      color: var(--ink-heading);
      margin-bottom: 8px;
    }
    .canopy-header p {
      font-size: 14px;
      color: var(--ink-muted);
      line-height: 1.5;
    }
    .canopy-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 20px;
      max-width: 1300px;
      margin: 0 auto;
    }
    .trunk-card {
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
    }
    .trunk-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 10px 28px rgba(44, 30, 20, 0.08);
      border-color: var(--leaf-green);
    }
    .trunk-card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }
    .trunk-card-badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 10px;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      background: rgba(46, 125, 50, 0.1);
      color: var(--leaf-green);
    }
    .trunk-card h3 {
      font-family: var(--font-serif);
      font-size: 19px;
      font-weight: 700;
      color: var(--ink-heading);
      line-height: 1.25;
      margin-bottom: 6px;
    }
    .trunk-card-meta {
      font-size: 12px;
      color: var(--sap-gold);
      font-weight: 600;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .trunk-card-desc {
      font-size: 12px;
      color: var(--ink-muted);
      line-height: 1.45;
      margin-bottom: 16px;
      flex: 1;
    }
    .trunk-card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 12px;
      border-top: 1px solid var(--bg-subtle);
      font-size: 12px;
      font-weight: 600;
      color: var(--ink-deep);
    }
    .trunk-card-action {
      color: var(--leaf-green);
      display: flex;
      align-items: center;
      gap: 4px;
    }

    /* VIEW 3: LIVING TREE CANVAS (ÁRVORE FILOGENÉTICA VIVA) */
    #view-tree {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      cursor: grab;
      user-select: none;
      display: none;
    }
    #view-tree.dragging {
      cursor: grabbing;
    }
    #viewport-canvas {
      position: absolute;
      top: 0; left: 0;
      transform-origin: 0 0;
      will-change: transform;
    }

    svg.organic-tree {
      display: block;
      overflow: visible;
    }
    .vine-edge {
      fill: none;
      stroke: #A89B8C;
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: stroke 0.3s, stroke-width 0.3s;
    }
    .vine-edge.sap-flow {
      stroke: var(--sap-gold);
      stroke-width: 3.5;
      stroke-dasharray: 6 3;
      animation: sapFlow 1.8s linear infinite;
      filter: drop-shadow(0 0 6px var(--sap-glow));
    }
    @keyframes sapFlow {
      from { stroke-dashoffset: 27; }
      to { stroke-dashoffset: 0; }
    }

    .node-capsule {
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
    }
    .node-capsule:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 6px 18px rgba(44, 30, 20, 0.1);
      border-color: var(--leaf-green);
    }
    .node-capsule.active {
      border: 2px solid var(--sap-gold) !important;
      background: #FFFDF5 !important;
      box-shadow: 0 0 16px var(--sap-glow) !important;
    }
    .node-capsule.sap-path {
      border-color: var(--sap-gold);
      box-shadow: 0 0 10px rgba(217, 119, 6, 0.25);
    }

    .node-capsule.type-proto {
      background: #EFF6FF;
      border-color: var(--proto-border);
    }
    .node-capsule.type-extinct {
      background: #FEF2F2;
      border-color: var(--extinct-border);
    }
    .node-capsule.type-living {
      background: #F0FDF4;
      border-color: var(--leaf-border);
    }
    .node-capsule.type-branch {
      background: var(--bg-surface);
    }

    .node-header {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 2px;
    }
    .node-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .node-dot.living { background: var(--leaf-green); }
    .node-dot.extinct { background: var(--extinct-clay); }
    .node-dot.proto { background: var(--proto-azure); }
    .node-dot.branch { background: var(--branch-bark); }

    .node-title {
      font-size: 13px;
      font-weight: 700;
      color: var(--ink-heading);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .node-endonym {
      font-family: var(--font-serif);
      font-size: 11px;
      font-style: italic;
      color: var(--ink-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .node-meta {
      font-size: 10px;
      color: var(--ink-light);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 2px;
    }

    .node-toggle-btn {
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
    }
    .node-toggle-btn:hover {
      background: var(--bg-subtle);
      border-color: var(--ink-deep);
    }

    .tree-banner {
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
    }
    .tree-banner-title {
      font-family: var(--font-serif);
      font-size: 15px;
      font-weight: 700;
      color: var(--ink-heading);
    }
    .tree-banner-era {
      font-size: 11px;
      color: var(--sap-gold);
      font-weight: 600;
    }
    .btn-all-trunks {
      background: var(--bg-subtle);
      border: 1px solid var(--border-warm);
      border-radius: 8px;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 600;
      color: var(--ink-deep);
      cursor: pointer;
    }
    .btn-all-trunks:hover {
      background: var(--bg-linen);
    }

    .zoom-hud {
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
    }
    .hud-btn {
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
    }
    .hud-btn:hover {
      background: var(--bg-subtle);
    }

    /* Herbarium Specimen Drawer */
    #herbarium-drawer {
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
    }
    #herbarium-drawer.open {
      right: 0;
    }
    .drawer-header {
      padding: 20px 24px;
      border-bottom: 1px solid var(--border-warm);
      background: var(--bg-surface-elevated);
      position: relative;
    }
    .drawer-close {
      position: absolute;
      top: 18px; right: 18px;
      background: none;
      border: none;
      font-size: 24px;
      color: var(--ink-light);
      cursor: pointer;
      line-height: 1;
    }
    .drawer-close:hover {
      color: var(--ink-deep);
    }
    .drawer-badge-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }
    .drawer-badge {
      display: inline-block;
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
    .badge-living { background: rgba(46, 125, 50, 0.12); color: var(--leaf-green); border: 1px solid var(--leaf-border); }
    .badge-extinct { background: rgba(185, 28, 28, 0.12); color: var(--extinct-clay); border: 1px solid var(--extinct-border); }
    .badge-proto { background: rgba(29, 78, 216, 0.12); color: var(--proto-azure); border: 1px solid var(--proto-border); }
    .badge-branch { background: rgba(74, 59, 50, 0.12); color: var(--branch-bark); border: 1px solid var(--branch-border); }

    .drawer-title {
      font-family: var(--font-serif);
      font-size: 24px;
      font-weight: 700;
      color: var(--ink-heading);
      line-height: 1.2;
    }
    .drawer-endonym {
      font-family: var(--font-serif);
      font-size: 16px;
      font-style: italic;
      color: var(--sap-gold);
      margin-top: 4px;
    }

    .drawer-body {
      padding: 24px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .specimen-card {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 16px;
    }
    .specimen-card-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .specimen-card p {
      font-size: 13px;
      color: var(--ink-deep);
      line-height: 1.5;
    }
    .breadcrumbs {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 4px;
      font-size: 12px;
    }
    .crumb {
      color: var(--leaf-green);
      cursor: pointer;
      font-weight: 600;
    }
    .crumb:hover {
      text-decoration: underline;
    }
    .crumb-sep {
      color: var(--ink-light);
    }

    .drawer-actions {
      padding: 16px 24px;
      border-top: 1px solid var(--border-warm);
      background: var(--bg-surface-elevated);
      display: flex;
      gap: 10px;
    }
    .btn-trace-sap {
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
    }
    .btn-trace-sap:hover {
      background: #B45309;
      transform: translateY(-1px);
    }

    .forest-legend {
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
    }
    .legend-item {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .legend-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
    }
  </style>
</head>
<body>
  <div class="linen-pattern"></div>

  <header>
    <div class="brand">
      <div class="brand-icon">🌿</div>
      <div class="brand-text">
        <h1>Herbário Filogenético das Línguas do Mundo</h1>
        <p>Globo Filogeográfico 3D &amp; Árvore Viva — Theodor Cole (2026), Glottolog &amp; Campbell</p>
      </div>
    </div>

    <div class="header-actions">
      <div class="view-pills">
        <button id="pillGlobe" class="pill-btn active">🌍 Globo 3D &amp; Geografia</button>
        <button id="pillCanopy" class="pill-btn">🏛️ Dossel dos Troncos</button>
        <button id="pillTree" class="pill-btn">🌿 Árvore Filogenética</button>
      </div>

      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-bar" placeholder="Buscar língua, família ou berço...">
        <div id="searchResults" class="search-results"></div>
      </div>

      <div class="filter-pills">
        <button class="filter-chip active" data-filter="all">Todas</button>
        <button class="filter-chip" data-filter="living">🟢 Vivas</button>
        <button class="filter-chip" data-filter="extinct">🔴 Extintas (†)</button>
        <button class="filter-chip" data-filter="proto">🔵 Protolínguas</button>
      </div>
    </div>
  </header>

  <main id="app-container">
    <!-- VIEW 1: 3D GLOBE & GEOGRAPHY -->
    <section id="view-globe">
      <div id="globeCanvasWrapper">
        <canvas id="globeCanvas" width="600" height="600"></canvas>
        <div class="globe-controls">
          <button id="globeZoomIn" class="globe-btn" title="Aproximar">＋</button>
          <button id="globeZoomOut" class="globe-btn" title="Afastar">－</button>
          <button id="globeReset" class="globe-btn" title="Recentrar">◎</button>
        </div>
        <div class="globe-caption">Arraste para girar em 3D · Clique nos brotos dourados para focar no berço</div>
      </div>

      <div id="globeTrunkInfo">
        <div class="geo-trunk-card">
          <span class="geo-trunk-badge">Macro-Família Filogenética</span>
          <h2 id="geoTrunkTitle" class="geo-trunk-title">Proto-Indo-Europeu</h2>
          <div id="geoTrunkEra" class="geo-trunk-era">⏳ ~4.500–3.000 a.C.</div>
          
          <div class="geo-trunk-urheimat">
            <b>📍 Berço Ancestral (*Urheimat*):</b><br>
            <span id="geoTrunkUrheimatText">Estepes Pôntico-Cáspias (Norte do Mar Negro e Mar Cáspio)</span>
          </div>

          <p id="geoTrunkDesc" style="font-size:13px; color:var(--ink-muted); line-height:1.5; margin-bottom:16px;">
            Radiação de mais de 440 línguas em direção à Europa, Ásia Menor, Irã e Índia.
          </p>

          <div style="font-size:12px; font-weight:700; text-transform:uppercase; color:var(--ink-muted); margin-bottom:6px;">
            🌱 Vetores de Dispersão Histórica &amp; Ramos Filhos:
          </div>
          <div id="geoDispersionList" class="geo-dispersion-list"></div>

          <button id="btnExploreTreeFromGlobe" class="btn-dive-tree">
            🌿 Explorar Árvore Filogenética Completa deste Ramo ➔
          </button>
        </div>
      </div>
    </section>

    <!-- VIEW 2: CANOPY MACRO OVERVIEW -->
    <section id="view-canopy">
      <div class="canopy-header">
        <h2>Dossel Macro da Linhagem Humana</h2>
        <p>Selecione um grande tronco filogenético para explorar suas ramificações em árvore viva ou visualizar no globo 3D.</p>
      </div>
      <div id="canopyGrid" class="canopy-grid"></div>
    </section>

    <!-- VIEW 3: LIVING TREE CANVAS -->
    <section id="view-tree">
      <div class="tree-banner">
        <div>
          <div id="treeBannerTitle" class="tree-banner-title">Proto-Indo-Europeu</div>
          <div id="treeBannerEra" class="tree-banner-era">~4.500–3.000 a.C. — Estepes Pôntico-Cáspias</div>
        </div>
        <button id="btnViewOnGlobe" class="btn-all-trunks" style="background:#FFF9E6; border-color:#D97706; color:#9A5707;">🌍 Ver no Globo 3D</button>
        <button id="btnReturnCanopy" class="btn-all-trunks">🏛️ Ver Dossel</button>
      </div>

      <div id="viewport-canvas">
        <svg id="treeSvg" class="organic-tree" width="12000" height="8000">
          <g id="vinesGroup"></g>
        </svg>
        <div id="htmlNodesGroup"></div>
      </div>

      <div class="zoom-hud">
        <button id="btnZoomIn" class="hud-btn" title="Aumentar Zoom">＋</button>
        <button id="btnZoomOut" class="hud-btn" title="Diminuir Zoom">－</button>
        <button id="btnResetView" class="hud-btn" title="Enquadrar Tronco">⤢</button>
      </div>

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
''')

print("template_head.html written successfully.")
