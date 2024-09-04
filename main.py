from flask import Flask, url_for, render_template

# inicialização
app = Flask(__name__)

# rotas

@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"usuario": "Guilherme", "membro_ativo": True},
        {"usuario": "João", "membro_ativo": True},
        {"usuario": "Maria", "membro_ativo": False},
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)  

@app.route("/sobre")
def pagina_sobre():
    
    return render_template('sobre.html')

# execução
app.run(debug=True)