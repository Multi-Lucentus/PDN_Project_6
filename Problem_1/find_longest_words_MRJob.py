from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRLongestWord(MRJob):
    
    def mapper(self, _, line):
        word_dictionary = {}
        for word in WORD_RE.findall(line):
            if word.lower() in word_dictionary:
                word_dictionary[word.lower()] += 1
            else:
                word_dictionary[word.lower()] = 1

        for(key, local_value) in word_dictionary.items():
            yield(key, local_value)

    def reducer(self, word, counts):
        yield(word, sum(counts)) 


if __name__ == "__main__":
    MRLongestWord.run() 