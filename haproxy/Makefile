

hap-reload:
	docker-compose exec haproxy 'haproxy -q -f /etc/haproxy.conf -p $$(cat /var/run/haproxy.pid) -st $$(cat /var/run/haproxy.pid)'
