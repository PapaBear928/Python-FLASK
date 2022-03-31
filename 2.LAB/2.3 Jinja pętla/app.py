from msilib.schema import Class
from flask import Flask, render_template,url_for , request,redirect

app = Flask(__name__)



Class PriorityType:
    def __init__(self, code, description, selected):
        self.code = code
        self.description = description
        self.selected = selected


Class NotifciationPriorities:

    def __init__(self):
        self.list_of_priorities = []
    
    def load_priorities(self):
        self.list_of_priorities.append(PriorityType('high', 'HIGH', 'FALSE'))
        self.list_of_priorities.append(PriorityType('mediun', 'MEDIUM', 'FALSE'))
        self.list_of_priorities.append(PriorityType('normal', 'NOT URGENT', 'FALSE'))

    def get_priority_by_code(self,code):
        for p in self.list_of_priorities:
            if p.code == code:
                return p
        return PriorityType('normal', 'NOT URGENT', True)

@app.route('/notification', methods=['GET','POST'])
def notification():


    notification_priorities = NotifciationPriorities()
    notification_priorities.load_priorities()


    if request.method == 'GET':
        return render_template('notification.html',
         list_of_priorities=notification_priorities.list_of_priorities)

    else:
        room_number = request.form['room_number'] if 'room_number' in request.form else ''
        guest_name = request.form['guest_name'] if 'guest_name' in request.form else ''
        disfunction =  request.form['disfunction'] if 'disfunction' in request.form else ''
        priority = request.form['priority'] if 'priority' in request.form else 'normal'

        return render_template('templatka.html',
                room_number=room_number, guest_name=guest_name, disfunction=disfunction, priority_type=priority_type)



    