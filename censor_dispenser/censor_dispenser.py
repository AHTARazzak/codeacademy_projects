# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

import re


def censorword(email, word):
  wordstart=[m.start() for m in re.finditer(word, str(email_one))]
  wordlen=len(word)
  for wordlocation in wordstart:
    email=str(email)[:wordlocation]+("-"*wordlen)+str(email)[wordlocation+wordlen:]
  return email

#print(censorword(email_one,'learning algorithms'))


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censorwordlist(email, wordlist):
  smallemail=str(email).lower()
  for word in wordlist:
    wordstart=[m.start() for m in re.finditer(word, smallemail)]
    wordlen=len(word)
    for wordlocation in wordstart:
      email=email[:wordlocation]+("-"*wordlen)+email[wordlocation+wordlen:]
  return email

#print(censorwordlist(email_two, proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


def censorspecialwordlist(email, wordlist,propwordlist):
  email=str(censorwordlist(email,propwordlist))
  smallemail=str(email).lower()
  for word in wordlist:
    wordstart=[m.start() for m in re.finditer(word, smallemail)]
    wordlen=len(word)
    if len(wordstart)>1:
      for wordlocation in wordstart:
        email=email[:wordlocation]+("-"*wordlen)+email[wordlocation+wordlen:]
  return email

#print(censorspecialwordlist(email_three, negative_words,proprietary_terms))

def censorspecialwordlist2(email, wordlist,propwordlist):
  allwords=wordlist+propwordlist
  email=str(censorwordlist(email,allwords))
  splitemail=email.split()
  count=0
  for element in splitemail:
    if "-" in element:
      wordbeforelen=len(splitemail[count-1])
      splitemail[count-1]="-"*wordbeforelen
      if count<len(splitemail)-1:
        wordafterlen=len(splitemail[count+1])
        splitemail[count+1]="-"*wordafterlen
    count+=1
  return(splitemail)

#print(censorspecialwordlist2(email_three, negative_words,proprietary_terms))
