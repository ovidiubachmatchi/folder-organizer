from os import listdir, mkdir, rename, getcwd
from os.path import splitext, exists, isdir
from sys import argv

def organize(path):
    success = False
    print(f"\nThe current working directory is '{path}'")
    for file in listdir(path):
        if argv[0] != f'{path}\\{file}' and __file__ != f'{path}\\{file}':
            if isdir(f'{path}\\{file}') is False:
                categorized_folder_name = folder(splitext(file)[1])
                if exists(f'{path}\\{categorized_folder_name}') is False:
                    try:
                        mkdir(f'{path}\\{categorized_folder_name}')
                    except OSError as error:
                        print(error)
                try:
                    rename(f'{path}\\{file}', f'{path}\\{categorized_folder_name}\\{file}')
                    print(f"'{file}' has been moved in '{categorized_folder_name}' folder")
                    success = True
                except OSError as error:
                    print(f"'{file}' already exists in '{categorized_folder_name}' folder, we will not overwrite")
    return success


def folder(extension):
    extensions_dict = {
        '.doc': 'Text', '.docx': 'Text', '.pdf': 'Text', '.rtf': 'Text', '.tex': 'Text', '.wpd': 'Text', '.txt': 'Text',
        '.aif': 'Audio', '.cda': 'Audio', '.mp3': 'Audio', '.mpa': 'Audio', '.ogg': 'Audio', '.wav': 'Audio',
        '.wma': 'Audio', '.wpl': 'Audio', '.7z': 'Compressed files', '.arj': 'Compressed files',
        '.deb': 'Compressed files', '.pkg': 'Compressed files', '.rar': 'Compressed files', '.rpm': 'Compressed files',
        '.gz': 'Compressed files', '.z': 'Compressed files', '.zip': 'Compressed files', '.bin': 'Disc and media',
        '.dmg': 'Disc and media', '.iso': 'Disc and media', '.toast': 'Disc and media', '.vcd': 'Disc and media',
        '.csv': 'Data and database', '.dat': 'Data and database', '.db': 'Data and database',
        '.dbf': 'Data and database', '.log': 'Data and database', '.mdb': 'Data and database',
        '.sav': 'Data and database', '.sql': 'Data and database', '.tar': 'Data and database',
        '.xml': 'Data and database', '.apk': 'Executable files', '.bat': 'Executable files', '.cgi': 'Executable files',
        '.com': 'Executable files', '.exe': 'Executable files', '.gadget': 'Executable files',
        '.jar': 'Executable files', '.msi': 'Executable files', '.py': 'Programming files', '.wsf': 'Executable files',
        '.ai': 'Images', '.bmp': 'Images', '.gif': 'Images', '.ico': 'Images', '.jpeg': 'Images', '.jpg': 'Images',
        '.png': 'Images', '.ps': 'Images', '.psd': 'Images', '.svg': 'Images', '.tif': 'Images', '.tiff': 'Images',
        '.css': 'Internet related files', '.aspx': 'Internet related files', '.asp': 'Internet related files',
        '.html': 'Internet related files', '.htm': 'Internet related files', '.js': 'Internet related files',
        '.jsp': 'Internet related files', '.php': 'Internet related files', '.xhtml': 'Internet related files',
        '.key': 'Presentations', '.odp': 'Presentations', '.pps': 'Presentations', '.ppt': 'Presentations',
        '.pptx': 'Presentations', '.c': 'Programming files', '.pl': 'Programming files', '.class': 'Programming files',
        '.cpp': 'Programming files', '.cs': 'Programming files', '.h': 'Programming files', '.lnk': 'Shortcuts',
        '.java': 'Programming files', '.sh': 'Programming files', '.swift': 'Programming files',
        '.vb': 'Programming files', '.ods': 'Spreadsheet files', '.xls': 'Spreadsheet files',
        '.xlsm': 'Spreadsheet files', '.xlsx': 'Spreadsheet files', '.avi': 'Video', '.3g2': 'Video', '.3gp': 'Video',
        '.flv': 'Video', '.h264': 'Video', '.m4v': 'Video', '.mkv': 'Video', '.mov': 'Video', '.mp4': 'Video',
        '.mpg': 'Video', '.mpeg': 'Video', '.rm': 'Video', '.swf': 'Video', '.vob': 'Video', '.wmv ': 'Video'
    }
    return extensions_dict.get(extension, 'Other files')

if __name__ == '__main__':
    try:
        current_path = argv[1]
    except IndexError:
        current_path = getcwd()
    if exists(current_path):
        try:
            folder_organizer(current_path)
        except Exception as error:
            print(error)
    else:
        print("The directory path you want to organize doesn't exists")
