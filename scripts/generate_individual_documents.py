import os
from io import open # to support encoding in python 2

directory = "individual"

if not os.path.exists(directory):
	os.makedirs(directory)

documents = open("cleaned_text.txt", encoding='utf-8').read().split("\n")
n = len(documents)
print(n)
j = 1
for document in documents:
	with open(directory + '/' + str(j) + ".txt", "w", encoding='utf-8') as fout:
		fout.write(document)
	j += 1

print("Done")


