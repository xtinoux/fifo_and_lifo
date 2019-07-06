# project/test_basic.py
 

# Relative imports (as in from .. import mymodule) only work in a package. To import 'mymodule' that is in the parent directory of your current module:

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import unittest
from  main import * 
# from project import app, db, mail
 
 
TEST_DB = 'test.db'
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        # db.drop_all()
        # db.create_all()
 
        # Disable sending emails during unit testing
        # mail.init_app(app)
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_homepage(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    def test_enigme(self):
        for i in range(1,3):
            response = self.app.get(f'/enigme/{i}', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()