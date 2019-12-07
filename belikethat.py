import numpy as np

phrase="it really do be like that sometimes"
arr=phrase.split(" ")

np.random.shuffle(arr)

for word in arr:
	print(word, end=" ")
