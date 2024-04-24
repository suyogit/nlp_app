import nlpcloud

class API:
    def __init__(self):
        self.token="479520ccef150c2986b67ff0e9e0c32e58991a55"


    def sentiment_analysis(self,text):
        self.client = nlpcloud.Client("distilbert-base-uncased-emotion", self.token, gpu=False)
        response=self.client.sentiment(text)
        return response

    def grammar_correction(self,text):
        client = nlpcloud.Client("finetuned-llama-3-70b",self.token, gpu=True)
        response=client.gs_correction(text)
        return response

    def headline_generation(self,text):
        client = nlpcloud.Client("t5-base-en-generate-headline",self.token, gpu=False)
        response=client.summarization(text)
        return response
