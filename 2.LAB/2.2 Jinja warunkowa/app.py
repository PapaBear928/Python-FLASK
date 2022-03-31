from flask import Flask, render_template,url_for , request

app = Flask(__name__)

@app.route('/')
def index():

    return 'Napis ćwiczebny do wyświetlania'


@app.route('/notification', methods=['GET','POST'])
def exchange():

    if request.method == 'GET':
        return render_template('notification.html')

    
    else:
        room_number = request.form['room_number'] if 'room_number' in request.form else ''
        guest_name = request.form['guest_name'] if 'guest_name' in request.form else ''
        disfunction =  request.form['disfunction'] if 'disfunction' in request.form else ''
        priority = request.form['priority'] if 'priority' in request.form else 'normal'

        return render_template('templatka.html',
                room_number=room_number, guest_name=guest_name, disfunction=disfunction, priority=priority)



    