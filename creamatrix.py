def leggivda(file, arrot):
    text = file.jump_and_read()
    fori = list()
    totcur = 0
    totpun = 0
    i = 0
    while i < len(text):
        line = text[i]
        if "CIRCLE /" in line or "CIRCLE/" in line:
            complete_line = line[line.find("/") + 1:-8].strip()
            while complete_line.count(",") <= 11 and complete_line[:-1] == ",":
                i += 1
                complete_line += text[i][:-8].strip()
            numbers = complete_line.split(",")
            fori.append((
                round(float(numbers[3]), arrot) * 2,
                round(float(numbers[0]), arrot),
                round(float(numbers[1]), arrot),
                round(float(numbers[2]), arrot)))
        if "CURVE /" in line or "CURVE/" in line:
            totcur += 1
        if "POINT /" in line or "POINT/" in line:
            totpun += 1
        i += 1
    # trova duplicati
    unique = [foro for counter, foro in enumerate(fori) if foro not in fori[:counter]]
    unique.sort()

    messaggio = "Sono stati trovati:\n"
    if len(fori) > 0:
        messaggio += "{0} archi (più altri {1} duplicati ignorati) processati come fori\n"\
            .format(len(unique), len(fori) - len(unique))
    if totcur > 0:
        messaggio += "{0} linee e/o curve ignorate\n".format(totcur)
    if totpun > 0:
        messaggio += "{0} punti ignorati\n".format(totpun)

    print(messaggio)

    return unique
