#!/usr/bin/env python
# coding: utf-8

# #Script para acesso e manipulação de dados do <b>SIGA_DESENV.SRC_PRICING_MERCADOEDU</b>

# In[1]:


import pandas as pd
import cx_Oracle


# Dados de <b>CONEXÃO</b>

# In[2]:


CONNECT_TO_ORACLE = True
con_oracle = CONNECT_TO_ORACLE

if con_oracle:
    try:
        import cx_Oracle
        import pandas as pd

        ip = '172.16.137.63'
        port = '1521'
        service_name = 'aesabi'
        dsn_tns = cx_Oracle.makedsn(ip, port, service_name=service_name)
        connection = cx_Oracle.connect('bi_read', 'bi_read', dsn_tns, encoding="UTF-8", nencoding="UTF-8")

    except:
        connection = None
        print("Oracle AESA BI db connection could not be created")
else:
    connection = None

def read_origin_to_pandas(sql="", path="", sep=',', encoding='utf-8', dtype={}, connection=connection):
    if (con_oracle) or (con_oracle=="True"):
        return pd.read_sql(sql, con=connection)
    else:
        return print('Erro') ##uploads_to_panda(path, sep=sep, encoding=encoding, dtype=dtype)


# <b>SCRIPT</b>

# In[3]:


sql_teste = "select * from SIGA_DESENV.SRC_PRICING_MERCADOEDU WHERE DT_DATE >=TO_DATE('01/02/2019','dd/mm/yyyy')"


# In[4]:


sql_teste


# In[5]:


TGT_BI_DF = read_origin_to_pandas(sql = sql_teste, path="TESTE", sep=',',dtype={'ID': object})
TGT_BI_DF.head()


# In[6]:


df = pd.DataFrame(TGT_BI_DF)
df.head(3)


# In[8]:


def trata_local_name(row):
    if (row['DS_LOCAL_NAME'])=='-':
        val is None
    else:
        val = row['DS_LOCAL_NAME']
    return val


# In[9]:


df['DS_LOCAL_NAME_DF'] = df.apply(trata_local_name, axis = 1)


# In[10]:


df['DS_LOCAL_ADDRESS_DF'] = df['DS_LOCAL_ADDRESS'].astype(str)
df['DS_COUSER_NAME_DF'] = df['DS_COUSER_NAME'].str.upper()
df['DS_COURSE_DEGREE_DF'] = df['DS_COURSE_DEGREE'].str.upper()
df['DS_COURSE_MODALITY_DF'] = df['DS_COURSE_MODALITY'].str.upper()


# In[11]:


def trata_course_shift(row):
    if (row['DS_COURSE_SHIFT'])=='-':
        val is None
    else:
        val = row['DS_COURSE_SHIFT']
    return val


# In[12]:


df['DS_COURSE_SHIFT_DF'] = df.apply(trata_course_shift, axis = 1)


# In[13]:


df['DS_IES_SIGLE_DF'] = df['DS_IES_SIGLE'].str.upper()
df['DS_CITY_NAME_DF'] = df['DS_CITY_NAME'].str.upper()
df['DS_STATE_NAME_DF'] = df['DS_STATE_NAME'].str.upper()
df['DS_PAYMENT_PLAN_DF'] = df['DS_PAYMENT_PLAN'].str.upper()
df['DS_QT_CREDITS_DF'] = df['DS_QT_CREDITS'].str.upper()
df['DS_ROBO_NAME_DF'] = df['DS_ROBO_NAME'].str.upper()
df['ROBO_ORIG_DF'] = df['DS_ROBO_NAME'].str.upper()
df['ENDERECO_LOCAL_DF'] = df['DS_LOCAL_ADDRESS_DF'].astype(str)
import time
df['DT_BASE_DF'] = time.strftime("%d/%m/%Y")


# In[14]:


def trata_robo_tratado(row):
    if (row['DS_ROBO_NAME'])=='EDUCAMAIS BRASIL':
        val = 'EDUCA MAIS'
    elif (row['DS_ROBO_NAME'])=='QUERO BOLSA':
        val = 'QUERO BOLSA'
    else:
        val = 'SITE'
    return val


