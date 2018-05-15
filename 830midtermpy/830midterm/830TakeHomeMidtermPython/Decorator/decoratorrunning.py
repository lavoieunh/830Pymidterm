from midtermdecorator import Adverb, Verb, Adjective
import fileinput



adverb = Adverb()
advreplace = adverb.adverb_words() 


verb = Verb() 
verbreplace = verb.verb_words()

adjective = Adjective() 
adjreplace = adjective.advjective_words()


filechoice= raw_input('Would you like sentences1 or sentences2? ')
filechoices = (filechoice + '.txt') 

with open(filechoices) as holder:
    sentences = holder.read().replace('\n', 'r')
    sentenced = sentences.replace('ADVERB', advreplace).replace('VERB', verbreplace).replace('ADJECTIVE', adjreplace)
    print sentenced
