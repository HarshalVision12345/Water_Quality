# 1. ph: pH of 1. water (0 to 14).
# 2. Hardness: Capacity of water to precipitate soap in mg/L.
# 3. Solids: Total dissolved solids in ppm.
# 4. Chloramines: Amount of Chloramines in ppm.
# 5. Sulfate: Amount of Sulfates dissolved in mg/L.
# 6. Conductivity: Electrical conductivity of water in μS/cm.
# 7. Organic_carbon: Amount of organic carbon in ppm.
# 8. Trihalomethanes: Amount of Trihalomethanes in μg/L.
# 9. Turbidity: Measure of light emiting property of water in NTU.
# 10. Potability: Indicates if water is safe for human consumption. Potable -1 and Not potable -0

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

quality_df = pd.read_csv("water_potability.csv")
# print(quality)

# profile = ProfileReport(quality_df,title="Water Quality Predictor",explorative=True)
# profile.to_file("Water_quality.html")

x = quality_df.iloc[:,:-1]
y = quality_df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# plt.pie(quality_df["Potability"].value_counts(),labels=("Poluted","Not Poluted"),autopct="%0.2f")
# plt.show()


# plotued -----> 61
# Not Poluted -----> 39
# DATA IS MOSTLY BALANCED ------------> 

missing_col = ["ph","Sulfate","Trihalomethanes"]

#imputation ------------------------>
missing = ColumnTransformer(transformers=[
    ("impute",SimpleImputer(strategy="mean"),missing_col)
],remainder="passthrough")

# StandardScaler ---------------------------------> 
scale = ColumnTransformer(transformers=[
    ("scaler",StandardScaler(),slice(0,8))
],remainder="passthrough")


clf1 = LogisticRegression()
clf2 = SVC(probability=True)
clf3 = RandomForestClassifier()
clf4 = GaussianNB()

estimators = [
    ('Lr',clf1),
    ('SVC',clf2),
    ('Rfc',clf3),
    ('NB',clf4)
    ]

# for name,model in estimators:
#     model_pipeline = Pipeline(steps=[
#         ("impute",missing),
#         ("scaler",scale),
#         ("Classifier",model)
#     ])
#     score = cross_val_score(model_pipeline,x,y,cv=10,scoring="accuracy")
#     print(f"Model is {name} = {np.round(np.mean(score),2)}")

# Model is Lr = 0.61
# Model is SVC = 0.65
# Model is Rfc = 0.64
# Model is NB = 0.61

# voting_soft = VotingClassifier(estimators=estimators,voting="soft")

# soft_voting_classifier = Pipeline(steps=[
#     ("impute",missing),
#     ("scaler",scale),
#     ("classifier",voting_soft)
# ])

# score1 = cross_val_score(soft_voting_classifier,x,y,cv=10,scoring="accuracy")
# print(f" Scoring of the Soft Voting Classifier = {np.round(np.mean(score1),2)}")  # Scoring of the Soft Voting Classifier = 0.65

# voting_hard = VotingClassifier(estimators=estimators,voting="hard")

# hard_voting_classifier = Pipeline(steps=[
#     ("impute",missing),
#     ("scaler",scale),
#     ("classifier",voting_hard)
# ])

# score2 = cross_val_score(hard_voting_classifier,x,y,cv=10,scoring="accuracy")
# print(f" Scoring of the hard Voting Classifier = {np.round(np.mean(score2),2)}")  # Scoring of the Soft Voting Classifier = 0.64


# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             for l in range(1,5):
#                 vt_clf = VotingClassifier(estimators=estimators,voting="soft")
#                 classifier_pipeline = Pipeline(steps=[
#                     ("impute",missing),
#                     ("scaler",scale),
#                     ("classifier",vt_clf)
#                 ])
#                 score3 = cross_val_score(classifier_pipeline,x,y,cv=10,scoring="accuracy")
#                 print("for i = {} , j = {} , k = {} , l = {} ".format(i,j,k,l),np.round(np.mean(score3),2))


voting_weighted_soft = VotingClassifier(estimators=estimators,voting="soft",weights=[1,2,2,1])
classifier_weigthed_pipeline = Pipeline(steps=[
    ("impute",missing),
    ("scaler",scale),
    ("classifier",voting_weighted_soft)
])
score4 = cross_val_score(classifier_weigthed_pipeline,x,y,cv=10,scoring="accuracy")
print(f"The score if the weighted soft classifier = {np.round(np.mean(score4),2)}")