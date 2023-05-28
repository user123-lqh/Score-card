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
application_train,bureau,bureau_balance,credit_card_balance,installments_payments,POS_CASH_balance,previous_application = load_date(date_path)

#application_check = toad.detect(application_train)  #检验数据的质量
#display(application_check.head(10))

print('top 10 features with high IV') #使用iv来判断数据的区分度
display(toad.quality(application_train.drop("SK_ID_CURR", axis=1), "TARGET", iv_only=True)[:10])
print('top 10 features with the lowest IV')
display(toad.quality(application_train.drop("SK_ID_CURR", axis=1), "TARGET", iv_only=True)[-10:])

