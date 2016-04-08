def getShortest(part1, part2):
	if len(part1) <= len(part2):
		return part1
	else:
		return part2

def getLongest(part1, part2):
	if len(part1) >= len(part2):
		return part1
	else:
		return part2

def noSpace(string):
	parts = string.split()
	out = ""
	for word in parts:
		for letter in word:
			out = out + letter
	return out

def tallyLetters(part):
	letters = noSpace(part)
	count = dict()
	for letter in letters:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
	return count

# anagrams : defined as words made from the letters of another word. 
# isAnagram(): an anagram does not have to use all the letters of the parent word.
# isRealAnagram(): an anagram does have to use all the letters of the parent word.

def isAnagram(basePart, part):
	basePart = basePart.lower()
	part = part.lower()
	if len(noSpace(basePart)) < len(noSpace(part)):
		return False
	count_part = tallyLetters(part)
	count_base = tallyLetters(basePart)
	for letter in count_part:
		if letter in count_base:
			if count_part[letter] > count_base[letter]:
				return False
		else:
			return False
	return True

def isRealAnagram(basePart, part):
	basePart = basePart.lower()
	part = part.lower()
	if len(noSpace(basePart)) < len(noSpace(part)):
		return False
	count_part = tallyLetters(part)
	count_base = tallyLetters(basePart)
	for letter in count_base:
		if letter in count_part:
			if count_part[letter] > count_base[letter] or count_part[letter] < count_base[letter]:
				return False
		else:
			return False
	return True	

def zip(part1, part2):
	shortword = getShortest(part1, part2)
	longword = getLongest(part1, part2) 
	zipped = ""
	for i in range(len(shortword)):
		zipped = zipped + part1[i] + part2[i]
	zipped = zipped + longword[i:]
	print zipped


