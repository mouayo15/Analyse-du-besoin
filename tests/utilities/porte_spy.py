from analyse_besoin.i_porte import IPorte

class PorteSpy(IPorte):
    def __init__(self):
        self.nombre_ouvertures_demandees = 0

    @property
    def ouverture_demande(self):
        return self.nombre_ouvertures_demandees > 0

    def ouvrir(self):
        self.nombre_ouvertures_demandees += 1
