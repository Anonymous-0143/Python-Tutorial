import hashlib 
from difflib import SequenceMatcher 


def hash_file(fileName1, fileName2): 


	h1 = hashlib.sha1() 
	h2 = hashlib.sha1() 

	with open(fileName1, "rb") as file: 

	 
		chunk = 0
		while chunk != b'': 
			chunk = file.read(1024) 
			h1.update(chunk) 
			
	with open(fileName2, "rb") as file: 

		chunk = 0
		while chunk != b'': 
			chunk = file.read(1024) 
			h2.update(chunk) 

		
		return h1.hexdigest(), h2.hexdigest() 


file1, file2 = hash_file("demo1.pdf ", "demo1(2).pdf") 

if(file1 != file2): 
	print("These files are not identical") 
else: 
	print("These files are identical") 