# In[15]:


df['ROBO_TRATADO_DF'] = df.apply(trata_robo_tratado, axis = 1)


# Dados de <b>'NR_PRICE'</b> e <b>'NR_PRICE_W_D'</b> convertidos para String, <p>para o cálculo das info's sobre <b>'NR_PRICE_TRATADO'</b> e <b>'NR_PRICE_W_D_TRATADO'</b>

# In[16]:


df['NR_PRICE_STR'] = df['NR_PRICE'].apply(lambda x: str(x))


# In[17]:


df['NR_PRICE_LN'] = df["NR_PRICE_STR"].apply(lambda x: len(str(x)))


# In[18]:


def trata_price(row):
    if(row['NR_PRICE_LN']==5):
        val = row['NR_PRICE_STR']
    elif row['NR_PRICE_LN']==6:
        val = row['NR_PRICE_STR']
    else:
        val = row['NR_PRICE_STR']
    return val


# In[19]:


df['NR_PRICE_TRATADO_DF'] = df.apply(trata_price, axis = 1) 


# In[20]:


df['NR_PRICE_WD_STR'] = df['NR_PRICE_W_D'].apply(lambda x: str(x))


# In[21]:


df['NR_PRICE_WD_LN'] = df["NR_PRICE_WD_STR"].apply(lambda x: len(str(x)))


# In[22]:


def trata_price_wd(row):
    if(row['NR_PRICE_WD_LN']==5):
        val = row['NR_PRICE_WD_STR']
    elif row['NR_PRICE_WD_LN']==6:
        val = row['NR_PRICE_WD_STR']
    else:
        val = row['NR_PRICE_WD_STR']
    return val


# In[23]:


df['NR_PRICE_W_D_TRATADO_DF'] = df.apply(trata_price, axis = 1) 


# In[24]:


def trata_preco(row):
    if(row['NR_PRICE_LN']==0):
        val = row['NR_PRICE_W_D_TRATADO_DF']
    else:
        val = row['NR_PRICE_TRATADO_DF']
    return val


# In[25]:


df['PRECO_DF']= df.apply(trata_preco, axis = 1) 


# In[26]:


def trata_preco_desc(row):
    if(row['NR_PRICE_WD_LN']==0):
        val = row['NR_PRICE_TRATADO_DF']
    else:
        val = row['NR_PRICE_W_D_TRATADO_DF']
    return val


# In[27]:


df['PRECO_DESCONTO_DF']= df.apply(trata_preco_desc, axis = 1) 


# In[28]:


def trata_credits(row):
    if(row['DS_QT_CREDITS']!=None):
        val = row['DS_QT_CREDITS']


# In[29]:


df['QTD_CREDITOS_DF']= df.apply(trata_credits, axis = 1) 


# Merge para a geração do CAMPO <b>'Plano_Pagamento'</b>

# In[30]:


pgto = pd.read_excel('DePara_Plano_Pagto.xlsx')
pgto.head()


# In[31]:


pgto['ROBO'] = pgto['ROBO'].str.upper()
pgto['DE_Plano_Pagto'] = pgto['DE_Plano_Pagto'].str.upper()
pgto['PARA_Plano_Pagto'] = pgto['PARA_Plano_Pagto'].str.upper()


# In[32]:


#criação do campo concatenado
pgto['chave_pgto'] = pgto[['ROBO', 'DE_Plano_Pagto']].apply(lambda x: ''.join(str(x)), axis=1)


# In[33]:


# reordenar dataframe
pgto = pgto[['ROBO','DE_Plano_Pagto','chave_pgto','PARA_Plano_Pagto']]


# In[34]:


#campo concatenado no df
df['chave_pgto'] = df['DS_ROBO_NAME'].fillna('')+df['DS_PAYMENT_PLAN'].fillna('')
df.head()


# In[35]:


rs=pd.merge(df, pgto[['chave_pgto','PARA_Plano_Pagto']], on='chave_pgto', how='left')
rs["PARA_Plano_Pagto"].fillna("NI", inplace = True) 
rs.head()


# In[36]:


rs.rename(index=str, columns={"PARA_Plano_Pagto": "PLANO_PAGAMENTO_DF"})
rs.head()


