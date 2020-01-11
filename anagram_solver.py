from itertools import combinations
from string import ascii_lowercase as alphabet
from collections import Counter
from Trie import Trie
from itertools import permutations
from hashlib import md5
import timeit


"""
        Todo: 
            create new class: hash encoder from all anagrams
            create new class: precalc all anagrams
            create new helper class
"""

def read_words(fname):
    print('Loading file... ')
    f = open(fname, 'r')
    lines = f.read().splitlines()
    f.close()
    print("Done!")
    return lines

def trim(x):
    return "".join(x.split())

def main():

    anagrams = []

    # base_string = "poultry outwits ants"
    base_string = "poultry outwits"
    word_len = base_string.count(" ") + 1
    encoded_hash = "23170acc097c24edb98fc5488ab033fe"

    words = read_words('clean_words.dms')
    anagram_counter = Counter(trim(base_string))

    trie = Trie()

    for word in words:
        trie.add_word(word)

    print("Generating anagrams...")
    for anagram in trie.anagrams(anagram_counter, word_len = word_len):
        anagrams.append(anagram)
    print("Done!")

    print("Encoding hash: " + encoded_hash + "\n")
    for wordtup in anagrams:
       
        for anagtup in permutations(wordtup):
            anagram = ' '.join(anagtup)
            anagram_hash = md5(anagram.encode()).hexdigest()
            print("hey!!!",anagram_hash)
            if anagram_hash == encoded_hash:
                print('Target anagram found: ' + anagram)



if __name__ == '__main__':
    main()
