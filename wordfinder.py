"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Used to find a random word from a dictionary created from reading file

    >>> wf = WordFinder("words.txt")
       235886 words read
    """

    def __init__(self, path):
        """Read file and return number of items read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file to list of words"""
        return [w.strip() for w in dict_file]

    def random(self):
        """Returns a random word from list"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special word finder that ignores comments and blank lines in file

        >>> wf = SpecialWordFinder("specialWords.txt")
        235886 words read
    """
    def parse(self, dict_file):
        """Parse dict_file to list of words but skips new lines and comments"""
        return [w.strip() for w in dict_file 
                if w.strip() and not w.startswith("#")]


