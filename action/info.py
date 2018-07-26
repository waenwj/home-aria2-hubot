import sys
from aria2c import Aria2c

client = Aria2c('127.0.0.1', '6800')
print(client.tellActive().encode('utf8'))


