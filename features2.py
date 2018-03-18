import rake
import operator
import os
import json
import nltk
import re
from nltk.stem.porter import PorterStemmer


p_stemmer = PorterStemmer()
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
count=0

for f in files:
    if 'json' in f:
        with open('/home/phd/tirthankar2/Ananya/RecSysAnanya/Journals/ARTINT/artint_acc_tot_json/'+f) as input_file:
            data = (json.load(input_file))
        count+=1
        print(f+'   '+str(count))
        
        bodykword=open('bodyrakekwords.txt','a')
        bodykword.write('\n'+f)
        textfile3 = open('bodyUnqKwd.txt','a')
        textfile4 = open('bodyAllKwd.txt','a')
        if data['metadata']['sections']:
            text=["" for col in range(len(data['metadata']['sections']))]
            rake_object = rake.Rake("SmartStoplist.txt",3,3,1)
            for i in range(len(data['metadata']['sections'])):
                text[i]= str(data['metadata']['sections'][i]['text'].encode('UTF-8'))
            conctext=" ".join(text)
            keyword3=rake_object.run(conctext)
            for i in range(len(keyword3)):
                kwd = keyword3[i]
                if kwd[1]>=1:
                  cbodyToken=nltk.word_tokenize(kwd[0])
                  strBody=''
                  for k in cbodyToken:
                    #try:
                      #strBody+=p_stemmer.stem(k)+ ' '
                    #except:
                      strBody+=k+' '
                  if strBody[:-1] not in bodyUnikwrd:
                      print(strBody[:-1])
                      bodyUnikwrd.append(strBody[:-1])
                      textfile3.write(strBody[:-1])
                      textfile3.write('\n')
                  textfile4.write(strBody[:-1])
                  textfile4.write('\n')
                      
                  #bodyrakearray.append(str(keyword3[i]))
                  bodykword.write('\n'+str(keyword3[i]))
        #bodyrakearray.append('...')
        bodykword.write('\n...\n')
        bodykword.close()
        textfile3.close()
        textfile4.close()
        
        h=data['metadata']['abstractText']
        text=str(h)
        textfile1 = open('titleAbstractUniqKwd.txt','a')
        textfile2 = open('titleAbstractAllKwd.txt','a')
        bodykword=open('abstractkwords.txt','a')
        bodykword.write('\n'+f)
      
        if text != 'None':   
          rake_object = rake.Rake("SmartStoplist.txt",3,3,1)
          keyword=rake_object.run(text)
        for i in range(len(keyword)):
           kwd = keyword[i]
           if kwd[1] >= 1: 
              cabstractToken=nltk.word_tokenize(kwd[0])
              strAbstract=''
              for k in cabstractToken:
                #try:
                  #strAbstract+=p_stemmer.stem(k)+ ' '
                #except:
                  strAbstract+=k+' '
              if strAbstract[:-1] not in unikwrd:
                unikwrd.append(strAbstract[:-1])
                textfile1.write(strAbstract[:-1])
                textfile1.write('\n')
              textfile2.write(strAbstract[:-1])
              textfile2.write('\n')
              #titlerakearray.append(str(kwd))
              bodykword.write('\n'+str(kwd))
        bodykword.write('\n...\n')
        bodykword.close()
        s=data['metadata']['title']

        text2=str(s)
        bodykword2=open('titlerakekwords2.txt','a')
    
        bodykword2.write('\n'+f)
        if s != 'None':
            rake_object2 = rake.Rake("SmartStoplist.txt",3,3,1)
            keyword2=rake_object2.run(text2)
        for i in range(len(keyword2)):
           kwd = keyword2[i]
           if kwd[1] >= 1: 
               ctitleToken=nltk.word_tokenize(kwd[0])
               strTitle=''
               for k in ctitleToken:
                 #try:
                   #strTitle+=p_stemmer.stem(k)+ ' '
                 #except:
                 strTitle+=k + ' '
               if strTitle[:-1] not in unikwrd:
                 unikwrd.append(strTitle[:-1])    
                 textfile1.write(strTitle[:-1])
                 textfile1.write('\n')
               textfile2.write(strTitle[:-1])
               textfile2.write('\n')
              
               bodykword2.write('\n'+str(keyword2[i]))
           
        bodykword2.write('\n...\n')
        bodykword2.close()
        textfile1.close()
        textfile2.close()
        
print('Complete')
