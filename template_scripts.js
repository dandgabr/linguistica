
  <script>
    const NODES = __NODES__;
    const TRUNKS = __TRUNKS__;
    const GEO = __GEO__;
    const LAND = __LAND__;
    const ROOT_ID = 'node_poster_4';

    // State
    let currentView = 'globe'; // 'globe' | 'canopy' | 'tree'
    let currentTrunkId = 'node_ie_4';
    let selectedNodeId = null;
    let activeFilter = 'all';

    // Tree Pan & Zoom
    let scale = 0.85;
    let panX = 80;
    let panY = 100;
    let isTreeDragging = false;
    let treeStartX, treeStartY;
    const collapsedNodes = new Set();

    // Globe State
    let centerLat = 48.0;
    let centerLon = 42.0;
    let globeRotation = 0;
    let globeScale = 1.0;
    let isGlobeDragging = false;
    let globeLastX = 0, globeLastY = 0;
    let targetLat = 48.0, targetLon = 42.0;
    let isAnimatingGlobe = false;

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
        resizeGlobe();
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

    // --- 3D BOTANICAL GLOBE ENGINE ---
    function resizeGlobe() {
      const rect = globeCanvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      globeCanvas.width = Math.round(rect.width * dpr);
      globeCanvas.height = Math.round(rect.height * dpr);
      gCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
      drawGlobe();
    }

    function globeRadius() {
      return Math.min(globeCanvas.clientWidth, globeCanvas.clientHeight) * 0.44 * globeScale;
    }

    function projectGlobe(lat, lon) {
      const phi = lat * Math.PI / 180;
      const lam = lon * Math.PI / 180;
      const phi0 = centerLat * Math.PI / 180;
      const lam0 = centerLon * Math.PI / 180 + globeRotation;
      const dl = lam - lam0;

      const z = Math.sin(phi0) * Math.sin(phi) + Math.cos(phi0) * Math.cos(phi) * Math.cos(dl);
      const r = globeRadius();
      const x = r * Math.cos(phi) * Math.sin(dl);
      const y = -r * (Math.cos(phi0) * Math.sin(phi) - Math.sin(phi0) * Math.cos(phi) * Math.cos(dl));

      return { x: globeCanvas.clientWidth / 2 + x, y: globeCanvas.clientHeight / 2 + y, z };
    }

    function toVector(lat, lon) {
      const p = lat * Math.PI / 180;
      const l = lon * Math.PI / 180;
      return [Math.cos(p) * Math.cos(l), Math.cos(p) * Math.sin(l), Math.sin(p)];
    }

    function drawGlobe() {
      const w = globeCanvas.clientWidth;
      const h = globeCanvas.clientHeight;
      if (!w || !h) return;

      gCtx.clearRect(0, 0, w, h);
      const r = globeRadius();

      // Clip Sphere
      gCtx.save();
      gCtx.beginPath();
      gCtx.arc(w / 2, h / 2, r, 0, Math.PI * 2);
      gCtx.clip();

      // Ocean Base Gradient
      const grad = gCtx.createRadialGradient(w * 0.42, h * 0.38, r * 0.05, w / 2, h / 2, r * 1.15);
      grad.addColorStop(0, '#F5F0E4');
      grad.addColorStop(1, '#D8CEBD');
      gCtx.fillStyle = grad;
      gCtx.fillRect(w / 2 - r, h / 2 - r, r * 2, r * 2);

      // Graticule Grid
      gCtx.strokeStyle = '#D0C3AF';
      gCtx.lineWidth = 0.6;
      for (let lat = -60; lat <= 75; lat += 20) {
        gCtx.beginPath();
        let active = false;
        for (let lon = -180; lon <= 180; lon += 4) {
          const p = projectGlobe(lat, lon);
          if (p.z > 0) {
            if (!active) gCtx.moveTo(p.x, p.y);
            else gCtx.lineTo(p.x, p.y);
            active = true;
          } else active = false;
        }
        gCtx.stroke();
      }
      for (let lon = -180; lon < 180; lon += 20) {
        gCtx.beginPath();
        let active = false;
        for (let lat = -85; lat <= 85; lat += 4) {
          const p = projectGlobe(lat, lon);
          if (p.z > 0) {
            if (!active) gCtx.moveTo(p.x, p.y);
            else gCtx.lineTo(p.x, p.y);
            active = true;
          } else active = false;
        }
        gCtx.stroke();
      }

      // Landmass Polygons
      for (const poly of LAND) {
        gCtx.beginPath();
        let active = false;
        for (const pt of poly) {
          const p = projectGlobe(pt[0], pt[1]);
          if (p.z > 0) {
            if (!active) gCtx.moveTo(p.x, p.y);
            else gCtx.lineTo(p.x, p.y);
            active = true;
          } else active = false;
        }
        if (active) {
          gCtx.closePath();
          gCtx.fillStyle = '#9AAF8F';
          gCtx.fill();
          gCtx.strokeStyle = '#6E8564';
          gCtx.lineWidth = 1;
          gCtx.stroke();
        }
      }

      // Migration Arcs for Selected Trunk
      const activeGeo = GEO[currentTrunkId];
      if (activeGeo && activeGeo.dispersions) {
        const rootP = projectGlobe(activeGeo.lat, activeGeo.lon);
        if (rootP.z > 0) {
          for (const dest of activeGeo.dispersions) {
            gCtx.beginPath();
            const endP = projectGlobe(dest.lat, dest.lon);
            const a = toVector(activeGeo.lat, activeGeo.lon);
            const b = toVector(dest.lat, dest.lon);
            const dot = Math.max(-1, Math.min(1, a[0]*b[0] + a[1]*b[1] + a[2]*b[2]));
            const omega = Math.acos(dot);

            let arcActive = false;
            for (let i = 0; i <= 36; i++) {
              const t = i / 36;
              const v = omega < 1e-5 ? a : a.map((x, k) => Math.sin((1-t)*omega)/Math.sin(omega)*x + Math.sin(t*omega)/Math.sin(omega)*b[k]);
              const lat = Math.asin(v[2]) * 180 / Math.PI;
              const lon = Math.atan2(v[1], v[0]) * 180 / Math.PI;
              const p = projectGlobe(lat, lon);
              if (p.z > 0) {
                if (!arcActive) gCtx.moveTo(p.x, p.y);
                else gCtx.lineTo(p.x, p.y);
                arcActive = true;
              } else arcActive = false;
            }
            gCtx.strokeStyle = 'rgba(46, 125, 50, 0.65)';
            gCtx.lineWidth = 1.8;
            gCtx.setLineDash([4, 3]);
            gCtx.stroke();
            gCtx.setLineDash([]);

            // Child target marker
            if (endP.z > 0) {
              gCtx.beginPath();
              gCtx.arc(endP.x, endP.y, 3.5, 0, Math.PI * 2);
              gCtx.fillStyle = '#2E7D32';
              gCtx.fill();
              gCtx.strokeStyle = '#FFFFFF';
              gCtx.lineWidth = 1;
              gCtx.stroke();
            }
          }
        }
      }

      // 19 Urheimat Pins
      for (const [tid, g] of Object.entries(GEO)) {
        const p = projectGlobe(g.lat, g.lon);
        if (p.z <= 0) continue;

        const isCurrent = tid === currentTrunkId;
        const pinR = isCurrent ? 7.5 : 5;

        // Glowing halo for selected
        if (isCurrent) {
          gCtx.beginPath();
          gCtx.arc(p.x, p.y, 16, 0, Math.PI * 2);
          gCtx.fillStyle = 'rgba(217, 119, 6, 0.22)';
          gCtx.fill();
        }

        gCtx.beginPath();
        gCtx.arc(p.x, p.y, pinR, 0, Math.PI * 2);
        gCtx.fillStyle = isCurrent ? '#D97706' : '#6A8C5A';
        gCtx.fill();
        gCtx.strokeStyle = '#FFFDF8';
        gCtx.lineWidth = 1.6;
        gCtx.stroke();

        // Label if active
        if (isCurrent) {
          gCtx.font = '700 12px sans-serif';
          gCtx.fillStyle = '#1B3524';
          gCtx.fillText(g.nome, p.x + 10, p.y - 8);
        }
      }

      gCtx.restore();

      // Sphere Outer Rim
      gCtx.beginPath();
      gCtx.arc(w / 2, h / 2, r, 0, Math.PI * 2);
      gCtx.strokeStyle = '#63775A';
      gCtx.lineWidth = 1.8;
      gCtx.stroke();

      // Atmospheric botanical vignette shine
      const shine = gCtx.createRadialGradient(w * 0.35, h * 0.28, 0, w * 0.35, h * 0.28, r * 0.95);
      shine.addColorStop(0, 'rgba(255, 255, 255, 0.28)');
      shine.addColorStop(1, 'rgba(255, 255, 255, 0)');
      gCtx.beginPath();
      gCtx.arc(w / 2, h / 2, r, 0, Math.PI * 2);
      gCtx.fillStyle = shine;
      gCtx.fill();
    }

    // Globe Drag Rotation
    globeCanvas.addEventListener('pointerdown', (e) => {
      isGlobeDragging = true;
      globeLastX = e.clientX;
      globeLastY = e.clientY;
      globeCanvas.classList.add('dragging');
      globeCanvas.setPointerCapture(e.pointerId);
    });

    window.addEventListener('pointermove', (e) => {
      if (!isGlobeDragging) return;
      const dx = e.clientX - globeLastX;
      const dy = e.clientY - globeLastY;
      globeLastX = e.clientX;
      globeLastY = e.clientY;

      globeRotation -= (dx / globeRadius()) * 0.75;
      centerLat = Math.max(-85, Math.min(85, centerLat + (dy / globeRadius()) * 50));
      drawGlobe();
    });

    window.addEventListener('pointerup', (e) => {
      if (!isGlobeDragging) return;
      isGlobeDragging = false;
      globeCanvas.classList.remove('dragging');

      // Click check for pin hit
      const rect = globeCanvas.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;

      let nearestTrunk = null;
      let minDist = 22;

      for (const [tid, g] of Object.entries(GEO)) {
        const p = projectGlobe(g.lat, g.lon);
        if (p.z <= 0) continue;
        const dist = Math.hypot(clickX - p.x, clickY - p.y);
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
      globeScale = Math.min(globeScale * 1.18, 1.8);
      drawGlobe();
    });
    document.getElementById('globeZoomOut').addEventListener('click', () => {
      globeScale = Math.max(globeScale / 1.18, 0.65);
      drawGlobe();
    });
    document.getElementById('globeReset').addEventListener('click', () => {
      globeScale = 1.0;
      focusGlobeOnTrunk('node_ie_4');
    });

    function focusGlobeOnTrunk(tid) {
      const g = GEO[tid];
      if (!g) return;

      currentTrunkId = tid;
      targetLat = g.lat;
      targetLon = g.lon;

      // Smooth step to target
      centerLat = targetLat;
      centerLon = targetLon;
      globeRotation = 0;

      updateGeoDossier(tid);
      drawGlobe();
    }

    function updateGeoDossier(tid) {
      const g = GEO[tid] || { nome: "Macro-Família", era: "Histórica", urheimat: "", desc: "", dispersions: [] };
      document.getElementById('geoTrunkTitle').textContent = g.nome;
      document.getElementById('geoTrunkEra').textContent = `⏳ ${g.era}`;
      document.getElementById('geoTrunkUrheimatText').textContent = `${g.urheimat} (${g.lat.toFixed(1)}°, ${g.lon.toFixed(1)}°)`;
      document.getElementById('geoTrunkDesc').textContent = g.desc;

      const listEl = document.getElementById('geoDispersionList');
      let html = '';
      (g.dispersions || []).forEach(d => {
        html += `<span class="dispersion-pill" onclick="centerGlobeOn(${d.lat}, ${d.lon})">📍 ${escapeHtml(d.nome)}</span>`;
      });
      listEl.innerHTML = html;
    }

    window.centerGlobeOn = function(lat, lon) {
      centerLat = lat;
      centerLon = lon;
      globeRotation = 0;
      drawGlobe();
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
        
        let count = 0;
        function countKids(nid) {
          count++;
          for (const c of (NODES[nid]?.children || [])) countKids(c);
        }
        countKids(tid);

        html += `
          <div class="trunk-card" onclick="selectTrunkAndOpenTree('${tid}')">
            <div>
              <div class="trunk-card-header">
                <span class="trunk-card-badge">Macro-Família</span>
                <span style="font-size:12px; color:var(--ink-light);">${count} nós</span>
              </div>
              <h3>${escapeHtml(meta.nome)}</h3>
              <div class="trunk-card-meta">⏳ ${escapeHtml(meta.era)}</div>
              <p class="trunk-card-desc">${escapeHtml(meta.desc)}</p>
            </div>
            <div class="trunk-card-footer">
              <span>📍 ${escapeHtml(meta.urheimat)}</span>
              <span class="trunk-card-action">Explorar Ramo ➔</span>
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
      document.getElementById('treeBannerTitle').textContent = meta.nome;
      document.getElementById('treeBannerEra').textContent = `${meta.era} — ${meta.urheimat || 'Berço Ancestral'}`;

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
          vinesHtml += `<path id="vine_${nid}_${cid}" data-parent="${nid}" data-child="${cid}" class="vine-edge" d="${d}" />`;

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
            ${node.endonym ? `<div class="node-endonym">${escapeHtml(node.endonym)}</div>` : ''}
            ${node.subtitle ? `<div class="node-meta">${escapeHtml(node.subtitle.substring(0, 35))}</div>` : ''}
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
      scale = 0.85;
      updateTreeTransform();

      if (selectedNodeId && positions.has(selectedNodeId)) {
        highlightAncestralSap(selectedNodeId);
      }
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
      const urheimatText = trunkMeta.urheimat || 'Consulte histórico da família';
      const eraText = trunkMeta.era || 'Período Histórico';
      document.getElementById('drawerUrheimat').innerHTML = `<b>Época Estimada:</b> ${eraText}<br><b>Berço de Origem (*Urheimat*):</b> ${urheimatText}`;

      document.getElementById('drawerSynthesis').textContent = 
        `${node.title} constitui um nó fulcral na filogenia das línguas do ramo ${node.trunk_name}. Sua classificação é referenciada nos corpora de Theodor Cole (2026), Glottolog e estudos histórico-comparativos clássicos.`;

      document.getElementById('drawerTypology').textContent = 
        node.is_proto 
          ? "Protolíngua com inventário fonêmico reconstruído pelo método histórico-comparativo rigoroso, exibindo leis fonéticas regulares e correspondências morfológicas estritas com suas descendentes atestadas."
          : (node.is_extinct 
              ? "Língua conservada exclusivamente em registros epigráficos, tábuas de argila, manuscritos clássicos ou tradição litúrgica."
              : "Língua ativa falada por comunidades nativas contemporâneas, com morfossintaxe viva e dialetologia documentada.");

      document.getElementById('drawerSpeakers').textContent = 
        node.subtitle || "Consulte dados etnográficos e censos linguísticos da região.";
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

      scale = 1.0;
      panX = (viewTree.clientWidth / 2) - x * scale - 100;
      panY = (viewTree.clientHeight / 2) - y * scale;
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

    // Filters
    document.querySelectorAll('.filter-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.getAttribute('data-filter');
        applyFilterToView();
      });
    });

    function applyFilterToView() {
      document.querySelectorAll('.node-capsule').forEach(cap => {
        const nid = cap.getAttribute('data-id');
        const node = NODES[nid];
        if (!node) return;

        let visible = true;
        if (activeFilter === 'living' && !node.is_living) visible = false;
        if (activeFilter === 'extinct' && !node.is_extinct) visible = false;
        if (activeFilter === 'proto' && !node.is_proto) visible = false;

        cap.style.opacity = visible ? '1' : '0.2';
      });
    }

    // Tree Pan and Zoom
    function updateTreeTransform() {
      viewportCanvas.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
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

    viewTree.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = 1.12;
      const mouseX = e.clientX;
      const mouseY = e.clientY;

      let newScale = e.deltaY < 0 ? scale * zoomFactor : scale / zoomFactor;
      newScale = Math.min(Math.max(0.2, newScale), 2.2);

      panX = mouseX - (mouseX - panX) * (newScale / scale);
      panY = mouseY - (mouseY - panY) * (newScale / scale);
      scale = newScale;
      updateTreeTransform();
    }, { passive: false });

    document.getElementById('btnZoomIn').addEventListener('click', () => {
      scale = Math.min(scale * 1.25, 2.2);
      updateTreeTransform();
    });

    document.getElementById('btnZoomOut').addEventListener('click', () => {
      scale = Math.max(scale / 1.25, 0.2);
      updateTreeTransform();
    });

    document.getElementById('btnResetView').addEventListener('click', () => {
      panX = 80;
      panY = 100;
      scale = 0.85;
      updateTreeTransform();
    });

    function escapeHtml(str) {
      return (str || '').replace(/[<>&]/g, c => ({'<':'&lt;', '>':'&gt;', '&':'&amp;'}[c]));
    }

    // Window Resize Observer for Globe
    window.addEventListener('resize', () => {
      if (currentView === 'globe') resizeGlobe();
    });

    // Initial Load
    renderCanopy();
    switchView('globe');
    focusGlobeOnTrunk('node_ie_4');
  </script>
</body>
</html>
