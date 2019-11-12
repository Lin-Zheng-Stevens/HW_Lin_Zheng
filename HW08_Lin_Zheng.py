"""
Created on Thr Oct 25 2019

@author: Lin Zheng

HW08 implementation file layout template
"""

import datetime
import os
from prettytable import PrettyTable

def date_arithmetic():
    """ a function to use Python’s datetime module to answer the questions"""
    date1 = "Feb 27, 2000"
    date2 = "Feb 27, 2017"
    date3 = "Jan 1, 2017"
    date4 = "Oct 31, 2017"

    dt1 = datetime.datetime.strptime(date1, "%b %d, %Y")
    dt2 = datetime.datetime.strptime(date2, "%b %d, %Y")
    dt3 = datetime.datetime.strptime(date3, "%b %d, %Y")
    dt4 = datetime.datetime.strptime(date4, "%b %d, %Y")

    num_days = 3
    dt5 = dt1 + datetime.timedelta(days=num_days)
    dt6 = dt2 + datetime.timedelta(days=num_days)
    three_days_after_02272000 = dt5.strftime('%m/%d/%Y')
    three_days_after_02272017 = dt6.strftime('%m/%d/%Y')

    delta = dt4 - dt3
    days_passed_01012017_10312017 = delta.days

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017

def file_reading_gen(path, fields, sep=',', header=False):
    """ a generator function file_reading_gen to read field-separated text files and yield a tuple """
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open '{path}'")
    else:
        with fp:
            for index, line in enumerate(fp, 1):
                line = tuple(line.rstrip('\n').split(sep))
                if len(line) != fields:
                    raise ValueError(f'{path} has {len(line)} fields on line {index} but expected {fields}')
                elif index == 1 and header:
                    continue
                else:
                    yield line
                    index += 1

class FileAnalyzer:
    """ a class that searches given directory for Python files and calculate a summary of the files """
    def __init__(self, directory):
        """ __init__(self, directory) """
        self.directory = directory
        self.files_summary = dict() 

        self.analyze_files() # summerize the python files data

    def analyze_files(self):
        """ populate the summarized data into self.files_summary """
        try:
            filelist = os.listdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find '{self.directory}'")
        else:

            for file in filelist:
                if file.lower().endswith('.py'):
                    filename = os.path.join(self.directory, file)
                    try: 
                        fp = open(filename, 'r')
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Can't open '{filename}'")
                    else:
                        with fp:
                            Classes = Functions = Lines = Characters = 0
                            for i in fp:
                                Lines += 1
                                Characters += len(i)
                                if i.strip().startswith('def '):
                                    Functions += 1
                                if i.strip().startswith('class '):
                                    Classes += 1
                            self.files_summary[filename] = {'class': Classes, 'function': Functions, 'line': Lines, 'char': Characters}
                                               
    def pretty_print(self):
        """ print out the pretty table from the data stored in the self.files_summary """
        pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
        for key, value in self.files_summary.items():
            pt.add_row([key, value['class'], value['function'], value['line'], value['char']])
        print(f'Summary for {self.directory}')
        return pt
                    