.PHONY: all

all: up sentinel-get-master-addr simulate-master-down sentinel-tunnel-connect down

up:
	docker-compose up -d --build

simulate-master-down:
	docker-compose exec redis-0 redis-cli DEBUG sleep 5

sentinel-logs:
	docker-compose logs -f sentinel-0

sentinel-info:
	docker-compose exec sentinel-0 redis-cli -h localhost -p 26379 info sentinel

sentinel-masters:
	docker-compose exec sentinel-0 redis-cli -p 26379 SENTINEL MASTERS

sentinel-get-master-addr:
	docker-compose exec sentinel-0 redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

sentinel-tunnel-connect:
	docker-compose exec redis-0 redis-cli -h sentinel-tunnel -p 6379 INFO Replication

sentinel-failover:
	docker-compose exec sentinel-0 redis-cli -h localhost -p 26379 sentinel failover mymaster

down:
	docker-compose down --remove-orphans
