FROM python:alpine3.7
LABEL Author="Bacha Ilyes"



COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5001
ENTRYPOINT ["python"]

CMD ["app.py"]
