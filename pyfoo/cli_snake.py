import os
import sys

# https://stackoverflow.com/questions/14211575/any-python-function-to-get-data-files-root-directory
def main():
    data_dir = os.path.join(sys.prefix, 'magic','resources')
    print('resource root:', data_dir)
    print(open(os.path.join(data_dir, 'snake.txt')).read())


if __name__ == '__main__':
    main()
