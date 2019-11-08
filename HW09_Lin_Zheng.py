"""
Created on Thr Oct 31 2019

@author: Lin Zheng

HW09 implementation file layout template
"""

from prettytable import PrettyTable
from HW08_Lin_Zheng import file_reading_gen
from prettytable import PrettyTable
from collections import defaultdict
import os

class Student:
    """
        Stores information about a single student with all of the relevant information including:
        - CWID
        - name
        - major
        - Container of courses and grades
    """
    PT_FIELDS = ['CWID', 'Name', 'Major', 'Courses']

    def __init__(self, cwid, name, major):
        """ __init__ """
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()  # track _courses[course] = grade

    def add_course(self, course, grade):
        """ store the grade associated with a course for this student """
        self._courses[course] = grade

    def pt_row(self):
        """ return a list of values needed in the pretty table for one student (me) """
        return [self._cwid, self._name, self._major, sorted(self._courses.keys())]

    def __repr__(self):
        """ return string """
        return str((self._cwid, self._name, self._major, sorted(self._courses.keys())))


class Instructor:
    """
        Stores information about a single Instructor with all of the relevant information including:
        - CWID
        - name
        - department
        - Container of courses taught and the number of students in each course
    """
    PT_FIELDS = ['CWID', 'Name', 'Dept', 'Course', 'Students#']

    def __init__(self, cwid, name, dept):
        """ __init__ """
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)   # track _courses[course] = students#

    def add_student(self, course):
        """ Note that the instructor taught another course to the student """
        self._courses[course] += 1

    def pt_row(self):
        """ return a list of values needed in the pretty table for one student (me) """
        for course, students in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, students]
            
    def __repr__(self):
        """ return string """
        return str((self._cwid, self._name, self._dept))


class Repository:
    """
        Holds all of the data for a specific organization:
        - Container for all students
        - Container for all instructors
        - Read the grades.txt file and process each grade
    """
    def __init__(self, path, ptable=False):
        """ __init__ """
        self._path = path   # directory with the students, instructors, and grades files
        self._students = dict()   # students[cwid] = Student()
        self._instructors = dict()   # instructors[cwid] = Instructor()

        try:
            self._get_students(os.path.join(path, 'students.txt'))
            self._get_instructors(os.path.join(path, 'instructors.txt'))
            self._get_grades(os.path.join(path, 'grades.txt'))
        except ValueError as ve:
            print(ve)
        except FileNotFoundError as fnfe:
            print(fnfe)

        if ptable:
            print('\nStudents Summary')
            self.student_prettytable()

            print('\nInstructor Summary')
            self.instructor_prettytable()

    def _get_students(self, path):
        """ read the students and populate self._students """
        for cwid, name, major in file_reading_gen(path, 3, sep='\t', header=False):
            self._students[cwid] = Student(cwid, name, major)
    
    def _get_instructors(self, path):
        """ read the instructors and populate self._instructors """
        for cwid, name, dept in file_reading_gen(path, 3, sep='\t', header=False):
            self._instructors[cwid] = Instructor(cwid, name, dept)

    def _get_grades(self, path):
        """ get grades """
        for student_cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep='\t', header=False):
            if student_cwid in self._students:
                self._students[student_cwid].add_course(course, grade)   # tell the student about a course
            else:
                print(f'Found grade for unknown student {student_cwid}')

            if instructor_cwid in self._instructors:
                self._instructors[instructor_cwid].add_student(course)   # tell the instructor about a course/student
            else:
                print(f'Found grade for unknown instructor {instructor_cwid}')

    def student_prettytable(self):
        """ print the student pretty table """
        pt = PrettyTable(field_names=Student.PT_FIELDS)
        for student in self._students.values():
            pt.add_row(student.pt_row())

        print(pt)

    def instructor_prettytable(self):
        """ print the instructor pretty table """
        pt = PrettyTable(field_names=Instructor.PT_FIELDS)
        for instructor in self._instructors.values():
            # each instructor may teach zero, one, or many classes
            for row in instructor.pt_row():
                pt.add_row(row)

        print(pt)


def main():
    stevens = Repository('C:\\Users\\LSM\\Desktop\\stevens', ptable=True)   # read files and generate prettytables


if __name__ == '__main__':
    main()
    #print(Repository('C:\\Users\\LSM\\Desktop\\stevens')._students)
    