class AssociationsLecteurPorte:
    def __init__(self):
        self._associations = set()

    @property
    def lecteurs_ayant_detecte_un_badge(self):
        groupes = {}
        for lecteur, porte in self._associations:
            if lecteur not in groupes:
                groupes[lecteur] = []
            groupes[lecteur].append(porte)

        for lecteur, portes in groupes.items():
            if lecteur.badge_detecte:
                yield self.Lecteur(portes)

    def enregistrer(self, lecteur, porte):
        self._associations.add((lecteur, porte))

    class Lecteur:
        def __init__(self, portes):
            self.portes = portes