# Merge para geração do CAMPO <b>'CIDADE_UF'</b>

# In[37]:


cid = pd.read_excel('DePara_Robo_Preços_Novo.xlsx', sheetname='Local_Marca_Grupo_Cidade_Grau')
cid.head()


# In[38]:


cid['ROBO'] = cid['ROBÔ'].str.upper()
cid['SIGLA_IES_DE'] = cid['SIGLA_IES_DE'].str.upper()
cid['CIDADE_DE'] = cid['CIDADE_DE'].str.upper()
cid['UF_DE'] = cid['UF_DE'].str.upper()
cid['NOME_LOCAL_DE'] = cid['NOME_LOCAL_DE'].str.upper()
cid['NOME_LOCAL_PARA'] = cid['NOME_LOCAL_PARA'].str.upper()
cid['MARCA_PARA'] = cid['MARCA_PARA'].str.upper()
cid['GRUPO_PARA'] = cid['GRUPO_PARA'].str.upper()
cid['CIDADE_PARA'] = cid['CIDADE_PARA'].str.upper()
cid['UF_PARA'] = cid['UF_PARA'].str.upper()


# In[ ]:


# upper(DS_ROBO_NAME) &'|'& upper(DS_IES_SIGLE)  &'|'& upper(DS_CITY_NAME) &'|'& upper(DS_STATE_NAME) &'|'& upper(DS_LOCAL_NAME)


# In[39]:


cid['chave_cuf'] = cid['ROBO'].fillna('')+cid['SIGLA_IES_DE'].fillna('')+cid['CIDADE_DE'].fillna('')+cid['UF_DE'].fillna('')+cid['NOME_LOCAL_DE'].fillna('')
cid.head()


# In[ ]:


#cid.set_index('month')


# In[40]:


# reordenar dataframe
cid = cid[['ROBO','SIGLA_IES_DE','CIDADE_DE','UF_DE','NOME_LOCAL_DE','chave_cuf','NOME_LOCAL_PARA','MARCA_PARA','GRUPO_PARA','CIDADE_PARA','UF_PARA']]


# In[41]:


# upper(DS_ROBO_NAME) &'|'& upper(DS_IES_SIGLE)  &'|'& upper(DS_CITY_NAME) &'|'& upper(DS_STATE_NAME) &'|'& upper(DS_LOCAL_NAME)
rs['chave_cuf'] = rs['DS_ROBO_NAME'].fillna('')+rs['DS_IES_SIGLE'].fillna('')+rs['DS_CITY_NAME'].fillna('')+rs['DS_STATE_NAME'].fillna('')+rs['DS_LOCAL_NAME'].fillna('')


# In[42]:


#rst=pd.merge(rs, cid, on='chave_cuf', how='left')
rft=pd.merge(rs, cid[['chave_cuf','CIDADE_PARA','NOME_LOCAL_PARA','GRUPO_PARA','MARCA_PARA']], on='chave_cuf', how='left')
rft.head()


# In[43]:


rft["CIDADE_PARA"].fillna("NI", inplace = True)
rft.rename(index=str, columns={"CIDADE_PARA": "CIDADE_UF_DF"})


# In[44]:


rft["NOME_LOCAL_PARA"].fillna("NI", inplace = True) 
rft.rename(index=str, columns={"NOME_LOCAL_PARA": "NOME_LOCAL_DF"})


# In[45]:


rft["GRUPO_PARA"].fillna("NI", inplace = True) 
rft.rename(index=str, columns={"GRUPO_PARA": "GRUPO_DF"})


# In[46]:


rft["MARCA_PARA"].fillna("NI", inplace = True) 
rft.rename(index=str, columns={"MARCA_PARA": "MARCA_PARA_DF"})


# Merge para geração da planilha sobre <b>'CURSO_GRAU'</b>

# In[62]:


curse = pd.read_excel('DePara_Robo_Preços_Novo.xlsx', sheetname='Curso_Grau')
curse.head()


# In[63]:


