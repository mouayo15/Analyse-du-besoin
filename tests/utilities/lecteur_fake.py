from analyse_besoin.i_lecteur import ILecteur

class LecteurFake(ILecteur):
    def __init__(self):
        self._detection_simulee = False
        self._badge_valide = True

    @property
    def badge_detecte(self):
        returned_value = self._detection_simulee and self._badge_valide
        self._detection_simulee = False
        return returned_value

    def simuler_detection_badge(self, valide=True):
        self._detection_simulee = True
        self._badge_valide = valide
