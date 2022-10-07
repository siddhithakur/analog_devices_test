'''Script to run unit tests for linecount.py'''
import unittest
import linecount

class TestLineCount(unittest.TestCase):
    ''' Class to test linecount.py methods'''
    def setUp(self):
        '''Repetitive Setup'''
        self.l_object = linecount.LineCount('./testcase')
        self.l_object.get_count()
        self.filename = 'newfile1.txt'
    def test_calculate_line_count(self):
        '''Method to test calculate_line_count'''
        self.assertEqual(self.l_object.calculate_line_count(self.l_object.dir_location,\
                                    self.filename), 6, "incorrect number of lines")
    def test_get_total_files(self):
        '''Method to test get_total_files'''
        self.assertEqual(self.l_object.get_total_files(), 2, "incorrect count of files")
    def test_get_total_lines(self):
        '''Method to test get_total_lines'''
        self.assertEqual(self.l_object.get_total_lines(), 13, "incorrect count of lines")
    def test_get_avg_lines(self):
        '''Method to test get_avg_lines'''
        self.assertEqual(self.l_object.get_avg_lines(), 6.5,
                         "incorrect average count of lines in the files")
if __name__ == "__main__":
    unittest.main()
