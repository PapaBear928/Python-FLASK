from flask import (
    Flask, 
    jsonify
)

# Function that create the app 
def create_app(test_config=None ):
    # create and configure the app
    app = Flask(__name__)

    # Simple route
    @app.route('/')
    def hello_world(): 
        return jsonify({
           "status": "success",
            "message": "Hello World!"
        }) 
     
    @app.route('/about')
    def about():
        return '<h1> We are BOIs</h1>'
        
    return app # do not foget to return the app

APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    APP.run(debug=True)