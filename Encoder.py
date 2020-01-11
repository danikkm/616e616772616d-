from itertools import permutations
from hashlib import md5


class Encoder:
    def __init__(self):
        self.anagrams = []
        self.encoded_anagrams = {}
        self.__base_string = ""

    def set_base_string(self, string_to_set):
        self.__base_string = string_to_set

    def get_base_string(self):
        return self.__base_string

    def read_anagrams(self):
        f = open('set_of_' + str(self.get_base_string().count(" ") + 1) + "_anagrams.dms")
        for line in f:
            self.anagrams.append(tuple(line.strip().split(' ')))
        # print(self.anagrams)

    def encode_anagrams(self):
        for wordtuple in self.anagrams:
            for anagtuple in permutations(wordtuple):
                anagram = ' '.join(anagtuple)
                self.encoded_anagrams[anagtuple] = md5(anagram.encode()).hexdigest()

    def decode(self, md5_hash):
        print("Encoding hash: " + md5_hash + "\n")
        for anagram, anagram_hex in self.encoded_anagrams.items():
            if anagram_hex == md5_hash:
                print ("Target anagram found: " + ' '.join(anagram))

    def run(self, base_string, md5_hash):
        self.set_base_string(base_string)
        self.read_anagrams()
        self.encode_anagrams()
        self.decode(md5_hash)
