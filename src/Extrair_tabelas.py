import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
from time import sleep

# Função para abrir navegador e extrair a tabela de uma URL específica
def abrir_navegador(url, nome_pais, nome_grupo, nome_produto):
    inicio = time.time()
    print(f"Carregando URL: {url}")

    # Configuração do WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Desativar o carregamento de imagens para acelerar
    prefs = {
        "profile.managed_default_content_settings.images": 2,  # Desativa imagens
        "profile.managed_default_content_settings.stylesheets": 2,  # Desativa CSS
        "profile.managed_default_content_settings.javascript": 1  # Mantém JavaScript ativo
    }
    options.add_experimental_option("prefs", prefs)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)

    try:
        # Acessar a URL
        navegador.get(url)
        print(f"Página carregada em {time.time()-inicio} segundos")
        table = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'ctl00_PageContent_MyGridView1')))
        sleep(5)
        # Selecionar 300 por página para carregar todos os dados
        num_pagina = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_PageContent_GridViewPanelControl_DropDownList_PageSize"))
        )
        maximo = Select(num_pagina)
        maximo.select_by_value("300")
        sleep(7)

        # Esperar a tabela ser visível
        table = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'ctl00_PageContent_MyGridView1')))
        
        # Extrair HTML da tabela completa
        table_html = table.get_attribute('outerHTML')
        print("Tabela HTML extraída!")

        # Processar a tabela com BeautifulSoup
        soup = BeautifulSoup(table_html, 'html.parser')
        headers = [th.text.strip() for th in soup.find_all('th')]
        
        rows = []
        for row in soup.find_all('tr')[1:]:  # Ignora o cabeçalho
            cells = [td.text.strip() for td in row.find_all('td')]
            rows.append(cells)

        # Criar a pasta 'data/tabelas_Extraidas' caso não exista
        if not os.path.exists(r'data/tabelas_Extraidas'):
            os.makedirs(r'data/tabelas_Extraidas')

        # Ajustar o nome do arquivo com base nos filtros aplicados
        partes_nome = []
        if nome_pais.lower() != "nenhum":
            partes_nome.append(nome_pais)
        if nome_grupo.lower() != "nenhum":
            partes_nome.append(nome_grupo)
        if nome_produto.lower() != "nenhum":
            partes_nome.append(nome_produto)

        nome_arquivo = os.path.join(r'data/tabelas_Extraidas', f"{'_'.join(partes_nome)}.csv")
        
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        
        print(f"Tabela salva em {nome_arquivo}. Tempo total: {time.time()-inicio} segundos")
    
    except Exception as e:
        print(f"Erro ao processar a URL {url}: {e}")
        raise  # Lança a exceção para ser tratada externamente

    finally:
        navegador.quit()

# Função principal que itera sobre o arquivo JSON e executa o processo para cada URL
import json
def extrair_tabelas():
    with open(r'data/urls_geradas.json', 'r', encoding='utf-8') as file:
        urls_data = json.load(file)
    inicio_cod=time.time()
    for url, filtros in urls_data.items():
        nome_pais = filtros["pais"]
        nome_grupo = filtros["grupo de paises"]
        nome_produto = filtros["produto"]
        sucesso = False
        tentativas = 0
        while not sucesso and tentativas < 3:  # Tenta no máximo 3 vezes
            try:
                abrir_navegador(url, nome_pais, nome_grupo, nome_produto)
                sucesso = True
            except Exception as e:
                tentativas += 1
                print(f"Tentativa {tentativas} falhou para a URL {url}. Erro: {e}")
                if tentativas >= 3:
                    print(f"Não foi possível processar a URL {url} após {tentativas} tentativas.")
    print(f"Tempo total: {time.time()-inicio_cod} segundos")
# Permite que o script seja executado diretamente
if __name__ == "__main__":
    extrair_tabelas()
