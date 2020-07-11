FROM python:stretch

WORKDIR /usr/src/backend

COPY ./ ./

RUN pip install -r req.txt
RUN chmod 644 app.py

EXPOSE 5000

CMD ["/bin/bash"]

