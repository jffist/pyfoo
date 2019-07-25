import sys
from pyfoo.foo import bar

def main():
    if len(sys.argv)!=2:
        print(f"Usage: {sys.argv[0]} N\nN - integer")
    else:
        res = bar(int(sys.argv[1]))
        print('result:', res)

#if __name__ == '__main__':
#    main()
