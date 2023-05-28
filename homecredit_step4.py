import pandas as pd  #数据分析,结构化表格及其操作
import numpy as np  #数值计算，科学计算
import matplotlib.pyplot as plt  #作图工具
from pathlib import Path  #将csv文件整合成py可以识别的类型
from IPython.display import display
import toad

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def load_date(path): #读取文档，载入数据
    application = pd.read_csv(Path(path, 'home-credit-default-risk/application_train.csv'))
    bureau = pd.read_csv(Path(path, 'home-credit-default-risk/bureau.csv'))
    bureau_balance = pd.read_csv(Path(path, 'home-credit-default-risk/bureau_balance.csv'))
    credit_card_balance = pd.read_csv(Path(path, 'home-credit-default-risk/credit_card_balance.csv'))
    installments_payments = pd.read_csv(Path(path, 'home-credit-default-risk/installments_payments.csv'))
    POS_CASH_balance = pd.read_csv(Path(path, 'home-credit-default-risk/POS_CASH_balance.csv'))
    previous_application = pd.read_csv(Path(path, 'home-credit-default-risk/previous_application.csv'))
    return application,bureau,bureau_balance,credit_card_balance,installments_payments,POS_CASH_balance,previous_application

date_path = "C:/Users/test/Desktop/评分卡构建/"
application_train_ft,bureau_ft,bureau_balance_ft,credit_card_balance_ft,installments_payments_ft,POS_CASH_balance_ft,previous_application_ft = load_date(date_path)

df_ft = application_train_ft
bureau_avg = bureau_ft.groupby('SK_ID_CURR').mean()
bureau_avg['buro_count'] = bureau_ft[['SK_ID_BUREAU', 'SK_ID_CURR']].groupby('SK_ID_CURR').count()['SK_ID_BUREAU']
bureau_avg.columns = ['b_' + f_ for f_ in bureau_avg.columns]
df_ft = df_ft.merge(right=bureau_avg.reset_index(), how='left', on='SK_ID_CURR')

