#!/usr/bin/env python
from password import Password

def create_user(self,username,number,password,pas2):
    new_user = Password(username,number,password,pas2)
    return new_user

def save_password(password):
    password.save_user()

# def create_password(username,phone_number,password):
#     new_password = password(username,phone_number,password)
#     return new_password

# def save_password(password):
#     password.save_password()

def del_password(password):
    password.delete_password()

def find_user(username):
    return Password.password_list

def display_password():
    return Password.display_passwords()

# def authenticate_user(loginname,password):
#     return User.user_authenticate(loginname,password)

# def valid_user(full_name,login_name,email,password):
#     if full_name=="" or login_name=="" or email=="" or password=="":
#         return False
#     else:
#         return True

def main():
  print("Hello!Welcome to The password locker!")


    

  print("What is your name")

  user_name = input()

  print(f"Hello {user_name}.What would you like to do?")
  print('\n')

  while True:
    list =('''
    cc-create account
    dc - delete account 
    fc - find account 
    '''
    )
    print ("use these short codes to decide what to do:") 
    print (list)
    

    short_code = input().lower()
    
    if short_code == 'cc':
      print("New User:")

      print("Enter your name:")
      username =input()

      print("Enter your phone number:")
      number = input()

      print("create password:")
      password = input()

      print("confirm passsword:")
      pas2 = input()
    
      save_password(create_user(username,number,password,pas2)) 
      
      print("Thank you!you have successfully created an acc.")

    elif short_code == 'dc':                
        print("enter your username")
        del_info = input()
        del_password = find_user(del_info)

        if del_password == del_info:                     
            del_password.delete_password()     
            print('/n')
            print("You have deleted your account")
        else:    
            print('/n')
            print("The above file does not exist")        
            print('/n')    
        
    elif short_code == 'fc':      
        print("enter your username")      
        find_user = input()
        find_password_by_username = find_user(find_user)

        if find_password_by_username == find_user:
            find_user.find_user()    


if __name__ == '__main__':
    main()