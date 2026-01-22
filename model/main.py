import pandas as pd
import pickle as pkl
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def get_cleaned_data():
    uncleaned_data = pd.read_csv("dataset/cdata.csv")
    uncleaned_data = uncleaned_data.drop(["Unnamed: 32", "id"], axis=1)
    uncleaned_data["diagnosis"] = uncleaned_data["diagnosis"].map(
        { "M" : 1,
          "B" : 0
        }
    )
    cleaned_data = uncleaned_data
    return cleaned_data

def create_model(data):
    X = data.iloc[:, 1:]
    y = data.iloc[:, 0]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy of the model:" , accuracy_score(y_test, y_pred))
    print("Classification report: \n" , classification_report(y_test, y_pred))
    return model, scaler

def main():
    cancer_data = get_cleaned_data()
    model, scaler = create_model(cancer_data)

    with open("model.pkl", "wb") as file:
        pkl.dump(model, file)
    with open("scaler.pkl", "wb") as file:
        pkl.dump(scaler, file)

if __name__ == '__main__':
    main()


