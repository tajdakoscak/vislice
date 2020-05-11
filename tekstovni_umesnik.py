import model

trenutna_igra = model.nova_igra()

def izpis_poraza(igra):
    return f"IZGUBIL SI, geslo je bilo: {igra.geslo}"

def izpis_zmaga(igra):
    return f"ZMAGAL SI, geslo je bilo: {igra.geslo}" 


def izpis_igre(igra):
    text = (
        f"Stanje gesla: {igra.pravilni_ugibi()} \n"
        f"imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako"
    )

def zahtevaj_vnos():
    return input("Vpiši naslednjo črko")

