from collections import Counter

# Todo: create method for external call 
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

    def trim(self, str):
        return "".join(str.split())

    def save_to_file(self, fname):
        with open(fname, 'w') as filehandle:
            for listitem in self.words:
                filehandle.write('%s\n' % listitem)


def main():

    cleanup = Cleanup()
    cleanup.read_words("wordlist.dms")
    cleanup.remove_impossible_words_from(Counter("poultry outwits ants"))
    cleanup.save_to_file("clean_words.dms")

if __name__ == "__main__":
    main()