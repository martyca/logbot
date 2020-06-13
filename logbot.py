import random
import time
import os
if 'INTERVAL' in os.environ:
    interval = int(os.environ['INTERVAL'])
else:
    interval = 3
lines = open('mb.txt').read().splitlines()
lines = list(filter(None, lines))
while True:
    print(random.choice(lines))
    time.sleep(interval)
