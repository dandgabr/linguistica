#!/usr/bin/env python3
"""
Generator for complete linguistic genealogical trees in draw.io format.
Based on Theodor C. H. Cole & E. Siebert-Cole (ResearchGate 2026),
UsefulCharts (Athif Aslam R), and Minna Sundberg's Old World language taxonomy.
"""

import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

# Color palette matching Image 1, 2, and 3:
STYLE_LIVING = "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontColor=#1b4332;fontSize=11;fontFamily=Helvetica;"
STYLE_EXTINCT = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontColor=#5c1d1d;fontSize=11;fontFamily=Helvetica;"
STYLE_BRANCH = "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;fontColor=#1a202c;fontSize=11;fontStyle=1;fontFamily=Helvetica;"
STYLE_FAMILY_HEADER = "rounded=1;whiteSpace=wrap;html=1;fillColor=#2b6cb0;strokeColor=#1a365d;fontColor=#ffffff;fontSize=14;fontStyle=1;fontFamily=Helvetica;shadow=1;"
STYLE_SUBFAMILY_HEADER = "rounded=1;whiteSpace=wrap;html=1;fillColor=#edf2f7;strokeColor=#718096;fontColor=#2d3748;fontSize=12;fontStyle=1;fontFamily=Helvetica;"
STYLE_EDGE = "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#4a5568;strokeWidth=1.5;endArrow=none;"
STYLE_EDGE_ARROW = "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#4a5568;strokeWidth=1.5;endArrow=classic;endSize=4;"
STYLE_CONTAINER = "swimlane;startSize=28;fillColor=#f7fafc;strokeColor=#cbd5e0;fontColor=#2d3748;fontSize=13;fontStyle=1;rounded=1;arcSize=8;collapsible=0;html=1;"

print("Styles initialized successfully.")
