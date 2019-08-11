import missingletters
import os
import sys

def main ():
    for arg in sys.argv[1:]:
        if os.path.exists(arg):
            missingletters.processFile(arg)
        else:
            print(missingletters.processLine(arg))

main()
