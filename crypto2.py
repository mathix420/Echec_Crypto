from secrets import choice
import qrcode, unidecode
import numpy as np

print("""
               ATTENTION
CE SYSTEME N'EST ABSOLUMENT PAS SECURISE
 IL EST UTILE POUR DES JEUX UNIQUEMENT !

""")
#alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Créer une répétition de l'aphabet pour remplir 64 cases
alph_lst = list(alphabet*3)[:8*8]

#Créer la matrice, et la redimensionne
alph_mtrc = np.array(alph_lst).reshape(8,8)

#Les étiquettes des abscices et ordonnées
ex = list('ABCDEFGH')
ey = list('87654321')

tx_cl = input("Entrez le texte à chiffrer :\n > ")
#On néttoie les accents
tx_cl = unidecode.unidecode(tx_cl)
output = ''

for i in tx_cl.lower():
    ly = np.where(alph_mtrc == i)[0]
    lx = np.where(alph_mtrc == i)[1]
    #Cherche toutes les occurrences de la lettre et retourne ses coordnées
    found = [(ly[i],lx[i]) for i in range(len(lx))]
    if i in alph_mtrc:
        #Choisi une coordonée au hasard
        idy, idx = choice(found)
        #Ajoute la coordonée formatée avec les étiquettes
        output += ex[idx] + ey[idy] + ' '

print("Données chiffrés : ", output[:-1])

img = qrcode.make(output[:-1] + '\nBonne chance !')

img.save('QRcode.png')

print("QRcode saved !")

aaa = input("Press enter to quit !")
