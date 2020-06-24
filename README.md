# logbot
docker image that prints random lines on STDOUT and to `/var/log/logbot.log`, ideal for testing logging solutions.
## source files
mb.txt is a modified version of Moby Dick which is in the public domain, downloaded from [project Gutenberg](https://www.gutenberg.org/)
## output interval
The default output interval of the lines is one every 3 seconds, pass the `INTERVAL` environment variable with a number to change the output interval.
#### example:
`docker run -e INTERVAL=1 martyca/logbot`

This will output a line every second.

## GutenBerg license - short version:
This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.net
## GutenBerg license - Full version:
https://www.gutenberg.org/wiki/Gutenberg:The_Project_Gutenberg_License
