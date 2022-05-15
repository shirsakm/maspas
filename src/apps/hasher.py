from hashlib import pbkdf2_hmac
from os import urandom

class Hasher():
  def pswd_hash(self):
    HASH_NAME = 'sha256'
    ITERS = 1000
    SALT = self.__get_salt()
    pswd = b'test'

    print(pbkdf2_hmac(HASH_NAME, pswd, SALT, ITERS).hex())
    
  def __get_salt(self):
    # Checking if there is a pre-exsiting salt
    try:
      # Getting the salt
      with open('data/key/salt.txt', 'rt') as salt_file:
        _salt = bytes(salt_file.read(), 'utf-8')
      
      return _salt

    # Making a new salt and writing it if there is no salt
    except FileNotFoundError:
      # Making a new salt 
      _salt = urandom(16)

      # Writing the salt to the file for further use 
      with open('data/key/salt.txt', 'wt') as salt_file:
        salt_file.write(str(_salt))
      
      return _salt