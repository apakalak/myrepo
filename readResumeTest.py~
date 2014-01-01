import unittest
import os
from readResume import CheckFileExistence , ParseResume

class TestParseResume(unittest.TestCase):

    def setUp(self):
        pass

    def test_FileExistence_txtFilePass(self):
        """ Check If resume file exists - Pass case """        
        doesExists = CheckFileExistence("resume2.txt")
        self.assertTrue(doesExists)

    def test_FileExistence_txtFileFail(self):
        """ Check If resume file exists - Fail case """
	doesExists = CheckFileExistence("abc.txt")
	self.assertFalse(doesExists)

    def test_FileExistence_docFileExists(self):
        """ With existing non .txt file as input - Fail case """        
        doesExists = CheckFileExistence("sampleResume.doc")
        self.assertFalse(doesExists)


    def test_FileExistence_docFileNonExists(self):
        """ With non-existing non .txt file as input - Fail case """        
        doesExists = CheckFileExistence("resume2.doc")
        self.assertFalse(doesExists)

    def test_ParseResume_pass(self):
        """ Check If resume Parse - Fail case """
	doesExists = ParseResume("abc.txt")
	self.assertFalse(doesExists)

    def test_ParseResume_fail(self):
        """ Check If resume Parse - Pass case """
	doesExists = ParseResume("resume2.txt")
	self.assertTrue(doesExists)

if __name__ == '__main__':
    unittest.main()
