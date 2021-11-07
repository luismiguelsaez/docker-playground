
###### Manual version 4

start-manual:
	docker-compose -f docker-compose-manual.yml up -d

cl-benchmark-manual:
	docker run -it --rm --network host --entrypoint=redis-benchmark redis:6-alpine -h 127.0.0.1 -p 6382 -t ping --cluster

cl-set-manual:
	docker run -it --rm --network host --entrypoint=redis-cli redis:6-alpine -h 127.0.0.1 -p 6382 set foo bar --cluster

cl-nodes:
	docker run -it --rm --network host --entrypoint=redis-cli redis:6-alpine -h 127.0.0.1 -p 6382 cluster nodes

cl-init-manual:
	docker run --network host -it --rm inem0o/redis-trib create --replicas 1 127.0.0.1:6379 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384

stop-manual:
	docker-compose -f docker-compose-manual.yml down --remove-orphans


###### Automated version 6

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
	docker-compose down --remove-orphans
