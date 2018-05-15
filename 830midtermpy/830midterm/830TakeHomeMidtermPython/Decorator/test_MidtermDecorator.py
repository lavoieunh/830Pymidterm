from midtermdecorator import Adverb, Adjective, Verb
import unittest

adv = Adverb() 
#adj = Adjective 
#ver = Verb()

advwords = adv.adverb_words() 


class TestAdverb(unittest.TestCase): 
    @classmethod
    def setUpClass(self): 
        self.adverb = Adverb() 
        self.expected = ['beautifully', 'lazily', 'quickly', 'awkwardly', 'dearly', 'loftily', 'colorfully', 'rapidly', 'deeply', 'loosely' ]

 
    def testadverbwords(self):

        #adverb_list = self.__class__.adverb.adverb_words
        #advlist_final = self.__class__.adverb.adverb_words
        testadverb_list = ['beautifully', 'lazily', 'quickly', 'awkwardly', 'dearly', 'loftily', 'colorfully', 'rapidly', 'deeply', 'loosely' ] 
        
        self.assertEquals(testadverb_list, self.expected)

        testadvlist = ','.join(testadverb_list)
        self.advlist = ','.join(self.expected)

        self.assertEquals(testadvlist, self.advlist) 
        self.assertTrue(testadvlist, testadverb_list)

        testadvlist_final = testadvlist.split(",")
        advlist_final = self.advlist.split(",")
        
        self.assertEquals(testadvlist_final, advlist_final)

        #return(choice(advlist_final)) 


class TestVerb(unittest.TestCase):
    
    @classmethod 
    def setUpClass(self): 
        self.verb = Verb() 
        self.expected = ['hang', 'march', 'mix', 'name', 'lock', 'bake', 'cook', 'fight', 'promise', 'zip' ]

    def testverb_words(self):
        testverb_list = ['hang', 'march', 'mix', 'name', 'lock', 'bake', 'cook', 'fight', 'promise', 'zip' ]

        self.assertEquals(testverb_list, self.expected)

        testverblist = ','.join(testverb_list)
        verblist = ','.join(self.expected)

        self.assertEquals(testverblist, verblist)

        testvlist_final = testverblist.split(",")
        vlist_final = verblist.split(",")

        self.assertEqual(testvlist_final, vlist_final)

    
class testAdjective(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.adjective = Adjective() 
        self.expected = ['clumsy', 'bored', 'disgusting', 'moody', 'brave', 'relieved', 'important', 'talented', 'nervous', 'fierce' ]

    def advjective_words(self):

        testadjective_list = ['clumsy', 'bored', 'disgusting', 'moody', 'brave', 'relieved', 'important', 'talented', 'nervous', 'fierce' ]

        self.assertEquals(testadjective_list, self.expected)

        testadjlist = ','.join(testadjective_list) 
        adjlist = ','.join(self.expected)

        self.assertEquals(testadjlist, adjlist)

        testalist = testadjlist.split(",")
        alist = adjlist.split(",")

        self.assertEqual(testalist, alist)

        #return(choice(alist))

    
if __name__ == 'main': 
    unittest.main()