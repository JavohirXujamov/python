from colorama import Fore, init


init()

ism = input("Ismingizni kiriting: ")
familya = input("Familyangizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")

print(Fore.RED + f"Salom, sizning ismingiz {ism}, familyangiz {familya}, yoshingiz {yosh} da." + Fore.RESET)
input("To'g'rimi")
