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

## Código

```python
import os

def analyze_directory(base_dir):
    structure = {}
    for root, dirs, files in os.walk(base_dir):
        # Ignore the .venv and .idea directories
        if '.venv' in dirs:
            dirs.remove('.venv')
        if '.idea' in dirs:
            dirs.remove('.idea')
        rel_path = os.path.relpath(root, base_dir)
        structure[rel_path] = files
    return structure

def generate_script(structure, output_script, project_name):
    with open(output_script, 'w', encoding='utf-8') as f:
        f.write('import os\n\n')
        f.write('def create_project_structure(destination):\n')
        for dir_path, files in structure.items():
            if dir_path != ".":
                f.write(f'    os.makedirs(os.path.join(destination, r"{dir_path}"), exist_ok=True)\n')
            for file in files:
                f.write(f'    open(os.path.join(destination, r"{os.path.join(dir_path, file)}"), "w").close()\n')
        f.write('\nif __name__ == "__main__":\n')
        f.write('    destination = input("Digite o diretório onde você quer salvar o projeto: ").strip(\'"\')\n')
        f.write('    create_project_structure(destination)\n')

def main():
    print("Bem-vindo ao Auto Scripter.\nCom ele você pode selecionar o diretório do seu projeto e gerar um script "
          "python que recria a estrutura de diretórios e arquivos do seu projeto.\nSiga as instruções na tela para "
          "continuar.\n")
    base_directory = input("Digite o caminho do projeto para o qual você quer criar o acelerador: ").strip('"')
    output_directory = input("Digite o caminho onde você quer salvar o script acelerador do projeto: ").strip('"')

    project_name = os.path.basename(os.path.normpath(base_directory))
    output_script_path = os.path.join(output_directory, f'acelerador_{project_name}.py')

    structure = analyze_directory(base_directory)
    generate_script(structure, output_script_path, project_name)
    print(f"Script gerado em: {output_script_path}")

if __name__ == "__main__":
    main()
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT.
