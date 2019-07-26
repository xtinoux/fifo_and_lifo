texte = """bravo vous avez reussi a decrypter le message secret crypter par la methode de cesar.
Ce codage comme vous pouvez le constater n'est pas tres efficace puisqu'une analyse de la repetition de la lettre la plus courante d'une langue permet de connaitre le decallage.
Actuellement certain cryptage repose l'usage de cle privee - cle public."""


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
decallage = 9
alphabet_crypte = [ alphabet[(i+decallage)%26] for i in range(26)]

for i in alphabet:
	print(f" Le nombre d'occurence de {i} est {texte.count(i)}")

texte_crypte = ""
for i in texte:
	try:
		index_lettre = alphabet.index(i)
		texte_crypte += alphabet_crypte[index_lettre]
	except:
		texte_crypte += i
print(texte_crypte)



caracteres_specials = ["'", "P" ," " , "4"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(alphabet_crypte)





eval_caractere_special():
	"""
	
	"""
	for texte in caracteres_specials:
		texte_decrypte = decryptage(texte)
		self.assertEqual(texte_decrypte, texte)

eval_caractere_normal():
	"""

	"""
	for texte in alphabet_crypte:
		texte_decrypte = decryptage(texte)
		self.assetEqual(texte_decrypte, alphabet[alphabet_crypte.index(text)])

