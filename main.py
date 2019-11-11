from flask import Flask, request, jsonify

app = Flask(__name__)
polls = {}


@app.route('/')
def hello_world():
    return 'Carleton Poll'


def set_poll(name, question, choices, answers):
    polls[name] = {'question': question, 'choices': choices, 'answers': answers}
    return '200'


def get_poll(name):
    question = (polls.get(name)).get('question', '')
    choices = (polls.get(name)).get('choices', '')
    answers = (polls.get(name)).get('answers', '')
    poll = {'question': question, 'choices': choices, 'answers': answers}
    return jsonify(poll)


@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data['name']
            question = data['question']
            choices = data['choices']
            choices = choices.split(',,')
            answers = data['answers']
            answers = answers.split(',,')

            return set_poll(name, question, choices, answers)
        except Exception as e:
            print(e)
            return e
    if request.method == 'GET':
        try:
            data = request.get_json()
            name = data['name']
            return get_poll(name)
        except Exception as e:
            print(e)
            return e


@app.route('/poll/answer', methods=['POST'])
def answer():
    try:
        data = request.get_json()
        name = data['name']
        choice = data['answer']
        answers = (polls.get(name)).get('answers', '')
        if choice in answers:
            return 'Correct'

        else:
            return 'Incorrect'

    except Exception as e:
        print(e)
        return e


app.run(debug=True)
