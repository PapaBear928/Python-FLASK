
from flask import Flask, requests, url_for , redirect


app = Flask(__name__)

@app.route('/cooking', methods = ['GET','POST'])
def cooking():

    if requests.methods == 'GET':
        body = f'''
    
        <form id="cooking_form" action="{url_for('cooking')}" method="POST>
            <label for=note>What is your note for the receipt?</label><br>
            <select id="nore" name="note">
                <option value="5">It is great!</option>
                <option value="4">It is very good</option>
                <option value="3" selected>It is just good</option>
                <option value="2">It was poor</option>
                <option value="1">It was horrible!</option>
            </select><br> 

            <label for=comment>Write down your comments:</label><br>
            <textarea id="comment" name="comment" rows="3" cols="50">
                ...
            </textarea><br>

            <label for="decision">Would you cook it for your family?</label><br>
            <input type="checkbox" id="decision" name="decision"><br>

            <input type="submit" value="Share my feedback">
        </form>
    
    
        '''
        return body

    else:

        note = 3
        if 'note' in requests.form:
            note = requests.form['note']

        comment = ''

        if 'comment' in requests.form:
            comment = requests.form['comment']

        decision = False

        if 'decision' in requests.form:
            decision = requests.form['decision']


        return body

@app.route('recipe', method=['POST'])
def recipe():


    note = 3
    if 'note' in requests.form:
        note = requests.form['note']

    comment = ''

    if 'comment' in requests.form:
        comment = requests.form['comment']

    decision = False

    if 'decision' in requests.form:
        decision = requests.form['decision']

    