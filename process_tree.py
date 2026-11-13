#!/usr/bin/env python3
import json
import build_organic_data as bod

def generate():
    nodes, edges = bod.load_graph()
    
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
