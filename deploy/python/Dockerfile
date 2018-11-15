 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /chat
 WORKDIR /chat
 RUN git clone https://github.com/stackingEc/chatter.git .
 RUN pip install -r requirements.txt && python3 manage.py collectstatic --no-input && cd chat
 EXPOSE 8000
 CMD ["gunicorn", "--chdir", "chat", "--bind", ":8000", "chat.wsgi:application"]