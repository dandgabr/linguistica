#!/usr/bin/env python3
import json
import build_geo_data as geo

with open('landmasses.json', 'r') as f:
    LANDMASSES = json.load(f)

TRUNKS = geo.TRUNK_GEO

HTML = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Herbário Linguístico — Globo Botânico Interativo</title>
  <style>
    :root {
      --bg-linen: #F7F4EB;
      --bg-surface: #FFFFFF;
      --bg-subtle: #EFE9DC;
      --border-warm: #E2D9C8;
      --ink-deep: #1B3524;
      --ink-muted: #5C6B5F;
      --moss: #2E7D32;
      --leaf: #5F8769;
      --sap: #D97706;
      --terracotta: #B91C1C;
      --proto: #1D4ED8;
      --font-serif: Georgia, "Baskerville", "Palatino Linotype", serif;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    * { box-sizing: border-box; }
    body { margin:0; height:100vh; overflow:hidden; background:var(--bg-linen); color:var(--ink-deep); font-family:var(--font-sans); display:flex; flex-direction:column; }
    header { padding:12px 22px; border-bottom:1px solid var(--border-warm); background:rgba(247,244,235,.96); display:flex; justify-content:space-between; align-items:center; gap:14px; z-index:5; }
    header h1 { font:700 20px var(--font-serif); margin:0; }
    header p { margin:3px 0 0; font-size:11px; color:var(--ink-muted); }
    .top-actions { display:flex; gap:9px; align-items:center; }
    button { cursor:pointer; font:600 12px var(--font-sans); color:var(--ink-deep); background:var(--bg-surface); border:1px solid var(--border-warm); padding:8px 12px; border-radius:999px; transition:transform .2s, background .2s; }
    button:hover { background:var(--bg-subtle); transform:translateY(-1px); }
    input { width:230px; padding:9px 13px; border-radius:999px; border:1px solid var(--border-warm); outline:none; color:var(--ink-deep); background:#fff; }
    input:focus { border-color:var(--moss); box-shadow:0 0 0 3px #2e7d3222; }
    main { display:grid; grid-template-columns:minmax(380px, 45%) 1fr; gap:0; min-height:0; flex:1; }
    #globePane { position:relative; display:flex; align-items:center; justify-content:center; overflow:hidden; border-right:1px solid var(--border-warm); background:radial-gradient(ellipse at center,#fffdf8 0%,#f4eedf 68%,#efe8d8 100%); }
    #globeCanvas { width:min(90%,680px); aspect-ratio:1; touch-action:none; cursor:grab; }
    #globeCanvas.dragging { cursor:grabbing; }
    .globe-caption { position:absolute; left:22px; bottom:18px; font:italic 13px var(--font-serif); color:var(--ink-muted); }
    .globe-hud { position:absolute; top:18px; left:18px; display:flex; gap:6px; }
    .globe-hud button { width:35px; height:35px; padding:0; border-radius:50%; font-size:16px; }
    #canopyPane { min-height:0; display:flex; flex-direction:column; overflow:hidden; }
    .canopy-head { padding:20px 22px 12px; border-bottom:1px solid var(--border-warm); background:#fffdf9; }
    .canopy-head h2 { font:700 22px var(--font-serif); margin:0 0 5px; }
    .canopy-head p { font-size:12px; color:var(--ink-muted); margin:0; line-height:1.5; }
    #trunkList { padding:14px 16px 30px; overflow:auto; display:grid; grid-template-columns:repeat(auto-fill,minmax(245px,1fr)); gap:11px; align-content:start; }
    .trunk-card { background:var(--bg-surface); border:1px solid var(--border-warm); border-radius:15px 18px 14px 19px; padding:14px; cursor:pointer; transition:transform .2s cubic-bezier(.16,1,.3,1),box-shadow .2s,border-color .2s; }
    .trunk-card:hover,.trunk-card.selected { border-color:var(--moss); transform:translateY(-2px); box-shadow:0 7px 20px #2c3a2412; }
    .trunk-card h3 { font:700 17px var(--font-serif); margin:0 0 5px; }
    .trunk-card .era { color:#9A5707; font-size:11px; font-weight:700; margin-bottom:5px; }
    .trunk-card .home { color:var(--ink-muted); font-size:11px; line-height:1.4; }
    .trunk-card .desc { color:#354b3c; font-size:12px; line-height:1.45; margin-top:8px; }
    #geoDrawer { position:absolute; left:16px; top:16px; width:min(330px,calc(100% - 32px)); background:#fffdf8f2; backdrop-filter:blur(10px); border:1px solid var(--border-warm); border-radius:17px 20px 16px 21px; box-shadow:0 8px 28px #25291b18; padding:15px; z-index:2; transform:translateX(calc(-100% - 28px)); transition:transform .35s cubic-bezier(.16,1,.3,1); }
    #geoDrawer.open { transform:translateX(0); }
    #geoDrawer h3 { font:700 20px var(--font-serif); margin:0 28px 6px 0; }
    #geoDrawer .close { position:absolute; right:10px; top:8px; border:0; background:transparent; font-size:22px; padding:4px 9px; }
    #geoDrawer .geo-meta { color:#9A5707; font-size:12px; font-weight:700; margin-bottom:5px; }
    #geoDrawer .geo-home { font:italic 14px var(--font-serif); margin-bottom:9px; }
    #geoDrawer .geo-desc { color:#354b3c; line-height:1.5; font-size:12px; }
    #geoDrawer .geo-count { color:var(--ink-muted); font-size:11px; margin-top:10px; padding-top:8px; border-top:1px solid var(--border-warm); }
    .legend { position:absolute; right:15px; bottom:15px; display:flex; gap:10px; flex-wrap:wrap; font-size:10px; color:var(--ink-muted); background:#fffdf8e8; border:1px solid var(--border-warm); padding:8px 10px; border-radius:13px; }
    .legend span { display:flex; align-items:center; gap:4px; }
    .dot { width:8px; height:8px; border-radius:50%; display:inline-block; }
    #mobileTab { display:none; }
    @media (max-width:850px) {
      header { padding:10px 13px; flex-wrap:wrap; }
      header h1 { font-size:17px; }
      .top-actions { width:100%; justify-content:space-between; }
      input { width:min(54vw,280px); }
      main { display:flex; flex-direction:column; }
      #globePane { flex:1; border-right:0; min-height:300px; }
      #canopyPane { height:45vh; border-top:1px solid var(--border-warm); }
      #trunkList { grid-template-columns:repeat(auto-fill,minmax(210px,1fr)); }
      .globe-caption { bottom:7px; left:12px; font-size:11px; }
      .legend { bottom:8px; right:8px; }
    }
    @media (prefers-reduced-motion:reduce) { *,*::before,*::after { animation-duration:.01ms!important; transition-duration:.01ms!important; } }
  </style>
</head>
<body>
  <header>
    <div><h1>Herbário Filogenético das Línguas</h1><p>Um dossel botânico sobre o globo — raízes, dispersões e famílias linguísticas</p></div>
    <div class="top-actions"><input id="search" type="search" placeholder="Buscar tronco ou região…" aria-label="Buscar tronco linguístico"><button id="resetGlobe" type="button">◎ Recentrar globo</button><button id="homeView" type="button">Dossel</button></div>
  </header>
  <main>
    <section id="globePane" aria-label="Globo geográfico interativo">
      <canvas id="globeCanvas" aria-label="Globo 3D rotativo. Arraste para girar; selecione um marcador para detalhes." role="img"></canvas>
      <div class="globe-hud"><button id="zoomIn" aria-label="Aumentar globo">+</button><button id="zoomOut" aria-label="Diminuir globo">−</button></div>
      <div class="globe-caption">Arraste o globo · selecione um broto para explorar</div>
      <aside id="geoDrawer" aria-live="polite"><button class="close" aria-label="Fechar dossiê">×</button><h3></h3><div class="geo-meta"></div><div class="geo-home"></div><div class="geo-desc"></div><div class="geo-count"></div></aside>
      <div class="legend"><span><i class="dot" style="background:#D97706"></i> Berço ancestral</span><span><i class="dot" style="background:#2E7D32"></i> Dispersão</span></div>
    </section>
    <section id="canopyPane">
      <div class="canopy-head"><h2>Dossel dos troncos</h2><p>Escolha uma família para recentrar o globo. O ponto dourado marca o *Urheimat*; os arcos verdes mostram dispersões históricas selecionadas.</p></div>
      <div id="trunkList"></div>
    </section>
  </main>
  <script>
    const TRUNKS = __TRUNKS__;
    const LAND = __LAND__;
    const canvas = document.getElementById('globeCanvas');
    const ctx = canvas.getContext('2d');
    const list = document.getElementById('trunkList');
    const drawer = document.getElementById('geoDrawer');
    const search = document.getElementById('search');
    const order = Object.keys(TRUNKS);
    const entries = order.map(id => ({id, ...TRUNKS[id]}));
    let selected = null, centerLat = 25, centerLon = 15, rotation = 0, scale = 1, dragging = false, lastX = 0, lastY = 0;
    let pointer = {x:0,y:0};
    const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    function resize() {
      const r = canvas.getBoundingClientRect();
      const dpr = Math.min(devicePixelRatio || 1, 2);
      canvas.width = Math.max(1, Math.round(r.width*dpr)); canvas.height = Math.max(1, Math.round(r.height*dpr));
      ctx.setTransform(dpr,0,0,dpr,0,0); draw();
    }
    function radius() { return Math.min(canvas.clientWidth,canvas.clientHeight)*.44*scale; }
    function project(lat,lon) {
      const phi=lat*Math.PI/180, lam=lon*Math.PI/180, phi0=centerLat*Math.PI/180, lam0=centerLon*Math.PI/180+rotation;
      const dl=lam-lam0, z=Math.sin(phi0)*Math.sin(phi)+Math.cos(phi0)*Math.cos(phi)*Math.cos(dl);
      const r=radius(), x=r*Math.cos(phi)*Math.sin(dl), y=-r*(Math.cos(phi0)*Math.sin(phi)-Math.sin(phi0)*Math.cos(phi)*Math.cos(dl));
      return {x:canvas.clientWidth/2+x,y:canvas.clientHeight/2+y,z};
    }
    function pathCoords(points, close=false) {
      let d='', active=false;
      for(let i=0;i<points.length;i++) {
        const p=project(points[i][0],points[i][1]);
        if(p.z>0) { d+=(active?'L':'M')+p.x.toFixed(1)+' '+p.y.toFixed(1)+' '; active=true; }
        else active=false;
      }
      return active&&close ? d+'Z' : d;
    }
    function drawGrid() {
      ctx.strokeStyle='#CDBFA8'; ctx.lineWidth=.65;
      for(let lat=-60;lat<=75;lat+=15) {
        ctx.beginPath(); let active=false;
        for(let lon=-180;lon<=180;lon+=3) { const p=project(lat,lon); if(p.z>0) { if(!active) ctx.moveTo(p.x,p.y); else ctx.lineTo(p.x,p.y); active=true; } else active=false; }
        ctx.stroke();
      }
      for(let lon=-180;lon<180;lon+=15) {
        ctx.beginPath(); let active=false;
        for(let lat=-90;lat<=90;lat+=3) { const p=project(lat,lon); if(p.z>0) { if(!active) ctx.moveTo(p.x,p.y); else ctx.lineTo(p.x,p.y); active=true; } else active=false; }
        ctx.stroke();
      }
    }
    function drawLand() {
      for(const poly of LAND) {
        ctx.beginPath(); let active=false;
        for(const point of poly) { const p=project(point[0],point[1]); if(p.z>0) { if(!active) ctx.moveTo(p.x,p.y); else ctx.lineTo(p.x,p.y); active=true; } else active=false; }
        if(active) { ctx.closePath(); ctx.fillStyle='#9BAF91'; ctx.fill(); ctx.strokeStyle='#70856D'; ctx.lineWidth=1; ctx.stroke(); }
      }
    }
    function drawArcs(entry) {
      if(!entry) return;
      const root=project(entry.lat,entry.lon);
      if(root.z<=0) return;
      for(const dest of entry.dispersions) {
        ctx.beginPath();
        const end=project(dest.lat,dest.lon);
        // Sample a spherical interpolation to trace a great-circle-like migration arc.
        const a=toVec(entry.lat,entry.lon), b=toVec(dest.lat,dest.lon), dot=Math.max(-1,Math.min(1,a[0]*b[0]+a[1]*b[1]+a[2]*b[2])), omega=Math.acos(dot);
        let active=false;
        for(let i=0;i<=40;i++) {
          const t=i/40, v=omega<1e-6?a:a.map((x,k)=>Math.sin((1-t)*omega)/Math.sin(omega)*x+Math.sin(t*omega)/Math.sin(omega)*b[k]);
          const lat=Math.asin(v[2])*180/Math.PI, lon=Math.atan2(v[1],v[0])*180/Math.PI, p=project(lat,lon);
          if(p.z>0) { if(!active) ctx.moveTo(p.x,p.y); else ctx.lineTo(p.x,p.y); active=true; } else active=false;
        }
        ctx.strokeStyle='rgba(46,125,50,.56)'; ctx.lineWidth=1.5; ctx.setLineDash([3,4]); ctx.stroke(); ctx.setLineDash([]);
        if(end.z>0) { ctx.beginPath(); ctx.arc(end.x,end.y,3.2,0,Math.PI*2); ctx.fillStyle='#2E7D32'; ctx.fill(); }
      }
    }
    function toVec(lat,lon) { const p=lat*Math.PI/180,l=lon*Math.PI/180; return [Math.cos(p)*Math.cos(l),Math.cos(p)*Math.sin(l),Math.sin(p)]; }
    function drawMarkers() {
      for(const e of entries) {
        const p=project(e.lat,e.lon); if(p.z<=0) continue;
        const chosen=selected===e.id, r=chosen?7:5;
        if(chosen) { ctx.beginPath(); ctx.arc(p.x,p.y,15,0,Math.PI*2); ctx.fillStyle='rgba(217,119,6,.14)'; ctx.fill(); }
        ctx.beginPath(); ctx.arc(p.x,p.y,r,0,Math.PI*2); ctx.fillStyle=chosen?'#D97706':'#6A8C5A'; ctx.fill(); ctx.strokeStyle='#fffdf8'; ctx.lineWidth=1.7; ctx.stroke();
        if(chosen) { ctx.font='600 11px sans-serif'; ctx.fillStyle='#1B3524'; ctx.fillText(e.nome,p.x+9,p.y-8); }
      }
    }
    function draw() {
      if(!ctx || !canvas.clientWidth) return;
      const w=canvas.clientWidth,h=canvas.clientHeight; ctx.clearRect(0,0,w,h);
      const r=radius(); ctx.save(); ctx.beginPath(); ctx.arc(w/2,h/2,r,0,Math.PI*2); ctx.clip();
      const grad=ctx.createRadialGradient(w*.42,h*.38,r*.04,w/2,h/2,r*1.15); grad.addColorStop(0,'#F5F0E4'); grad.addColorStop(1,'#DAD0BC'); ctx.fillStyle=grad; ctx.fillRect(w/2-r,h/2-r,r*2,r*2);
      drawGrid(); drawLand(); drawArcs(selected?TRUNKS[selected]:null); drawMarkers();
      ctx.restore(); ctx.beginPath(); ctx.arc(w/2,h/2,r,0,Math.PI*2); ctx.strokeStyle='#63775A'; ctx.lineWidth=1.6; ctx.stroke();
      // Soft highlight for an organic globe surface.
      const shine=ctx.createRadialGradient(w*.34,h*.27,0,w*.34,h*.27,r*.9); shine.addColorStop(0,'rgba(255,255,255,.27)'); shine.addColorStop(1,'rgba(255,255,255,0)'); ctx.beginPath(); ctx.arc(w/2,h/2,r,0,Math.PI*2); ctx.fillStyle=shine; ctx.fill();
    }
    function renderCards() {
      list.innerHTML=entries.map(e=>`<article class="trunk-card" data-id="${e.id}" tabindex="0" role="button" aria-label="Explorar ${escapeHtml(e.nome)}"><h3>${escapeHtml(e.nome)}</h3><div class="era">${escapeHtml(e.era)}</div><div class="home">${escapeHtml(e.urheimat)}</div><p class="desc">${escapeHtml(e.desc)}</p></article>`).join('');
      list.querySelectorAll('.trunk-card').forEach(card=>{ card.addEventListener('click',()=>selectTrunk(card.dataset.id)); card.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();selectTrunk(card.dataset.id);}}); });
    }
    function selectTrunk(id) {
      if(!TRUNKS[id]) return; selected=id; const e=TRUNKS[id]; centerLat=e.lat; centerLon=e.lon; rotation=0;
      list.querySelectorAll('.trunk-card').forEach(c=>c.classList.toggle('selected',c.dataset.id===id));
      drawer.querySelector('h3').textContent=e.nome; drawer.querySelector('.geo-meta').textContent=e.era; drawer.querySelector('.geo-home').textContent=e.urheimat; drawer.querySelector('.geo-desc').textContent=e.desc; drawer.querySelector('.geo-count').textContent=`${e.dispersions.length} áreas de dispersão selecionadas · Coordenadas do berço: ${e.lat.toFixed(1)}°, ${e.lon.toFixed(1)}°`;
      drawer.classList.add('open'); draw();
    }
    function escapeHtml(s) { return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
    function screenPos(e) { const r=canvas.getBoundingClientRect(); return {x:e.clientX-r.left,y:e.clientY-r.top}; }
    function hitTest(pos) {
      let best=null,dist=Infinity;
      for(const e of entries) { const p=project(e.lat,e.lon); if(p.z<=0) continue; const d=Math.hypot(pos.x-p.x,pos.y-p.y); if(d<dist){dist=d;best=e;} }
      return dist<18?best:null;
    }
    canvas.addEventListener('pointerdown',e=>{dragging=true; lastX=e.clientX; lastY=e.clientY; pointer=screenPos(e); canvas.classList.add('dragging'); canvas.setPointerCapture(e.pointerId);});
    canvas.addEventListener('pointermove',e=>{
      if(!dragging) return;
      const dx=e.clientX-lastX, dy=e.clientY-lastY; lastX=e.clientX; lastY=e.clientY;
      rotation-=dx/(radius())*.75; centerLat=Math.max(-85,Math.min(85,centerLat+dy/(radius())*55)); draw();
    });
    canvas.addEventListener('pointerup',e=>{ if(!dragging)return; dragging=false; canvas.classList.remove('dragging'); const p=screenPos(e); if(Math.hypot(e.clientX-lastX,e.clientY-lastY)<5){const hit=hitTest(p);if(hit)selectTrunk(hit.id);} });
    canvas.addEventListener('pointercancel',()=>{dragging=false;canvas.classList.remove('dragging');});
    canvas.addEventListener('wheel',e=>{e.preventDefault();scale=Math.max(.72,Math.min(1.5,scale*(e.deltaY<0?1.08:.92)));resize();},{passive:false});
    document.getElementById('zoomIn').addEventListener('click',()=>{scale=Math.min(1.5,scale*1.15);resize();});
    document.getElementById('zoomOut').addEventListener('click',()=>{scale=Math.max(.72,scale/1.15);resize();});
    document.getElementById('resetGlobe').addEventListener('click',()=>{centerLat=25;centerLon=15;rotation=0;scale=1;draw();});
    document.getElementById('homeView').addEventListener('click',()=>{drawer.classList.remove('open'); selected=null; list.querySelectorAll('.trunk-card').forEach(c=>c.classList.remove('selected'));draw();});
    drawer.querySelector('.close').addEventListener('click',()=>drawer.classList.remove('open'));
    search.addEventListener('input',()=>{const q=search.value.trim().toLocaleLowerCase('pt-BR'); list.querySelectorAll('.trunk-card').forEach(c=>{const e=TRUNKS[c.dataset.id];c.hidden=!!q&&!(`${e.nome} ${e.urheimat} ${e.desc}`.toLocaleLowerCase('pt-BR').includes(q));});});
    new ResizeObserver(resize).observe(canvas);
    renderCards(); resize();
  </script>
</body>
</html>'''

with open('arvore_interativa_globo.html', 'w', encoding='utf-8') as f:
    f.write(HTML.replace('__TRUNKS__', json.dumps(TRUNKS, ensure_ascii=False)).replace('__LAND__', json.dumps(LANDMASSES, ensure_ascii=False)))
print('arvore_interativa_globo.html generated')
