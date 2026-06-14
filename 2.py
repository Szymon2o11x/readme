word = input("Podaj słowo: ")

for litera in word:
    if litera.lower() in "aąeęiouóy":
        print(litera)