import os
from flask import Flask
from app.routes.home import home_route

app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(home_route)

app.run(debug=True)