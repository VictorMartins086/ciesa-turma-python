class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem

    def __str__(self):
        return f"{self.nome} ({self.senioridade}) - {self.pontos_por_dia} pts/dia - {self.linguagem}"


class Projeto:
    def __init__(self, descricao, prazo_dias, pontos_funcao):
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos_funcao = pontos_funcao
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)
        print(f"Desenvolvedor {desenvolvedor.nome} adicionado ao projeto '{self.descricao}'.")

    def calcular_capacidade_total(self):
        total = sum(d.pontos_por_dia for d in self.desenvolvedores)
        return total * self.prazo_dias

    def verificar_viabilidade(self):
        capacidade = self.calcular_capacidade_total()
        print(f"\nProjeto: {self.descricao}")
        print(f"Pontos de função necessários: {self.pontos_funcao}")
        print(f"Capacidade total da equipe: {capacidade} pontos em {self.prazo_dias} dias")
        if capacidade >= self.pontos_funcao:
            print(">>> Projeto VIÁVEL <<<")
        else:
            print(">>> Projeto INVIÁVEL <<<")

    def __str__(self):
        return f"Projeto '{self.descricao}' - Prazo: {self.prazo_dias} dias - PF: {self.pontos_funcao}"


# --- Demonstração ---

projeto = Projeto("Sistema de Gestão Acadêmica", prazo_dias=30, pontos_funcao=500)

dev1 = Desenvolvedor("Ana", "Sênior", 8, "Python")
dev2 = Desenvolvedor("Carlos", "Pleno", 5, "Python")
dev3 = Desenvolvedor("Beatriz", "Júnior", 3, "Python")

projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)
projeto.adicionar_desenvolvedor(dev3)

projeto.verificar_viabilidade()
