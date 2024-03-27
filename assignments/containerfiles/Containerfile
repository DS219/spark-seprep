FROM alpine
WORKDIR /akshat-sharma
ADD scripts.py /akshat-sharma
RUN apk add --update python3 py3-pip curl
RUN chmod +x scripts.py

CMD ["python3", "./scripts.py"]
