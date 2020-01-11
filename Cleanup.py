from collections import Counter


class Cleanup:
    def __init__(self):
        self.unnecessary_wrods = []
        self.words = []

    def read_words(self, fname):
        f = open(fname, 'r')
        lines = f.readlines()
        f.close()
        self.unnecessary_wrods = lines

    def remove_impossible_words_from(self, anagram_counter):
        i = 0
        while i < len(self.unnecessary_wrods):
            self.unnecessary_wrods[i] = self.trim(self.unnecessary_wrods[i])
            word_counter = Counter(self.unnecessary_wrods[i])
            if not all(x in anagram_counter for x in word_counter):
                self.unnecessary_wrods.pop(i)
            else:
                i += 1
        self.words = sorted(list(set(self.unnecessary_wrods)))

    def trim(self, string_to_trim):
        return "".join(string_to_trim.split())

    def save_to_file(self, fname):
        with open(fname, 'w') as filehandle:
            for listitem in self.words:
                filehandle.write('%s\n' % listitem)

    def run(self, base_string):
        print("Generating file witout impossible words A.K.A clean_wrods")
        self.read_words("wordlist.dms")
        self.remove_impossible_words_from(Counter(base_string))
        self.save_to_file("clean_words.dms")
