## About the Project
In this project I used `Django` as backend and `Django REST Framework` to build the RESTful
API to analyse the sentiment of a text. The API endpoint is `/analyze` which takes the following
data as POST request payload:

```json
{
  "text": "Simple text"
}
```
And return the output after analyse the sentiment of that text as following:
```json
{
  "sentiment": "positive/negative/neutral"
}
```
The API can be tested at `docs/` endpoint which will load the `Swagger Docs`.

## About the Model
The pre-trained model used in this project to analyze the sentiment of a sentence/text
`cardiffnlp/twitter-roberta-base-sentiment-latest` which can be found 
[here](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest).

This is Twitter-roBERTa-base for Sentiment Analysis model which updated at 2022 and trained on ~124M tweets from 
January 2018 to December 2021, and fine-tuned for sentiment analysis with the TweetEval benchmark.

## Project Setup
The project can be setup and run by **2 ways**:

- By using Docker
- Manual Setup

### Using Docker
This is the easiest way to set up and run the project. For this, the `Docker` and `docker compose plugin` are
need to be installed in your local computer. The installation instructions can be found [here](https://docs.docker.com/engine/install/).

After that, use the following commands to run the project:
1. `git clone https://github.com/shazolKh/Sentiment-Analysis.git`
2. `cd Sentiment-Analysis/`
3. `cp .env.example .env` and put some random text as the value of `SECRET_KEY` at `.env` file.
4. `docker compose up --build`

The last command will take some time to download the model and install the required dependencies to run the project.
The project will be available at `localhost:8000` or `http://127.0.0.1:8000`. 
After that, the API can be tested with API testing tool or at `docs/` endpoint with **Swagger**.

### Manual Setup
Assuming you have completed the necessary setup to perform `python` related commands. And also assuming
that you are using a linux computer. Use the following commands to run the project. 
Noted that, at least, python 3.8 is needed.

1. `apt update`
2. `apt-get install git-lfs`
3. `git lfs install`
4. `git clone https://github.com/shazolKh/Sentiment-Analysis.git`
5. `cd Sentiment-Analysis/`
6. `python -m venv venv` or `python3 -m venv venv`
7. Activate the virtual environment.
8. `pip install -r requirements.txt`
9. Change the working directory to `model/` folder.
10. `git lfs clone https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest`
11. Change the working directory back to `Sentiment-Analysis/` i.e. project root folder.
12. `python manage.py migrate`
13. `python manage.py runserver`

The project will be available at `http://127.0.0.1:8000`. And the API can be tested with API testing tool or 
at `docs/` endpoint with **Swagger**.