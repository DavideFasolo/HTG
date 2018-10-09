def esporta_csv(fori,f,separ,virgo):
    exf=f+"csv"
    out_excel = open(exf,"w+")
    out_excel.write('Pos;Diam;X;Y;Z\n')
    i=0
    while i<len(fori):
        stringaforo=str(fori[i][0])+separ+str(fori[i][1])+separ+str(fori[i][2])+separ+str(fori[i][3])
        stringaforo=stringaforo.replace(".",virgo)
        out_excel.write(str(i+1)+separ+stringaforo+"\n")
        i+=1
    out_excel.close()
    print("Creato il file \n"+exf+"\n"+"Nella cartella dove si trova il file vda selezionato")
