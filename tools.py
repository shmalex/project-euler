import os
import time
def dprint(*args):
    if 'A' in os.environ and os.environ['A'] == '1':
        print(time.strftime('%Y-%m-%d %H:%M:%S STC', time.localtime()), *args)
