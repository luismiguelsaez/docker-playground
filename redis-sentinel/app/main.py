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

logLevel = environ.get('LOG_LEVEL') if 'LOG_LEVEL' in environ else 'ERROR'
reqSleep = environ.get('REQ_SLEEP') if 'REQ_SLEEP' in environ else 0.10

countSuccess = 0
countFailure = 0
countTotal = 0

r = redis.StrictRedis(host=redisHost, port=redisPort, db=redisDb, socket_timeout=redisTimeout)

logging.basicConfig(level=logLevel)

val_len = 16

loopCount = 0

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

    countSuccess += 1

  except redis.exceptions.ConnectionError as clConn:
    logging.critical("Node connection error: {}".format(str(clConn)))
    countFailure += 1

  except redis.exceptions.TimeoutError as clTout:
    logging.critical("Node timeout error: {}".format(str(clTout)))
    countFailure += 1

  countTotal += 1
  loopCount += 1

  if loopCount % 100 == 0:
    logging.info("Requests total: {} - Success: {} - Error: {}".format(str(countTotal), str(countSuccess, str(countFailure))))
    loopCount = 0

  sleep(float(reqSleep))
