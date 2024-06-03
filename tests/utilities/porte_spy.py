from analyse_besoin.i_porte import IPorte
class PorteSpy(IPorte):
    def __init__(self):
        self.nombre_ouvertures_demandees = 0
        self.forcee_ouverte = False
        self.forcee_verrouillee = False  

    @property
    def ouverture_demande(self):
        return self.nombre_ouvertures_demandees > 0 

    def ouvrir(self):
        if not self.forcee_ouverte and not self.forcee_verrouillee:  
            self.nombre_ouvertures_demandees += 1

    def forcer_ouverture(self):
        self.forcee_ouverte = True
        self.nombre_ouvertures_demandees += 1

    def forcer_verrouillage(self):  
        self.forcee_verrouillee = True

    def reset_ouverture(self):
        self.nombre_ouvertures_demandees = 0
        self.forcee_ouverte = False
        self.forcee_verrouillee = False  