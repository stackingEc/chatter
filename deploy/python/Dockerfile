 FROM python:3.5
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /opt/services/chat
 WORKDIR /opt/services/chat
 RUN git clone https://github.com/stackingEc/chatter.git .
 RUN pip install -r requirements.txt
 RUN cd deploy/python && pipenv install --system
 RUN cd ../ && python3 manage.py collectstatic
 EXPOSE 8000
 CMD ["gunicorn", "--chdir", "chat", "--bind", ":8000", "chat.wsgi:application"]