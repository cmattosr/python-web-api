# carregar os dados
dados = [
    {"nome": "Joaquim", "idade": 20},
    {"nome": "Maria", "idade": 30}
]

# processar
template = """\
<html>
<body>
    <ul>
        <li> Nome: {dados[nome]} </li>
        <li> Idade: {dados[idade]} </li>
    </ul>
</body>
</html>
"""

# renderizar
for item in dados:
    print(template.format(dados=item))