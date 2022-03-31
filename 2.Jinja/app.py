from locale import currency
from flask import Flask, render_template,url_for , request, flash

app = Flask(__name__)


class Currency:

    def __init__(self,code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return '<currency {}>'.format(self.code)
        

class CantorOffer:
    def __init__(self):
        self.currencies = []
        self.denied_codes = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'US Dollar', 'US_flag.png'))
        self.currencies.append(Currency('EUR', 'Euro', 'EU_flag.png'))
        self.currencies.append(Currency('DKK', 'Danske Koronen', 'dkk_flag.png'))
        self.currencies.append(Currency('JPY', 'Japanese Yen', 'jap_flag.png'))
        self.currencies.append(Currency('PLN', 'Polish zloty', 'PL_flag.png'))
        self.denied_codes.append('USD')

    def get_by_code(self,code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknown', 'unknown', 'pirate_flag.png')
        
@app.route('/')
def index():

    return render_template ('index.html')

app.config['SECRET_KEY'] = 'AVF131'
@app.route('/exchange', methods=['GET','POST'])
def exchange():


    offer = CantorOffer()
    offer.load_offer()

    if request.method == 'GET':
        return render_template('exchange.html',offer=offer)


    else: 
        currency = 'EUR'    
        if 'currency' in request.form:
            currency = request.form['currency']

        if currency in offer.denied_codes:
            flash('The Currency {} can not be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('This selected currency is unknown for us and cant be accepted')
        else:
            flash('Request to exchange {} was accepted'.format(currency))
        
        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']


        return render_template('exchange_result.html', currency=currency, amount=amount, currency_info=offer.get_by_code(currency) )