from os import listdir, mkdir, rename, getcwd
from os.path import splitext, exists, isdir
from sys import executable


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


def folder_organizer(path):
    list_dir = listdir(path)
    for file in list_dir:
        if executable != f'{path}\\{file}' and __file__ != f'{path}\\{file}':
            if isdir(f'{path}\\{file}') is False:
                extension = splitext(file)[1]
                if exists(folder(extension)) is False:
                    try:
                        mkdir(folder(extension))
                    except OSError:
                        print(OSError)
                try:
                    rename(f'{path}\\{file}', f'{path}\\{folder(extension)}\\{file}')
                    print(file, 'has been moved in', folder(extension))
                except OSError:
                    print(f'ERROR: {file} already exists in {folder(extension)}')
    print("This directory has been organized!")


if __name__ == '__main__':
    current_path = getcwd()
    try:
        print('\nThe current working directory is', current_path)
        folder_organizer(current_path)
    except Exception as error:
        print(error)
