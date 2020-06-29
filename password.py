class Password:
    """
    Class that creates new passwords
    """
    password_list = []

def __init__(self,username,number,password,pas2):
    '''
    __init__ method helps you create your credentials.
    '''

    self.username = username
    self.phone_number = number
    self.password = password
    self.password = pas2


def save_password(self):
    '''
    '''
    Password.password_list.append(self)

def delete_password(self):
    Password.password_list.remove(self)

@classmethod
def find_by_username(cls,username):
    '''
    This allows one to find username
    '''
    for password in cls.password_list:
        if password.username == username:
            return password

@classmethod
def username_exist(cls,username):
    '''
    '''
    for password in cls.password_list:
        if password.username == username:
            return True

    return False     

@classmethod
def display_passwords(cls):
    '''
    '''
    return cls.password_list

