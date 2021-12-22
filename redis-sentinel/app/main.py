import redis
from time import sleep
from time import sleep
from datetime import datetime
import string
import random
import uuid
import logging

r = redis.StrictRedis(host='sentinel.tunnel.local', port=6379, db=0, socket_timeout=1)

logging.basicConfig(level=logging.ERROR)

val_len = 16

while True:
  d = datetime.now()
  key = str(uuid.uuid1())
  value = ''.join(random.choices(string.ascii_uppercase + string.digits, k = val_len)) 
  try:
    logging.debug("{} - Setting key [{}] value [{}]".format(d, key, value))
    r.set(key, value)
    logging.debug("{} - Getting value for key [{}]".format(d, key))
    gvalue = r.get(key)
    logging.debug("{} - Got value [{}] for key [{}]".format(d, gvalue, key))
  except redis.exceptions.ConnectionError as clConn:
    logging.critical("Node connection error: {}".format(str(clConn)))
  except redis.exceptions.TimeoutError as clTout:
    logging.critical("Node timeout error: {}".format(str(clTout)))

  sleep(1)
