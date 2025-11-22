# file_organizer_python

script em Python que organiza automaticamente arquivos em pastas separadas por extensão.


Funcionalidades

- Detecta automaticamente todos os arquivos na pasta onde o script está.
- Cria pastas baseadas na extensão (por exemplo: `pdf/`, `png/`, `xlsx/`).
- Move cada arquivo para sua pasta correspondente.
- Ignora arquivos que não possuem extensão.
- Não precisa instalar nenhuma biblioteca externa.

---

Como o script funciona

script percorre os arquivos da pasta atual (`Path.cwd()`), verifica a extensão e cria uma subpasta para ela, caso não exista.  
Depois, move o arquivo para dentro da pasta.

---

## 📌 Código utilizado

```python
from pathlib import Path

pasta = Path.cwd()  # Usa a pasta onde o script está

for item in pasta.iterdir():
    if item.is_file():
        
        if item.suffix == "":
            continue

        print(item.name, "→", item.suffix)

        nova_pasta = pasta / item.suffix[1:]
        nova_pasta.mkdir(exist_ok=True)

        item.replace(nova_pasta / item.name)
