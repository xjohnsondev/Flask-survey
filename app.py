from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "key"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    instructions = survey.instructions
    return render_template('survey-start.html', instructions=instructions)

@app.route('/question/add', methods=['POST'])
def add_answer():
    answer = request.form['option']
    responses.append(answer)
    print(responses)
    return redirect(f"/question/{len(responses)+1}")

@app.route('/question/<int:q>')
def show_question(q):

    if q != len(responses)+1:
        flash('Invalid question', 'error')
        return redirect(f"/question/{len(responses)+1}")

    if len(responses) < len(survey.questions):
        q = survey.questions[len(responses)].question
        choices = survey.questions[len(responses)].choices
        return render_template('question.html', q=q, choices=choices)
    else: 
        flash('Survey submitted', 'success')
        return render_template('survey-end.html')

@app.route('/survey-end')
def survey_end():
    return render_template('survey-end.html')
