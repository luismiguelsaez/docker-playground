
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
Created topic test.
```

### List topics
```
❯ docker compose exec zoo3 zkCli.sh -server localhost:2181 ls /brokers/topics
[test]
```

### Launch test
```
❯ docker compose exec kafka1 kafka-producer-perf-test --topic test --num-records 10 --record-size 10 --throughput -1 --producer-props acks=1 bootstrap.servers=kafka1:9092
10 records sent, 6.557377 records/sec (0.00 MB/sec), 267.50 ms avg latency, 1482.00 ms max latency, 132 ms 50th, 1482 ms 95th, 1482 ms 99th, 1482 ms 99.9th.
```
