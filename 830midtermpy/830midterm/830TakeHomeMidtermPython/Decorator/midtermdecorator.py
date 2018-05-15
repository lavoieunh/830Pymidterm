import random
from random import choice, shuffle

class Adverb(object):
    def adverb_words(self):
        adverb_list = ['beautifully', 'lazily', 'quickly', 'awkwardly', 'dearly', 'loftily', 'colorfully', 'rapidly', 'deeply', 'loosely' ]
        advlist = ','.join(adverb_list)

        advlist_final = advlist.split(",")

        return(choice(advlist_final))

class Verb(object):
    def verb_words(self):

        verb_list = ['hang', 'march', 'mix', 'name', 'lock', 'bake', 'cook', 'fight', 'promise', 'zip' ]

        verblist = ','.join(verb_list)

        vlist_final = (verblist.split(","))
        
        return(choice(vlist_final))

class Adjective(object):
    def advjective_words(self):

        adjective_list = ['clumsy', 'bored', 'disgusting', 'moody', 'brave', 'relieved', 'important', 'talented', 'nervous', 'fierce' ]

        adjlist = ','.join(adjective_list)

        alist = (adjlist.split(","))

        return(choice(alist)) 

