from collections import Counter


class Cleanup:
    def __init__(self):
        self.unnecessary_words = {}
        self.words = []

    def read_words(self, fname):
        f = open(fname, 'r')
        lines = f.read().splitlines()
        f.close()
        for item in lines:
            self.unnecessary_words[item] = Counter(item)

    def remove_unnecessary_words(self, anagram_counter):
        for key, value in self.unnecessary_words.items():
            if all(x in anagram_counter for x in value):
                self.words.append(key)
        self.words = sorted(set(self.words))

    def save_to_file(self, fname):
        with open(fname, 'w') as filehandle:
            for listitem in self.words:
                filehandle.write('%s\n' % listitem)

    def run(self, base_string):
        print("Generating file witout impossible words A.K.A clean_words")
        self.read_words("wordlist.dms")
        self.remove_unnecessary_words(Counter(base_string))
        self.save_to_file("clean_words.dms")
