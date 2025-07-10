FROM python:3.14-rc-slim

WORKDIR /app

COPY requirement.txt .

RUN python3 -m pip install --no-cache-dir -r requirement.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
