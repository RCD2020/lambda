import sys

if len(sys.argv) != 2:
    print('ya goofed hard, you were supposed to include one and one only extra argument.')
else:
    print(sys.argv[1].upper())