#import RAKE
import operator
import re
import os
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy
#from nltk.stem.porter import PorterStemmer

# Create p_stemmer of class PorterStemmer
#p_stemmer = PorterStemmer()

def process(line):

   stop_words = set(stopwords.words('english'))
   line=line.lower()
   stt2=''
   i=0
   stt1=''
   arr=[]
   while i<(len(line)):
      if line[i] == '.':
         stt1 += ''
      elif line[i] == ',':
         stt1 += ''
      elif line[i] == ')':
         stt1 += ''
      elif line[i] == '(':
         stt1 += ''
      elif line[i] == ':':
         stt1 += ''
      elif line[i] == '`':
         stt1 += ''
      elif line[i] == '-':
         stt1 += ''
      elif line[i] == '_':
         stt1 += ''
      elif line[i] == '!':
         stt1 += ''
      elif line[i] == ';':
         stt1 += ''
      elif line[i] == '@':
         stt1 += ''
      elif line[i] == '#':
         stt1 += ''
      elif line[i] == '$':
         stt1 += ''
      elif line[i] == '%':
         stt1 += ''
      elif line[i] == '^':
         stt1 += ''
      elif line[i] == '&':
         stt1 += ''
      elif line[i] == '*':
         stt1 += ''
      elif line[i] == '+':
         stt1 += ''
      elif line[i] == '=':
         stt1 += ''
      elif line[i] == '<':
         stt1 += ''
      elif line[i] == '>':
         stt1 += ''
      elif line[i] == '|':
         stt1 += ''
      elif line[i]=='?':
         stt1+=''
      else:
         stt1 += line[i]
      i += 1
      
   word_tokens = nltk.tokenize.word_tokenize(stt1)
   stt1=''
   for words in word_tokens:
      stt1 += words + " "
   return stt1

