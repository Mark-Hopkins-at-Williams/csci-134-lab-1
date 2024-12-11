import os
import sys
import subprocess
from cryptography.fernet import Fernet


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file
    and writes it.

    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open('test.py', "wb") as file:
        file.write(decrypted_data)


key = sys.argv[1]
test = sys.argv[2]
try:
    decrypt('test_bakesale.py', key)
    result = subprocess.call(['python3', '-m', 'unittest', 'test.' + test])
except Exception as e:
    print(e)
    result = 1
finally:
    if os.path.exists("test.py"):
        os.remove("test.py")

if result == 1:
    exit(1)