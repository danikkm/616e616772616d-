from itertools import combinations

from trie import Trie
from encoder import Encoder
from generator import Generator
import helper as h
from itertools import permutations
import timeit


def main():
    generator = Generator()
    encoder = Encoder()
    anagrams = []
    base_string = "poultry outwits ants"
    encoded_md5hash = "23170acc097c24edb98fc5488ab033fe"
    word_len = base_string.count(" ") + 1

    try:
        f = open('set_of_' + str(word_len) + "_anagrams.dms")
        for line in f:
            anagrams.append(tuple(line.strip().split(' ')))
        encoder.run(base_string, encoded_md5hash)
    except IOError:
        print("File not found, generating...")
        generator.run(base_string)
        f = open('set_of_' + str(word_len) + "_anagrams.dms")
        for line in f:
            anagrams.append(tuple(line.strip().split(' ')))
        encoder.run(base_string, encoded_md5hash)


if __name__ == '__main__':
    main()
