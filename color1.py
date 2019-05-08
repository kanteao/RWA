#!/usr/bin/python3

color = [0,0,0,0,0,0]
voisin=['12', '023', '0134', '1245','235','34']
#voisin=['15','023','013','12']
v = [0,1,2,3,4,5]
start=0
j=0

def get_color(voisin,start):
	color[start]=1
	i=0
	while i<len(voisin):
		if i==start:
			color[start]=1
			i=i+1
			print('i',i)
			print('color',color)
		else:
			j=0
			color[i]=1;
			print('i',i)
			while j<len(voisin[i]):
				#color[i]+=1
				print('voisin',i,'->',voisin[i][j])
				print('color',color)
				print ('condition',color[i],'==',color[int(voisin[i][j])])
				if color[i]==color[int(voisin[i][j])]:
					color[i]+=1
					print('color',color)
				j+=1
			i+=1
get_color(voisin,start)
print('color',color)
		
