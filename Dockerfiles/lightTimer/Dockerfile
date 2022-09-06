FROM python:3.8

COPY lightTimer.py ./
COPY growFunctions.py ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir RPi.GPIO

CMD ["python", "./lightTimer.py"]