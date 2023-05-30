from transformers import pipeline


class Article:

    MAX_LENGTH = 1024

    def __init__(self, article: str = None):
        self.__article = article

    def get_summary(self, min_length: int = 25, max_length: int = 150) -> str:
        self.__validate()

        summarizer = pipeline('summarization')
        summary = summarizer(self.__article, min_length=min_length, max_length=max_length, do_sample=False)

        return summary[0]['summary_text'].strip()

    def __validate(self) -> bool:
        if len(self.__article) > self.MAX_LENGTH:
            raise ValueError(f'The length exceeds the maximum limit of {self.MAX_LENGTH} characters.')

        return True