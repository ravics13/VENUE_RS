# extracting the features author keyword list, bib-title & bib-venue frequency list for the candidate paper


import nltk
import re
import json
import os
from nltk.corpus import stopwords

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

def frequency(file1):

  x=nltk.word_tokenize(file1)
  print x
  ls=[]
  ls2=[]
  for c,val in enumerate(x):
    if val=='Keywords' and x[c+1]==':':
      ls.append(c+2)
      for i in range(c,len(x)):
        if x[i]=='...':
          ls2.append(i)
          break
    elif val=='Key' and x[c+1]=='words':
      ls.append(c+3)
      for i in range(c,len(x)):
        if x[i]=='...':
          ls2.append(i)
          break
  fl=[]
  for i in range(0,len(ls)):
    st=''
    for j in range(ls[i],ls2[i]+1):
      if x[j]!=';' and x[j]!='...' and x[j]!=',':
        st+=str(x[j])+str(' ')
      if x[j]==';' or x[j]=='...' or x[j]==',':
        fl.append(st)
        print(st)
        ff.write(st)
        ff.write('\n')
        st=''
  ff.close()
  #print fl



def unikfrq(file01):
   rt=open('candidate_authuni.txt','w')
   fil=open(file01,'r')
   print(fil)
   newlst = []
   #y=nltk.word_toke
   #frequency = []
   for word in fil:#(0,len(fil)):
      print(word)
      if word not in newlst:
            newlst.append(word)
            rt.write(word)
            #rt.write('\n')
   rt.close()



def textfrq(file01,file02):
   file1=open(file01,'r').readlines()
   file2=open(file02,'r').readlines()
   ff=open('candidate_auth_uni_frq',"w")
   for i in file2:
      print(i)
      count=0
      for j in file1:
          if j==i:
            count+=1
      #ff.write(i)
      ff.write(i+str(count))
      ff.write("\n")
   ff.close()

def authKwrd(data1):
   authkeyword=open('candidate_authkeywords.txt','a')
   authkeyword.write('\n'+f)
   keyref=list()
   if data1['metadata']['sections']:
       keyref=re.split(r"\n",data1['metadata']['sections'][0]['text']) 
       for i in range(len(keyref)):
          if(re.search(r"Key words:",keyref[i])):
             authkeyword.write('\n'+str(keyref[i]))#.encode("utf-8",errors='ignore'))
          elif(re.search(r"Keywords:",keyref[i])):
             authkeyword.write('\n'+str(keyref[i]))#.encode("utf-8",errors='ignore'))
   authkeyword.write('\n...\n')
   authkeyword.close()

def titleKwrd(data):
   stopword=set(stopwords.words('english'))
   bib_Title_Array = []
   bib_Title_Frq = []
   bib_title_uni_array = []
   bib_title_uni_kwd = []
   for j in range(len(data['metadata']['references'])):
       if data['metadata']['references'][j]['title']:
           p=process(data['metadata']['references'][j]['title'])
           q=str(p.encode('utf-8'))
           stt=''
           for a in range(2,len(q)-2):
              stt+=q[a]
           if len(stt) <> 0:
              bib_Title_Array.append(stt)
           else:
              bib_Title_Array.append('None')
           bib_Title_Frq.append(0)

   for j in range(0,len(data['metadata']['referenceMentions'])):
         if data['metadata']['referenceMentions'][j]['referenceID']:
             index = int(data['metadata']['referenceMentions'][j]['referenceID'])
             bib_Title_Frq[index]  = int(bib_Title_Frq[index]) + 1
   for i in range(0,len(bib_Title_Array)):
       if bib_Title_Array[i] not in bib_title_uni_array:
         bib_title_uni_array.append(bib_Title_Array[i])
       else:
         index2 = bib_title_uni_array.index(bib_Title_Array[i])
         bib_Title_Frq[index2]  = int(bib_Title_Frq[index2]) + 1
              
   title=open('bib_Title_Frq.txt','w')
   for i in range(0,len(bib_title_uni_array)):
      title.write(bib_title_uni_array[i]+'\n')
      title.write(str(bib_Title_Frq[i])+'\n')
   title.close()


   myfile2 = open("titlekwrd.txt","w")
                       
   for j in range(0,len(bib_title_uni_array)):

       word=nltk.word_tokenize(process(bib_title_uni_array[j]))
       for p in word:
          if p not in bib_title_uni_kwd:
             if p not in stopword:
                bib_title_uni_kwd.append(p)
                myfile2.write(p)
                myfile2.write('\n')
   myfile2.close()

