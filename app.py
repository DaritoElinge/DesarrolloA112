from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/comportamiento')
def comportamiento():
    return render_template('comportamiento.html')

@app.route('/alimentacion')
def alimentacion():
    return render_template('alimentacion.html')

@app.route('/habitos')
def habitos():
    return render_template('habitos.html')

@app.route('/domesticacion')
def domesticacion():
    return render_template('domesticacion.html')


if __name__== '__main__':
    app.run(debug=True)

