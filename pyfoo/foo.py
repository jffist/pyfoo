import sys

def bar(x):
    print(f"calling foo.bar with x={x}")
    return x+2

def main():
    if len(sys.argv)!=2:
        print(f"Usage: {sys.argv[0]} N\nN - integer")
    else:
        res = bar(int(sys.argv[1]))
        print('result:', res)
