FROM python:3.8

COPY waterLevelSensor.py ./
COPY growFunctions.py ./
COPY SDL_Adafruit_ADS1x15 ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir RPi.GPIO && \
    pip install --no-cache-dir smbus

CMD ["python", "./waterLevelSensor.py"]