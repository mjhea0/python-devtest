

def vowel_counter(str):
    
	vowel_freqs = {}
	vowel_list = ['a', 'e', 'i', 'o', 'u']
	for word in str:
		str_list = str.split()
		for v in vowel_list:
			f = word.find(v)
			if f !=-1:
				if v in vowel_freqs:
					vowel_freqs[v] += 1
				else:
					vowel_freqs[v] = 1

	for key,value in vowel_freqs.items():
		print key, value
		
		
if __name__ == '__main__':
	str = raw_input("Please input a string: ")
	vowel_counter(str)
	
   
