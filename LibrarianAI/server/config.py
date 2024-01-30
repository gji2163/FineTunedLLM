import requests
from bs4 import BeautifulSoup

url = 'https://t.ly/hkAkB'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    target_class = 'plaintext'
    element = soup.find(class_=target_class).text


models = {
    #'text-gpt-0035-render-sha-0': 'gpt-3.5-turbo',
    #'text-gpt-0035-render-sha-0301': 'gpt-3.5-turbo-0314',
    'text-gpt-0040-render-sha-0314': 'gpt-4-0314',
    'text-gpt-0040-render-sha-0': 'gpt-4',
}

special_instructions = {
    'default': [
        {
            'role': 'system',
            'content': element,
        },
        {
            'role': 'assistant',
            'content': 'instructions applied and understood'
        }
    ]
}
