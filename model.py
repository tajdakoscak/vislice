
import random


#definiranje konstant:

STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = "Z"

#konstante za rezultate ugibanj
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

#konstante za zmago in poraz
ZMAGA = "W"
PORAZ = "X"

#odpremo bazo in zaženemo bazen besed
bazen_besed = []


with open("vislice/besede.txt") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())


class Igra:


    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = crke.lower()


    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

            

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]
        # { ; if a \not \in A }


    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True

    def pravilni_del_gesla(self):
        trenutno = ""
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += "_"
        return trenutno

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())
        
    def ugibaj(self, ugibana_crka):
        ugibana_crka == ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        
        self.crke.append(ugibana_crka)

        if ugibana_crka in self.geslo:
            #uganil je
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
            
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA



def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)

    


class Vislice:

    #skrbi za trenutno stanje VEČ iger (imel bo več objektov tipa Igra)
    def __init__(self):
        #slovar, ki ID ju priredi igro
        self.igre ={}
        #če nardiš self.igre[20] dobiš napako! TO MORMO PAZT
        #v ta slovar igre dodajamo

    #šelimo spremljati igro z (igra(ID),stanje)

    #kako dobiš ID k ga zihr še ni v našem slovarju
        # lahko daš neki na random pa na neko veliko številko
        
    def prosti_od_igre(self):
        #vrne nek id, ki ga ne uporablja nobena igra

        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):

        #dobimo svež id
        nov_id = self.prosti_od_igre()

        #naredimo novo igro
        sveza_igra = nova_igra()

        #vse to shanimo v self.igre
        self.igre[nov_id] = (sveza_igra, ZACETEK)

        #VRNEMO NOV ID
        return nov_id

    def ugibaj(self, id_igre, crka):
        #dobimo staro igro ven
        trenutna_igra, _ = self.igre[id_igre]

        #ugibamo črko
        novo_stanje = trenutna_igra.ugibaj(crka)

        #zapišemo posodobljeno stanje in igro nazaj v "BAZO"
        self.igre[id_igre] = (trenutna_igra, novo_stanje)



        


    
   
    

