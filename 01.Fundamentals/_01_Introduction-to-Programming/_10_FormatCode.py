from pathlib import Path

def print_formatted_CSharp_code():
    data_directory= Path('_01_Introduction-to-Programming/UtilityFiles')
    filestream_formattedCode = open(data_directory/'FormattedCSharpCode.txt', 'r')
    content_formattedCode = filestream_formattedCode.read()
    filestream_formattedCode.close()

    print(content_formattedCode)


print_formatted_CSharp_code()

