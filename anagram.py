import sys
import time
import pdb

hint = sys.argv[1]
hint_length = 18
potential_words = []
final_words = []

word_file = 'wordlist'
counter = 0

skip_words = ['b', 'b\'s', 'c', 'c\'s', 'd', 'd\'s', 'e', 'e\'s', 'f', 'f\'s', 'g', 'g\'s', 'h', 'h\'s', 'j', 'j\'s', 'k', 'k\'s', 'l', 'l\'s', 'm', 'm\'s', 'n', 'n\'s', 'o', 'o\'s', 'p', 'p\'s', 'q', 'q\'s', 'r', 'r\'s', 's', 's\'s', 't', 't\'s', 'u', 'u\'s', 'v', 'v\'s', 'x', 'x\'s', 'y', 'y\'s', 'z', 'z\'s']
#1522726

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

print len(potential_words)


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

print '\nfinished first check\n'
print len(potential_phrases)
print final_words
print '-------------'
#print potential_phrases


potential_phrases2 = []

# for phrase in potential_phrases:
# 	for word in potential_words:
# 		bla = phrase[:]
# 		bla.append(word)
# 		print bla
counter = 0

start = time.time()
while potential_phrases != []:
	for phrase in potential_phrases[:1000]:

		for word in potential_words:
			combined_word = word
			for word2 in phrase:
				combined_word = combined_word + word2

			if (len(combined_word) <= 18) and (included_check(combined_word)):
				copy = phrase[:]
				copy.append(word)
				

				if len(combined_word) == 18:
					final_words.append(copy)
					#print 'final: ', words
				else:
					potential_phrases2.append(copy)
					#print 'potential: ', words

	potential_phrases = potential_phrases2
	potential_phrases2 = []
stop = time.time()

#print potential_phrases2
print len(potential_phrases)

print len(final_words)

print stop-start
#print final_words


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











