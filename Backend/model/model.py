import openai
from os import environ

"""
This is just a sample OpenAI model, please replace the key or the model

Get your key at: https://platform.openai.com/account/api-keys

"""


# openai.api_key = "your_OPENAI_KEY"
openai.api_key = "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"

def textmodel(input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="generate a paragraph related to:" + input,
        temperature=0.7, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0
    )
    
    print(response)
    
    return response
