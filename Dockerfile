FROM python:3.9.1-buster -m install --upgrade pip

WORKDIR /root/dreamkiller

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","dreamkiller"]
