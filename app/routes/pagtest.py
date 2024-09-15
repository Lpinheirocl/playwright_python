from flask import Blueprint, render_template, request
import os
import subprocess

pagtest_route = Blueprint('pagtest', __name__)

@pagtest_route.route('/<folder_name>')
def folder_content(folder_name):
    # Caminho para o diretório da pasta
    directory_path = os.path.join(os.path.dirname(__file__), '../tests', folder_name)
    
    # Liste os arquivos .py no diretório
    py_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f)) and f.endswith('.py')]

    return render_template('pagtest/pagtest.html', folder_name=folder_name, py_files=py_files)

@pagtest_route.route('/execute/<folder_name>/<file_name>', methods=['POST'])
def execute_file(folder_name, file_name):
    # Caminho para o diretório e arquivo
    file_path = os.path.join(os.path.dirname(__file__), '../tests', folder_name, file_name)
    
    # Executa o arquivo .py
    result = subprocess.run(['python', file_path], capture_output=True, text=True)

    # Renderize o template com o resultado da execução
    return render_template('pagtest/pagtest.html', folder_name=folder_name, py_files=[file_name], result=result.stdout)