ind = 1
input_dir='/home/phd/tirthankar2/Ananya/RecSysAnanya/Journals/ARTINT/artint_acc_tot_json'
files=os.listdir(input_dir)
input_file=""
unikwrd=[]
bodyUnikwrd=[]
#titlearray=[]
#authorsarray=[]
#bibtitlearray=[]
#bibvenuearray=[]
#titlerakearray=[]
#bodyrakearray=[]
for f in files:
    if 'json' in f:
        with open('/home/phd/tirthankar2/Ananya/RecSysAnanya/Journals/ARTINT/artint_acc_tot_json/'+f) as input_file:
            data = (json.load(input_file))
        '''
        title= open('title.txt','a')
        title.write('\n'+f)
        
        print(f+'   '+str(ind))
        if data['metadata']['title']:
           #if str(data['metadata']['title']) not in titlearray:
               #titlearray.append(str(data['metadata']['title']))
               title.write('\n'+str(data['metadata']['title']))
        title.write('\n...\n')
        title.close()
        
        authors= open('authors.txt','a')
        authors.write('\n'+f)
        
        #print f
        if data['metadata']['authors']: 
           #if str(data['metadata']['authors']) not in authorsarray:
               #authorsarray.append(str(data['metadata']['authors']))  
               authors.write('\n'+str(data['metadata']['authors']))
        authors.write('\n...\n')
        authors.close()
        
        reftitle=open('bibtitle.txt','a')
        reftitle.write('\n'+f)
        #bibtitlearray.append(f)
        for j in range(len(data['metadata']['references'])):
            if data['metadata']['references'][j]['title']:
                p=process(data['metadata']['references'][j]['title'])
                q=str(p.encode('utf-8'))
                stt=''
                #print(len(q))
                for a in range(2,len(q)-2):
                   stt+=q[a]
                #bibtitlearray.append('title: '+stt)
                reftitle.write('\ntitle: '+stt)
                #print(stt)
                #u' '.join((agent_contact, agent_telno)).encode('utf-8').strip()
        #bibtitlearray.append('...')
        reftitle.write('\n...\n')
        reftitle.close()
        #print('reftitle')
        refvenue=open('bibvenue.txt','a')	
        #bibvenuearray.append(f)
        refvenue.write('\n'+f)
        for j in range(len(data['metadata']['references'])):
            if data['metadata']['references'][j]['venue']:
                p=process(data['metadata']['references'][j]['venue'])
                q=str(p.encode('utf-8'))
                stt=''
                #print(len(q))
                for a in range(2,len(q)-2):
                   stt+=q[a]
                refvenue.write('\nvenue: '+stt)
        #        bibvenuearray.append('venue: '+stt)
        #bibvenuearray.append('...')
        refvenue.write('\n...\n')
        refvenue.close()
        #print('refvenue')
        
        authkeyword=open('authkeywords.txt','a')
        authkeyword.write('\n'+f)
        keyref=list()
        if data['metadata']['sections']:
            keyref=re.split(r"\n",data['metadata']['sections'][0]['text'])    
            for i in range(len(keyref)):
                if(re.search(r"eyword",keyref[i])):
                    authkeyword.write('\n'+str(keyref[i]))#.encode("utf-8",errors='ignore'))
                if(re.search(r"Key word",keyref[i])):
                    authkeyword.write('\n'+str(keyref[i]))#.encode("utf-8",errors='ignore'))
        authkeyword.write('\n...\n')
        authkeyword.close()
        #print('authkwords')
        
def bib_Title(file01,file02):
  nltk.download('stopwords')
  nltk.download('punkt')
  ind1=1
  stopword=set(stopwords.words(file02))
  with open(file01) as f1:
   file1=f1.read()
   bibTextTokenize = nltk.word_tokenize(file1)
   arrayTitleName=[]
   arrayTitleFrequency=[]
   arrayUniKeyword=[]
   index=0
   #print(len(bibTextTokenize))
   for i in range(0,len(bibTextTokenize)):
     if bibTextTokenize[i].find('.json')!=-1:
        print(bibTextTokenize[i]+'   '+str(ind1))
        pp1 = bibTextTokenize[i]
        ind1 += 1
        i=i+1
        while bibTextTokenize[i]!='...':
           title=''
           if bibTextTokenize[i]=='title' and bibTextTokenize[i+1]==':':
              i=i+2
              if bibTextTokenize[i]=='title' and bibTextTokenize[i+1] != ':':
                 if bibTextTokenize[i] not in stopword:
                    title+=bibTextTokenize[i] + " "
                 i=i+1
              while bibTextTokenize[i]!='title':
                 if bibTextTokenize[i] not in stopword:
                    title+=bibTextTokenize[i] + " "
                 i=i+1
                 if bibTextTokenize[i]=='title' and bibTextTokenize[i+1] != ':':
                     if bibTextTokenize[i] not in stopword:
                        title+=bibTextTokenize[i] + " "
                     i=i+1
                 if bibTextTokenize[i]=='...':
                    break
             # print(title)
              if title in arrayTitleName:
                 index_title = arrayTitleName.index(title)
                 arrayTitleFrequency[index_title] = int(arrayTitleFrequency[index_title]) + 1
              else: 
                arrayTitleName.append(title)
                arrayTitleFrequency.append(1)
                index += 1
  #print('--------------------------------------------------------------------------------------------------------')
  input_dir='/home/phd/tirthankar2/Ananya/RecSysAnanya/Journals/ARTINT/artint_acc_tot_json'
  files=os.listdir(input_dir)
  pp2=0
  for f in files:
        with open('/home/phd/tirthankar2/Ananya/RecSysAnanya/Journals/ARTINT/artint_acc_tot_json/'+f) as fileJson:
          pp2+=1
          print(fileJson)
          print(pp2)
          data=(json.load(fileJson))
          arrayReference = []
          for j in range(0,len(data['metadata']['references'])):
              if data['metadata']['references'][j]['title']:
                p=process(data['metadata']['references'][j]['title'])
                q=str(p.encode('utf-8'))
                stt=''
                #print(len(q))
                for a in range(2,len(q)-2):
                   if bibTextTokenize[i] not in stopword:
                      stt+=q[a]		
                arrayReference.append(stt)
                #print(stt)
                
          for j in range(0,len(data['metadata']['referenceMentions'])):
              if data['metadata']['referenceMentions'][j]['referenceID']:
                  index = int(data['metadata']['referenceMentions'][j]['referenceID'])
                  t=len(arrayTitleName)
                  #print(t)
                  #for j in range(0,t):
                      #a11=[]
                      #a22=[]
                      #a1=nltk.word_tokenize(arrayReference[index])
                      #a2=nltk.word_tokenize(arrayTitleName[j])
                      #for words in a1:
                      #  a11.append(words)
                      #for words in a2:
                       # a22.append(words)
                      #if numpy.array_equal(a11,a22):
                  if str(arrayReference[index]) in list(arrayTitleName):
                #  if arrayTitleName.contains(arrayReference(index)):
                       index_title = arrayTitleName.index(str(arrayReference[index]))
                       arrayTitleFrequency[index_title] = int(arrayTitleFrequency[index_title]) + 1
                    
  titlefile=open("bib_Title_Frq.txt","w")             
  for i in range(0,len(arrayTitleName)):
      
    titlefile.write(str(arrayTitleName[i]))
    titlefile.write(":")
    titlefile.write(str(arrayTitleFrequency[i]))
    titlefile.write("\n")

  myfile2 = open("title_kwrd.txt","w")
                       
  for j in range(0,len(arrayTitleFrequency)):
     word=nltk.word_tokenize(process(arrayTitleName[j]))
     for p in word:
        if p not in arrayUniKeyword:
           if p not in stopword:
              arrayUniKeyword.append(p)
              myfile2.write(p)
              myfile2.write('\n')
  myfile2.close()
'''
def bib_Venue(file01,file02):
  
  stopword=set(stopwords.words(file02))
  nltk.download('stopwords')
  nltk.download('punkt')
  with open(file01) as f1:
   file1=f1.read()
   bibTokenize = nltk.word_tokenize(file1)
   arrayVenueName=[]
   arrayVenueFrequency=[]
   arrayUniqKeyword=[]
   index3=0
   pq=1
   for i in range(0,len(bibTokenize)):
     if bibTokenize[i].find('.json')!=-1:
        print(bibTokenize[i])
        print(pq)
        pq+=1
        i=i+1
        while bibTokenize[i]!='...':
           venue=''
           if bibTokenize[i]=='venue' and bibTokenize[i+1]==':':
              i=i+2
              if bibTokenize[i]=='venue' and bibTokenize[i+1] != ':':
                 if bibTokenize[i] not in stopword:
                    venue+=bibTokenize[i] + " "
                 i=i+1
              while bibTokenize[i]!='venue':
                 if bibTokenize[i] not in stopword:
                    venue+=bibTokenize[i] + " "
                 i=i+1
                 if bibTokenize[i]=='venue' and bibTokenize[i+1] != ':':
                     if bibTokenize[i] not in stopword:
                        venue+=bibTokenize[i] + " "
                     i=i+1
                 if bibTokenize[i]=='...':
                    break
              if venue in arrayVenueName:
                 index_venue = arrayVenueName.index(venue)
                 arrayVenueFrequency[index_venue] = int(arrayVenueFrequency[index_venue]) + 1
              else: 
                arrayVenueName.append(venue)
                arrayVenueFrequency.append(1)
                index3 += 1
  #print('--------------------------------------------------------------------------------------------------------')
   input_dir='/home/phd/tirthankar2/Ananya/RecSysAnanya/Journals/ARTINT/artint_acc_tot_json'
   files=os.listdir(input_dir)
   pp3=0
   for f in files:
        with open('/home/phd/tirthankar2/Ananya/RecSysAnanya/Journals/ARTINT/artint_acc_tot_json/'+f) as fileJson:
          pp3+=1
          print(fileJson)
          print(pp3)
          data=(json.load(fileJson))
          arrayReference1 = []
          for j in range(0,len(data['metadata']['references'])):
              if data['metadata']['references'][j]['venue']:
                p=process(data['metadata']['references'][j]['venue'])
                q=str(p.encode('utf-8'))
                stt=''
                #print(len(q))
                for a in range(2,len(q)-2):
                 if a not in stopword:
                   arrayReference1.append(q[a])
              else:
                  arrayReference1.append("null")  
          for j in range(0,len(data['metadata']['referenceMentions'])):
              if data['metadata']['referenceMentions'][j]['referenceID']:
                  index3 = int(data['metadata']['referenceMentions'][j]['referenceID'])
                  if str(arrayReference1[index3]) in list(arrayVenueName):
                     index_venue = arrayVenueName.index(arrayVenueName[j])
                     arrayVenueFrequency[index_venue] = int(arrayVenueFrequency[index_venue]) + 1
                    
   venuefile=open("bib_Venue_Frq.txt","w")             
   for i in range(0,len(arrayVenueName)):
      
      venuefile.write(str(arrayVenueName[i]))
      venuefile.write(":")
      venuefile.write(str(arrayVenueFrequency[i]))
      venuefile.write("\n")
   venuefile.close()

   myfile2 = open("venue_kwrd.txt","w")
                       
   for j in range(0,len(arrayVenueFrequency)):
       #print 'Title: ',arrayTitleName[j],'  \nFrequency: ',arrayTitleFrequency[j]
       word=nltk.word_tokenize(process(arrayVenueName[j]))
       for p in word:
          if p not in arrayUniqKeyword:
             if p not in stopword:
                arrayUniqKeyword.append(p)
                myfile2.write(p)
                myfile2.write('\n')
   myfile2.close()
'''
def textfrq(file01,file02):
 with open(file01) as f1:
   file1=f1.read()
   TextTokens= nltk.word_tokenize(file1)
 with open(file02) as f2:
     file2=f2.read()
     TextTokens2=nltk.word_tokenize(file2)
 ff=open('frqscr',"w")
 for i in range(0,len(TextTokens2)):
   count=0
   for j in range(0,len(TextTokens)):
       if TextTokens2[i]==TextTokens[j]:
            count+=1
   ff.write(TextTokens2[i])
   ff.write(' '+str(count))
   ff.write("\n")
 ff.close()
'''
#print('calling bibtitle\n')      
#bib_Title("bibtitle.txt","SmartStoplistvenue.txt")
print('calling bibvenue\n')
bib_Venue("bibvenue.txt","SmartStoplistvenue.txt")
#print('freqncy score')
#textfrq("bib_Title_Frq.txt","title_kwrd.txt")
#textfrq("bib_Venue_Frq.txt","venue_kwrd.txt")
