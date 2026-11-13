#!/usr/bin/env python3
import json
import build_organic_data as bod

def generate():
    nodes, edges = bod.load_graph()

    # Incorporar novas famílias autóctones da Oceania (Austrália e Trans-Nova Guiné)
    oceania_nodes = {
        # --- PAMA-NYUNGAN (AUSTRÁLIA) ---
        "node_oceania_pama_nyungan": {
            "id": "node_oceania_pama_nyungan",
            "title": "Proto-Pama-Nyungan",
            "raw_title": "Proto-Pama-Nyungan",
            "subtitle": "c. 3.500–2.500 a.C. · Golfo de Carpentária",
            "endonym": "*Pama-Nyungan",
            "is_extinct": False,
            "is_proto": True,
            "is_living": False,
            "is_branch": False,
            "is_root": False,
            "children": ["node_au_desert", "node_au_arnhem", "node_au_east"],
            "parents": ["node_poster_4"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_au_desert": {
            "id": "node_au_desert",
            "title": "Ramo do Deserto & Ocidente",
            "raw_title": "Ramo do Deserto & Ocidente",
            "subtitle": "Deserto de Tanami e Grande Deserto Ocidental",
            "endonym": "Ngumpin-Yapa / Wati",
            "is_extinct": False,
            "is_proto": False,
            "is_living": False,
            "is_branch": True,
            "is_root": False,
            "children": ["node_warlpiri", "node_pitjantjatjara"],
            "parents": ["node_oceania_pama_nyungan"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_warlpiri": {
            "id": "node_warlpiri",
            "title": "Warlpiri",
            "raw_title": "Warlpiri",
            "subtitle": "~3.000 falantes nativos · NT, Austrália",
            "endonym": "Warlpiri",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_au_desert"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_pitjantjatjara": {
            "id": "node_pitjantjatjara",
            "title": "Pitjantjatjara",
            "raw_title": "Pitjantjatjara",
            "subtitle": "~4.000 falantes nativos · Terras APY, Austrália",
            "endonym": "Pitjantjatjara",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_au_desert"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_au_arnhem": {
            "id": "node_au_arnhem",
            "title": "Ramo Yolŋu-Matha & Norte",
            "raw_title": "Ramo Yolŋu-Matha & Norte",
            "subtitle": "Enclave Pama-Nyungan no Top End",
            "endonym": "Yolŋu-Matha",
            "is_extinct": False,
            "is_proto": False,
            "is_living": False,
            "is_branch": True,
            "is_root": False,
            "children": ["node_yolngu", "node_gunwinyguan"],
            "parents": ["node_oceania_pama_nyungan"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_yolngu": {
            "id": "node_yolngu",
            "title": "Yolŋu (Dhuwal)",
            "raw_title": "Yolŋu (Dhuwal)",
            "subtitle": "~4.500 falantes · Terra de Arnhem, NT",
            "endonym": "Yolŋu-Matha",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_au_arnhem"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_gunwinyguan": {
            "id": "node_gunwinyguan",
            "title": "Gunwinyguan (Não-Pama-Nyungan)",
            "raw_title": "Gunwinyguan (Não-Pama-Nyungan) †",
            "subtitle": "Linhagem autóctone pleistocênica relicta · Arnhem",
            "endonym": "Bininj Gun-wok",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_au_arnhem"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_au_east": {
            "id": "node_au_east",
            "title": "Ramo Oriental & Murray-Darling",
            "raw_title": "Ramo Oriental & Murray-Darling",
            "subtitle": "Costa leste e bacia fluvial sudeste",
            "endonym": "Pama Oriental / Kulin",
            "is_extinct": False,
            "is_proto": False,
            "is_living": False,
            "is_branch": True,
            "is_root": False,
            "children": ["node_dyirbal", "node_wiradjuri"],
            "parents": ["node_oceania_pama_nyungan"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_dyirbal": {
            "id": "node_dyirbal",
            "title": "Dyirbal (†)",
            "raw_title": "Dyirbal †",
            "subtitle": "Célebre sistema de 4 classes nominais · QLD (†)",
            "endonym": "Dyirbal",
            "is_extinct": True,
            "is_proto": False,
            "is_living": False,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_au_east"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },
        "node_wiradjuri": {
            "id": "node_wiradjuri",
            "title": "Wiradjuri",
            "raw_title": "Wiradjuri",
            "subtitle": "Língua em revitalização ativa · NSW, Austrália",
            "endonym": "Wiradjuri",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_au_east"],
            "trunk_id": "node_oceania_pama_nyungan",
            "trunk_name": "Pama-Nyungan (Austrália)"
        },

        # --- TRANS-NOVA GUINÉ (PAPUA) ---
        "node_oceania_trans_new_guinea": {
            "id": "node_oceania_trans_new_guinea",
            "title": "Proto-Trans-Nova Guiné",
            "raw_title": "Proto-Trans-Nova Guiné",
            "subtitle": "c. 4.000–2.500 a.C. · Terras Altas de Papua (Kuk Swamp)",
            "endonym": "*Trans-New Guinea",
            "is_extinct": False,
            "is_proto": True,
            "is_living": False,
            "is_branch": False,
            "is_root": False,
            "children": ["node_tng_highland", "node_tng_lowland"],
            "parents": ["node_poster_4"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        },
        "node_tng_highland": {
            "id": "node_tng_highland",
            "title": "Ramo das Terras Altas (Highlands)",
            "raw_title": "Ramo das Terras Altas (Highlands)",
            "subtitle": "Cordilheira central e vales Wahgi/Asaro",
            "endonym": "Engan / Chimbu-Wahgi",
            "is_extinct": False,
            "is_proto": False,
            "is_living": False,
            "is_branch": True,
            "is_root": False,
            "children": ["node_enga", "node_melpa", "node_dani"],
            "parents": ["node_oceania_trans_new_guinea"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        },
        "node_enga": {
            "id": "node_enga",
            "title": "Enga",
            "raw_title": "Enga",
            "subtitle": "~250.000 falantes (maior língua de PNG) · Terras Altas",
            "endonym": "Enga",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_tng_highland"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        },
        "node_melpa": {
            "id": "node_melpa",
            "title": "Melpa (Hagen)",
            "raw_title": "Melpa (Hagen)",
            "subtitle": "~130.000 falantes · Vale do Wahgi / Monte Hagen",
            "endonym": "Melpa",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_tng_highland"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        },
        "node_dani": {
            "id": "node_dani",
            "title": "Dani Ocidental (Grand Valley)",
            "raw_title": "Dani Ocidental (Grand Valley)",
            "subtitle": "~270.000 falantes · Vale de Baliem, Papua Ocidental",
            "endonym": "Dani",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_tng_highland"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        },
        "node_tng_lowland": {
            "id": "node_tng_lowland",
            "title": "Ramo das Planícies & Insular",
            "raw_title": "Ramo das Planícies & Insular",
            "subtitle": "Sul pantanoso da Nova Guiné e Timor-Alor-Pantar",
            "endonym": "Asmat-Kamoro / Timor-Alor",
            "is_extinct": False,
            "is_proto": False,
            "is_living": False,
            "is_branch": True,
            "is_root": False,
            "children": ["node_asmat", "node_makasae"],
            "parents": ["node_oceania_trans_new_guinea"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        },
        "node_asmat": {
            "id": "node_asmat",
            "title": "Asmat",
            "raw_title": "Asmat",
            "subtitle": "~50.000 falantes · Manguezais e planícies do litoral sul",
            "endonym": "Asmat",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_tng_lowland"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        },
        "node_makasae": {
            "id": "node_makasae",
            "title": "Makasae",
            "raw_title": "Makasae",
            "subtitle": "~130.000 falantes · Timor-Leste (Ramo Papuano Ocidental)",
            "endonym": "Makasae",
            "is_extinct": False,
            "is_proto": False,
            "is_living": True,
            "is_branch": False,
            "is_root": False,
            "children": [],
            "parents": ["node_tng_lowland"],
            "trunk_id": "node_oceania_trans_new_guinea",
            "trunk_name": "Trans-Nova Guiné (Papua)"
        }
    }

    # Mesclar nós da Oceania no catálogo e na raiz geral
    nodes.update(oceania_nodes)
    if 'node_poster_4' in nodes:
        for tid in ["node_oceania_pama_nyungan", "node_oceania_trans_new_guinea"]:
            if tid not in nodes['node_poster_4']['children']:
                nodes['node_poster_4']['children'].append(tid)

    # Associate each node with its trunk
    trunks = list(bod.TRUNK_META.keys())
    
    node_to_trunk = {}
    
    def assign_trunk(nid, current_trunk):
        node_to_trunk[nid] = current_trunk
        for c in nodes[nid]['children']:
            assign_trunk(c, current_trunk)
            
    for tid in trunks:
        if tid in nodes:
            assign_trunk(tid, tid)
            
    node_to_trunk['node_poster_4'] = 'node_poster_4'
    
    # Compute ancestor path for each node
    ancestors_map = {}
    
    def get_ancestors(nid):
        if nid in ancestors_map:
            return ancestors_map[nid]
        pars = nodes[nid]['parents']
        if not pars:
            ancestors_map[nid] = [nid]
            return [nid]
        p = pars[0]
        res = get_ancestors(p) + [nid]
        ancestors_map[nid] = res
        return res
        
    for nid in nodes:
        get_ancestors(nid)
        
    # Build clean serializable node payload
    clean_nodes = {}
    for nid, n in nodes.items():
        t_id = node_to_trunk.get(nid, 'node_poster_4')
        t_meta = bod.TRUNK_META.get(t_id, {})
        t_name = t_meta.get('nome', 'Geral')
        
        clean_nodes[nid] = {
            "id": nid,
            "title": n['title'],
            "raw": n['raw_title'],
            "subtitle": n['subtitle'],
            "endonym": n['endonym'],
            "is_extinct": n['is_extinct'],
            "is_proto": n['is_proto'],
            "is_living": n['is_living'],
            "is_branch": n['is_branch'],
            "is_root": n['is_root'],
            "children": n['children'],
            "parents": n['parents'],
            "ancestors": ancestors_map.get(nid, [nid]),
            "trunk_id": t_id,
            "trunk_name": t_name
        }

    print(f"Serialized {len(clean_nodes)} clean nodes.")
    return clean_nodes, bod.TRUNK_META

if __name__ == '__main__':
    generate()
