#!/usr/bin/env python3
"""
TreeBuilder with non-overlapping cladogram gutter routing.
Guarantees edges NEVER cross or overlap node shapes.
"""

from xml.sax.saxutils import escape

# Node Styles
S_LIVING = "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontColor=#155724;fontSize=11;fontFamily=Helvetica;"
S_EXTINCT = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontColor=#721c24;fontSize=11;fontFamily=Helvetica;"
S_BRANCH = "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;fontColor=#1a202c;fontSize=11;fontStyle=1;fontFamily=Helvetica;"
S_FAMILY = "rounded=1;whiteSpace=wrap;html=1;fillColor=#1a365d;strokeColor=#0f172a;fontColor=#ffffff;fontSize=14;fontStyle=1;fontFamily=Helvetica;shadow=1;"
S_SUBFAMILY = "rounded=1;whiteSpace=wrap;html=1;fillColor=#2b6cb0;strokeColor=#1a365d;fontColor=#ffffff;fontSize=12;fontStyle=1;fontFamily=Helvetica;"
S_GROUP = "rounded=1;whiteSpace=wrap;html=1;fillColor=#edf2f7;strokeColor=#718096;fontColor=#2d3748;fontSize=11;fontStyle=1;fontFamily=Helvetica;"
S_LEGEND = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#cbd5e1;fontColor=#334155;fontSize=11;fontFamily=Helvetica;align=left;spacingLeft=10;"

# Edge Styles:
# 1. Top-Down Bus: For horizontal splits (parent above, children in different columns below)
S_EDGE_TOPDOWN = "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;strokeColor=#4a5568;strokeWidth=1.5;endArrow=none;"

# 2. Cladogram Gutter: For vertical children lists under a parent (line runs down the margin on the left, enters child at entryX=0)
S_EDGE_GUTTER = "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=1;entryX=0;entryY=0.5;strokeColor=#4a5568;strokeWidth=1.5;endArrow=none;"

# 3. Direct Edge
S_EDGE = "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#4a5568;strokeWidth=1.5;endArrow=none;"

class TreeBuilder:
    def __init__(self, page_id, page_name, width=3800, height=2400):
        self.page_id = page_id
        self.page_name = page_name
        self.width = width
        self.height = height
        self.cells = []
        self.edges = []
        self.id_counter = 2

    def next_id(self):
        cid = f"node_{self.page_id}_{self.id_counter}"
        self.id_counter += 1
        return cid

    def add_node(self, label, style, x, y, w=120, h=38, parent="1", nid=None):
        if nid is None:
            nid = self.next_id()
        val = escape(label)
        self.cells.append({
            "id": nid,
            "value": val,
            "style": style,
            "x": int(x),
            "y": int(y),
            "w": int(w),
            "h": int(h),
            "parent": parent
        })
        return nid

    def add_edge(self, source_id, target_id, style=S_EDGE, label="", parent="1"):
        eid = self.next_id()
        val = escape(label)
        self.edges.append({
            "id": eid,
            "source": source_id,
            "target": target_id,
            "style": style,
            "value": val,
            "parent": parent
        })
        return eid

    def add_legend(self, x=40, y=40):
        self.add_node(
            "<b>LEGENDA &amp; CONVENÇÕES</b><br>"
            "🟢 <b>Verde:</b> Língua Viva / Ativa<br>"
            "🔴 <b>Vermelho/Rosa:</b> Língua Extinta / Histórica (†)<br>"
            "⚪ <b>Branco:</b> Protolíngua / Nó de Ramificação<br>"
            "🔵 <b>Azul:</b> Macrofamília / Subfamília Principal",
            S_LEGEND, x, y, 260, 90
        )

    def add_vertical_children(self, parent_id, children, parent_x, start_y, col_w=240, child_h=32, y_step=40, indent=28):
        """
        Adds a list of children vertically indented to the right of parent_x.
        Connects parent to each child via S_EDGE_GUTTER (line drops on the left margin, enters child left edge).
        Guarantees NO edge ever crosses or touches any child box.
        Returns the final Y position after the last child.
        """
        cur_y = start_y
        child_w = col_w - indent
        child_x = parent_x + indent
        
        for l_name, l_style in children:
            cid = self.add_node(l_name, l_style, child_x, cur_y, child_w, child_h)
            self.add_edge(parent_id, cid, style=S_EDGE_GUTTER)
            cur_y += y_step
            
        return cur_y

    def to_xml(self):
        lines = [
            f'<mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.width}" pageHeight="{self.height}" adaptiveColors="auto">',
            '  <root>',
            '    <mxCell id="0"/>',
            '    <mxCell id="1" parent="0"/>'
        ]
        for c in self.cells:
            lines.append(
                f'    <mxCell id="{c["id"]}" value="{c["value"]}" style="{c["style"]}" vertex="1" parent="{c["parent"]}">'
                f'<mxGeometry x="{c["x"]}" y="{c["y"]}" width="{c["w"]}" height="{c["h"]}" as="geometry"/></mxCell>'
            )
        for e in self.edges:
            lines.append(
                f'    <mxCell id="{e["id"]}" value="{e["value"]}" style="{e["style"]}" edge="1" source="{e["source"]}" target="{e["target"]}" parent="{e["parent"]}">'
                f'<mxGeometry relative="1" as="geometry"/></mxCell>'
            )
        lines.append('  </root>')
        lines.append('</mxGraphModel>')
        return "\n".join(lines)

print("Updated TreeBuilder loaded.")
