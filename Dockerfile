FROM python:3.9

ADD requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY wait.sh /
RUN chmod +x /wait.sh
ENTRYPOINT ["/wait.sh"]

