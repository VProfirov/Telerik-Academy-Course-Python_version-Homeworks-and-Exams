
# Path is used to account for the OS's stringification of the path (Win:'\'), (Unix:'/'), etc...
from pathlib import Path

# Path is breaking depending on the directory level, when the project is open, so use import os
# import os

def get_formatted_CSharp_code():
        # FIXME: use the fallowing line:
    # print('===> ' + os.getcwd())
        # to fix the path in the
        # code line: 'data_directory = Path('01.Fundamentals/_01_Introduction-to-Programming/UtilityFiles'
        # by adding or removing directories

    # solution
    data_directory = Path('01.Fundamentals/_01_Introduction-to-Programming/UtilityFiles')
    filestream_formattedCode = open(data_directory/'FormattedCSharpCode.txt', 'r')
    content_formattedCode = filestream_formattedCode.read()
    filestream_formattedCode.close()

    return content_formattedCode



if __name__ == '__main__':
    print(get_formatted_CSharp_code())