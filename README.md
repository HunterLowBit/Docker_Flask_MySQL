# Docker_Flask_MySQL

Objetivo: Criar uma aplicação flask(Python) para gerenciar banco de dados MySQL pela web, se possivel orientar a criação da aplicação em docker.

## Checklist de Progresso

1. [X] Clonar o projeto "Docker_Instancia" para molde rapido
2. [X] Instalar e utilizar o Python
3. [ ] Criar a querry do banco de dados com MySQL-Workbench e testar modelagem
4. [X] Instalar o Flask e congelar versão (PIP FREEZE)
5. [X] Criar rotas basicas de teste
6. [ ] Utilizar gerenciador de MySQL ao Python (IMPORT MODULE)
7. [ ] Desenvolver paginas estaticas para testar formularios ao banco
8. [ ] Retocar a aparência das paginas [OPICIONAL]
9. [ ] Subir em DOCKER [OPICIONAL]
1. [ ] Finalizar a documentação [MANDATÓRIO]

---

## 1 O que está sendo feito

### 1.1 Template do projeto Docker Instância foi baixado e agora segue a seguinte extrutura de pastas:

```
|- bin
|  |- deploy.bat
|  |- deploy.sh
|  |- deployCD.bat
|  |- deployCD.sh
|
|- flask_mysql
|  |- staticFiles
|  |    |- css
|  |        |- style.css
|  |
|  |- templateFiles
|  |    |- index.html
|  |
|  |- app.py
|  |- dockerfile
|  |- requirements.txt
|
|- docker-compose.yaml
|- README.md
```

### 1.2 O codigo está sendo adaptado para receber as rotas basicas, em breve deve receber as querrys

#### app.py

```
from flask import Flask, render_template


app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port="3000", debug=True)
```

#### requirements.txt

```

```
