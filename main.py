from flask import Flask, request, jsonify

app = Flask(__name__)
polls = {}


@app.route('/')
def hello_world():
    """
    Returns a string
    """
    return 'Carleton Poll'


def set_poll(name, question, choices, answers):
    """
    Saves all the poll information to a dictionary called 'polls'

    Args:
        name: Name of the poll
        question: Question of the poll
        choices: List of choices
        answers: List of correct answer(s)
    Returns:
        string: A status code
    """
    polls[name] = {'question': question, 'choices': choices, 'answers': answers}
    return '200'


def get_poll(name):
    """
    Returns some of the poll information to a user

    Args:
        name: Name of the poll
    Returns:
        json: A json object with the question and the choices of the poll
    """
    question = (polls.get(name)).get('question', '')
    choices = (polls.get(name)).get('choices', '')
    answers = (polls.get(name)).get('answers', '')
    poll = {'question': question, 'choices': choices, 'answers': answers}
    return jsonify(poll)


@app.route('/poll', methods=['GET', 'POST'])
def poll():
    """
    Gets all the poll information from a POST request to /poll

    Returns:
        set_poll: Calls the set_poll() function with the poll information passed as arguments
    Raises:
        Exception: Raises an exception if the function fails
    """
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
    """
    Gets the users selection and checks if it's correct or not

    Returns:
        string: Returns 'Correct' or 'Incorrect' based on the answer
    Raises:
        Exception: Raises an exception if the function fails
    """
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
