from flask import Blueprint, render_template
import os

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    # Caminho para o diretório de testes
    directory_path = os.path.join(os.path.dirname(__file__), '../tests')
    
    # Liste as pastas no diretório e filtre aquelas que começam com "site"
    folders = [f for f in os.listdir(directory_path) 
               if os.path.isdir(os.path.join(directory_path, f)) and f.startswith('site')]
    
    return render_template('home/index.html', folders=folders)