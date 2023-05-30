from transformers import pipeline
from flask import request, make_response

from API.ContentAIClient import ContentAIClient


class Article:

    MAX_LENGTH = 1024

    def __init__(self, article: str = None):
        self.__article = article

    def get_summary(self, min_length: int = 25, max_length: int = 150) -> str:
        self.__validate()

        summarizer = pipeline('summarization')
        summary = summarizer(self.__article, min_length=min_length, max_length=max_length, do_sample=False)

        return summary[0]['summary_text'].strip()

    def generate(self) -> str:
        return ContentAIClient().generate_article()

    def __validate(self) -> bool:
        if len(self.__article) > self.MAX_LENGTH:
            raise ValueError(f'The length exceeds the maximum limit of {self.MAX_LENGTH} characters.')

        return True




# import requests
#
# url = "https://contentai-net-text-generation.p.rapidapi.com/text-generation/api/"
#
# querystring = {"category": "health-and-medicine"}
#
# headers = {
#     "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
#     "X-RapidAPI-Host": "contentai-net-text-generation.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())