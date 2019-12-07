#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[24]:


#Lendo arquivos csv
df_2016 =pd.read_csv(r'Microdados_EOL_Matriculas_2016.csv', delimiter=';', encoding='iso-8859-1', usecols=['MODALIDADE', 'SITUACAO_MAT','SIT_AL_CONCL'])
df_2017 =pd.read_csv(r'Microdados_EOL_Matriculas_2017.csv', delimiter=';', encoding='iso-8859-1', usecols=['MODALIDADE', 'SITUACAO_MAT','SIT_AL_CONCL'])
df_2018 =pd.read_csv(r'Microdados_EOL_Matriculas_2018.csv', delimiter='|', encoding='iso-8859-1', usecols=['MODALIDADE', 'SITUACAO_MAT','SIT_AL_CONCL'])


# In[25]:


#variaveis para o grafico
anos = ['2016', '2017', '2018']
dados_por_ano_eja = []
dados_por_ano_medio = []


# In[26]:


#consulta de matriculados ensino EJA
eja_2016 = df_2016.query('MODALIDADE == "EJA"')['MODALIDADE'].count()
eja_2017 = df_2017.query('MODALIDADE == "EJA"')['MODALIDADE'].count()
eja_2018 = df_2018.query('MODALIDADE == "EJA"')['MODALIDADE'].count()


# In[27]:


eja_2016, eja_2017, eja_2018


# In[28]:


#consulta de matriculados ensino médio
medio_2016 = df_2016.query('MODALIDADE == "MEDIO"')['MODALIDADE'].count()
medio_2017 = df_2017.query('MODALIDADE == "MEDIO"')['MODALIDADE'].count()
medio_2018 = df_2018.query('MODALIDADE == "MEDIO"')['MODALIDADE'].count()


# In[29]:


medio_2016, medio_2017, medio_2018


# In[30]:


#adicionando as consultas na lista dados_por_ano_eja
dados_por_ano_eja.append(eja_2016)
dados_por_ano_eja.append(eja_2017)
dados_por_ano_eja.append(eja_2018)


# In[31]:


dados_por_ano_eja


# In[32]:


#adicionando as consultas na lista dados_por_ano_medio
dados_por_ano_medio.append(medio_2016)
dados_por_ano_medio.append(medio_2017)
dados_por_ano_medio.append(medio_2018)


# In[33]:


dados_por_ano_medio


# In[45]:


#Número de matriculados EJA ao longo de 3 anos
plt.bar(anos, dados_por_ano_eja, color='#ff7f27', width=0.20)
plt.ylabel('Matriculados  EJA')
plt.xlabel('Anos')
plt.title('Matriculados na rede municipal de SP - EJA')


# In[50]:


#Número de matriculados ensino MEDIO ao longo de 3 anos
plt.bar(anos, dados_por_ano_medio, color= '#27A7FF', width=0.20)
plt.ylabel('Matriculados ensino MEDIO')
plt.xlabel('Anos')
plt.title('Matriculados na rede municipal de SP - Ensino MEDIO')


# In[54]:


#Matriculados por_ano EJA
#Matriculados por_ano Ensino MEDIO

# largura da barra
barWidth = 0.25

# posicao barra
b1 = np.arange(len(dados_por_ano_eja))
b2 = [x + barWidth for x in b1]

# criaçao de barras
plt.bar(b1, dados_por_ano_eja, color='#ff7f27', width=barWidth, label='EJA')
plt.bar(b2, dados_por_ano_medio, color='#27A7FF', width=barWidth, label='MEDIO')

# legenda
plt.xlabel('Anos')
plt.xticks([b + barWidth for b in range(len(dados_por_ano_eja))], anos)
plt.ylabel('Matriculados EJA e Medio')
plt.title('Matriculados na rede municipal de SP - EJA e Ensino Medio')

plt.legend()


# In[ ]:




