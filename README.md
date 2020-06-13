# logbot
docker image that prints random lines on STDOUT, ideal for testing logging solutions.
## source files
mb.txt is a modified version of Moby Dick which is in the public domain, downloaded from [project Gutenberg](https://www.gutenberg.org/)

## output interval
The default output interval of the lines is one every 3 seconds, pass the `INTERVAL` environment variable with a number to change the output interval.
#### example:
`docker run -e INTERVAL=1 martyca/logbot`

This will output a line every second.
