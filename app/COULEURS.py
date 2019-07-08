
#Liste de couleur
TURQUOISES = [ '#178d81',  '#0c4f4a', '#40e0d0', '#78eade', '#117169', '#94ede5', '#20c7b6', '#aff1ec']
JAUNES = [ '#8d8117',  '#4f4a0c', '#e0d040', '#eade78', '#716911', '#ede594', '#c7b620', '#f1ecaf']
VIOLETS = [ '#81178d',  '#4a0c4f', '#d040e0', '#de78ea', '#691171', '#e594ed', '#b620c7', '#ecaff1']


#Dictionnaire des couleurs
JAUNES_D = { 'couleur1':'#8d8117', 'couleur2': '#4f4a0c', 'couleur3':'#e0d040', 'couleur4':'#eade78', 'couleur5':'#716911', 'couleur6':'#ede594', 'couleur7':'#c7b620', 'couleur8':'#f1ecaf'}
TURQUOISES_D = {'couleur1': '#178d81', 'couleur2': '#0c4f4a', 'couleur3': '#40e0d0', 'couleur4': '#78eade', 'couleur5': '#117169', 'couleur6': '#94ede5', 'couleur7': '#20c7b6', 'couleur8': '#aff1ec'}
VIOLETS_D = {'couleur1': '#81178d', 'couleur2': '#4a0c4f', 'couleur3': '#d040e0', 'couleur4': '#de78ea', 'couleur5': '#691171', 'couleur6': '#e594ed', 'couleur7': '#b620c7', 'couleur8': '#ecaff1'}

#liste2dic
def liste2dic(couleurs):
	dic = {}
	for key, couleur in enumerate(couleurs):
		dic['couleur{}'.format(key+1)] = couleur
	return dic


if __name__ == '__main__':
	# print(liste2dic(TURQUOISES))
	pass
 
