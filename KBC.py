#instructions 
i=["Rules for playing KBC:-","1> You have to answer the questions on your screen by","selecting your option and type the option using 'A', 'B', 'C', 'D', ", "If at any question you want not to answer and choose", "the safe path (as in real kbc show) type'0'","That's all!!! 🤗", "try to win as many price as you can👍 Have fun"]
#i set above list according to mobile in order to set in screen frame u can modify according to your situation by merging index[ 0] and [1] in 1 index also index [2] and [3] in another index but leave the rest 
print(i[0]) 
print(i[1]) 
print(i[2]) 
print(i[3]) 
print(i[4]) 
print(i[5]) 
print(i[6]) 
#list for questions 
q=[
["1. What does not grow on tree according to a popular Hindi saying?","A. Money","B. Flowers","C. Leaves","D. Fruits"],
["2. Which god is also known as ‘Gauri Nandan’?","A. Agni","B. Indra","C. Hanuman","D. Ganesha"],
["3. Which city is known as Pink City in India","A. Banglore","B. Maysore","C. Jaipur","D. Kochi"],
["4.Who wrote Vande Mataram?","A.Sarat Chandra Chattopadhyay", "B.Rabindranath Tagore", "C.Bankim Chandra Chatterjee", "D.Ishwar Chandra Vidyasagar" ], 
["5.Which city is known as the 'Silicon Valley Of India'?","A. Delhi","B. Mumbai","C. Chennai","D. Bangalore "], 
["6.How many religions are there in India?","A.6","B.7", "C.8", "D.9" ], 
["7.Which day is observed as the World Standards  Day?", "A.	June 26", "B.	Oct 14", "C. Nov 15", "D.	Dec 2"], 
["8.Which of the following musical instruments is NOT of foreign origin?","A.Tabla", "B.Flute", "C.Sitar", "D.Violin"], 
["9.Which Indian city hosts Indian movie industry?", "A.Goa", "B.Mumbai", "C.Chennai", "D.Calcutta"], 
["10.Current Railway Minister of India is ", "A.Mamta Banarjee", "B.Ram Vilash", "C.Ashwini Vaishnaw", "D.Piyush Goyal"], 
["11.When is the National Hindi Diwas celebrated?", "A.13 September", "B.14 September", "C.14 July", "D.15 August"], 
["12.Which one of the following places is famous for the Great Vishnu Temple?", "A.Bordubar, Indonesia", "B.Bamiyan, Afghanistan", "C.Panja Sahib, Pakistan", "D.Ankorvat, Cambodia"]


]
#list for answers
a=["a","d","c","c","d","a","b","b", "b","c","b","d"]
#list for prize
money=["5000","10000","20000","40000","80000","160000","320000", "640000","1250000","2500000","5000000","1crore",]
mn=0

for i in range(0,len(q)):
  qu=q[i]
  print(qu[0])
  print(qu[1])
  print(qu[2])    #for questions to
  print(qu[3])    #appear
  print(qu[4])
  b= input("type you ans:")
  b=b.lower()
  #statements for correct answer
  if b==a[i]:
    print("correct 💯")
    print("you earn",money[i])
    if i==3:
      mn=40000
    elif i==7:
      mn=640000
    elif i==12:
      mn="1crore"
 #statements for incorrect answer of dropping from game
  elif b!=a[i]:
    if b=="0":
      print(i)
      if i!=0:
        new_i= i-1
        mn=money[new_i]
      print("Alas! Well.. The correct answer is ",a[i])
    else:
      print("wrong!")
      print("The correct answer is ", a[i])
    break
print("your go home money is", mn) 
    
    
    
    