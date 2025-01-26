FROM python:latest
WORKDIR /app
#COPY package.json .
#RUN npm install
COPY sample.py /app
#EXPOSE 3000

CMD ["python","sample.py"]