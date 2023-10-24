#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import sys
import import_ipynb
from whats_love_dados_secretos import mensagens
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from random import choice, randint
servico = EdgeChromiumDriverManager().install()
options = webdriver.EdgeOptions()
options.add_argument(r'user-data-dir=C:\******** CAMINHO PROFILE EDGE COM PERFIL WHATS CONECTADO ********')
navegador = webdriver.Edge(options=options)
nome_programa = 'whats_love_1.0'


try:
    # VAI ESCOLHER UMA MENSAGEM ALEATÓRIA DE "mensagens" QUE ESTÁ NO ARQUIVO "whats_love_dados_secretos"
    msg = choice(mensagens)

    # MENSAGEM
    navegador.get('https://web.whatsapp.com/')
    time.sleep(randint(41, 49))
    navegador.refresh()
    time.sleep(randint(11, 19))
    link = f'https://web.whatsapp.com/send?phone=******** NÚMERO WHATS DESTINO COM CÓDIGO PAÍS E ÁREA TIPO 5551996661010 ********&text={msg}'
    navegador.get(link)
    time.sleep(randint(51, 59))
    try:
        navegador.maximize_window()
    except:
        pass
    time.sleep(randint(5, 8))

    # ENVIAR MENSAGEM
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    time.sleep(randint(11, 21))

    # FIM COM SUCESSO
    navegador.quit()
    data_hora_fim = time.ctime()
    print(f'\n\n****** Programa {nome_programa} finalizado com SUCESSO em {data_hora_fim}\n\n')


# FIM COM ERRO
except:
    data_hora_erro = time.ctime()
    print(
        f'\n\n****** Programa {nome_programa} finalizado com ERRO em {data_hora_erro}\n\n')
    sys.exit()


# In[ ]:




