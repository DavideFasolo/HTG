#########################################################################################################
#########################################################################################################
#########################################################################################################
####                                                                                                 ####
####                                   POST PROCESSORE PER HTG                                       ####
####                                    per macchina isograph                                        ####
####                                                                                                 ####
####                                                                                                 ####
####                                      guida ai parametri                                         ####
####                                                                                                 ####
#### Scrivere in fondo al file la riga di foratura desiderata. Il carattere "#"                      ####
#### indica al programma di andare a capo in una nuova riga.                                         ####
####                                                                                                 ####
#### identificatore riga:   solitamente è "N", e rappresenta la prima lettera di ogni riga           ####
####                        esempio: N1 F110 S2000                                                   ####
####                                 N2 X10 Y45                                                      ####
####                                 N3 ...                                                          ####
####                                                                                                 ####
#### incremento riga:       rappresenta il numero di riga dopo l'identificatore                      ####
####                        questo paramentro definisce di quanto il valore aumenta                  ####
####                        per ogni riga                                                            ####
####                                                                                                 ####
#### <z>                                                                                             ####
#### Z di arrivo comune:    quando specificato, sostituisce tutte le coordinate Z dei fori           ####
####                        con questo valore. Rappresenta la coordinata di fine foro.               ####
####                        Inserire un valore per fermare tutti i fori alla stessa coordinata       ####
####                                                                                                 ####
#### <s>                                                                                             ####
#### giri al minuto:        rappresenta la velocità del mandrino per tutti i fori. Viene usata       ####
####                        solo quando "velocita di taglio" è impostata su 0                        ####
####                                                                                                 ####
#### velocita di taglio:    quando diversa da 0, si ignora il valore "giri al minuto". Questo        ####
####                        valore viene usato per calcolare automaticamente i giri in base          ####
####                        al diametro del foro                                                     ####
####                                                                                                 ####
#### i parametri <x> ed <y> rappresentano le coordinate del foro                                     ####
####                                                                                                 ####
#### il parametro <n>       rappresenta il numero del foro specificato sulla tabella allegata alla   ####
####                        messa in tavola del pezzo.                                               ####
####                                                                                                 ####
#### il parametro <d>       rappresenta il diametro del foro                                         ####
####                                                                                                 ####
#########################################################################################################
#########################################################################################################
#########################################################################################################

[generale]
identificatore riga:N
incremento riga:10
Z di arrivo comune:-6.
velocita di taglio:0
giri al minuto:1500

riga di foratura:(foro <n> --->DA SOPRA<---)#F150 M3 S<s> H0 G83 X<x> Y<y> Z250. W0. R1. E<z> D10.#G80