import pandas as pd  #数据分析,结构化表格及其操作
import numpy as np  #数值计算，科学计算
import matplotlib.pyplot as plt  #作图工具
from pathlib import Path  #将csv文件整合成py可以识别的类型
from IPython.display import display
import toad
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def load_date(path): #读取文档，载入数据
    application = pd.read_csv(Path(path, 'home-credit-default-risk/application_train.csv'))
    '''
    bureau = pd.read_csv(Path(path, 'home-credit-default-risk/bureau.csv'))
    bureau_balance = pd.read_csv(Path(path, 'home-credit-default-risk/bureau_balance.csv'))
    credit_card_balance = pd.read_csv(Path(path, 'home-credit-default-risk/credit_card_balance.csv'))
    installments_payments = pd.read_csv(Path(path, 'home-credit-default-risk/installments_payments.csv'))
    POS_CASH_balance = pd.read_csv(Path(path, 'home-credit-default-risk/POS_CASH_balance.csv'))
    previous_application = pd.read_csv(Path(path, 'home-credit-default-risk/previous_application.csv'))
    return application,bureau,bureau_balance,credit_card_balance,installments_payments,POS_CASH_balance,previous_application
    '''
    return application

date_path = "C:/Users/test/Desktop/评分卡构建/"
#application_train,bureau,bureau_balance,credit_card_balance,installments_payments,POS_CASH_balance,previous_application = load_date(date_path)
application_train = load_date(date_path) #测试用例


application_train['DAYS_EMPLOYED'].replace(365243, np.nan, inplace=True) #将数值为365243的值设为nan
print(application_train['HOUSETYPE_MODE'].unique())
application_train['HOUSETYPE_MODE'] = application_train['HOUSETYPE_MODE'].astype('str') #将原本np.nan 类型的空值转化成str
print(application_train['HOUSETYPE_MODE'].unique())

def process_cat_feature(df): #label encoding
    le = LabelEncoder()
    le_count = 0
    for col in df:
        if df[col].dtype == 'object':
            if len(list(df[col].unique())) <= 2:
                print(col)
                le.fit(df(col))
                df[col] = le.transform(df[col])
                le_count += 1
    print('{} variable are label encoded'.format(le_count))
    return df









