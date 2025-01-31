from deeznutsHelper import deezStringer
import unittest

class testDeezNuts(unittest.TestCase):
    def testNoInput(self):
        self.assertEqual(deezStringer(""),"deez nuts")
    def testSmallInput(self):
        self.assertEqual(deezStringer("how"),"Well why don't you how d e e ")
    def testBigInput(self):
        self.assertEqual(deezStringer("howdyboafff"),"Well why don't you howdyboafff d e e z n u t s d e e ")
        
if __name__ == "__main__":
    unittest.main()