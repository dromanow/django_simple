from python:3.8.6

RUN pip3 install --upgrade pip

COPY ./ ./
RUN rm ./test_project/local_settings.py
RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

