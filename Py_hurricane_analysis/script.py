import operator
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damagestocost(damageslist):
  newlist=[]
  for damages in damageslist:
    if damages[0:1].isnumeric():
      if damages[-1:]=="M":
        newlist.append(float(damages[0:-1])*1000000)
      elif damages[-1:]=="B":
        newlist.append(float(damages[0:-1])*1000000000)
    else:
      newlist.append(damages)
  return newlist
  
updated_damages=(damagestocost(damages))

# write your construct hurricane dictionary function here:

listoffeatures=[names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths]

def listsintodictionary(thefeatures):
  count=0
  hurricanes={}
  for index in range(len(listoffeatures[0])):
    hurricanes[names[index]]={}
    hurricanes[names[index]]['Name']=names[index]
    hurricanes[names[index]]['Month']=months[index]
    hurricanes[names[index]]['Year']=years[index]
    hurricanes[names[index]]['Max Sustained Wind']=max_sustained_winds[index]
    hurricanes[names[index]]['Areas Affected']=areas_affected[index]
    hurricanes[names[index]]['Damage']=updated_damages[index]
    hurricanes[names[index]]['Deaths']=deaths[index]
  return hurricanes

namehurricanedict=listsintodictionary(listoffeatures)
#print(namehurricanedict)

# write your construct hurricane by year dictionary function here:

def hurricanebyyear(hurricanelist):
  newhurricanelist={}
  for hurricane in hurricanelist:
      current_year = hurricanelist[hurricane]['Year']
      current_cane = hurricanelist[hurricane]
      if current_year not in newhurricanelist:
          newhurricanelist[current_year] = [current_cane]
      else:
          newhurricanelist[current_year].append(current_cane)
  return newhurricanelist

#print(hurricanebyyear(namehurricanedict))

# write your count affected areas function here:
def areahitcount(hurricanelist):
  arealist={}
  for h_id, h_info in hurricanelist.items():
    for area in h_info["Areas Affected"]:
      if area not in arealist:
        arealist[area] = 0
      else:
        arealist[area]+=1
  return arealist

affectedarea=areahitcount(namehurricanedict)

# write your find most affected area function here:

#print({hit: area for hit, area in sorted(affectedarea.items(), key=lambda item: item[1])})

def mosthitarea(hurricanehit):
  return (max(hurricanehit.items(), key=operator.itemgetter(1))[0]+" "+str(hurricanehit.get(max(hurricanehit.items(), key=operator.itemgetter(1))[0])))

#print(mosthitarea(affectedarea))

# write your greatest number of deaths function here:

def deaths(hurricanelist):
  deathlist={}
  for h_id, h_info in hurricanelist.items():
    deathlist[h_info["Name"]]=h_info["Deaths"]
  return (max(deathlist.items(), key=operator.itemgetter(1))[0]+" "+str(deathlist.get(max(deathlist.items(), key=operator.itemgetter(1))[0])))

#print(deaths(namehurricanedict))


# write your catgeorize by mortality function here:

def mortalityscale(hurricanelist):
  deathlist={}
  mortalitylist={0:[],1:[],2:[],3:[],4:[]}
  for h_id, h_info in hurricanelist.items():
    deathlist[h_info["Name"]]=h_info["Deaths"]
  for d_id, d_info in deathlist.items():
    if d_info==0:
      mortalitylist[0].append(d_id)
    elif 0<d_info<=100:
      mortalitylist[1].append(d_id)
    elif 100<d_info<=500:
      mortalitylist[2].append(d_id)
    elif 500<d_info<=1000:
      mortalitylist[3].append(d_id)
    elif 1000<d_info<=10000:
      mortalitylist[4].append(d_id)
  return(mortalitylist)

#print(mortalityscale(namehurricanedict))




# write your greatest damage function here:

def mostdamage(hurricanelist):
  damagelist={}
  for h_id, h_info in hurricanelist.items():
    if not h_info['Damage']=="Damages not recorded":
      damagelist[h_info["Name"]]=h_info["Damage"]
  return (max(damagelist.items(), key=operator.itemgetter(1))[0]+" "+str(damagelist.get(max(damagelist.items(), key=operator.itemgetter(1))[0])))

#print(mostdamage(namehurricanedict))



# write your catgeorize by damage function here:

def damagescale(hurricanelist):
  damagelist={}
  damagescale={0:[],1:[],2:[],3:[],4:[]}
  for h_id, h_info in hurricanelist.items():
    if not h_info['Damage']=="Damages not recorded":
      damagelist[h_info["Name"]]=h_info["Damage"]
  for d_id, d_info in damagelist.items():
    if damagescale==0:
      mortalitylist[0].append(d_id)
    elif 0<d_info<=100000000:
      damagescale[1].append(d_id)
    elif 100000000<d_info<=1000000000:
      damagescale[2].append(d_id)
    elif 1000000000<d_info<=10000000000:
      damagescale[3].append(d_id)
    elif 10000000000<d_info<=50000000000:
      damagescale[4].append(d_id)
  return(damagescale)

#print(damagescale(namehurricanedict))
