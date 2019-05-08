v=[0,1,2,3,4,5]
start=0;
dest=3
#G=[[0,10,50,10],[10,0,20,0],[50,20,0,10],[10,0,10,0]]
G=[[0,10,0,20,0,0],[10,0,10,20,30,0],[0,10,0,0,20,10],[20,20,0,0,10,0],[0,30,20,10,0,10],[0,0,10,0,10,0]]
d=[0,0,0,0,0,0]
visited=[0,0,0,0,0,0]
source=[]
tree=[]
source.append(start)
voisin=['','','','','','']
source_temp=[]
parent=[0,0,0,0,0,0]
color = [1,1,1,1,1,1]
chemin_inv=[]
for i in v:
	if i==0 :
		d[i]=0
	else:
		d[i]=1000
print(d)


def all_visited(visited):
	for i in visited:
		if i==0:
			temp = 1
		else:
			temp = 0
	return temp

def calc_d(G,source):
	source_temp=[]
	for s in source:
		for i in v:
			if G[s][i]!=0:
				if str(i) not in voisin[i]:
					voisin[s]=voisin[s]+str(i)
				if d[i]> d[s]+ G[s][i]:
					d[i]=d[s]+ G[s][i]
					parent[i]=s
					
					
				if(visited[i]==0):
					source_temp.append(i)
		visited[s]=1	
	return (source_temp)

print ('source1',source)
print ('d1',d)
print('voisin',voisin)

def reverse_slicing(s):
    return s[::-1]
    
terminer =all_visited(visited)
print ('terminer',terminer)
while terminer:
	source=calc_d(G,source)
	print ('source2',source)
	print ('d1',d)
	print ('parent',parent)
	print('voisin',voisin)
	terminer =all_visited(visited)
for k in v:
	chemin=str(k)
	if k==0:
		continue
	while 1:
		chemin=chemin+str(parent[k])
		if parent[k]==start:
			#chemin=chemin+str(k)+'>'+str(start)
			print('chemin',reverse_slicing(chemin))
			chemin_inv=reverse_slicing(chemin)
			tree.append(chemin_inv)
			break
		
		k=parent[k]
print(tree)


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
			print('i',i)
			while j<len(voisin[i]):
				#color[i]+=1
				print('voisin',i,'->',voisin[i][j],'color',color,'condition',color[i],'==',color[int(voisin[i][j])])
				#print('color',color)
				#print ('condition',color[i],'==',color[int(voisin[i][j])])
				if color[i]==color[int(voisin[i][j])]:
					color[i]+=1
					print('color',color)
				j+=1
			i+=1
get_color(voisin,start)
print('color',color)


