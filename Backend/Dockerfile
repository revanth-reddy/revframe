FROM python:3.9-alpine

WORKDIR /backend
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install -r requirements.txt
EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0","--port=5001"]