curse['CURSO_DE'] = curse['CURSO_DE'].str.upper()
curse['GRAU_DE'] = curse['GRAU_DE'].str.upper()
curse['CURSO_PARA'] = curse['CURSO_PARA'].str.upper()
curse['GRAU_PARA'] = curse['GRAU_PARA'].str.upper()
curse['ID_CURSO_PARA'] = curse['ID_CURSO_PARA'].str.upper()


# In[64]:


curse['chave_curso'] = curse['CURSO_DE'].fillna('')+curse['GRAU_DE'].fillna('')


# In[65]:


#reordenar o dataframe
curse=curse[['CURSO_DE','GRAU_DE','chave_curso','CURSO_PARA','GRAU_PARA','ID_CURSO_PARA']]


# In[67]:


rft.head()


# In[68]:


rft['chave_curso'] = rs['DS_COUSER_NAME'].fillna('')+rs['DS_COURSE_DEGREE'].fillna('')


# In[69]:


rft=pd.merge(rft, curse[['chave_curso','CURSO_PARA','GRAU_PARA','ID_CURSO_PARA']], on='chave_curso', how='left')
rft.head()


# In[70]:


rft["CURSO_PARA"].fillna("NI", inplace = True) 
rft.rename(index=str, columns={"CURSO_PARA": "CURSO_PARA_DF"})


# In[71]:


rft["GRAU_PARA"].fillna("NI", inplace = True) 
rft.rename(index=str, columns={"GRAU_PARA": "GRAU_PARA_DF"})


# In[72]:


rft["ID_CURSO_PARA"].fillna("NI", inplace = True) 
rft.rename(index=str, columns={"ID_CURSO_PARA": "ID_CURSO_PARA_DF"})


# In[ ]:





# In[ ]:





# <b>conexão postgreSQL</b><p>
# Host: pricing.cfefnwtyvvt2.us-east-1.rds.amazonaws.com<p>
# Port: 5432<p>
# Database: pricing<p>
# User: kroton_pricing<p>
# Pass: krt8s0F4<p>
# Schema: kroton_pricing

# In[73]:


#Conexão ao Redshift - postgres
import pandas_redshift as pr
def to_redshift():
    pr.connect_to_redshift(dbname = 'pricing',
                        host  = 'pricing.cfefnwtyvvt2.us-east-1.rds.amazonaws.com',
                        port  = '5432',
                        user  = 'kroton_pricing',
                        password = 'krt8s0F4')
    print('Connect to RedShift')
    return pr.redshift_to_pandas('select * from kroton_pricing.bd_ccr')
#data = pr.redshift_to_pandas('select * from db_ccr')


# In[74]:


df_conn = to_redshift()


# In[75]:


df_conn.head()


# In[76]:


def to_redshift(data_frame):
    #date_str =data_base.strftime('%Y/%m/%d')
    print('connect_to_redshift')
    pr.connect_to_redshift(dbname = 'pricing',
                        host  = 'pricing.cfefnwtyvvt2.us-east-1.rds.amazonaws.com',
                        port  = '5432',
                        user  = 'kroton_pricing',
                        password = 'krt8s0F4')
    print('connect_to_s3')
    pr.connect_to_s3(aws_access_key_id="AKIAILQVO2DJQHRLFLQQ",
                     aws_secret_access_key="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",
                     bucket="kroton-analytics",
                     subdirectory="raw/uploads/esteira"
                     )
    print('pandas_to_redshift')
    pr.pandas_to_redshift(data_frame=data_frame,
                          ##columns_data_types = ['real_mes' float64, 'real_ano_anterior' float64, 'acumulado_ano' float64, 'meta_ano' float64],
                          ##column_data_types=['VARCHAR(250)','DATE','VARCHAR(250)','VARCHAR(250)','VARCHAR(250)','VARCHAR(250)','VARCHAR(250)','VARCHAR(250)','VARCHAR(250)','VARCHAR(250)','VARCHAR(250)','FLOAT','FLOAT','FLOAT','FLOAT'],
                          index=False,
                          ##column_data_types = None,
                          redshift_table_name='kroton_pricing.tb_dev_bd_ccr',
                          append = True)
    return print('fim save_to_redshift')


# In[ ]:


#export do dataframe para Redshift
to_redshift(rft)

