import random
import time
import os
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    filename='/var/log/logbot.log',
    level=logging.DEBUG
    )

if 'INTERVAL' in os.environ:
    interval = int(os.environ['INTERVAL'])
else:
    interval = 3
lines = open('mb.txt').read().splitlines()
lines = list(filter(None, lines))
while True:
    line = random.choice(lines)
    print(line)
    logging.info(line)
    time.sleep(interval)
