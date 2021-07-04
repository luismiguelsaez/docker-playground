
## Create cluster
```
❯ docker compose up -d
```

## Status commands

### Check ZK nodes status
```
❯ docker compose exec zoo1 zkServer.sh status | grep "Mode:"
Mode: follower

❯ docker compose exec zoo2 zkServer.sh status | grep "Mode:"
Mode: follower

❯ docker compose exec zoo3 zkServer.sh status | grep "Mode:"
Mode: leader
```

### Check brokers
```
❯ docker compose exec zoo3zkCli.sh -server localhost:2181 ls /brokers/ids
```

## Create topics
### Create Kafka topic
```
❯ docker compose exec kafka1 kafka-topics --zookeeper zoo3:2181 --create --replication-factor 2 --partitions 3 --topic test
```

### List topics
```
❯ docker compose exec zoo3 zkCli.sh -server localhost:2181 ls /brokers/topics
[test]
```
