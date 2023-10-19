password = "DEV@2023"
att = 3

while att > 0:
    X = input("Entrez le mot de passe : ")
    if X == password:
        print("Bonjour")
        break
    else:
        att -= 1
        if att > 0:
            print("Mot de passe incorrect. Il vous reste", att," tentative(s).")
        else:
            Y = input("Répondez à la question secrète : Quel est votre film préféré ? ")
            
