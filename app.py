import sqlite3

def conectar():
    return sqlite3.connect("Usuarios.db")

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)" , (nome, email)
    )
    conn.commit()
    conn.close()


    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(usuario)
    
    conn.close()

def deletar_usuario():
    id_usuario = input("Digite o ID do usuário: ")
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario))

    conn.commit()
    conn.close()

    print("Usuário deletado com sucesso!")

while True:
    print("\Sistema de Cadastro")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Deletar usuário")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        deletar_usuario()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida")