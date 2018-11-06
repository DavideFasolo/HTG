N1 [
N2 [Fori Ø6.0
N3 [
N4 [----------
N5 [[
N6 [Fori Ø6.0
N7 [
N8 [Richiesta parametri
N9 [
N10 P40=1500    [Immettere valore giri/min S=
N11 P41=1000    [Immettere valore avanzamento F=
N12 P42=3    [Immettere valore incremento foratura I=
N13 P43=-40    [Immettere quota di arrivo a fine foro Z=
N14 P44=200    [Immettere quota di disompegno Q=
N15 [
N16 [Inizio programma
N17 [
N18 G17
N19 FP41 M03 SP40
N20 [
N21 [foro 1 da tabella disegno
N22 [
N23 G83 ZP43 IP42 J-15.777 QP44
N24 X-51.655 Y83.781
N25 G80 ZP44
N26 [
N27 [foro 2 da tabella disegno
N28 [
N29 G83 ZP43 IP42 J-3.655 QP44
N30 X-33.943 Y83.781
N31 G80 ZP44
N32 [
N33 [foro 3 da tabella disegno
N34 [
N35 G83 ZP43 IP42 J-3.655 QP44
N36 X33.277 Y83.781
N37 G80 ZP44
N38 [
N39 [foro 4 da tabella disegno
N40 [
N41 G83 ZP43 IP42 J-15.777 QP44
N42 X50.989 Y83.781
N43 G80 ZP44
N44 G0 Z200.0
N45 M30
