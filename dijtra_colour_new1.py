#!/usr/bin/python3
def init_graph(v,d):
	for i in v:
		parent[i]=i
		if i==start :
			d[i]=0
		else:
			d[i]=10**6
	print(d)


def all_visited(visited):
	for i in visited:
		if i==0:
			temp = 1
			break
		else:
			temp = 0
	#print('i##################',i)
	print('visited____________',visited)
	return temp

def calc_d(G,source):
	source_temp=[]
	for s in source:
		for i in v:
			if G[s][i]!=0:
				#if str(i) not in voisin[i]:
				#	voisin[s]=voisin[s]+str(i)
				if d[i]> d[s]+ G[s][i]:
					
					d[i]=d[s]+ G[s][i]
					parent[i]=s
					#print('parent',parent)
					
				if(visited[i]==0):
					source_temp.append(i)
		visited[s]=1
		print('d_______',d)	
	return (source_temp)

def reverse_slicing(s):
    return s[::-1]

#v=[0,1,2,3]
v=[0,1,2]
lp=[]
lightpaths={}
l=0
start=0;
dest=3
#G=[[0,10,50,10],[10,0,20,0],[50,20,0,10],[10,0,10,0]]
#G=[[0,500,600,0,0,0],[500,0,300,400,0,0],[600,300,0,500,400,0],[0,400,500,0,300,400],[0,0,400,300,0,600],[0,0,0,400,600,0]]
G=[[0,400,0],[400,0,600],[0,600,0]]
i=0

voisins=['']*len(v)
#print ('voisins___________',voisins)
while i < len(v):
	start=i
	
	print ('start______________________________________',start)
	d=[0]*len(v)
	visited=[0]*len(v)
	source=[]
	tree=[]
	source.append(start)
	voisin=['']*len(v)
	source_temp=[]
	parent=[0]*len(v)
	
	chemin_inv=[]
	#print ('source1',source)
	#print ('d1',d)
	#print('voisin',voisin)


	init_graph(v,d)
	terminer =all_visited(visited)
	#print ('terminer111111111111111111',terminer)
	while terminer:
		source=calc_d(G,source)
		#print ('source2',source)
		#print ('d1',d)
		print ('parent',parent)
		#print('voisin',voisin)
		#print('visited------------------',visited)
		terminer =all_visited(visited)
		#print('terminer###########################',terminer)
	for k in v:
		#print('k______________',k)
		chemin=str(k)
		if k==start:
			continue
		while 1:
			chemin=chemin+str(parent[k])
			#print('test chemin_______',chemin)
			if parent[k]==start:
				#chemin=chemin+str(k)+'>'+str(start)
				print('chemin',reverse_slicing(chemin))
				chemin_inv=reverse_slicing(chemin)
				tree.append(chemin_inv)
				if chemin_inv not in lp:
					l=l+1
					x='l'+str(l)	
					print('________',x)
					lp.append(chemin_inv)
					lightpaths[x]=chemin_inv
					#print('lightpaths______',lightpaths)
				break
			
			k=parent[k]
	t=0
	while t< len(parent):
		p=parent[t];
		if t!=p:
			voisin[t]=voisin[t]+str(p);
			voisin[p]=voisin[p]+str(t);
			if str(p) not in voisins[t]:
				voisins[t]=voisins[t]+str(p);
			if str(t) not in voisins[p]:
				voisins[p]=voisins[p]+str(t);
		t=t+1;
	#print('d1______________________',d)
	#print('parent__________________',parent)
	#print('tree____________________',tree)
	#print('voisin__________________',voisin)
	#print('voisins__________________',voisins)
	i=i+1
print('voisins__________________',voisins)

##############################____Algorithm de coloration____##############################

start=0
j=0
color=[0]*len(v)

def get_color(voisins,start):
	color=[0]*len(voisins)
	color[start]=1
	i=0
	while i<len(voisins):
		if i==start:
			color[start]=1
			i=i+1
		else:
			j=0
			color[i]=1;
			
			while j<len(voisins[i]):
				
				if color[i]==color[int(voisins[i][j])]:
					color[i]+=1	
				j+=1
			i+=1
	return color
get_color(voisins,start)
print('voi______________',voisins)
print('color*********************************',color)
print('lp______________',lp)
print('lightpaths______',lightpaths)

lp_graph=[]
i=0
lp_graph_num=[]
lp_voisin=['']*len(lp)
print('lp_voisin___',lp_voisin)
for i in range(len(lp)):
	j=0
	for j in range(len(lp)):
		if i!=j:
			if (lp[i] in lp[j]):
				temp=[]
				temp1=''
				temp.append('l'+str(i+1))
				temp.append('l'+str(j+1))
				
				lp_graph.append(temp)
		
				if str(j) not in lp_voisin[j]:
					lp_voisin[i]=lp_voisin[i]+str(j)
				if str(i) not in lp_voisin[j]:
					lp_voisin[j]=lp_voisin[j]+str(i)
print('lp_graph___',lp_graph)
print('lp_voisin___',lp_voisin)
lp_color=[]
lp_color=get_color(lp_voisin,start)
print('lp_color___',lp_color)
			
