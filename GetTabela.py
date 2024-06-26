from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def save_to_excel(tabelas_df, titulo):
    with pd.ExcelWriter(titulo+".xlsx") as writer:
        for tab_name, tab_data in tabelas_df.items():
            tab_data.to_excel(writer, sheet_name=tab_name, index=False)

def getTabela(link):
    driver = webdriver.Chrome()
    driver.get(link)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,'table')))

    titulo = driver.find_element(By.TAG_NAME,'title')
    tabelas = driver.find_elements(By.TAG_NAME,'table')
    titulo = titulo.get_attribute('text')
    print(titulo)

    dict_tabelas = {}

    for idx, tabela in enumerate(tabelas):
        df = pd.read_html(tabela.get_attribute('outerHTML'))[0]
        dict_tabelas[f'Tabela {idx+1}'] = df
    driver.quit()

    save_to_excel(dict_tabelas, titulo)
    return dict_tabelas,titulo+".xlsx"

