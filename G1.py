import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()

      time.sleep(random.random() *.3)

mengetik('jangan lupa mandi\n') 
