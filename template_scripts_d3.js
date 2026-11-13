  <script>
    __D3_CODE__
  </script>
  <script>
    const NODES = __NODES__;
    const TRUNKS = __TRUNKS__;
    const GEO = __GEO__;
    const LAND_GEOJSON = __LAND_GEOJSON__;
    const ROOT_ID = 'node_poster_4';

    // State
    let currentView = 'globe'; // 'globe' | 'canopy' | 'tree'
    let currentTrunkId = 'node_ie_4';
    let selectedNodeId = null;
    let activeFilter = 'all';

    // Tree Pan & Zoom
    let treeScale = 0.85;
    let panX = 80;
    let panY = 100;
    let isTreeDragging = false;
    let treeStartX, treeStartY;
    const collapsedNodes = new Set();

    // Globe State (D3 Orthographic)
    let globeScaleFactor = 1.0;
    let isGlobeDragging = false;
    let globeLastX = 0, globeLastY = 0;
    let projection, geoPathGenerator, graticule;

    // DOM Elements
    const viewGlobe = document.getElementById('view-globe');
    const viewCanopy = document.getElementById('view-canopy');
    const viewTree = document.getElementById('view-tree');
    
    const pillGlobe = document.getElementById('pillGlobe');
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
    
    const globeCanvas = document.getElementById('globeCanvas');
    const gCtx = globeCanvas.getContext('2d');

    // --- VIEW SWITCHING ---
    function switchView(view) {
      currentView = view;
      [pillGlobe, pillCanopy, pillTree].forEach(p => p.classList.remove('active'));
      [viewGlobe, viewCanopy, viewTree].forEach(v => v.style.display = 'none');

      if (view === 'globe') {
        viewGlobe.style.display = 'grid';
        pillGlobe.classList.add('active');
        initOrResizeGlobe();
        updateGeoDossier(currentTrunkId);
      } else if (view === 'canopy') {
        viewCanopy.style.display = 'block';
        pillCanopy.classList.add('active');
      } else if (view === 'tree') {
        viewTree.style.display = 'flex';
        pillTree.classList.add('active');
        renderTreeForTrunk(currentTrunkId);
      }
    }

    pillGlobe.addEventListener('click', () => switchView('globe'));
    pillCanopy.addEventListener('click', () => switchView('canopy'));
    pillTree.addEventListener('click', () => switchView('tree'));
    document.getElementById('btnReturnCanopy').addEventListener('click', () => switchView('canopy'));
    document.getElementById('btnViewOnGlobe').addEventListener('click', () => {
      switchView('globe');
      focusGlobeOnTrunk(currentTrunkId);
    });

    // --- SPHERICAL VISIBILITY CHECK ---
    // Retorna true somente se o ponto estiver no hemisfério voltado para o observador (<= 90 graus)
    function isVisibleOnGlobe(lon, lat) {
      if (!projection) return false;
      const r = projection.rotate();
      const center = [-r[0], -r[1]];
      // d3.geoDistance calcula a distância angular em radianos [0, PI]
      const dist = d3.geoDistance(center, [lon, lat]);
      return dist <= (Math.PI / 2) + 0.002;
    }

    // --- HIGH-FIDELITY 3D BOTANICAL GLOBE (D3-POWERED) ---
    function initOrResizeGlobe() {
      const rect = globeCanvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const w = Math.round(rect.width * dpr);
      const h = Math.round(rect.height * dpr);

      if (w <= 0 || h <= 0) return;

      globeCanvas.width = w;
      globeCanvas.height = h;

      const baseR = Math.min(w, h) * 0.44 * globeScaleFactor;
      const currRotate = projection ? projection.rotate() : [-50.15, -53.20, 0];

      projection = d3.geoOrthographic()
        .scale(baseR)
        .translate([w / 2, h / 2])
        .rotate(currRotate)
        .clipAngle(90);

      geoPathGenerator = d3.geoPath(projection, gCtx);
      graticule = d3.geoGraticule10();

      drawGlobe();
    }

    function drawGlobe() {
      if (!projection || !geoPathGenerator) return;

      const w = globeCanvas.width;
      const h = globeCanvas.height;
      if (!w || !h) return;

      gCtx.clearRect(0, 0, w, h);
      const r = projection.scale();

      // 1. Esfera sólida / Gradiente de Oceano OPACIFICADO (impede ver o outro lado)
      gCtx.save();
      gCtx.beginPath();
      geoPathGenerator({ type: 'Sphere' });
      const grad = gCtx.createRadialGradient(w * 0.42, h * 0.38, r * 0.05, w / 2, h / 2, r * 1.15);
      grad.addColorStop(0, '#F5F0E4');
      grad.addColorStop(1, '#D8CEBD');
      gCtx.fillStyle = grad;
      gCtx.fill();

      // 2. Graticule (Meridianos e Paralelos)
      gCtx.beginPath();
      geoPathGenerator(graticule);
      gCtx.strokeStyle = '#D0C3AF';
      gCtx.lineWidth = 0.9;
      gCtx.stroke();

      // 3. Continentes Reais do Natural Earth 110m
      gCtx.beginPath();
      geoPathGenerator(LAND_GEOJSON);
      gCtx.fillStyle = '#9AAF8F';
      gCtx.fill();
      gCtx.strokeStyle = '#6E8564';
      gCtx.lineWidth = 1.2;
      gCtx.stroke();

      // 4. Arcos Geodésicos de Migração Histórica
      const activeGeo = GEO[currentTrunkId];
      if (activeGeo && activeGeo.dispersions) {
        for (const dest of activeGeo.dispersions) {
          const arcGeo = {
            type: 'LineString',
            coordinates: [
              [activeGeo.lon, activeGeo.lat],
              [dest.lon, dest.lat]
            ]
          };

          gCtx.beginPath();
          geoPathGenerator(arcGeo);
          gCtx.strokeStyle = 'rgba(46, 125, 50, 0.75)';
          gCtx.lineWidth = 2.2;
          gCtx.setLineDash([5, 4]);
          gCtx.stroke();
          gCtx.setLineDash([]);

          // Marcador do ramo filho (APENAS se visível na frente da Terra)
          if (isVisibleOnGlobe(dest.lon, dest.lat)) {
            const destP = projection([dest.lon, dest.lat]);
            if (destP) {
              gCtx.beginPath();
              gCtx.arc(destP[0], destP[1], 4.0, 0, Math.PI * 2);
              gCtx.fillStyle = '#2E7D32';
              gCtx.fill();
              gCtx.strokeStyle = '#FFFFFF';
              gCtx.lineWidth = 1.2;
              gCtx.stroke();
            }
          }
        }
      }

      // 5. Pinos dos 19 Urheimat Primordiais (APENAS os visíveis na face frontal)
      for (const [tid, g] of Object.entries(GEO)) {
        if (!isVisibleOnGlobe(g.lon, g.lat)) continue; // OCULTO ATRÁS DA ESFERA!

        const pt = projection([g.lon, g.lat]);
        if (!pt) continue;

        const isCurrent = tid === currentTrunkId;
        const pinR = isCurrent ? 8.5 : 5.5;

        // Verificar se a família tem membros correspondentes ao filtro ativo
        let trunkMatchesFilter = true;
        if (activeFilter !== 'all') {
          let countMatches = 0;
          function checkTrunkMatches(nid) {
            const kn = NODES[nid];
            if (kn) {
              if (activeFilter === 'living' && kn.is_living) countMatches++;
              else if (activeFilter === 'extinct' && kn.is_extinct) countMatches++;
              else if (activeFilter === 'proto' && kn.is_proto) countMatches++;
            }
            for (const c of (NODES[nid]?.children || [])) checkTrunkMatches(c);
          }
          checkTrunkMatches(tid);
          if (countMatches === 0) trunkMatchesFilter = false;
        }

        gCtx.save();
        if (!trunkMatchesFilter) {
          gCtx.globalAlpha = 0.22;
        }

        // Pulso dourado no nó ativo
        if (isCurrent && trunkMatchesFilter) {
          gCtx.beginPath();
          gCtx.arc(pt[0], pt[1], 18, 0, Math.PI * 2);
          gCtx.fillStyle = 'rgba(217, 119, 6, 0.25)';
          gCtx.fill();
        }

        gCtx.beginPath();
        gCtx.arc(pt[0], pt[1], pinR, 0, Math.PI * 2);
        gCtx.fillStyle = isCurrent ? '#D97706' : '#6A8C5A';
        gCtx.fill();
        gCtx.strokeStyle = '#FFFDF8';
        gCtx.lineWidth = 2.0;
        gCtx.stroke();

        // Rótulo da família no berço visível
        if (isCurrent) {
          gCtx.font = '700 13px sans-serif';
          gCtx.fillStyle = '#1B3524';
          gCtx.fillText(g.nome, pt[0] + 12, pt[1] - 8);
        }
        gCtx.restore();
      }

      // 6. Borda Externa da Esfera
      gCtx.beginPath();
      geoPathGenerator({ type: 'Sphere' });
      gCtx.strokeStyle = '#63775A';
      gCtx.lineWidth = 2.2;
      gCtx.stroke();

      // 7. Vinheta Atmosférica Botânica
      const shine = gCtx.createRadialGradient(w * 0.35, h * 0.28, 0, w * 0.35, h * 0.28, r * 0.95);
      shine.addColorStop(0, 'rgba(255, 255, 255, 0.30)');
      shine.addColorStop(1, 'rgba(255, 255, 255, 0)');
      gCtx.beginPath();
      geoPathGenerator({ type: 'Sphere' });
      gCtx.fillStyle = shine;
      gCtx.fill();
      gCtx.restore();
    }

    // Globe Drag Rotation (Mouse & Touch)
    globeCanvas.addEventListener('pointerdown', (e) => {
      isGlobeDragging = true;
      globeLastX = e.clientX;
      globeLastY = e.clientY;
      globeCanvas.classList.add('dragging');
      globeCanvas.setPointerCapture(e.pointerId);
    });

    window.addEventListener('pointermove', (e) => {
      if (!isGlobeDragging || !projection) return;
      const dx = e.clientX - globeLastX;
      const dy = e.clientY - globeLastY;
      globeLastX = e.clientX;
      globeLastY = e.clientY;

      const r = projection.rotate();
      const k = 75 / projection.scale();
      const nextLon = r[0] + dx * k;
      const nextLat = Math.max(-85, Math.min(85, r[1] - dy * k));

      projection.rotate([nextLon, nextLat, 0]);
      drawGlobe();
    });

    window.addEventListener('pointerup', (e) => {
      if (!isGlobeDragging) return;
      isGlobeDragging = false;
      globeCanvas.classList.remove('dragging');

      // Click check for pin hit (apenas nos pinos frontais visíveis)
      const rect = globeCanvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const clickX = (e.clientX - rect.left) * dpr;
      const clickY = (e.clientY - rect.top) * dpr;

      let nearestTrunk = null;
      let minDist = 28 * dpr;

      for (const [tid, g] of Object.entries(GEO)) {
        if (!isVisibleOnGlobe(g.lon, g.lat)) continue; // Ignora o verso!
        const pt = projection([g.lon, g.lat]);
        if (!pt) continue;
        const dist = Math.hypot(clickX - pt[0], clickY - pt[1]);
        if (dist < minDist) {
          minDist = dist;
          nearestTrunk = tid;
        }
      }

      if (nearestTrunk) {
        focusGlobeOnTrunk(nearestTrunk);
      }
    });

    // Globe Zoom
    document.getElementById('globeZoomIn').addEventListener('click', () => {
      globeScaleFactor = Math.min(globeScaleFactor * 1.18, 1.8);
      initOrResizeGlobe();
    });
    document.getElementById('globeZoomOut').addEventListener('click', () => {
      globeScaleFactor = Math.max(globeScaleFactor / 1.18, 0.65);
      initOrResizeGlobe();
    });
    document.getElementById('globeReset').addEventListener('click', () => {
      globeScaleFactor = 1.0;
      focusGlobeOnTrunk('node_ie_4');
    });

    // Smooth Sphere Rotation Animation to Target Trunk
    function focusGlobeOnTrunk(tid) {
      const g = GEO[tid];
      if (!g || !projection) return;

      currentTrunkId = tid;
      updateGeoDossier(tid);

      const targetRot = [-g.lon, -g.lat, 0];
      const startRot = projection.rotate();

      // Interpolação esférica suave
      const interpolator = d3.interpolate(startRot, targetRot);
      let startTime = null;
      const duration = 480;

      function animateStep(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const ease = d3.easeCubicOut(progress);

        projection.rotate(interpolator(ease));
        drawGlobe();

        if (progress < 1) {
          requestAnimationFrame(animateStep);
        }
      }
      requestAnimationFrame(animateStep);
    }

    function updateGeoDossier(tid) {
      const g = GEO[tid] || { nome: "Macro-Família", era: "Histórica", urheimat: "", desc: "", dispersions: [] };
      document.getElementById('geoTrunkTitle').textContent = g.nome;
      document.getElementById('geoTrunkEra').textContent = `⏳ ${g.era}`;
      document.getElementById('geoTrunkUrheimatText').textContent = `${g.urheimat} (${g.lat.toFixed(2)}°, ${g.lon.toFixed(2)}°)`;
      document.getElementById('geoTrunkDesc').textContent = g.desc;
      
      const ecologiaEl = document.getElementById('geoTrunkEcologia');
      if (ecologiaEl) ecologiaEl.textContent = g.ecologia || "Consulte dados biogeográficos";
      
      const alinhamentoEl = document.getElementById('geoTrunkAlinhamento');
      if (alinhamentoEl) alinhamentoEl.textContent = g.alinhamento ? `${g.alinhamento} · Ordem: ${g.ordem || 'Livre'}` : "Consulte perfil tipológico";

      const refEl = document.getElementById('geoTrunkRef');
      if (refEl) refEl.textContent = g.referencia || "Glottolog / Theodor Cole (2026)";

      const listEl = document.getElementById('geoDispersionList');
      let html = '';
      (g.dispersions || []).forEach(d => {
        html += `<span class="dispersion-pill" onclick="centerGlobeOn(${d.lat}, ${d.lon})">📍 ${escapeHtml(d.nome)}</span>`;
      });
      listEl.innerHTML = html;
    }

    window.centerGlobeOn = function(lat, lon) {
      if (!projection) return;
      const targetRot = [-lon, -lat, 0];
      const startRot = projection.rotate();
      const interpolator = d3.interpolate(startRot, targetRot);
      let startTime = null;
      const duration = 420;

      function step(ts) {
        if (!startTime) startTime = ts;
        const progress = Math.min((ts - startTime) / duration, 1);
        projection.rotate(interpolator(d3.easeCubicOut(progress)));
        drawGlobe();
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    };

    document.getElementById('btnExploreTreeFromGlobe').addEventListener('click', () => {
      switchView('tree');
    });

    // --- RENDER CANOPY CARDS ---
    function renderCanopy() {
      let html = '';
      for (const [tid, meta] of Object.entries(TRUNKS)) {
        const rootNode = NODES[tid];
        if (!rootNode) continue;
        
        let count = 0, livCount = 0, extCount = 0, proCount = 0;
        function countKids(nid) {
          count++;
          const kn = NODES[nid];
          if (kn) {
            if (kn.is_living) livCount++;
            if (kn.is_extinct) extCount++;
            if (kn.is_proto) proCount++;
          }
          for (const c of (NODES[nid]?.children || [])) countKids(c);
        }
        countKids(tid);

        const geoItem = GEO[tid] || {};

        html += `
          <div class="trunk-card" data-trunk-id="${tid}" onclick="selectTrunkAndOpenTree('${tid}')">
            <div>
              <div class="trunk-card-header">
                <span class="trunk-card-badge">Macro-Família</span>
                <span style="font-size:11px; color:var(--ink-light);">${count} nós</span>
              </div>
              <h3>${escapeHtml(meta.nome)}</h3>
              <div class="trunk-card-meta">⏳ ${escapeHtml(geoItem.era || meta.era)}</div>
              <div class="trunk-card-stats" style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:8px; font-size:10px;">
                <span style="padding:2px 6px; border-radius:6px; background:rgba(46,125,50,0.1); color:var(--leaf-green); font-weight:700;">🟢 ${livCount} vivas</span>
                <span style="padding:2px 6px; border-radius:6px; background:rgba(185,28,28,0.1); color:var(--extinct-clay); font-weight:700;">🔴 ${extCount} extintas</span>
                <span style="padding:2px 6px; border-radius:6px; background:rgba(29,78,216,0.1); color:var(--proto-azure); font-weight:700;">🔵 ${proCount} proto</span>
              </div>
              <p class="trunk-card-desc">${escapeHtml(geoItem.desc || meta.desc)}</p>
            </div>
            <div class="trunk-card-footer">
              <span>📍 ${escapeHtml(geoItem.urheimat || meta.urheimat)}</span>
              <span class="trunk-card-action">Explorar ➔</span>
            </div>
          </div>
        `;
      }
      canopyGrid.innerHTML = html;
    }

    window.selectTrunkAndOpenTree = function(tid) {
      currentTrunkId = tid;
      switchView('tree');
    };

    // --- DYNAMIC TIDY TREE LAYOUT ENGINE ---
    function computeTreeLayout(rootId) {
      const levelGap = 240;
      const nodeGap = 72;

      let leafY = 60;
      const positions = new Map();

      function layoutNode(nid, depth) {
        const node = NODES[nid];
        if (!node) return;

        const isCollapsed = collapsedNodes.has(nid);
        const children = isCollapsed ? [] : (node.children || []);

        if (children.length === 0) {
          positions.set(nid, { x: depth * levelGap + 80, y: leafY });
          leafY += nodeGap;
        } else {
          let sumY = 0;
          for (const cid of children) {
            layoutNode(cid, depth + 1);
            sumY += positions.get(cid).y;
          }
          const avgY = sumY / children.length;
          positions.set(nid, { x: depth * levelGap + 80, y: avgY });
        }
      }

      layoutNode(rootId, 0);
      return positions;
    }

    // --- RENDER LIVING TREE ---
    function renderTreeForTrunk(trunkId) {
      const rootNode = NODES[trunkId];
      if (!rootNode) return;

      const meta = TRUNKS[trunkId] || { nome: rootNode.title, era: "Radiação Humana" };
      const geoMeta = GEO[trunkId] || {};
      document.getElementById('treeBannerTitle').textContent = meta.nome;
      document.getElementById('treeBannerEra').textContent = `${geoMeta.era || meta.era} — ${geoMeta.urheimat || meta.urheimat || 'Berço Ancestral'}`;

      const positions = computeTreeLayout(trunkId);

      let maxX = 1200;
      let maxY = 800;
      for (const [_, pos] of positions) {
        if (pos.x > maxX) maxX = pos.x + 320;
        if (pos.y > maxY) maxY = pos.y + 200;
      }
      treeSvg.setAttribute('width', maxX);
      treeSvg.setAttribute('height', maxY);

      // Render Organic Bézier Vines
      let vinesHtml = '';
      function renderEdges(nid) {
        if (collapsedNodes.has(nid)) return;
        const p1 = positions.get(nid);
        const node = NODES[nid];
        if (!node || !p1) return;

        for (const cid of node.children) {
          const p2 = positions.get(cid);
          if (!p2) continue;

          const x0 = p1.x + 180;
          const y0 = p1.y + 24;
          const x1 = p2.x;
          const y1 = p2.y + 24;
          const dx = (x1 - x0) * 0.55;

          const d = `M ${x0} ${y0} C ${x0 + dx} ${y0}, ${x1 - dx} ${y1}, ${x1} ${y1}`;
          vinesHtml += `<path id=\"vine_${nid}_${cid}\" data-parent=\"${nid}\" data-child=\"${cid}\" class=\"vine-edge\" d=\"${d}\" />`;

          renderEdges(cid);
        }
      }
      renderEdges(trunkId);
      vinesGroup.innerHTML = vinesHtml;

      // Render Node Capsules
      let nodesHtml = '';
      for (const [nid, pos] of positions) {
        const node = NODES[nid];
        if (!node) continue;

        let typeClass = 'type-branch';
        let dotClass = 'branch';
        if (node.is_proto) { typeClass = 'type-proto'; dotClass = 'proto'; }
        else if (node.is_extinct) { typeClass = 'type-extinct'; dotClass = 'extinct'; }
        else if (node.is_living) { typeClass = 'type-living'; dotClass = 'living'; }

        const hasKids = node.children && node.children.length > 0;
        const isCollapsed = collapsedNodes.has(nid);

        nodesHtml += `
          <div class="node-capsule ${typeClass}" id="capsule_${nid}" data-id="${nid}" style="left:${pos.x}px; top:${pos.y}px;" onclick="onNodeClick('${nid}')">
            <div class="node-header">
              <span class="node-dot ${dotClass}"></span>
              <span class="node-title">${escapeHtml(node.title)}</span>
            </div>
            ${node.endonym ? `<div class="node-endonym">${escapeHtml(node.endonym)}</div>` : ''}\
            ${node.subtitle ? `<div class="node-meta">${escapeHtml(node.subtitle.substring(0, 35))}</div>` : ''}\
            ${hasKids ? `
              <div class="node-toggle-btn" title="${isCollapsed ? 'Expandir Ramo' : 'Recolher Ramo'}" onclick="toggleBranch(event, '${nid}')">
                ${isCollapsed ? '＋' : '−'}
              </div>` : ''}
          </div>
        `;
      }
      htmlNodesGroup.innerHTML = nodesHtml;

      panX = 80;
      panY = 100;
      treeScale = 0.85;
      updateTreeTransform();

      if (selectedNodeId && positions.has(selectedNodeId)) {
        highlightAncestralSap(selectedNodeId);
      }
      applyFilterToView();
    }

    window.toggleBranch = function(e, nid) {
      e.stopPropagation();
      if (collapsedNodes.has(nid)) {
        collapsedNodes.delete(nid);
      } else {
        collapsedNodes.add(nid);
      }
      renderTreeForTrunk(currentTrunkId);
    };

    window.onNodeClick = function(nid) {
      selectNode(nid);
    };

    // Node Selection & Sap Flow
    function selectNode(nid) {
      selectedNodeId = nid;
      const node = NODES[nid];
      if (!node) return;

      if (node.trunk_id && node.trunk_id !== currentTrunkId && node.trunk_id !== 'node_poster_4') {
        currentTrunkId = node.trunk_id;
        renderTreeForTrunk(currentTrunkId);
      }

      let needsRerender = false;
      for (const ancId of node.ancestors) {
        if (collapsedNodes.has(ancId)) {
          collapsedNodes.delete(ancId);
          needsRerender = true;
        }
      }
      if (needsRerender) {
        renderTreeForTrunk(currentTrunkId);
      }

      document.querySelectorAll('.node-capsule.active').forEach(el => el.classList.remove('active'));
      const cap = document.getElementById(`capsule_${nid}`);
      if (cap) cap.classList.add('active');

      highlightAncestralSap(nid);
      populateHerbariumDrawer(node);
      herbariumDrawer.classList.add('open');
    }

    function highlightAncestralSap(targetId) {
      document.querySelectorAll('.vine-edge.sap-flow').forEach(el => el.classList.remove('sap-flow'));
      document.querySelectorAll('.node-capsule.sap-path').forEach(el => el.classList.remove('sap-path'));

      const node = NODES[targetId];
      if (!node) return;

      const path = node.ancestors;
      for (let i = 0; i < path.length; i++) {
        const curr = path[i];
        const cap = document.getElementById(`capsule_${curr}`);
        if (cap) cap.classList.add('sap-path');

        if (i < path.length - 1) {
          const next = path[i + 1];
          const edge = document.getElementById(`vine_${curr}_${next}`);
          if (edge) edge.classList.add('sap-flow');
        }
      }
    }

    // Herbarium Drawer
    function populateHerbariumDrawer(node) {
      document.getElementById('drawerTitle').textContent = node.title;
      document.getElementById('drawerEndonym').textContent = node.endonym || 'Língua Filogenética Documentada';

      const badge = document.getElementById('drawerBadge');
      if (node.is_proto) {
        badge.className = 'drawer-badge badge-proto';
        badge.textContent = 'Protolíngua Reconstruída';
      } else if (node.is_extinct) {
        badge.className = 'drawer-badge badge-extinct';
        badge.textContent = 'Língua Extinta (†)';
      } else if (node.is_living) {
        badge.className = 'drawer-badge badge-living';
        badge.textContent = 'Língua Natural Viva';
      } else {
        badge.className = 'drawer-badge badge-branch';
        badge.textContent = 'Ramo Filogenético';
      }

      document.getElementById('drawerTrunkBadge').textContent = node.trunk_name || 'Tronco';

      const lineageEl = document.getElementById('drawerLineage');
      let lineageHtml = '';
      node.ancestors.forEach((ancId, idx) => {
        const ancNode = NODES[ancId];
        if (!ancNode) return;
        lineageHtml += `<span class="crumb" onclick="selectNode('${ancId}')">${escapeHtml(ancNode.title)}</span>`;
        if (idx < node.ancestors.length - 1) {
          lineageHtml += `<span class="crumb-sep">➔</span>`;
        }
      });
      lineageEl.innerHTML = lineageHtml;

      const trunkMeta = TRUNKS[node.trunk_id] || {};
      const geoMeta = GEO[node.trunk_id] || {};
      const urheimatText = geoMeta.urheimat || trunkMeta.urheimat || 'Consulte histórico da família';
      const eraText = geoMeta.era || trunkMeta.era || 'Período Histórico';
      document.getElementById('drawerUrheimat').innerHTML = `<b>Época Estimada:</b> ${eraText}<br><b>Berço Ancestral (*Urheimat*):</b> ${urheimatText}`;

      document.getElementById('drawerSynthesis').textContent = 
        `${node.title} constitui um nó fulcral na filogenia das línguas do ramo ${node.trunk_name}. Sua taxonomia e classificação comparativa são referenciadas nos corpora de Theodor Cole (2026), Glottolog e literatura especializada.`;

      document.getElementById('drawerTypology').textContent = 
        node.is_proto 
          ? (geoMeta.alinhamento ? `Protolíngua com inventário reconstruído via Método Histórico-Comparativo. Alinhamento: ${geoMeta.alinhamento}. Ordem de constituintes: ${geoMeta.ordem || 'SOV'}.` : "Protolíngua com correspondências fonológicas regulares reconstruídas pelo método histórico-comparativo rigoroso.")
          : (node.is_extinct 
              ? "Língua atestada em registros epigráficos antigos, tábuas de argila, papiros ou tradição litúrgica escrita."
              : "Língua natural viva com comunidade de falantes nativos contemporânea, dialetologia documentada e transmissão intergeracional ativa.");

      document.getElementById('drawerSpeakers').textContent = 
        node.subtitle || "Consulte dados censitários e atlas linguísticos regionais.";

      const refEl = document.getElementById('drawerReference');
      if (refEl) {
        refEl.textContent = geoMeta.referencia || "Glottolog 5.0 (2024); Cole, Theodor C. H. (2026). Poster Filogenético das Línguas do Mundo.";
      }
    }

    drawerCloseBtn.addEventListener('click', () => {
      herbariumDrawer.classList.remove('open');
    });

    document.getElementById('btnTraceSapAction').addEventListener('click', () => {
      if (selectedNodeId) {
        if (currentView !== 'tree') switchView('tree');
        focusOnNodeInTree(selectedNodeId);
        highlightAncestralSap(selectedNodeId);
      }
    });

    function focusOnNodeInTree(nid) {
      const cap = document.getElementById(`capsule_${nid}`);
      if (!cap) return;
      const x = parseFloat(cap.style.left);
      const y = parseFloat(cap.style.top);

      treeScale = 1.0;
      panX = (viewTree.clientWidth / 2) - x * treeScale - 100;
      panY = (viewTree.clientHeight / 2) - y * treeScale;
      updateTreeTransform();
    }

    // Search Autocomplete
    searchInput.addEventListener('input', () => {
      const query = searchInput.value.trim().toLowerCase();
      if (!query || query.length < 2) {
        searchResults.style.display = 'none';
        return;
      }

      let matches = [];
      for (const [nid, node] of Object.entries(NODES)) {
        const txt = (node.title + ' ' + (node.endonym || '') + ' ' + (node.subtitle || '') + ' ' + node.trunk_name).toLowerCase();
        if (txt.includes(query)) {
          matches.push(node);
          if (matches.length >= 25) break;
        }
      }

      if (matches.length === 0) {
        searchResults.innerHTML = '<div style="padding:14px; font-size:12px; color:var(--ink-muted);">Nenhum nó encontrado com este termo.</div>';
      } else {
        let html = '';
        matches.forEach(m => {
          const dot = m.is_proto ? '🔵' : (m.is_extinct ? '🔴' : (m.is_living ? '🟢' : '🌿'));
          html += `
            <div class="search-item" onclick="onSearchSelect('${m.id}')">
              <div class="search-item-title">
                <span>${dot}</span>
                <span>${escapeHtml(m.title)}</span>
                ${m.endonym ? `<span style="font-size:11px; font-style:italic; color:var(--sap-gold); font-family:var(--font-serif);">${escapeHtml(m.endonym)}</span>` : ''}
              </div>
              <div class="search-item-meta">${escapeHtml(m.trunk_name)} — ${escapeHtml(m.subtitle || '')}</div>
            </div>
          `;
        });
        searchResults.innerHTML = html;
      }
      searchResults.style.display = 'block';
    });

    window.onSearchSelect = function(nid) {
      searchResults.style.display = 'none';
      searchInput.value = '';
      selectNode(nid);
      if (currentView === 'tree') {
        setTimeout(() => focusOnNodeInTree(nid), 100);
      } else if (currentView === 'globe') {
        const node = NODES[nid];
        if (node && node.trunk_id) focusGlobeOnTrunk(node.trunk_id);
      }
    };

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-wrapper')) {
        searchResults.style.display = 'none';
      }
    });

    // Filters & Global Counter Initialization
    function updateGlobalFilterPills() {
      let totalLiving = 0, totalExtinct = 0, totalProto = 0, totalNodes = 0;
      for (const node of Object.values(NODES)) {
        totalNodes++;
        if (node.is_living) totalLiving++;
        if (node.is_extinct) totalExtinct++;
        if (node.is_proto) totalProto++;
      }
      
      const bAll = document.querySelector('.filter-chip[data-filter="all"]');
      const bLiving = document.querySelector('.filter-chip[data-filter="living"]');
      const bExtinct = document.querySelector('.filter-chip[data-filter="extinct"]');
      const bProto = document.querySelector('.filter-chip[data-filter="proto"]');

      if (bAll) bAll.textContent = `Todas (${totalNodes})`;
      if (bLiving) bLiving.textContent = `🟢 Vivas (${totalLiving})`;
      if (bExtinct) bExtinct.textContent = `🔴 Extintas (${totalExtinct})`;
      if (bProto) bProto.textContent = `🔵 Protolínguas (${totalProto})`;
    }

    document.querySelectorAll('.filter-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.getAttribute('data-filter');
        applyFilterToView();
      });
    });

    function applyFilterToView() {
      // 1. Filtrar nós na Árvore Viva
      document.querySelectorAll('.node-capsule').forEach(cap => {
        const nid = cap.getAttribute('data-id');
        const node = NODES[nid];
        if (!node) return;

        let visible = true;
        if (activeFilter === 'living' && !node.is_living) visible = false;
        if (activeFilter === 'extinct' && !node.is_extinct) visible = false;
        if (activeFilter === 'proto' && !node.is_proto) visible = false;

        cap.style.opacity = visible ? '1' : '0.18';
        cap.style.pointerEvents = visible ? 'auto' : 'none';
      });

      // 2. Filtrar cards no Dossel Macro
      document.querySelectorAll('.trunk-card').forEach(card => {
        const tid = card.getAttribute('data-trunk-id');
        if (!tid) return;

        let matchCount = 0;
        function countMatches(nid) {
          const kn = NODES[nid];
          if (kn) {
            if (activeFilter === 'all') matchCount++;
            else if (activeFilter === 'living' && kn.is_living) matchCount++;
            else if (activeFilter === 'extinct' && kn.is_extinct) matchCount++;
            else if (activeFilter === 'proto' && kn.is_proto) matchCount++;
          }
          for (const c of (NODES[nid]?.children || [])) countMatches(c);
        }
        countMatches(tid);

        if (activeFilter !== 'all' && matchCount === 0) {
          card.style.opacity = '0.25';
          card.style.filter = 'grayscale(0.8)';
          card.style.pointerEvents = 'none';
        } else {
          card.style.opacity = '1';
          card.style.filter = 'none';
          card.style.pointerEvents = 'auto';
        }
      });

      // 3. Atualizar o Globo 3D
      if (currentView === 'globe') {
        drawGlobe();
      }
    }

    // Tree Pan and Zoom
    function updateTreeTransform() {
      viewportCanvas.style.transform = `translate(${panX}px, ${panY}px) scale(${treeScale})`;
    }

    viewTree.addEventListener('mousedown', (e) => {
      if (e.target.closest('#herbarium-drawer') || e.target.closest('.zoom-hud') || e.target.closest('.tree-banner') || e.target.closest('.node-capsule')) return;
      isTreeDragging = true;
      viewTree.classList.add('dragging');
      treeStartX = e.clientX - panX;
      treeStartY = e.clientY - panY;
    });

    window.addEventListener('mousemove', (e) => {
      if (!isTreeDragging) return;
      panX = e.clientX - treeStartX;
      panY = e.clientY - treeStartY;
      updateTreeTransform();
    });

    window.addEventListener('mouseup', () => {
      isTreeDragging = false;
      viewTree.classList.remove('dragging');
    });

    // Touch support for Tree Pan
    viewTree.addEventListener('touchstart', (e) => {
      if (e.target.closest('#herbarium-drawer') || e.target.closest('.zoom-hud') || e.target.closest('.tree-banner') || e.target.closest('.node-capsule')) return;
      if (e.touches.length === 1) {
        isTreeDragging = true;
        treeStartX = e.touches[0].clientX - panX;
        treeStartY = e.touches[0].clientY - panY;
      }
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (!isTreeDragging || e.touches.length !== 1) return;
      panX = e.touches[0].clientX - treeStartX;
      panY = e.touches[0].clientY - treeStartY;
      updateTreeTransform();
    }, { passive: true });

    window.addEventListener('touchend', () => {
      isTreeDragging = false;
    });

    viewTree.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = 1.12;
      const mouseX = e.clientX;
      const mouseY = e.clientY;

      let newScale = e.deltaY < 0 ? treeScale * zoomFactor : treeScale / zoomFactor;
      newScale = Math.min(Math.max(0.2, newScale), 2.2);

      panX = mouseX - (mouseX - panX) * (newScale / treeScale);
      panY = mouseY - (mouseY - panY) * (newScale / treeScale);
      treeScale = newScale;
      updateTreeTransform();
    }, { passive: false });

    document.getElementById('btnZoomIn').addEventListener('click', () => {
      treeScale = Math.min(treeScale * 1.25, 2.2);
      updateTreeTransform();
    });

    document.getElementById('btnZoomOut').addEventListener('click', () => {
      treeScale = Math.max(treeScale / 1.25, 0.2);
      updateTreeTransform();
    });

    document.getElementById('btnResetView').addEventListener('click', () => {
      panX = 80;
      panY = 100;
      treeScale = 0.85;
      updateTreeTransform();
    });

    function escapeHtml(str) {
      return (str || '').replace(/[<>&]/g, c => ({'<':'&lt;', '>':'&gt;', '&':'&amp;'}[c]));
    }

    // Dynamic Resize Handling
    window.addEventListener('resize', () => {
      if (currentView === 'globe') initOrResizeGlobe();
    });

    // Initial Load
    renderCanopy();
    updateGlobalFilterPills();
    switchView('globe');
    focusGlobeOnTrunk('node_ie_4');
  </script>
</body>
</html>
