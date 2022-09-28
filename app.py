import pandas as pd
from data import data


class BIMCalculator(object):

    def __init__(self):
        self.data = data
        self.table_df = None
        self.wrange_from = 25
        self.wrange_to = 29.9

    def _load_json_data_into_dataframe(self):
        self.table_df = pd.DataFrame(self.data)

    def calculate_bmi(self):
        # convert height centimeter into meter
        self.table_df['HeightM'] = self.table_df.HeightCm / 100

        # calculate Body mass index
        self.table_df['BMI'] = self.table_df.WeightKg / (self.table_df.HeightM * self.table_df.HeightM)

    @staticmethod
    def check_bmi_range(df):
        """
        Check body mass index range, and add column value
        """
        if df.BMI <= 18.4:
            df['BMICategory'] = 'Underweight'
            df['BMIRange'] = '18.4 and below'
            df['HealthRisk'] = 'Malnutrition risk'
        elif 18.5 <= df.BMI <= 24.9:
            df['BMICategory'] = 'Normal Weight'
            df['BMIRange'] = '18.5 - 24.9'
            df['HealthRisk'] = 'Low risk'
        elif 25 <= df.BMI <= 29.9:
            df['BMICategory'] = 'Overweight'
            df['BMIRange'] = '25 - 29.9'
            df['HealthRisk'] = 'Enhanced risk'
        elif 30 <= df.BMI <= 34.9:
            df['BMICategory'] = 'Moderately obese'
            df['BMIRange'] = '30 - 34.9'
            df['HealthRisk'] = 'Medium risk'
        elif 35 <= df.BMI <= 39.9:
            df['BMICategory'] = 'Severely obese'
            df['BMIRange'] = '35 - 39.9'
            df['HealthRisk'] = 'High risk'
        else:
            df['BMICategory'] = 'Very severely obese'
            df['BMIRange'] = '40 and above'
            df['HealthRisk'] = 'Very high risk'

        return df

    def _process_bmi_data(self):
        """
        Process body mass index data, and add three columns with values in dataframe based on condition.
        """
        self.table_df = self.table_df.apply(self.check_bmi_range, axis=1)

    def _count_over_weight_people(self):
        """
        Count overweight people
        """
        return self.table_df.apply(lambda row: self.wrange_from <= row['BMI'] <= self.wrange_to, axis=1).sum()

    def run(self):
        # load jason data into dataframe
        self._load_json_data_into_dataframe()

        print(" ## Json Data ## \n")
        print(self.table_df)
        print("\n")

        # calculate body mass index
        self.calculate_bmi()

        print(" ##  Body mass index ##\n")
        print(self.table_df)
        print("\n")

        # process body mass index data
        self._process_bmi_data()

        print(" ## Body mass index with category and health risk ##\n")
        print(self.table_df)
        print("\n")

        # calculate total overweight people
        over_weight = self._count_over_weight_people()

        print("## Total overweight people ##")
        print(over_weight)


if __name__ == '__main__':
    # initialize instance
    bim = BIMCalculator()

    # process json data and print body mass index and total overweight people count
    bim.run()
