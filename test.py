from app import BIMCalculator


def test_overweight_total():
    # initialize instance
    bim = BIMCalculator()

    # load jason data into dataframe
    bim._load_json_data_into_dataframe()

    # calculate body mass index
    bim.calculate_bmi()

    assert bim._count_over_weight_people() == 1
