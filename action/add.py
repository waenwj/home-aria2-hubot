import sys
from aria2c import Aria2c

uri = sys.argv[1]


client = Aria2c('127.0.0.1', '6800')

print(client.addUri(uri))


