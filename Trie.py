from collections import Counter


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, word):
        node = self.root
        letters = sorted(self.trim(word))
        for letter in letters:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        node.is_end_of_word = True
        node.words.append(word)

    def does_word_exists(self, word):
        if word == "":
            return True
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_end_of_word

    def anagrams(self, anagram_counter, word_len, num_of_words=0):

        first_letter = sorted(anagram_counter)[0]
        first_letter_counter = Counter(first_letter)

        if first_letter in self.root.children and num_of_words < word_len:
            for words in self.possible_words(anagram_counter - first_letter_counter, self.root.children[first_letter]):
                counter_of_first_letters = Counter(words[0])
                if anagram_counter == counter_of_first_letters:
                    for word in words:
                        yield word,
                else:
                    for word_list in self.anagrams(anagram_counter - counter_of_first_letters, num_of_words=num_of_words + 1, word_len=word_len):
                        for word in words:
                            yield (word,) + word_list

    def possible_words(self, anagram_counter, node):
        if len(node.words) > 0:
            yield (node.words)
        for letter in anagram_counter:
            if letter in node.children:
                for words in self.possible_words(anagram_counter - Counter(letter), node.children[letter]):
                    yield (words)

    def trim(self, x):
        return "".join(x.split())
