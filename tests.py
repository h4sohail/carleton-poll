import requests

url = 'http://127.0.0.1:5000/poll'
name = 'Math Poll'
question = 'What is 2+2?'
choices = '1,,4,,0,,6,,4'
answers = '2,,5'

# Make a new poll
params = {'name': name, 'question': question, 'choices': choices, 'answers': answers}
response = requests.post(url, json=params)
print('[POST] Status Code: {}'.format(response.status_code))

# Return the poll
params = {'name': name}
response = requests.get(url, json=params)
print(f'[GET] Status Code: {response.status_code}')
print(f'Response: {response.text}')

# Answer the poll
url = 'http://127.0.0.1:5000/poll/answer'
params = {'name': name, 'answer': '2'}
response = requests.post(url, json=params)
print(f'[GET] Status Code: {response.status_code}')
print(f'Response: {response.text}')
