import pandas as pd
pd.set_option('display.max_colwidth', -1)

jep=pd.read_csv('jeopardy.csv')
#print(jep.head(10))
#print(jep.describe())
print(len(jep))
#for col in jep.columns: 
    #print(col) 

list=["King","England"]
#def filterquestions(db,wordlist):
#  for word in wordlist:
#    db[' Question']=db[' Question'].str.lower()
#    db=db[~db[' Question'].str.contains(word.lower())]
#  return db
def filterquestions(db,wordlist):
  db[' Question']=db[' Question'].str.lower()
  db[' Value']= db[' Value'].map(lambda x: x.strip('$,'))
  db[' Value']= db[' Value'].str.replace(",", "")
  if type(db[' Value'])=="str":
    db[' Value']=pd.to_numeric(db[' Value'], downcast="float")
  for word in wordlist:
    db=db[db[' Question'].str.contains(word.lower())]
  return db

newjep=filterquestions(jep,list)
print(len(newjep))
print(newjep[' Value'].mean())
print(newjep[' Answer'].nunique())
#print(len(jep))
#def filterquestions(db,wordlist):
  #db[' Question']=db[' Question'].str.lower()
  #db=db[' Question'].isin(wordlist)
  #return db
#jep=jep[jep[' Question'].isin(list)]
#newjep=filterquestions(jep,list)
#print(len(newjep))
#newjep=filterquestions(jep,list)
#print(len(newjep))
