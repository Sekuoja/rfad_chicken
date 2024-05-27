#FROM python:3.9.6-alpine
#
## create directory for the app user
#RUN mkdir -p /home/app
#
## create the app user
#RUN addgroup -S app && adduser -S app -G app
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
