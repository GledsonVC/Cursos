from pathlib import Path

arquivos = ['cats.txt', 'dogs.txt','passaro.txt']
caminho_relativo_arquivos ='.\\cap10\\faca_voce_mesmo\\gatos_e_cachorros\\' 

for arquivo in arquivos:
        try:
             path = Path(caminho_relativo_arquivos+arquivo)
             conteudo = path.read_text(encoding='utf-8')
        except FileNotFoundError:
              pass
        else:
              print(f'\nConteudo do arquivo "{arquivo}".')
              print(conteudo)
