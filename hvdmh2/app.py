
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina1():
    return render_template('pagina1.html')

@app.route('/estudios')
def pagina2():
    return render_template('pagina2.html')

@app.route('/experiencia')
def pagina3():
    return render_template('pagina3.html')

@app.route('/referencias')
def pagina4():
    return render_template('pagina4.html')

if __name__ == '__main__':
    app.run(debug=True)
