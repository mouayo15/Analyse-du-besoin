from analyse_besoin.associationslecteurporte import AssociationsLecteurPorte



class MoteurOuverture:
    def __init__(self):
        self._associations = AssociationsLecteurPorte()

    def interroger(self):
        lecteurs = self._associations.lecteurs_ayant_detecte_un_badge
        portes_a_ouvrir = set()

        for lecteur in lecteurs:
            for porte in lecteur.portes:
                portes_a_ouvrir.add(porte)

        for porte in portes_a_ouvrir:
            porte.ouvrir()

    def associer(self, lecteur, porte):
        self._associations.enregistrer(lecteur, porte)
