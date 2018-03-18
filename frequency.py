import nltk

def frq1(file01,file02,file03):
 with open(file01) as f1:
   file1=f1.read()
   ind=0
   TextTokens= nltk.word_tokenize(file1)

 with open(file02) as f2:
     file2=f2.read()
     TextTokens2=nltk.word_tokenize(file2)
 ff=open(file03,"w")
 for i in range(0,len(TextTokens2)):
   count=0
   flg=0
   ind=ind+1
   print(ind)
   for j in range(0,len(TextTokens)):
     try:
       p=int(TextTokens2[i])
       TextTokens.remove(TextTokens2[i])
       flg=1
     except:  
       if TextTokens2[i]==TextTokens[j]:
          count+=1
     if flg == 1:
          break
   if count!=0:
     ff.write(TextTokens2[i])
     ff.write(' '+str(count))
     ff.write("\n")
     
   #print(TextTokens2[i])    
 ff.close()

def frq2(file01,file02,file03):
   file1=open(file01,'r').readlines()
   file2=open(file02,'r').readlines()
   ff=open(file03,"w")
   ind=0
   for i in file2:
      #print(i)
      count=0
      ind+=1
      print(ind)
      for j in file1:
          if j==i:
            count+=1
          #print j
      #ff.write(i)
      ff.write(i+str(count))
      #ff.write()
      ff.write("\n")
   ff.close()
   

def frequency(file1):

  x=nltk.word_tokenize(file1)
  ls=[]
  ls2=[]
  ff=open('authklist','w')
  for c,val in enumerate(x):
    if val=='Keywords' and x[c+1]==':':
      ls.append(c+2)
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
  

def unikfrq(file01):
   rt=open('authuni.txt','w')
   fil=open(file01,'r')
   print(fil)
   newlst = []

   for word in fil:
      print(word)
      if word not in newlst:
            newlst.append(word)
            rt.write(word)
           
   rt.close()

def frq3(file01,file02):
   file1=open(file01,'r').readlines()
   file2=open(file02,'r').readlines()
   ff=open('auth_uni_frq',"w")
   for i in file2:
      print(i)
      count=0
      for j in file1:
          if j==i:
            count+=1
      ff.write(i+str(count))
      ff.write("\n")
   ff.close()

at=open('authkeywords.txt','r').read()
print(at)

#frequency(at)

#unikfrq('authklist')

#frq3('authklist','authuni.txt')


#frq1('bib_Title_Frq.txt','title_kwrd.txt','title_Uni_Kwd_Frq.txt')

#frq1('bib_Venue_Frq.txt','venue_kwrd.txt','venue_Uni_Kwd_Frq.txt')

#frq2('bodyAllKwd.txt','bodyUnqKwd.txt','bodyfrqscr')

frq2('titleAbstractAllKwd.txt','titleAbstractUniqKwd.txt','titleAbstractfrqscr')

print('complete')


