from colorama import Fore
import hashlib

print(Fore.BLUE+"@@             @@ @@@@@@@@@@@@  @@@@@@@@@   @@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@  @@         @@  @@@@@@@@@@@@  @@@@@@@@@")
print(Fore.BLUE+" @@           @@  @@            @@      @@        @@         @@                 @@      @@   @@            @@      @@")
print(Fore.BLUE+"  @@         @@   @@            @@     @@         @@         @@                   @@   @@    @@            @@     @@")
print(Fore.BLUE+"   @@       @@    @@@@@@@       @@@@@@@@          @@         @@@@@@@@@@             @@@      @@@@@@@@      @@@@@@@@")
print(Fore.BLUE+"    @@     @@     @@            @@     @@         @@         @@                     @@       @@            @@     @@")
print(Fore.BLUE+"     @@   @@      @@            @@     @@         @@         @@                    @@        @@            @@     @@")
print(Fore.BLUE+"      @@ @@       @@@@@@@@@@@@  @@     @@   @@@@@@@@@@@@@@@  @@                   @@         @@@@@@@@@@@@  @@     @@")
print(Fore.RED+"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

print(Fore.BLUE+"Github Link:- "+Fore.RED+"https://github.com/dragonwolf1o1\n")

def font():
    print(Fore.BLUE+"[1] "+Fore.GREEN+ "MD5")
    print(Fore.BLUE+"[2] "+Fore.GREEN+ "SHA-1")
    print(Fore.BLUE+"[3] "+Fore.GREEN+ "SHA-224")
    print(Fore.BLUE+"[4] "+Fore.GREEN+ "SHA-256")
    print(Fore.BLUE+"[5] "+Fore.GREEN+ "SHA-384")
    print(Fore.BLUE+"[6] "+Fore.GREEN+ "SHA-512")
    print(Fore.BLUE+"[0] " + Fore.GREEN + "EXIT")
font()

hash=input("ENTER YOUR GIVEN HASH VALUE: ")
file_location=input("ENTER THE FILE LOCATION: ")
num=int(input("CHOOSE THE HASHING ALGORITHM: "))

def md5():
    md5_hash = hashlib.md5()
    with open(file_location, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
        h=md5_hash.hexdigest()
        if hash==h:
            print(Fore.GREEN+"Verified!!")
        else:
            print(Fore.RED+"Not Verified!!")

def sha1():
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    with open(file_location, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    h=file_hash.hexdigest()
    if hash == h:
        print(Fore.GREEN + "Verified!!")
    else:
        print(Fore.RED + "Not Verified!!")
def sha256():
    sha256_hash = hashlib.sha256()
    with open(file_location, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        h=sha256_hash.hexdigest()
        if hash==h:
            print(Fore.GREEN+"Verified!!")
        else:
            print(Fore.RED+"Not Verified!!")

def sha512():
    file=file_location
    sha512_returned = hashlib.sha512(file.encode()).hexdigest()
    h=sha512_returned
    if hash == h:
        print(Fore.GREEN + "Verified!!")
    else:
        print(Fore.RED + "Not Verified!!")

def sha224():
    with open(file_location) as f:
        sha224 = hashlib.sha224()
        while chunk := f.read(4096):
            sha224.update(chunk)
    h=sha224.hexdigest()
    if hash == h:
        print(Fore.GREEN + "Verified!!")
    else:
        print(Fore.RED + "Not Verified!!")

def sha384():
    with open(file_location) as f:
        sha384 = hashlib.sha384()
    while chunk := f.read(4096):
            sha384.update(chunk)
    h=sha384.hexdigest()
    if hash == h:
        print(Fore.GREEN + "Verified!!")
    else:
        print(Fore.RED + "Not Verified!!")

while num!=0:
    if num == 1:
        md5()
        font()
        hash = input("IF YOU WANT TO EXIT THEN PRESS 0 OTHERWISE, ENTER YOUR GIVEN HASH VALUE: ")
        if hash == str(0):
            break
        else:
            file_location = input(Fore.GREEN + "ENTER THE FILE LOCATION: ")
            num = int(input(Fore.GREEN + "CHOOSE THE HASH ALGORITHM FROM MENTION ABOVE:"))
    elif num == 2:
        sha1()
        font()
        hash = input("IF YOU WANT TO EXIT THEN PRESS 0 OTHERWISE, ENTER YOUR GIVEN HASH VALUE: ")
        if hash == str(0):
            break
        else:
            file_location = input(Fore.GREEN + "ENTER THE FILE LOCATION: ")
            num = int(input(Fore.GREEN + "CHOOSE THE HASH ALGORITHM FROM MENTION ABOVE:"))
    elif num == 3:
        sha224()
        font()
        hash = input("IF YOU WANT TO EXIT THEN PRESS 0 OTHERWISE, ENTER YOUR GIVEN HASH VALUE: ")
        if hash == str(0):
            break
        else:
            file_location = input(Fore.GREEN + "ENTER THE FILE LOCATION: ")
            num = int(input(Fore.GREEN + "CHOOSE THE HASH ALGORITHM FROM MENTION ABOVE:"))
    elif num == 4:
        sha256()
        font()
        hash = input("IF YOU WANT TO EXIT THEN PRESS 0 OTHERWISE, ENTER YOUR GIVEN HASH VALUE: ")
        if hash == str(0):
            break
        else:
            file_location = input(Fore.GREEN + "ENTER THE FILE LOCATION: ")
            num = int(input(Fore.GREEN + "CHOOSE THE HASH ALGORITHM FROM MENTION ABOVE:"))
    elif num == 5:
        sha384()
        font()
        hash = input("IF YOU WANT TO EXIT THEN PRESS 0 OTHERWISE, ENTER YOUR GIVEN HASH VALUE: ")
        if hash == str(0):
            break
        else:
            file_location = input(Fore.GREEN + "ENTER THE FILE LOCATION: ")
            num = int(input(Fore.GREEN + "CHOOSE THE HASH ALGORITHM FROM MENTION ABOVE:"))
    elif num == 6:
        sha512()
        font()
        hash = input("IF YOU WANT TO EXIT THEN PRESS 0 OTHERWISE, ENTER YOUR GIVEN HASH VALUE: ")
        if hash == str(0):
            break
        else:
            file_location = input(Fore.GREEN + "ENTER THE FILE LOCATION: ")
            num = int(input(Fore.GREEN + "CHOOSE THE HASH ALGORITHM FROM MENTION ABOVE:"))

    else:
        num = int(input(Fore.CYAN + "PLEASE ENTER THE CORRECT NUMBER:"))