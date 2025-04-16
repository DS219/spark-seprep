FROM python:latest
WORKDIR /opt/app-root/bin
RUN pip install --upgrade jupyterlab 
WORKDIR /opt/app-root/src
COPY EvanLeong.ipynb .
COPY requirements.txt .
CMD ["jupyter", "lab", "--port=8888", "--allow-root", "--ip="]
