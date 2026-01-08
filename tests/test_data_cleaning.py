import pandas as pd
from data_cleaning import combine

def test_fertility_rate_is_non_negative():
    """
    Fertility Rate should never be negative.
    This validates plausibility of cleaned/merged data.
    """
    df = combine()

    # Only check rows where Fertility Rate exists (avoid NaNs from outer merges)
    fert = df["Fertility Rate"].dropna()

    assert (fert >= 0).all()
