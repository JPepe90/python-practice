FROM python:3.8

WORKDIR /charts
COPY requirements.txt /charts/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /charts/requirements.txt

COPY . /charts

CMD bash -c "while true; do sleep 1; done"