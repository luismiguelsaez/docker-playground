FROM python:3.6

RUN pip install redis-py-cluster==2.1.3

RUN mkdir /app
COPY cluster.py /app

ENTRYPOINT ["python","/app/cluster.py"]
