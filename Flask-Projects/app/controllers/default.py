# Rotas para páginas

from app import app

@app.route("/")
def index():
    return "Hello World!"