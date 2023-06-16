FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && \
    apt-get install git-lfs && \
    git lfs install

WORKDIR /usr/src/app
COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# As this application is not for production, won't use gunicorn
# RUN pip install gunicorn[eventlet] # if application code may need to pause for extended periods of time during request processing

COPY . .

RUN  git lfs clone https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest ./model/

EXPOSE 8000

RUN chmod +x start.sh

CMD ["./start.sh"]


