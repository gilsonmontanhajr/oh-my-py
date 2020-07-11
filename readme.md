# Oh-my-py
Esta é uma coletânea de scripts que venho criando para aprender python. Todos utilizam o serviço Flask (web).

#### Pré requisitos

Versão do Python superior ao 3.6 (3.7 recomendável)

Módulo `pip`.

##### Módulos necessários

* flask
* Mysql



#### Como instalar

```bash
python3 -m pip install flask mysql-connector
```



##### Utilização

Atualmente estou utilizando o pycharm para os testes, más fique à vontade para utilizar o editor de textos (ou IDE) que quiser.



Todos os scripts eu rodo da seguinte maneira : 

```bash
python nome_do_arquivo.py
```



## hello_world.py

Mini app que utiliza o Flask para mostrar um `hello world` no navegador.

A rota é a default /.

Para ver o código, basta rodar o script e acessar : 

```
http://localhost:5000
```

Ou

```bash
curl localhost:5000
```



## hello_template.json

Aqui temos duas rotas : 

* /
```
http://localhost:5000
```

* /people
```
http://localhost:5000/people/{name}/gender
```

Onde, a rota `/` não faz muita coisa, ele já tem um nome e sexo setados, só retorna um html com o resultado disso.

Já a rota `/people` recebe um método `GET` e recebe parâmetros via URL. Estes parâmetros são : 

```
http://localhost:5000/people/QualquerNome/{Male|Female}
```

Ambos os testes retornam o mesmo template html. Tem um teste feito via `render_template` (no arquivo html) neste projeto.



## hello_json.py

Mini aplicação web (Flask) que é acessada em localhost na rota hello_json, exemplo : 

```
http://localhost:5000/hello_json
```

Ele vai apresentar um formulário html básico e vai retornar um json com os dados adicionados ao formulário.



## mysql_test_conn.py

Este aqui já é um pouco mais avançado, utilizo as libs do `Flask` e do `MySQL`.

É um pequeno serviço que testa a conexão com o MySQL.

A rota de acesso é `/mysql` : 

```
http://localhost:5000/mysql
```

É um formulário formatado com CSS onde você entra com as informações e ele busca uma classe uma rota chamada `test_mysql` que vai tentar conectar no banco referente às informações.



## TODO

* Conexão com PostgreSQL
* Conexão com MongoDB
* Conexão com Kubernetes
  * Get pods
  * Get services
  * RBAC
    * Role
    * ClusterRole



Legal né ?

Sinta- se à vontade para contribuir e evoluir estes testes.