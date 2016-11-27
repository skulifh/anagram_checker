import sys

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

		if included_check(word):
			potential_words.append(word.strip())


#Go through the potential words and match them together
potential_phrases = []

for word in potential_words:
	for word2 in potential_words:
		combined_word = (word + word2)
		if included_check(combined_word):
			if len(combined_word) == 18:
				final_words.append([word, word2])
			else:
				potential_phrases.append([word, word2])


# potential_phrases2 = []

# for words in potential_phrases:
# 	for word in potential_words:
# 		combined_word = ''
# 		for word2 in potential_phrases:
# 			combined_word += word2


# 		if included_check(combined_word):
# 			if len(combined_word) == 18:
# 				final_words.append([word, word2])
# 			else:
# 				potential_phrases.append([word, word2])




print final_words
print len(final_words)
print len(potential_phrases)
print counter