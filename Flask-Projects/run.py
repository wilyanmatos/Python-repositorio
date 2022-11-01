#Execução do Aplicativo
# Dúvidas
'''
1 - Como o run.py consegue chamar as outros arquivos?
R:from app (refere-se ao app do topo das páginas) / import (refere-se ao app primeiro __init__.py)
'''

from app import app
from datetime import datetime


Hora = datetime.now().hour
Min = datetime.now().minute

print(f'Atualizado em: \033[34m{Hora}:{Min}\033[m')
if __name__ == '__main__':
    app.run(debug=True)