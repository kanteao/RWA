MatriceGene = [
		[0, 1, 0],
		[1, 0, 1],
		[0, 1, 0],
	];

matriceCom = [];

def matrice_Com(MatriceGene):
	lineCol = len(MatriceGene); 
	matriceCom = [[0]*lineCol for _ in range(lineCol)];
	for i in range(0,len(MatriceGene)):
		for j in range(0,len(MatriceGene)):
			if (i == j):
				matriceCom[i][j] = 0;
			else:
				matriceCom[i][j]= 1;
	return matriceCom;


def racine(MatriceGene):
	lineCol = len(MatriceGene);
	matrice_racine = [[0]*lineCol for _ in range(lineCol)];
	for i in range(0,len(MatriceGene)):
		for j in range(0,len(MatriceGene)):
			if (i == j or MatriceGene[i][j] == 1):
				matrice_racine[i][j] = i+1;
			else:
				matrice_racine[i][j] = (i+j+2)/2 ;		
	return matrice_racine;
			 
print "Matrice de communication entre les noeuds: ";
print matrice_Com(MatriceGene);

print "Racine";
print racine(MatriceGene);