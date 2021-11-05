
start:
	docker-compose up -d

cl-benchmark:
	docker-compose exec redis-node-1 redis-benchmark -n 1000000 -t set,get -P 16 -q -h 127.0.0.1 -p 6379 --cluster

cl-info:
	docker-compose exec redis-node-0 redis-cli CLUSTER INFO

cl-nodes: # https://redis.io/commands/cluster-nodes#serialization-format
	docker-compose exec redis-node-0 redis-cli CLUSTER NODES

get-cli:
	docker-compose exec redis-node-0 redis-cli

stop:
	docker-compose down
