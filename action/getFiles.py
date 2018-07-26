import sys
from aria2c import Aria2c

gid = sys.argv[1]

client = Aria2c('127.0.0.1', '6800')
print(client.getFiles(gid))


