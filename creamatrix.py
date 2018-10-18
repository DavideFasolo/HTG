def leggivda(in_file, arrot):
    # importa variabili di configurazione
    in_file.seek(0, 0)
    # salta le prime 21 righe
    i = 21
    while i > 0:
        text = in_file.readline()
        i -= 1
    #############################
    text = in_file.readlines()
    in_file.close()
    fori = list()
    i = 0
    totcer = 0
    totcur = 0
    totpun = 0
    while i < len(text):
        if text[i].count("CIRCLE /") + text[i].count("CIRCLE/"):
            foro = text[i][0:72].strip()
            g = 1
            while foro.count(",") <= 11 and foro[len(foro) - 1] == ",":
                foro += text[i + g][0:72].strip()
                g += 1
            foro = foro[foro.find("/") + 1:len(foro)].split(",")
            foro = [round(float(foro[3]), arrot) * 2, round(float(foro[0]), arrot), round(float(foro[1]), arrot),
                    round(float(foro[2]), arrot)]
            fori.append(foro)
            totcer += 1
        i += 1
    # trova duplicati
    univoci = [x for n, x in enumerate(fori) if x not in fori[:n]]
    totdup = len(fori) - len(univoci)
    fori = univoci
    totcer = len(fori)
    fori.sort()
    i = 0
    while i < len(text):
        if text[i].count("CURVE /") + text[i].count("CURVE/"):
            totcur += 1
        i += 1
    i = 0
    while i < len(text):
        if text[i].count("POINT /") + text[i].count("POINT/"):
            totpun += 1
        i += 1

    messaggio = "Sono stati trovati:\n"
    if totcer > 0:
        messaggio += str(totcer) + " archi (più altri " + str(totdup) + " duplicati ignorati) processati come fori\n"
    if totcur > 0:
        messaggio += str(totcur) + " linee e/o curve ignorate\n"
    if totpun > 0:
        messaggio += str(totpun) + " punti ignorati\n"

    print(messaggio)
    #################

    return fori
