from random import shuffle
from functions import factorial as fact
import sys

arr = [123, "Gautam", 2.1, [4,5]]
KEY = "38248237fds23dbqedejk3248"
isJoke = True

print(sys.path)
sys.path.append('/foo')

print(help(shuffle))
shuffle(arr)
print(arr)

print(fact(8))

if isJoke:
    import antigravity
else:
    import webbrowser, re

__all__ = [arr]