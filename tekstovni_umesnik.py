import model

trenutna_igra = model.nova_igra()

def izpis_poraza(igra):
    return f"IZGUBIL SI, geslo je bilo: {igra.geslo}"

def izpis_zmaga(igra):
    return f"ZMAGAL SI, geslo je bilo: {igra.geslo}" 


def izpis_igre(igra):
    text = (
        f"Stanje gesla: {igra.pravilni_ugibi()}\n"
        f"imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako"
    )

def zahtevaj_vnos():
    return input("Vpiši naslednjo črko")

def pozeni_vmesnik():
    #naredi novo igro
    trenutna_igra = model.nova_igra()

    while True:
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmaga(trenutna_igra))
            return

        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            return 
            
pozeni_vmesnik()
        

    #ponavljamo

    #vnos

    #preveri zmago/poraz

    #nazaj na vnos