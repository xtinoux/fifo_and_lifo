# project/test_enigme2.py
 

# Relative imports (as in from .. import mymodule) only work in a package. To import 'mymodule' that is in the parent directory of your current module:

import os,sys

# Ajout du répéretoire parent au chemin.
currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from  main import * 
from  app.enigme2.enigme2 import reponse_enigme2


# reponse_enigme2()

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # code that is executed before each test /// A COMPRENDRE A QUOI ÇA SERT
    def teardown(self):
        pass 

################################
#### tests  pour l'enigme 2 ####
################################
 
    def test_reponse_enigme2_element0(self):
        """
        Test la fonction de réponse de l'enigme 2
        """
        reponse = reponse_enigme2(123456780)
        self.assertIn("contenir de 0", reponse["msg"])


    def test_reponse_enigme2_mauvaise_taille(self):
        """
        Test la fonction de réponse de l'enigme 2
        """
        reponse = reponse_enigme2(12345678)
        self.assertIn("nombre de chiffres", reponse["msg"])
         

    def test_reponse_enigme2_redondance(self):
        """
        Test la fonction de réponse de l'enigme 2
        """
        reponse = reponse_enigme2(123456782)
        self.assertIn("plusieur fois", reponse["msg"])
 
 

    def test_reponse_enigme2_diviseur(self):
        """
        Test la fonction de réponse de l'enigme 2
        """
        reponse = reponse_enigme2(193456782)
        self.assertIn("divisible", reponse["msg"])
 
 

if __name__ == "__main__":
    unittest.main()