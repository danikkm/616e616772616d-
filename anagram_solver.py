from itertools import combinations
from string import ascii_lowercase as alphabet
from collections import Counter
from Trie import Trie
import helper as h
from itertools import permutations
from hashlib import md5
import timeit 


"""
        Todo: 
            create new class: hash encoder from all anagrams
"""

def main():

    anagrams = []
    base_string = "poultry outwits ants"
    word_len = base_string.count(" ") + 1
    
    encoded_hash = "23170acc097c24edb98fc5488ab033fe"

    try:
        f = open('set_of_' + str(word_len) + "_anagrams.dms")
        for line in f:
            anagrams.append(tuple(line.strip().split(' ')))

    except FileNotFoundError:
        words = h.read_words('clean_words.dms')
        anagram_counter = Counter(h.trim(base_string))

        trie = Trie()

        for word in words:
            trie.add_word(word)

        print("Generating anagrams...")
        for anagram in trie.anagrams(anagram_counter, word_len = word_len):
            anagrams.append(anagram)
        print("Done!")

    print("Encoding hash: " + encoded_hash + "\n")
    for wordtuple in anagrams:
        for anagtuple in permutations(wordtuple):
            anagram = ' '.join(anagtuple)
            anagram_hash = md5(anagram.encode()).hexdigest()
            if anagram_hash == encoded_hash:
                print('Target anagram found: ' + anagram)

if __name__ == '__main__':
    main()
