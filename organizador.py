from pathlib import Path

pasta = Path.cwd() # Define o diretório atual como a pasta a ser organizada

for item in pasta.iterdir(): # Itera sobre os itens na pasta
    if item.is_file():  # Verifica se é um arquivo
        
        if item.suffix == "":
            continue

        print(item.name, "→", item.suffix) # Imprime o nome do arquivo e sua extensão  

        nova_pasta = pasta / item.suffix[1:]
        nova_pasta.mkdir(exist_ok=True)  # Cria a pasta se não existir

        item.replace(nova_pasta / item.name)    # Move o arquivo para a nova pasta