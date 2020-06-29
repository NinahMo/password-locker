# import unittest
# from user import User

# class Testuser(unittest.TestCase):
#     def setUp(self):
#         self.new_user = User("Ninah Mozzy","ninah","ninah@gmail.com","aBcDeF")

#     def test_init(self):
#         self.assertEqual(self.new_user.full_name,"Ninah Mozzy")
#         self.assertEqual(self.new_user.login_name,"ninah")
#         self.assertEqual(self.new_user.email,"ninah@gmail.com")
#         self.assertEqual(self.new_user.password,"aBcDeF")

#     def test_save_user(self):
#         self.new_user.save_user()
#         self.assertEqual(len(User.user_list),1)

# if __name__ == '__main__':
#     unittest.main()