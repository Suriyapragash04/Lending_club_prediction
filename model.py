import pandas as pd
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the csv file
df = pd.read_csv("clean_club.csv",index_col='Unnamed: 0')

train, test = train_test_split(df, test_size=0.2, random_state=42)

def remove_outliers(col):
    low = train[col].mean()-3*train[col].std()
    upp = train[col].mean()+3*train[col].std()
    return train.loc[(train[col]<upp)&(train[col]>low)]

remove = ['annual_inc', 'fico_range_high',  'int_rate',
       'loan_amnt', 'num_actv_bc_tl',  'mort_acc', 'tot_cur_bal',
       'open_acc','total_acc','revol_util','dti','pub_rec']

for col in remove:
    train=remove_outliers(col)
# Select independent and dependent variable
X_train, y_train = train.drop('loan_status', axis=1), train.loan_status
X_test, y_test = test.drop('loan_status', axis=1), test.loan_status

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test= sc.transform(X_test)

# Instantiate the model
xgb_clf = XGBClassifier()
xgb_clf.fit(X_train, y_train)


# Make pickle file of our model
pickle.dump(xgb_clf, open("model.pkl", "wb"))