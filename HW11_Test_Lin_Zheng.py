"""
Created on Tue Nov 12 2019

@author: Lin Zheng

Test cases for HW11_Lin_Zheng.
"""

import unittest

from HW11_Lin_Zheng import Student, Instructor, Repository
from HW08_Lin_Zheng import file_reading_gen
import os

class TestRepository(unittest.TestCase):
    """ Test of Repository

        - Test for the dictionaries

    """
    def setUp(self):
        self.test_path = 'C:\\Users\\LSM\\Desktop\\\Python\\HW\\HW#11\\stevens'
        self.repo = Repository(self.test_path, False)

    def test_majors(self):
        """ test_majors """
        expect = [('SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']), \
                  ('CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810'])]

        calculated = [student.pt_row() for cwid, student in self.repo._majors.items()]
        self.assertEqual(calculated, expect)

    def test_students(self):
        """ test_students """
        expect = {'10103': ['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 540', 'SSW 555'}, None], \
                  '10115': ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], {'SSW 540', 'SSW 555'}, {'CS 501', 'CS 546'}], \
                  '10183': ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 501', 'CS 546'}], \
                  '11714': ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], None, None], \
                  '11717': ['11717', 'Kernighan, B', 'CS', [], {'CS 570', 'CS 546'}, {'SSW 810', 'SSW 565'}]}

        calculated = {cwid: student.pt_row() for cwid, student in self.repo._students.items()}
        self.assertEqual(calculated, expect)

    def test_instructors(self):
        """ test_instructors """
        expect = {('98762', 'Hawking, S', 'CS', 'CS 570', 1), ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1), \
                  ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1), ('98762', 'Hawking, S', 'CS', 'CS 501', 1), \
                  ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4), ('98762', 'Hawking, S', 'CS', 'CS 546', 1)}
        calculated = {tuple(row) for instructor in self.repo._instructors.values() for row in instructor.pt_row()}
        self.assertEqual(calculated, expect)

    def test_instructor_table_db(self):
        """ test_instructors_new """
        expect = {('98762', 'Hawking, S', 'CS', 'CS 570', 1), ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1), \
                  ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1), ('98762', 'Hawking, S', 'CS', 'CS 501', 1), \
                  ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4), ('98762', 'Hawking, S', 'CS', 'CS 546', 1)}
        db_path = "C:\\Users\\LSM\\Desktop\\Python\\HW\\sqlite-tools-win32-x86-3300100\\810_startup.db"
        calculated = {tuple(row) for row in self.repo._instructor_table_db_data(db_path)}
        self.assertEqual(calculated, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)