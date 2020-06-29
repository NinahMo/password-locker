import unittest
from password import Password

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_password = Password("Ninahmozzy","0712345678","aBcDeF","aBcDeF")

    def tearDown(self):
        Password.password_list = []

    def test_init(self):
        self.assertEqual(self.new_password.username,"Ninahmozzy")
        self.assertEqual(self.new_password.phone_number,"0712345678")
        self.assertEqual(self.new_password.password,"aBcDeF")
        self.assertEqual(self.new_password.pas2,"aBcDeF")

    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

    def test_save_multiple_contact(self):
        '''
        '''
        self.new_password.save_password()
        test_password=Password("Ninahmozzy","0712345678","aBcDeF","aBcDeF")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

    def delete_password(self):
        Password.password_list.remove(self)

    def test_find_password_by_username(self):
        self.new_password.save_password()
        test_password = Password("Ninahmozzy","0712345678","aBcDeF","aBcDeF")
        test_password.save_password()

        found_password = Password.find_by_username("Ninahmozzy")

        self.assertEqual(found_password.password,test_password.password)

    def test_display_all_usernames(self):
        self.assertEqual(Password.display_passwords(),Password.password_list)

if __name__ == '__main__':
    unittest.main()