 FROM python:3.5
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /chat
 WORKDIR /chat
 RUN git clone https://github.com/defStacker/chat.git .
 RUN pip install -r requirements.txt
 ADD . /chat/