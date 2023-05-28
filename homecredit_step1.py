import pandas as pd  #数据分析,结构化表格及其操作
import numpy as np  #数值计算，科学计算
import matplotlib.pyplot as plt  #作图工具
from pathlib import Path  #将csv文件整合成py可以识别的类型

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

#application_train[ 'TARGET' ].astype(int).plot.hist() #使用astype转化成整数类型，用plot.hist进行展示
#plt.show()

def application_stat(application, show_res = False): #处理单个表格的数据
    users = len(application['SK_ID_CURR'].unique()) #有多少个独一无二的用户
    default_users = len(application[application['TARGET'] == 1]['SK_ID_CURR'].unique())
    if show_res:
        print("users in application",users)
        print("default users in application",default_users)
        radio = default_users / users
        print("Default users is",radio*100,"percent")
    return users, default_users
#application_stat(application_train, show_res=True)

def application_coverage(application, right_table, table_name, key="SK_ID_CURR"): #显示applicaiton表中的信息有多少可以在其他的表格中找到. 使用merge()进行关联,和sql类似
    users, default_users = application_stat(application_train)
    joined_table = application.merge(right_table, on = key, how = 'inner')
    covered_user = len(joined_table[key].unique())
    print("all users covered by", table_name, covered_user)
    radio = covered_user / users
    print("all users covered by", table_name, radio*100, "%")
    covered_default_user = len(joined_table[joined_table['TARGET'] == 1]['SK_ID_CURR'].unique())
    print("all default users covered by", table_name, covered_default_user)
    radio_default = covered_default_user / default_users
    print("all default users covered by", table_name, radio_default*100, "%")

#application_coverage(application_train, bureau, 'bureau')



