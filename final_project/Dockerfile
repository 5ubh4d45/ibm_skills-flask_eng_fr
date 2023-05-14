FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirments.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]