
up:
	docker-compose up -d

simulate-master-down:
	docker-compose exec redis-0 redis-cli DEBUG sleep 30

sentinel-logs:
	docker-compose logs -f sentinel-0

sentinel-masters:
	docker-compose exec sentinel-0 redis-cli -p 26379 SENTINEL MASTERS

sentinel-get-master-addr:
	docker-compose exec sentinel-0 redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

sentinel-tunnel-connect:
	docker-compose exec redis-0 redis-cli -h sentinel-tunnel -p 6379

down:
	docker-compose down --remove-orphans
