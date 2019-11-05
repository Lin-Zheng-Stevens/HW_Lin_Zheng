"""
Created on Tue Nov 3 2019

@author: Lin Zheng

Test cases for HW09_Lin_Zheng.
"""

import unittest

from HW09_Lin_Zheng import Student, Instructor, Repository
from HW08_Lin_Zheng import file_reading_gen
import os

class TestRepository(unittest.TestCase):
    """ Test of Repository

        - Test for the dictionaries

    """
    def setUp(self):
        self.test_path = 'C:\\Users\\LSM\\Desktop\\stevens'
        self.repo = Repository(self.test_path, False)

    def test_students(self):
        """ test_students """
        expect = {'10103': ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']], 
                  '10115': ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']], 
                  '10172': ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567']], 
                  '10175': ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687']], 
                  '10183': ['10183', 'Chapman, O', 'SFEN', ['SSW 689']], 
                  '11399': ['11399', 'Cordova, I', 'SYEN', ['SSW 540']], 
                  '11461': ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800']], 
                  '11658': ['11658', 'Kelly, P', 'SYEN', ['SSW 540']], 
                  '11714': ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645']], 
                  '11788': ['11788', 'Fuller, E', 'SYEN', ['SSW 540']]}

        calculated = {cwid: student.pt_row() for cwid, student in self.repo._students.items()}
        self.assertEqual(calculated, expect)

    def test_instructors(self):
        """ test_instructors """
        expect = {('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3), 
                ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1), 
                ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3), 
                ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1), 
                ('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4), 
                ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3), 
                ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1), 
                ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1), 
                ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1), 
                ('98763', 'Newton, I', 'SFEN', 'SSW 555',1), 
                ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2), 
                ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1)}
        calculated = {tuple(row) for instructor in self.repo._instructors.values() for row in instructor.pt_row()}
        self.assertEqual(calculated, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)