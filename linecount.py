'''Script to get Number of lines in a file'''
import os
import sys
class LineCount:
    ''' Class to get count of lines for files in a directory'''
    def __init__(self, dir_location, extension=".txt"):
        self.dir_location = dir_location
        self.extension = extension
        self.total_line_count = 0
        self.total_files = 0
    def calculate_line_count(self, path, name):
        ''' A method to count lines in each file'''
        try:
            file_name = open(os.path.join(path, name), 'r', errors='ignore')
            line_count = 0
            for _ in file_name:
                line_count += 1
            file_name.close()
            self.total_files += 1
            self.total_line_count += line_count
            return line_count
        except FileNotFoundError:
            print("File Not Found")

    def get_count(self):
        ''' Get Files of required extension and print the count of lines'''
        if os.path.isdir(self.dir_location):
            for path, _, files in os.walk(self.dir_location):
                for name in files:
                    if name.endswith(self.extension):
                        line_count = self.calculate_line_count(path, name)
                        print(name, line_count)
    def get_total_files(self):
        '''Get total number of files of required extension'''
        return self.total_files
    def get_total_lines(self):
        '''Get total lines in all expected files'''
        return self.total_line_count
    def get_avg_lines(self):
        '''Get Average count of lines per file'''
        try:
            return self.total_line_count/self.total_files
        except ZeroDivisionError:
            return 0
if __name__ == "__main__":
    args = sys.argv[1:]
    FOLDER = ""
    EXT = ""
    if len(args) == 0:
        print("Enter Directory Location")
    if len(args) == 1:
        FOLDER = args[0]
        EXT = ".txt"
    elif len(args) == 2:
        FOLDER = args[0]
        EXT = args[1]
    l = LineCount(FOLDER, EXT)
    l.get_count()
    total_files = l.get_total_files()
    print("Number of files found: ", total_files)
    total_lines = l.get_total_lines()
    print("Total number of lines : ", total_lines)
    avg_lines = l.get_avg_lines()
    print("Average lines per file: ", avg_lines)
