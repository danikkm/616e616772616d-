from collections import Counter
from trie import Trie
from cleanup import Cleanup


class Generator:
    def __init__(self):
        self.anagrams = []
        self.trie = Trie()
        self.data = []
        self.__base_string = ""

    def set_base_string(self, string_to_set):
        self.__base_string = string_to_set

    def get_base_string(self):
        return self.__base_string

    def read_words(self, fname):
        print('Loading file... ')
        f = open(fname, 'r')
        lines = f.read().splitlines()
        f.close()
        print("Done!")
        self.data = lines

    def calc(self):
        word_len = self.get_base_string().count(" ") + 1
        anagram_counter = Counter(self.trim(self.get_base_string()))
        for word in self.data:
            self.trie.add_word(word)
        for anagram in self.trie.anagrams(anagram_counter, word_len=word_len):
            self.anagrams.append(anagram)
        sorted(self.anagrams)

    def trim(self, string_to_trim):
        return "".join(string_to_trim.split())

    def save_to_file(self, fname):
        with open(fname, 'w') as filehandle:
            for t in self.anagrams:
                line = ' '.join(str(x) for x in t)
                filehandle.write(line + '\n')

    def run(self, base_string):
        self.set_base_string(base_string)
        try:
            self.read_words("clean_words.dms")
        except IOError:
            cleanup = Cleanup()
            cleanup.run(self.get_base_string())
            self.read_words("clean_words.dms")
        self.calc()
        self.save_to_file(
            "set_of_" + str(self.get_base_string().count(" ") + 1) + "_anagrams.dms")
