from rediscluster import RedisCluster

startup_nodes = [
  {"host": "127.0.0.1", "port": "6379"},
  {"host": "127.0.0.1", "port": "6380"},
  {"host": "127.0.0.1", "port": "6381"},
  {"host": "127.0.0.1", "port": "6382"},
  {"host": "127.0.0.1", "port": "6383"},
  {"host": "127.0.0.1", "port": "6384"},
]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

rc.set("foo", "bar")
print(rc.get("foo"))
