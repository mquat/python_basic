#EOFerror : raised when one of the built-in functions input() or raw_input() hits an end-of-file condition (EOF) without reading any data.
#source: https://www.geeksforgeeks.org/handling-eoferror-exception-in-python/

while True:
    try:
        print(input())
    except EOFError:
        break
