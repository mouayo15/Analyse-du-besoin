import unittest
from analyse_besoin.associationslecteurporte import AssociationsLecteurPorte
from analyse_besoin.moteur_ouverture import MoteurOuverture
from tests.utilities.lecteur_fake import LecteurFake
from tests.utilities.porte_spy import PorteSpy

class ControleAccesTest(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge
        porte = PorteSpy()
        lecteur = LecteurFake()

        lecteur.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.ouverture_demande)

    def test_cas_deux_portes(self):
        # ETANT DONNE deux Portes reliées à un Lecteur, ayant détecté un Badge
        porte1 = PorteSpy()
        porte2 = PorteSpy()
        lecteur = LecteurFake()

        lecteur.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte1)
        moteur_ouverture.associer(lecteur, porte2)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS le signal d'ouverture est envoyé aux deux portes
        self.assertTrue(porte1.ouverture_demande)
        self.assertTrue(porte2.ouverture_demande)

    def test_cas_deux_lecteurs(self):
        # ETANT DONNE une Porte reliée à deux Lecteurs, ayant tous les deux détecté un Badge
        porte = PorteSpy()

        lecteur1 = LecteurFake()
        lecteur1.simuler_detection_badge()

        lecteur2 = LecteurFake()
        lecteur2.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur1, porte)
        moteur_ouverture.associer(lecteur2, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS un seul signal d'ouverture est envoyé à la Porte
        self.assertEqual(1, porte.nombre_ouvertures_demandees)

    def test_cas_aucune_interrogation(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge
        porte = PorteSpy()
        lecteur = LecteurFake()

        lecteur.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte)

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.ouverture_demande)

    def test_cas_non_badge(self):
        # ETANT DONNE une Porte reliée à un Lecteur, n'ayant pas détecté un Badge
        porte = PorteSpy()
        lecteur = LecteurFake()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.ouverture_demande)

    def test_deux_portes(self):
        # ETANT DONNE un Lecteur ayant détecté un Badge
        # ET un autre Lecteur n'ayant rien détecté
        # ET une Porte reliée chacune à un Lecteur
        porte_devant_s_ouvrir = PorteSpy()
        porte_devant_rester_fermee = PorteSpy()

        lecteur_ayant_detecte = LecteurFake()
        lecteur_ayant_detecte.simuler_detection_badge()

        lecteur_nayant_pas_detecte = LecteurFake()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur_ayant_detecte, porte_devant_s_ouvrir)
        moteur_ouverture.associer(lecteur_nayant_pas_detecte, porte_devant_rester_fermee)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS seule la Porte reliée au Lecteur reçoît le signal d'ouverture
        self.assertFalse(porte_devant_rester_fermee.ouverture_demande)
        self.assertTrue(porte_devant_s_ouvrir.ouverture_demande)

    def test_deux_portes_mais_linverse(self):
        # ETANT DONNE un Lecteur ayant détecté un Badge
        # ET un autre Lecteur n'ayant rien détecté
        # ET une Porte reliée chacune à un Lecteur
        porte_devant_s_ouvrir = PorteSpy()
        porte_devant_rester_fermee = PorteSpy()

        lecteur_ayant_detecte = LecteurFake()
        lecteur_ayant_detecte.simuler_detection_badge()

        lecteur_nayant_pas_detecte = LecteurFake()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur_nayant_pas_detecte, porte_devant_rester_fermee)
        moteur_ouverture.associer(lecteur_ayant_detecte, porte_devant_s_ouvrir)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS seule la Porte reliée au Lecteur reçoît le signal d'ouverture
        self.assertFalse(porte_devant_rester_fermee.ouverture_demande)
        self.assertTrue(porte_devant_s_ouvrir.ouverture_demande)

    def test_porte_forcee_ouverte_avec_badge(self):
        # ETANT DONNE une Porte forcée en ouverture
        porte_forcee = PorteSpy()
        porte_forcee.forcer_ouverture()

        lecteur = LecteurFake()
        lecteur.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte_forcee)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS la Porte forcée reçoit le signal d'ouverture même sans présence de badge valide
        self.assertTrue(porte_forcee.ouverture_demande)

    def test_porte_forcee_ouverte_sans_badge(self):
        # ETANT DONNE une Porte forcée en ouverture
        porte_forcee = PorteSpy()
        porte_forcee.forcer_ouverture()

        lecteur = LecteurFake()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte_forcee)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS la Porte forcée reçoit le signal d'ouverture même sans présence de badge
        self.assertTrue(porte_forcee.ouverture_demande)
if __name__ == "__main__":
    unittest.main()
