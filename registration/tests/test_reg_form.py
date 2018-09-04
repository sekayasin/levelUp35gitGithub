import unittest
from reg_form import registrationForm

class registrationFormTest(unittest.TestCase):

    def setUp(self):
        self.regform = registrationForm()

    def test_reg_form_creation(self):
        self.assertIsInstance(self.regform, registrationForm)

    def test_add_user(self):
        self.regform.add_user(1, "Yasin", "Sekabira", "sekayasin@gmail.com", "patchedTeam", "0772062954")
        self.assertEqual(len(self.regform.user_details), 1)

