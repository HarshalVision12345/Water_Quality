import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
# from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
import joblib

quality_df = pd.read_csv("water_potability.csv")


x = quality_df.iloc[:,:-1]
y = quality_df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)


missing_col = ["ph","Sulfate","Trihalomethanes"]

#imputation ------------------------>
missing = ColumnTransformer(transformers=[
    ("impute",SimpleImputer(strategy="mean"),missing_col)
],remainder="passthrough")

# StandardScaler ---------------------------------> 
scale = ColumnTransformer(transformers=[
    ("scaler",StandardScaler(),slice(0,9))
],remainder="passthrough")

def train_selected_model(choice_model):
    if choice_model == "SVC":
        classifier = SVC(probability=True)
    elif choice_model == "RandomForest" :
        classifier = RandomForestClassifier(n_estimators=100)
    elif choice_model == "NaivesBayes":
        classifier = GaussianNB()
    elif choice_model == "LogisticsRegression":
        classifier = LogisticRegression()

    pipe = Pipeline(steps=[
        ("imputer",missing),
        ("scaler",scale),
        ("classifier",classifier)
    ])

    # Fit the model 
    pipe.fit(X_train,y_train)
    return pipe 

selected_algo = train_selected_model(input("select the model you want [SVC , RandomForest , NaivesBayes , LogisticsRegression]"))
y_pred = selected_algo.predict(X_test)

score = accuracy_score(y_test,y_pred)
print(score)

water_quality_model = f"water_model.pkl"
joblib.dump(selected_algo,water_quality_model)

print(f"Succesfully Saved : Water_quality_model")