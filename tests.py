import requests

url = 'http://127.0.0.1:5000/poll'

name = 'MathPoll'
question = 'What is 2+2?'
choices = '1,,4,,0,,6,,4'
answers = '2,,5'


params = {'name': name, 'question': question, 'choices': choices, 'answers': answers}
response = requests.post(url, json=params)
print('[POST] Status Code: {}'.format(response.status_code))


params = {'name': name}
response = requests.get(url, json=params)
print(f'[GET] Status Code: {response.status_code}')
print(f'Response: {response.text}')
