#Notes:
#This program first eliminates all the word from the given word file to minimize the work needed. It does this by removing
#any words from the wordfile that contains characters that are not a part of the given hint phrase. It also elimintaes all 
#single character words such as 'a', 'b', or 'c's' but leaves in 'i' and 'a'. It also eliminates all duplications.

#When the program finds an anagram that contain excatly as many letters as the given hint phrase (18 character long) it checks
#the corresponding hash and logs the word and the hash into a file. If the hash is the same as the given hint hash then the program
#shuts down since it has completed it's task.

#The program does not use very little RAM memory but instead uses the hard disk space since that is just as quick in this case,
#and using RAM would be very bad since we have to work with huge amount of data later on.

#The program only uses a single thread. It would be possible to make this run on many concurrent threads since it the nature
#of this data analysis is not dependent on anything that it does previously.

#The program took around 45 minutes to find the secret phrase on a single CPU. It takes around 24 hours to go through
#the whole word file to find all possible anagrams of the given hint phrase. 

#-----------

#How to run:
#python anagram.py 'poultry outwits ants'

#-----------

#Requirements:
#Python 2.7.10

import sys
import hashlib

hint = sys.argv[1]
hint_length = len(hint.strip().replace(' ', '').replace('\'', ''))
potential_words = []
log_file = open('log_file', 'w')
potential_phrases2_file = open('potential_phrases2_file', 'w')
word_file = 'wordlist'
kill = False
target_hash = '4624d200580677270a54ccff86b9610e'

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


#Find all the words from the word file that have characters that fit in the hint phrase
with open(word_file) as infile:
	for word in infile:
		
		#It would also be possible to eliminate words that contain the ' character which would eliminate many words and save a lot of run time. But since I wasn't sure I left them in.
		if ((len(word.strip()) <= hint_length) and (included_check(word)) and not (word.strip() in potential_words) and not (word.strip() in skip_words)):
			potential_words.append(word.strip())
			potential_phrases2_file.write(word.strip() + '\n')


potential_phrases2_file_second = 'potential_phrases2_file'

#Going through the words found and combining to see what phases fit into the given hint
with open(potential_phrases2_file_second, 'rw') as inline:
	for phrase in inline:

		for word in potential_words:
			copy = phrase.replace('\n', '') + ' ' + word.replace('\n', '')
			combined_word = copy.replace('\'', '').replace(' ', '')

			if (len(combined_word) <= 18) and (included_check(combined_word)):

				if (len(combined_word) == 18):
					#Adding all phrases that are complete anagrams of the given phrase into a file
					log_file.write(copy + '\n')
					log_file.write(hashlib.md5(copy).hexdigest() + '\n\n')

					#If we find the given hash we kill the program since we have found the phrase we are looking for
					if (hashlib.md5(copy).hexdigest() == target_hash):
						kill = True
						break

				else:
					#Adding the phrases that fit into the given hint phrase into a file to be read and checked later
					potential_phrases2_file.write(copy + '\n')
		if kill:
			break



