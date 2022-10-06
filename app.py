from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World"

@app.route("/have-a-nice-day")
def pagina_greeting():
    return "Have a nice day!"

if __name__ == '__main__':
    app.run()