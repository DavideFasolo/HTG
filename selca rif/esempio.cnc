N1      [Tabella fori diametro X
N2      [Totale 28 fori - fori dal <sta> al <end>
N3      [-----------------------
N4      [Immettere valore giri/min S=
N5      P40=?
N6      [Immettere valore avanzamento F=
N7      P41=?
N8      [Immettere valore incremento foratura I=
N9      P42=?
N10     [Immettere quota di fine fori Z=
N11     P43=?
N12     [Immettere quota disimpegno Q=
N13     P44=?
N14     [partenza programma
N14     G17
N15     [Avvio mandrino e impostazione parametri lavorazione
N16     FP41 M03 SP40
N17     [Foratura Tabella N°<num>:
N18     G83 ZP43 IP42 J<z> QP44
N19     X<x> Y<y>
N20     G80 ZP44
N21     G0 Z200
N22     M30