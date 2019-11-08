"""
Created on Tue Nov 3 2019

@author: Lin Zheng

Test cases for HW10_Lin_Zheng.
"""

import unittest

from HW10_Lin_Zheng import Student, Instructor, Repository
from HW08_Lin_Zheng import file_reading_gen
import os

class TestRepository(unittest.TestCase):
    """ Test of Repository

        - Test for the dictionaries

    """
    def setUp(self):
        self.test_path = 'C:\\Users\\LSM\\Desktop\\stevens'
        self.repo = Repository(self.test_path, False)

    def test_majors(self):
        """ test_majors """
        expect = [('SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']), \
                  ('SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'])]

        calculated = [student.pt_row() for cwid, student in self.repo._majors.items()]
        self.assertEqual(calculated, expect)

    def test_students(self):
        """ test_students """
        expect = {'10103': ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], \
                 {'SSW 540', 'SSW 555'}, None], \
                  '10115': ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], \
                 {'SSW 540', 'SSW 555'}, None], \
                  '10172': ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], \
                 {'SSW 564', 'SSW 540'}, {'CS 513', 'CS 545', 'CS 501'}], \
                  '10175': ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], \
                 {'SSW 540', 'SSW 555'}, {'CS 513', 'CS 545', 'CS 501'}], \
                  '10183': ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], \
                 {'SSW 564', 'SSW 540', 'SSW 567', 'SSW 555'}, {'CS 513', 'CS 545', 'CS 501'}], \
                  '11399': ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], 
                 {'SYS 612', 'SYS 800', 'SYS 671'}, None], \
                  '11461': ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], \
                 {'SYS 612', 'SYS 671'}, {'SSW 565', 'SSW 540', 'SSW 810'}], \
                  '11658': ['11658', 'Kelly, P', 'SYEN', [], \
                 {'SYS 612', 'SYS 800', 'SYS 671'}, {'SSW 565', 'SSW 540', 'SSW 810'}], \
                  '11714': ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], \
                 {'SYS 612', 'SYS 800', 'SYS 671'}, {'SSW 565', 'SSW 540', 'SSW 810'}], \
                  '11788': ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], \
                {'SYS 612', 'SYS 800', 'SYS 671'}, None]}

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