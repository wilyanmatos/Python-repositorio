from flask import Flask
from datetime import datetime
app = Flask(__name__)

Hora = datetime.now().hour
Min = datetime.now().minute


@app.route("/")
def index():
    return "Hello World!"


print(f'Atualizado em: \033[34m{Hora}:{Min}\033[m')
if __name__ == '__main__':
    app.run(debug=True)