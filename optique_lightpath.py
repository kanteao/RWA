#!/usr/bin/python3

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
			 


A=matrice_Com(MatriceGene)
B=racine(MatriceGene)
C=MatriceGene
print "Matrice de communication entre les noeuds: ";
print("A=",A);

print "Racine";
print("B=",B);
lp=[[0]*9 for i in range(9)]
k1=k2=k=0;


z=3
i=0
j=0
N=9

position = 0;

print(lp)
while i < z:
	while j<z:
		if A[i][j]!=0:
			if B[i][j]-1==i:
				print("i____________________",i+1)
				print("j____________________",j+1)
				m=j+1
				n=B[i][j]
				print("n__________",n)
				print("m__________",m)
				k=((m-1)*z)+n
				print("k",k)
				lp[position][k-1]=1
				position = position +1
			else:
				print("i____________________",i+1)
				print("j____________________",j+1)
				m1=j
				n1=B[i][j]-1
				m2=n1
				n2=i
				k1=((m1)*z)+n1+1
				k2=((m2)*z)+n2+1
				print("n1__________",n1)
				print("m1__________",m1)
				print("_________________________________")
				print("n2__________",n2)
				print("m2__________",m2)
				print("k1______________",k1)
				print("k2______________",k1)
				lp[position][k1-1]=1
				lp[position][k2-1]=1
				position = position +1
			j=j+1
		else:
			print("i____________________",i+1)
			print("j____________________",j+1)
			position = position +1
			j=j+1
	i=i+1
	j = 0
print("lp",lp)

i=0
j=0
print("___________________________trouver les 1___________________")
while i < N:
	while j<N:
		if lp[i][j]==1:
			k=i+1
			print("j_______________",j+1)
			while k<N:
				if lp[k][j]==1: 
					print("k____________",k)					
				k=k+1;
					
		j=j+1
	i=i+1
	j=0

