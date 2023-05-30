import configparser
import random

import requests


class ContentAIClient:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('config.ini')

        self.__rapid_api_key = self.__config['api']['RAPID_API_KEY']
        self.__content_ai_host = self.__config['api']['CONTENT_AI_HOST']
        self.__base_url = self.__config['api']['CONTENT_AI_BASE_URL']

        self.__category = Category()

    def generate_article(self):
        response = requests.get(f'{self.__base_url}/text-generation/api/', headers={
            "X-RapidAPI-Key": self.__rapid_api_key,
            "X-RapidAPI-Host": self.__content_ai_host
        }, params={
            "category": self.__category.one_random()
        })

        print(response)

        # url = "https://contentai-net-text-generation.p.rapidapi.com/text-generation/api/"
        # querystring = {"category": "health-and-medicine"}
        #
        #
        # response = requests.get(url, headers=headers, params=querystring)
        #
        # try:
        #     article = Article().generate()
        # except ValueError as ve:
        #     return make_response({
        #         'error': str(ve)
        #     }, 400)
        # except Exception as e:
        #     print(e)
        #     return make_response({
        #         'error': 'The server could not process the request.'
        #     }, 500)
        #
        # return {
        #     'article': article
        # }
        #
        # print(response.json())
        #
        # return ''


class Category:
    def __init__(self):
        self.__categories = [
            'biology',
            'history',
            'geography-and-places',
            'natural-sciences',
            'warfare',
            'music',
            'social-sciences-and-society',
            'language-and-literature',
            'media-and-drama',
            'engineering-and-technology',
            'sports-and-recreation',
            'transport',
            'video-games',
            'media',
            'art-and-architecture',
            'meteorology',
            'art-architecture-and-archaeology',
            'religion-mysticism-and-mythology',
            'agriculture-food-and-drink',
            'literature-and-theatre',
            'politics-and-government',
            'video-gaming',
            'business-economics-and-finance',
            'sport-and-recreation',
            'royalty-and-nobility',
            'computing',
            'education',
            'philosophy-and-religion',
            'culture-and-society',
            'food-and-drink',
            'physics-and-astronomy',
            'mathematics',
            'health-and-medicine',
            'law',
            'geology-and-geophysics',
            'chemistry-and-mineralogy',
            'philosophy-and-psychology',
            'language-and-linguistics',
            'heraldry-honors-and-vexillology'
        ]

    def one_random(self) -> str:
        return random.choice(self.__categories)

