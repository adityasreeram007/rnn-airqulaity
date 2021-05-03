import unittest 
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):         
        self.assertEqual('Chennai','Hydrabad') 
  
if __name__ == '__main__': 
    unittest.main() 