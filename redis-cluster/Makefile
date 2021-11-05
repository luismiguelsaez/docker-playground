
start:
	docker-compose up -d

start-manual:
	docker-compose -f docker-compose-manual.yml up -d

cl-init:
	docker run --net redis-cluster_redis-cluster -it --rm wenxiang/redis-trib create redis-0:6379 redis-1:6379 redis-2:6379 redis-3:6379 redis-4:6379 redis-5:6379

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
