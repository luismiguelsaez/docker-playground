import rediscluster
import redis
from time import sleep
from datetime import datetime
import string
import random
import uuid
import logging

logging.basicConfig(level=logging.ERROR)

startup_nodes = [
  {"host": "redis-node-0", "port": "6379"},
  {"host": "redis-node-1", "port": "6379"},
  {"host": "redis-node-2", "port": "6379"},
  {"host": "redis-node-3", "port": "6379"},
  {"host": "redis-node-4", "port": "6379"},
  {"host": "redis-node-5", "port": "6379"}
]

rc = rediscluster.RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

val_len = 16

while True:
  d = datetime.now()
  key = str(uuid.uuid1())
  value = ''.join(random.choices(string.ascii_uppercase + string.digits, k = val_len)) 
  try:
    logging.debug("{} - Setting key [{}] value [{}]".format(d, key, value))
    rc.set(key, value)
    logging.debug("{} - Getting value for key [{}]".format(d, key))
    gvalue = rc.get(key)
    logging.debug("{} - Got value [{}] for key [{}]".format(d, gvalue, key))
  except rediscluster.exceptions.ClusterError as clError:
    logging.error("Cluster error: {}".format(str(clError)))
  except rediscluster.exceptions.ClusterDownError as clDown:
    logging.critical("Cluster down, rebuilding client ...")
    rc = rediscluster.RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
  except redis.exceptions.ConnectionError as clConn:
    logging.critical("Node connection error: {}".format(str(clConn)))
  except rediscluster.exceptions.MovedError as clMvErr:
    logging.error("Data redirection: {}".format(str(clMvErr)))

  sleep(0.01)
