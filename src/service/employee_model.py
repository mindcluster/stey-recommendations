import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('src/dados.csv')

model = pickle.load(
    open('src/employee_model.pkl', 'rb'))


class EmployeeModel:

    def __init__(self):
        self.label_encoder_gender = LabelEncoder()
        self.label_encoder_sub_sl = LabelEncoder()
        self.label_encoder_promocao = LabelEncoder()
        self.label_encode()

    def label_encode(self):
        self.label_encoder_sub_sl.fit_transform(data['SUB_SL'])
        self.label_encoder_gender.fit_transform(data['GENDER'])
        self.label_encoder_promocao.fit_transform(data['PROMOÇAO'])

    def transform(self, df):
        df['GENDER'] = self.label_encoder_gender.transform(df['GENDER'])
        df['SUB_SL'] = self.label_encoder_sub_sl.transform(df['SUB_SL'])

        return df

    def get_inverse_transform(self, promotion):
        return self.label_encoder_promocao.inverse_transform(promotion)[0]

    @staticmethod
    def predict(df):
        return model.predict(df)