def venueKwrd(data):
   stopword=set(stopwords.words('english'))
   bib_Venue_Array = []
   bib_Venue_Frq = []
   bib_venue_uni_array = []
   bib_venue_uni_kwd = []
   for j in range(len(data['metadata']['references'])):
       if data['metadata']['references'][j]['venue']:
           p=process(data['metadata']['references'][j]['venue'])
           q=str(p.encode('utf-8'))
           stt=''
           for a in range(2,len(q)-2):
              stt+=q[a]
           if len(stt) <> 0:
              bib_Venue_Array.append(stt)
           else:
              bib_Venue_Array.append('None')
           bib_Venue_Frq.append(0)

   for j in range(0,len(data['metadata']['referenceMentions'])):
         if data['metadata']['referenceMentions'][j]['referenceID']:
             index = int(data['metadata']['referenceMentions'][j]['referenceID'])
             bib_Venue_Frq[index]  = int(bib_Venue_Frq[index]) + 1
   for i in range(0,len(bib_Venue_Array)):
       if bib_Venue_Array[i] not in bib_venue_uni_array:
         bib_venue_uni_array.append(bib_Venue_Array[i])
       else:
         index2 = bib_venue_uni_array.index(bib_Venue_Array[i])
         bib_Venue_Frq[index2]  = int(bib_Venue_Frq[index2]) + 1
              
   venue=open('bib_Venue_Frq.txt','w')
   for i in range(0,len(bib_venue_uni_array)):
      venue.write(bib_venue_uni_array[i]+'\n')
      venue.write(str(bib_Venue_Frq[i])+'\n')
   venue.close()


   myfile2 = open("venuekwrd.txt","w")
                       
   for j in range(0,len(bib_venue_uni_array)):

       word=nltk.word_tokenize(process(bib_venue_uni_array[j]))
       for p in word:
          if p not in bib_venue_uni_kwd:
             if p not in stopword:
                bib_venue_uni_kwd.append(p)
                myfile2.write(p)
                myfile2.write('\n')
   myfile2.close()


input_dir='art_test'
files=os.listdir(input_dir)
for f in files:
    if 'json' in f:
        print(f)
        with open('art_test/'+f) as input_file:
            data = (json.load(input_file))
        authKwrd(data)     
        ff=open('candidate_authklist','w')
        at=open('candidate_authkeywords.txt','r').read()
        print(at)
        frequency(at)
        print('frequency found')
        unikfrq('candidate_authklist')
        print('Unique Keyword found')
        textfrq('candidate_authklist','candidate_authuni.txt')
        print('frequency')
        authors= open('authors.txt','w')
        #authors.write('\n'+f)
        if data['metadata']['authors']:
           txt = str(data['metadata']['authors'])
           print txt
           txt = txt.replace("'",".")
           for i in range(1,len(txt)):
               if txt[i] == 'u' and txt[i+1] == '.':
                  i+=2
                  auth_Name=''
                  while txt[i] != ",":
                     if txt[i]==']':
                       break
                     auth_Name += txt[i]
                     i=i+1      
                  i=i+1
                  authors.write(auth_Name[:-1]+'\n')
        authors.close()
     
        bib_Title_Array = []
        bib_Title_Frq = []
        #
        #reftitle.write('\n'+f)
        #bibtitlearray.append(f)
        for j in range(len(data['metadata']['references'])):
            if data['metadata']['references'][j]['title']:
                p=process(data['metadata']['references'][j]['title'])
                q=str(p.encode('utf-8'))
                stt=''
                for a in range(2,len(q)-2):
                   stt+=q[a]
                if len(stt) <> 0:
                   bib_Title_Array.append(stt)
                else:
                   bib_Title_Array.append('None')
                bib_Title_Frq.append(0)
                #reftitle.write('\ntitle: '+stt)
        #bibtitlearray.append('...')
        #reftitle.write('\n...\n')
        #reftitle.close()
        print len(bib_Title_Array)
        for j in range(0,len(data['metadata']['referenceMentions'])):
              if data['metadata']['referenceMentions'][j]['referenceID']:
                  index = int(data['metadata']['referenceMentions'][j]['referenceID'])
                  bib_Title_Frq[index]  = int(bib_Title_Frq[index]) + 1
        
        title=open('bib_Title_Frq.txt','w')
        for i in range(0,len(bib_Title_Array)):
           title.write(bib_Title_Array[i]+'\n')
           title.write(str(bib_Title_Frq[i])+'\n')
        title.close()
        titleKwrd(data)
        venueKwrd(data)
        




