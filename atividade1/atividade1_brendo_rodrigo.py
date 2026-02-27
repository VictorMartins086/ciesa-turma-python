
def validar_alunos(alunos, cursos):
    validos = []
    invalidos = []
    for aluno in alunos:
        motivos = []
        nome = aluno["nome"]
        email = aluno["email"]
        idade = aluno["idade"]
        curso = aluno["curso"]
        if len(nome) < 3:
            motivos.append("Nome com menos de 3 caracteres")
        if "@" not in email or "." not in email.split("@")[1]:
            motivos.append("Email inválido")
        if idade < 16:
            motivos.append("Idade menor que 16 anos")
        if curso not in cursos:
            motivos.append("Curso não disponível")
        if motivos:
            invalidos.append({"nome": nome, "motivos": motivos})
        else:
            validos.append(aluno)
    return validos, invalidos

if __name__ == "__main__":
    alunos = [
        {"nome": "Riad", "email": "cto@chronokairo.com.br", "idade": 19, "curso": "CCP"},
        {"nome": "Luan", "email": "diretoria@chronokairo.com.br", "idade": 25, "curso": "IA"},
        {"nome": "Victor", "email": "cfo@chronokairo.com.br", "idade": 19, "curso": "CCP"},
    ]
    cursos = ["CCP", "ADS", "IA"]
    validos, invalidos = validar_alunos(alunos, cursos)
    print("alunos validos:", validos)
    print("alunos invalidos:", invalidos)
