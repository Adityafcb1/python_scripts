import fileinput

def wordc(fname, word_count):
	
	#Taking one word at a time from the list
	for i in word_count:
		count = 0
	
		#Reading the file 
		with open(fname, 'r') as f:

			#Spliting the file into line and words and replacing punctuation with space
			for line in f:
				words = line.replace(',','').replace('.','').replace('?','').split()
				
				#Taking one word at a time from the file and making it in lowercase to avoid mismatch
				for j in words:
					b = j.lower()

					#Comparing each word in file with the input word
					if(b==i):
						count = count + 1
		print(i, "occurs", count, "times")


#Enter file location and word list
fname = input("Enter file name: ")
word=[]

#no.of words you want to search
n =int(input("Enter the no.of words you want to search:"))
x = 0

#Inputing the word we want to search
for i in range(1,n+1):
	a = input(f"{i} Word: ")
	word.append(a)

#Calling the function
a = wordc(fname, word)
