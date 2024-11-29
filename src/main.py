from Gerar_links import fluxo_selecao, gerar_urls
from Extrair_tabelas import extrair_tabelas
import os

def main():
    # Verifica se o arquivo de URLs já existe
    if not os.path.exists("data/urls_geradas.txt"):
        print("Gerando URLs...")
        fluxo_selecao()  # Função de geração de URLs
    else:
        print("URLs já geradas e salvas em 'urls_geradas.txt'. Prosseguindo com a extração...")

    # Inicia o processo de extração das tabelas
    extrair_tabelas()

if __name__ == "__main__":
    main()