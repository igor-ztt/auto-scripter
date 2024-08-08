# Auto Scripter

## Descrição

O Auto Scripter é uma ferramenta que permite criar um script Python que recria a estrutura de diretórios e arquivos de um projeto existente. O script gerado pode ser executado para reconstruir a estrutura do projeto em um novo local.

## Funcionalidades

- Analisa a estrutura de diretórios e arquivos de um projeto.
- Ignora os diretórios `.venv` e `.idea`.
- Gera um script Python que, ao ser executado, recria a estrutura do projeto.

## Requisitos

- Python 3.x

## Como Utilizar

1. Clone este repositório ou copie o script para o seu ambiente local.

2. Execute o script `scripter.py`.

    ```sh
   python scripter.py

3. Siga as instruções na tela:

   - Digite o caminho do projeto para o qual você quer criar o acelerador.
   - Digite o caminho onde você quer salvar o script acelerador do projeto.

4. O script gerado será salvo no local especificado com o nome `acelerador_<nome_do_projeto>.py`.

## Exemplo de Uso

### Passo 1: Executar o Auto Scripter

```sh
python scripter.py
```

### Passo 2: Fornecer os Caminhos

```
Bem-vindo ao Auto Scripter.
Com ele você pode selecionar o diretório do seu projeto e gerar um script python que recria a estrutura de diretórios e arquivos do seu projeto.
Siga as instruções na tela para continuar.

Digite o caminho do projeto para o qual você quer criar o acelerador: "C:\Users\Seu_Usuario\Projetos\Nome_do_Projeto"
Digite o caminho onde você quer salvar o script acelerador do projeto: "C:\Users\Seu_Usuario\Projetos\Scripts"
```

### Passo 3: Resultado

```
Script gerado em: C:\Users\Seu_Usuario\Projetos\Scripts\acelerador_Nome_do_Projeto.py
```

### Passo 4: Executar o Script Gerado

1. Navegue até o diretório onde o script foi salvo.

   ```sh
   cd C:\Users\Seu_Usuario\Projetos\Scripts
   ```

2. Execute o script gerado.

   ```sh
   python acelerador_Nome_do_Projeto.py
   ```

3. Forneça o caminho onde você quer salvar a estrutura do projeto:

   ```
   Digite o diretório onde você quer salvar o projeto: "C:\Users\Seu_Usuario\Projetos\Novo_Nome_do_Projeto"
   ```

4. A estrutura do projeto será recriada no local especificado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT.
