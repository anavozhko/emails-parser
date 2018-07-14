import os
from fileparser import FileParser


def main():
    for filename in os.listdir('files'):
        filename = f'files/{filename}'
        if 'txt' in filename:
            p = FileParser(filename, '\n'*3)
            p.start()
        else:
            raise ValueError('Unknown file type')


if __name__ == '__main__':
    main()
