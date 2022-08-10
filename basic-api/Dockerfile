FROM ubuntu:20.04

WORKDIR /home

RUN apt-get update && apt-get -y install git \
    wget \
    locales \
    python3 \
    python3-pip

WORKDIR /home
COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
COPY api.py /home/

CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "4000"]