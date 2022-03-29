import redis
from time import sleep
from time import sleep
from datetime import datetime
import string
import random
import uuid
import logging
from os import environ

redisHost    = environ.get('REDIS_HOST')    if 'REDIS_HOST'    in environ else 'localhost'
redisPort    = environ.get('REDIS_PORT')    if 'REDIS_PORT'    in environ else 6379
redisDb      = environ.get('REDIS_DB')      if 'REDIS_DB'      in environ else 0
redisTimeout = environ.get('REDIS_TIMEOUT') if 'REDIS_TIMEOUT' in environ else 5

r = redis.StrictRedis(host=redisHost, port=redisPort, db=redisDb, socket_timeout=redisTimeout)

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

  sleep(0.10)
