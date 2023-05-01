import os
from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after', methods=['POST'])
def after():
    script_path ='main.py'
    python_bin_path = 'venv/bin/python' if not os.name == 'nt' else 'venv\\Scripts\\python.exe'
    subprocess.run([python_bin_path, script_path])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)