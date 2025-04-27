#4. Write a program that checks if a given word is a Python keyword.
import keyword as key
keywords = key.kwlist
keyword_1 = "if"
keyword_2 = "swabira"
def ISKEY(keyword_1):
	if (keyword_1 in keywords):
		print(keyword_1,"is a keyword")
	else:
		print(keyword_1,"is not a keyword")

ISKEY(keyword_1)
ISKEY(keyword_2)
