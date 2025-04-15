# Necessário apenas se for executar sem o comando shell
from manage import *
import contextlib, io

saida = io.StringIO()

# Inicialização do django e definição das configurações
with contextlib.redirect_stdout(saida):
    main()

# Seus imports necessários
from aula.models.exemplo import Exemplo
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


# User = get_user_model()
# User.objects.create_superuser('ifrs', 'admin@myproject.com', 'ifrs')

# Exemplo de consulta e de impressão do resuldado
# print(Exemplo.objects.find_by_nome("IFRS"))
def listar_registros():
    exemplos = Exemplo.objects.all()
    return exemplos


# Cria um registro
def criar_registro(nome):
    try:
        campus = Exemplo(nome=nome)
        campus.full_clean()
        campus.save()
    except ValidationError as e:
        print("Erro ao criar")
        raise e


def __main__():
    flag = True
    while flag:
        print("\n== MENU ===")
        print("1. Criar um registro")
        print("2. Listar registros")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("=== Criando registro para Exemplo ===")
            nome = input("Digite o nome do Exemplo que deseja criar: ")
            criar_registro(nome)

        if opcao == "2":
            print("=== Listando os registros encontrados para Exemplo ===")
            for exemplo in listar_registros():
                print(f"ID: {exemplo.id}: {exemplo.nome}")

        elif opcao == "0":
            print("Saindo do script...")
            flag = False
    print("Fim do script.")


if __name__ == "__main__":
    __main__()
