# Gerenciador de Contatos

Este é um aplicativo de terminal em Python para gerenciar uma agenda de contatos. Permite adicionar, editar, remover, listar e marcar contatos como favoritos, tudo de forma simples e interativa.

## Funcionalidades

- Adicionar um novo contato (nome, telefone, email, favorito)
- Listar todos os contatos
- Editar um contato existente
- Deletar um contato
- Marcar ou desmarcar um contato como favorito
- Listar apenas os contatos favoritos
- Persistência dos dados em arquivo `contacts.json`

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/tehrdias/gerenciadordecontatos.git
   cd gerenciadordecontatos
   ```

2. **Execute o programa:**
   ```bash
   python gerenciador-de-contatos.py
   ```

3. **Siga o menu interativo no terminal.**

## Requisitos

- Python 3.x

## Estrutura dos dados

Os contatos são salvos em um arquivo `contacts.json` no formato:
```json
[
  {
    "nome": "Exemplo",
    "telefone": "123456789",
    "email": "exemplo@email.com",
    "favorito": true
  }
]
```

## Licença

Este projeto está sob a
