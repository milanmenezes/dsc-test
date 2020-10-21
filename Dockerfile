FROM tiangolo/uwsgi-nginx-flask
COPY . /app
RUN pip install -r requirements.txt
ENV STATIC_URL /static
ENV STATIC_PATH /app/static
EXPOSE 80
EXPOSE 443