import pandas as pd
import random


class Adverb(object):
    def adverb_words(self):

        adverb_list = {'adverbs': 'beautifully', 'lazily', 'quickly', 'awkwardly', 'dearly', 'loftily', 'colorfully', 'rapidly', 'deeply', 'loosely' }

        advlist = ','.join(adverb_list)

        advlist_final = (advlist.split(","))

        return(random.choice(advlist_final))