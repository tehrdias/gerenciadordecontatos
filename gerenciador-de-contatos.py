import json
import os

ARQUIVO_CONTATOS = "contacts.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, "r") as f:
            return json.load(f)
    return []

def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w") as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato(contatos, nome, telefone, email, favorito):
    contatos.append({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    })

def listar_contatos(contatos):
    return [
        f"{i+1}. {'★' if c['favorito'] else ' '} {c['nome']} - {c['telefone']} - {c['email']}"
        for i, c in enumerate(contatos)
    ]

def editar_contato(contatos, idx, nome=None, telefone=None, email=None):
    if 0 <= idx < len(contatos):
        c = contatos[idx]
        if nome: c["nome"] = nome
        if telefone: c["telefone"] = telefone
        if email: c["email"] = email

def alternar_favorito(contatos, idx):
    if 0 <= idx < len(contatos):
        contatos[idx]["favorito"] = not contatos[idx]["favorito"]

def listar_favoritos(contatos):
    return [
        f"{i+1}. ★ {c['nome']} - {c['telefone']} - {c['email']}"
        for i, c in enumerate(contatos) if c["favorito"]
    ]

def deletar_contato(contatos, idx):
    if 0 <= idx < len(contatos):
        del contatos[idx]

def exibir_menu():
    print("\nGerenciador de Contatos")
    print("1. Listar Contatos")
    print("2. Adicionar Contato")
    print("3. Editar Contato")
    print("4. Deletar Contato")
    print("5. Marcar/Desmarcar Favorito")
    print("6. Listar Favoritos")
    print("7. Sair")

def main():
    contatos = carregar_contatos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nContatos:")
            for contato in listar_contatos(contatos):
                print(contato)

        elif opcao == "2":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            favorito = input("É favorito? (s/n): ").lower() == 's'
            adicionar_contato(contatos, nome, telefone, email, favorito)
            salvar_contatos(contatos)
            print("Contato adicionado.")

        elif opcao == "3":
            idx = int(input("Digite o número do contato para editar: ")) - 1
            nome = input("Novo nome (deixe em branco para manter): ")
            telefone = input("Novo telefone (deixe em branco para manter): ")
            email = input("Novo email (deixe em branco para manter): ")
            editar_contato(contatos, idx, nome or None, telefone or None, email or None)
            salvar_contatos(contatos)
            print("Contato atualizado.")

        elif opcao == "4":
            idx = int(input("Digite o número do contato para deletar: ")) - 1
            deletar_contato(contatos, idx)
            salvar_contatos(contatos)
            print("Contato deletado.")

        elif opcao == "5":
            idx = int(input("Digite o número do contato para marcar/desmarcar favorito: ")) - 1
            alternar_favorito(contatos, idx)
            salvar_contatos(contatos)
            print("Favorito alterado.")

        elif opcao == "6":
            print("\nContatos Favoritos:")
            for contato in listar_favoritos(contatos):
                print(contato)

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()