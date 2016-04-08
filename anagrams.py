import sys
import crash

words = set()

allLines = ""

for line in sys.stdin:
	line = line.strip();
	allLines = allLines + " " + line

elems = allLines.split()
groupSize = 3
groups = set()

for i in range(len(elems) - (groupSize-1)):
	sentence = ""
	for j in range(groupSize):
		if j == 0:
			sentence = elems[i]
		else:
			sentence = sentence + " " + elems[i + j]
	groups.add(sentence)
# print groups

for group in list(groups):
	for group2 in list(groups):
		if group != group2 and crash.isRealAnagram(group, group2):
			same = True
			words1 = group.split()
			words1_lower = list()
			for w in words1:
				words1_lower.append(w.lower())

			words2 = group2.split()
			words2_lower = list()
			for w2 in words2:
				words2_lower.append(w2.lower())

			for w in words1_lower:
				if w not in words2_lower:
					same = False
						
			if not same:
				print group + "  -  " + group2
			# print "------------------"








