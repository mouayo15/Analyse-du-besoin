from analyse_besoin.i_porte import IPorte
from datetime import datetime, timedelta

class PorteSpy(IPorte):
    def __init__(self):
        self.nombre_ouvertures_demandees = 0
        self.forcee_ouverte = False
        self.date_debloquage = datetime.now()
    @property
    def ouverture_demande(self):
        return self.nombre_ouvertures_demandees > 0 and datetime.now() >= self.date_debloquage

    def ouvrir(self):
        if not self.forcee_ouverte:
            self.nombre_ouvertures_demandees += 1

    def forcer_ouverture(self):
        self.forcee_ouverte = True
        self.nombre_ouvertures_demandees += 1

    def reset_ouverture(self):
        self.nombre_ouvertures_demandees = 0
        self.forcee_ouverte = False

    def bloquer_pendant(self, jours):
        self.date_debloquage = datetime.now() + timedelta(days=jours)