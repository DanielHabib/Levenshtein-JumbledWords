def levenshtein_distance(first, second):
	if len(first) > len(second):
		first, second = second, first
	if len(second) == 0:
		return len(first)
	first_length = len(first) + 1
	second_length = len(second) + 1
	distance_matrix = [[0] * second_length for x in range(first_length)]
	for i in range(first_length):
		distance_matrix[i][0] = i
		for j in range(second_length):
			distance_matrix[0][j]=j
	for i in range(1, first_length):
		for j in range(1, second_length):
			deletion = distance_matrix[i-1][j] + 1
			insertion = distance_matrix[i][j-1] + 1
			substitution = distance_matrix[i-1][j-1]
			if first[i-1] != second[j-1]:
				substitution += 1
			distance_matrix[i][j] = min(insertion, deletion, substitution)
	operations = distance_matrix[first_length-1][second_length-1]
	return (1-operations/len(s2))*100

def levenshtein_jumbledwords(self,first,second):
	#this is to handle venues that may appear like 
	#"City Hall of Dustin" Against "Dustin City Hall"
	s1 = ''
	s2 = ''
	if len(first)>len(second):
		s1=first
		s2=second
	else:
		s1=second
		s2=first
	potentialScore=0
	totalScore=0
	wordLoop1 = s1.split()
	wordLoop2 = s2.split()
	potentialScore = 100 * wordCount1
	for a in wordLoop1 :
		highestScore=0
		for b in wordLoop2 :
			score = self.levenshtein_distance(a,b)
			if score > highestScore :
				highestScore = score
		totalScore += highestScore
	return (totalScore/potentialScore)

