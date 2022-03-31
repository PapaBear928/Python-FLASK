from flask import Flask, render_template, session, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import hashlib
import binascii
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user, fresh_login_required
from urllib.parse import urlparse,  urljoin

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'First, please log in using this form:'
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = 'For safery reason, you need to login twice'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))


    def __repr__(self):
        return ('User: {}, {}'.format(self.name))


    def get_hashed_password(password):
        """Tutaj zahaszujemy hasło"""
        #wartość generowana używając os.urandom(60)
        os_urandom_static = b"ID_\x12p:\x8d\xe7&\xcb\xf0=H1\xc1\x16\xac\xe5BX\xd7\xd6j\xe3i\x11\xbe\xaa\x05\xccc\xc2\xe8K\xcf\xf1\xac\x9bFy(\xfbn.`\xe9\xcd\xdd'\xdf`~vm\xae\xf2\x93WD\x04" 
        salt = hashlib.sha256(os_urandom_static).hexdigest().encode('ascii') 
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000) 
        pwdhash = binascii.hexlify(pwdhash) 
        return (salt + pwdhash).decode('ascii')


    def verify_password( stored_password_hash, provided_password):
        """Tutaj je sobie zhaszujemy i porównamy"""
        salt = stored_password_hash[:64]
        stored_password = stored_password_hash[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii') 
        return pwdhash == stored_password
    

@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.id == id).first()

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

class LoginForm(FlaskForm):
    name = StringField('User name')
    password = PasswordField('Password')
    remember = BooleanField('Remember me')

@app.route('/init')

def init():
    db.create_all()

    admin = User.query.filter(User.name == 'admin').first()
    if admin == None:
        admin = User(id=1, name='admin', password=User.get_hashed_password('Passw0rd'),
                    first_name="King", last_name="Kong")
        db.session.add(admin)
        db.session.commit()


    return '<h1> Initial configuration done! </h1>'


app.route('/')
def index():
    return '<h1> No elko </h1>'

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.name == form.name.data).first()
        if user != None and User.verify_password(user.password, form.password.data ):
            login_user(user, remember=form.remember.data)

            next = request.args.get('next')
            if next and is_safe_url(next):
                return redirect(next)
            else:
                return '<h1> Sesja zalogowana drogi użytkowuniu </h1>'

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return '<h1> You are out </h1>'

@app.route('/docs')
@login_required
def docs():
    return '<h1> You have an acces to protected docs. Welcome here {}.  </h1>'.format(current_user.name)


@app.route('/secrets')
@fresh_login_required
def secrets():
    return '<h1> Not implemented yet </h1>'





