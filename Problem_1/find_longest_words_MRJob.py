from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRLongestWord(MRJob):
    
    def mapper(self, _, line):
        longest_dictionary = {}
        for word in WORD_RE.findall(line):
            if word.lower()[0] in longest_dictionary:
                if len(word) > len(longest_dictionary[word.lower()[0]][0]):
                    longest_dictionary[word.lower()[0]] = list(word.lower())
                elif len(word) == len(longest_dictionary[word.lower()[0]][0]):
                    longest_dictionary[word.lower()[0]].append(word.lower())
            else:
                longest_dictionary[word.lower()[0]] = list(word.lower())

        for(key, local_value) in longest_dictionary.items():
            yield(key, local_value)

    def reducer(self, letter, longest):
        yield(letter, longest) 


if __name__ == "__main__":
    MRLongestWord.run() 