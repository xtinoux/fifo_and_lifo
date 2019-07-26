# project/test_basic.py
 

# Relative imports (as in from .. import mymodule) only work in a package. To import 'mymodule' that is in the parent directory of your current module:

import os,sys

# Ajout du répéretoire parent au chemin.
currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from  main import * 
  
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
 
    # initialization logic
    # code that is executed before each test /// A COMPRENDRE A QUOI ÇA SERT
    def teardown(self):
        pass 

###############
#### tests ####
###############
 
    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
 


    def test_enigme(self):
        for i in range(1,2):
            response = self.app.get(f'/enigme/{i}')
            self.assertEqual(response.status_code, 200)

    def test_auth(self):
        response = self.app.post('/login', data={ "username": 'James', "password": '007' },follow_redirects=True)
        # this will fail, because current_user is an AnonymousUser
        self.assertRedirects(response, '/enigme')


if __name__ == "__main__":
    unittest.main()