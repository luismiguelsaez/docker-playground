
## Test

- Run
```bash
docker run --name cron -d cron:latest
```

- Follow logs
```bash
docker logs -f cron
```

- Stop
```bash
docker stop -s TERM -t 5 cron
```
