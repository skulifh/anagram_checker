#Could have done:
#Removing lines that have been read.
#Make it multi threaded. Maybe divide the file to the threads

import sys
import time
import pdb
import hashlib

hint = sys.argv[1]
hint_length = 18 #todo: Automate this
potential_words = []
log_file = open('log_file', 'w')
potential_phrases2_file = open('potential_phrases2_file', 'w')
word_file = 'wordlist'
kill = False

#Eliminating useless words. There are words in the wordfile that contain only one character. The uses this list to eliminate those apart from 'i' and 'a' which are legitimate words.
skip_words = ['b', 'b\'s', 'c', 'c\'s', 'd', 'd\'s', 'e', 'e\'s', 'f', 'f\'s', 'g', 'g\'s', 'h', 'h\'s', 'j', 'j\'s', 'k', 'k\'s', 'l', 'l\'s', 'm', 'm\'s', 'n', 'n\'s', 'o', 'o\'s', 'p', 'p\'s', 'q', 'q\'s', 'r', 'r\'s', 's', 's\'s', 't', 't\'s', 'u', 'u\'s', 'v', 'v\'s', 'x', 'x\'s', 'y', 'y\'s', 'z', 'z\'s']

#Checks if the given word can match into the given hint phrase
def included_check(word):
	consistent = True
	changed_hint = hint

	#Iterates through the characters in the hint phrase. Once a character mismatch is found it breaks and returns false
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
		
		#It would also be possible to eliminate words that contain the ' character which would eliminate many words and save a lot of run time. But since I wasn't sure I left them in.
		if ((len(word.strip()) <= hint_length) and (included_check(word)) and not (word.strip() in potential_words) and not (word.strip() in skip_words)):
			potential_words.append(word.strip())
			potential_phrases2_file.write(word.strip() + '\n')


potential_phrases2_file_second = 'potential_phrases2_file'

#todo: Combine this one with the previous one
with open(potential_phrases2_file_second, 'rw') as inline:
	for phrase in inline:

		for word in potential_words:
			copy = phrase.replace('\n', '') + ' ' + word.replace('\n', '')
			combined_word = copy.replace('\'', '').replace(' ', '')

			if (len(combined_word) <= 18) and (included_check(combined_word)):

				if len(combined_word) == 18:
					#Possible to add a checker here to kill the program once the correct hash has been found.
					log_file.write(copy + '\n')
					log_file.write(hashlib.md5(copy).hexdigest() + '\n\n')
					kill = True

				else:
					potential_phrases2_file.write(copy + '\n')

		


