FROM python:3.9-alpine

RUN pip install redis
COPY main.py /main.py

ENTRYPOINT ["python","/main.py"]
