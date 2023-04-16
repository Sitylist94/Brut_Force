liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
mot = input("Entrez votre mot de passe : ")

def brut_force(password, letters):
    for l1 in letters:
        for l2 in letters:
            for l3 in letters:
                for l4 in letters:
                    for l5 in letters:
                        chaine = l1+l2+l3+l4+l5
                        if chaine == password:
                            print('Vous avez trouvé ! Le mot de passe est ', chaine)
                            return
                        else:
                            print("Mot de passe incorrect :", chaine)

brut_force(mot, liste)
