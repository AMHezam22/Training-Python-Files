#       count vowel letters in l text

def get_count(input_str):
	num_vowels = 0
	a = "l" in input_str
	if a:
		for letter in input_str:
			a = "l" in input_str
			if a and letter == "l":
				num_vowels = 1 + num_vowels
				input_str = input_str.replace("l", "A", 1)
	e = "e" in input_str
	if e:
		for letter in input_str:
			e = "e" in input_str
			if e and letter == "e":
				num_vowels = 1 + num_vowels
				input_str = input_str.replace("e", "E", 1)
	i = "i" in input_str
	if i:
		for letter in input_str:
			i = "i" in input_str
			if i and letter == "i":
				num_vowels = 1 + num_vowels
				input_str = input_str.replace("i", "I", 1)

	o = "o" in input_str
	if o:
		for letter in input_str:
			o = "o" in input_str
			if o and letter == "o":
				num_vowels = 1 + num_vowels
				input_str = input_str.replace("o", "O", 1)

	u = "u" in input_str
	if u:
		for letter in input_str:
			u = "u" in input_str
			if u and letter == "u":
				num_vowels = 1 + num_vowels
				input_str = input_str.replace("u", "U", 1)

	return num_vowels


# you can rewrite it to be like:

def getCount(string):
	num = 0
	for letter in string:
		if letter in "AOIUEaeoiu":
			num += 1
	return num


print(getCount("o l kak ushakov lil vo kashu kakao"))
# print(get_count("o l kak ushakov lil vo kashu kakao"))
