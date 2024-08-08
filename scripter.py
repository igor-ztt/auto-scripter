import os


def analyze_directory(base_dir):
    structure = {}
    for root, dirs, files in os.walk(base_dir):
        # Ignore the .venv, .idea and .git directories
        if '.venv' in dirs:
            dirs.remove('.venv')
        if '.idea' in dirs:
            dirs.remove('.idea')
        if '.git' in dirs:
            dirs.remove('.git')
        rel_path = os.path.relpath(root, base_dir)
        structure[rel_path] = files
    return structure


def generate_script(structure, output_script, project_name, base_dir):
    with open(output_script, 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('import os\n\n')
        f.write('def create_project_structure(destination):\n')
        for dir_path, files in structure.items():
            if dir_path != ".":
                f.write(f'    os.makedirs(os.path.join(destination, r"{dir_path}"), exist_ok=True)\n')
            for file in files:
                file_path = os.path.join(base_dir, dir_path, file)
                f.write(
                    f'    with open(os.path.join(destination, r"{os.path.join(dir_path, file)}"), "w", encoding="utf-8") as new_file:\n')
                try:
                    content = open(file_path, "r", encoding="utf-8").read()
                    f.write(f'        new_file.write("""{content}""")\n')
                except UnicodeDecodeError:
                    f.write(f'        new_file.write("# Erro ao ler o arquivo original")\n')
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
    generate_script(structure, output_script_path, project_name, base_directory)
    print(f"Script gerado em: {output_script_path}")


if __name__ == "__main__":
    main()
