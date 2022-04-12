#!/usr/bin/env python
# coding: utf-8

# # BOT PARA MARCAR PESSOAS NO INSTAGRAM

# DEV: Igor Matheus Lial Venturin

# In[1]:


from selenium import webdriver
import time
driver = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
actions=ActionChains(driver)


# # ABRINDO A LISTA COM OS @

# README: A PRIMEIRA LINHA DA COLUNA COM OS @ DEVE SER 'USUÁRIOS' E OS @ PRECISAM SER EXATAMENTE COMO NO INSTAGRAM

# In[ ]:


import pandas as pd
df = pd.read_excel('D:\Estudos\Python\BOTs\@_instagram.xlsx') #LENDO A PLANILHA COM A LISTA DE CONTATOS
display(df)


# # LOGIN E AUTENTICAÇÃO NO INSTAGRAM

# In[4]:


driver.get('https://www.instagram.com/SORTEIO') #<---- LINK DO SORTEIO NO INSTAGRAM
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("LOGIN") #<--- LOGIN DA CONTA
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("SENHA") #<---SENHA DA CONTA
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(60)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button').click()
time.sleep(3)


# # ENVIO DOS COMENTARIOS COM OS @s

# In[ ]:


arrobas = df['USUÁRIOS']
y = 0
i = 0
erru = 0
for x in range(1,26): #<--- é o maior numero inteiro da divisão de @(566) que eu adicionei no banco de dados pela quantidade comentarios
    
    for i in range( y, y+16, 2 ):
        
        P1 = arrobas[i]
        P2 = arrobas[i+1]
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(f"{P1} {P2}")
        time.sleep(3)
        try:
            driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div').click()
        except: #estrutura para esperar caso o instagram limite os comentarios
            wrong += 1
            time.sleep(3)
            print(f" Deu {wrong} errors")
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/button[2]').click()
            time.sleep(122)
            driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
            time.sleep(2)
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            time.sleep(5)
            actions.key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main').click()
            pass
        time.sleep(10)
        
    y += 16
    time.sleep(301)
    print("\nFOI MAIS UMA VEZ\n")


# In[ ]:




