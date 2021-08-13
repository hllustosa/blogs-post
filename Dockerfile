FROM python
SHELL ["/bin/bash", "-c"] 

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV 'PRODUCTION'


# install dependencies
COPY . /usr/src/app
RUN pip3 install -r requirements.txt
EXPOSE 8000

CMD ["./run.sh"]