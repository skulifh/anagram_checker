import sys
import pdb

hint = sys.argv[1]
hint_length = 18
potential_words = []
final_words = []

word_file = 'wordlist'
counter = 0

# def find_next_potential_words(word_list = []):
# 	for pot_word in potential_words:

def included_check(word):
	consistent = True
	changed_hint = hint

	for character in word.strip():
		if (character in changed_hint or character == '\''):
			changed_hint = changed_hint.replace(character, '', 1)

		else:
			consistent = False
			break

	return consistent


#Find all the words that have characters that fit in the hint phrase
with open(word_file) as infile:
	for word in infile:
		counter += 1

		if ((len(word) <= hint_length) and (included_check(word))):
			potential_words.append(word.strip())


#Go through the potential words and match them together
potential_phrases = []

for word in potential_words:
	for word2 in potential_words:
		combined_word = (word + word2).replace('\'', '')

		if len(combined_word) <= hint_length and included_check(combined_word):
			if len(combined_word) == hint_length:
				final_words.append([word, word2])
			else:
				potential_phrases.append([word, word2])

print 'finished first check'
#print potential_phrases
print potential_phrases[4000:5000]


# potential_phrases2 = []

# for phrase in potential_phrases[1000:1010]:
# 	for word in potential_words:
# 		cop = phrase
# 		combined_word = word
# 		for word2 in phrase:
# 			combined_word = combined_word + word2

# 		cop.append(word)




#-----------



# for words in potential_phrases[:10]:
# 	for word in potential_words:
# 		combined_word = word
# 		for word2 in words:
# 			combined_word = combined_word + word2
# 		print words, word
# 		print combined_word
# 		print '\n'

# 		if (len(combined_word) < 18) and (included_check(combined_word)):
# 			words.append(word)
# 			if len(combined_word) == 18:
# 				final_words.append(words)
# 				#print 'final: ', words
# 			else:
# 				potential_phrases2.append(words)
# 				#print 'potential: ', words











