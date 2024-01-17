import random
import secrets
import pyperclip

szimbolumok = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'] 
szamok = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]   
nbetu =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
kbetu =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
osszes_karakter =  ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

random.shuffle(szimbolumok) #megkeverjük a listákat
random.shuffle(szamok)
random.shuffle(nbetu)
random.shuffle(kbetu)

jelszo_hossz = int(input("Add meg a jelszó hosszát: "))  # A jelszó hossza, amit megváltoztathatsz
jelszo_hossz_minusz = jelszo_hossz - 4 # Biztos legyen benne a v1 v2 v3 4v ből, ezért csinálunk helyet a 4 listának

jelszo_v1 = ''.join(secrets.choice(szimbolumok) for _ in range(1))
jelszo_v2 = ''.join(secrets.choice(szamok) for _ in range(1))
jelszo_v3 = ''.join(secrets.choice(nbetu) for _ in range(1))
jelszo_v4 = ''.join(secrets.choice(kbetu) for _ in range(1))

kesz_jelszo = ([jelszo_v1, jelszo_v2, jelszo_v3, jelszo_v4] +
                     [secrets.choice(osszes_karakter) for _ in range(jelszo_hossz_minusz)])

print(kesz_jelszo)

megkevert_jelszo = ''.join(random.sample(kesz_jelszo, len(kesz_jelszo)))

# Megkevert jelszó kiírása
print("Megkevert jelszó:", megkevert_jelszo)

# Másolás a vágólapra
pyperclip.copy(megkevert_jelszo)