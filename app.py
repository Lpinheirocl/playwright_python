import os
from flask import Flask
from app.routes.home import home_route
from app.routes.pagtest import pagtest_route

app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(home_route)
app.register_blueprint(pagtest_route)

app.run(debug=True)