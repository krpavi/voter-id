# voter id
print("Pls enter the following details to apply for your voter id")
print("Pls enter 'YES' if you have the upcoming credentials and 'NO' if not")
rc = input("Do you have your ration card: ")
ac = input("Do you have your aadhaar card: ")
dl = input("Do you have your driving license: ")
pc = input("Do you have your passport copy: ")
bc = input("Do you have your birth certificate: ")
if rc == 'YES' and ac == 'YES' and dl == 'YES' and pc == 'YES' and bc == 'YES':
    print("You can receive your voter id")
else:
    print("It seems you are missing a crucial detail")
    print("You are not qualified to receive your voter id")


