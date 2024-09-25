
import pandas as pd


def create_sales_report():
    """
    Creates a DataFrame representing sales data for different products across quarters.

    Returns:
        pandas.DataFrame: The DataFrame containing sales data.
    """

    data = {
        "product": ["Umbrella", "SleepingBag"],
        "quarter_1": [417, 800],
        "quarter_2": [224, 936],
        "quarter_3": [379, 93],
        "quarter_4": [611, 875],
    }

    return pd.DataFrame(data)


def reshape_data_to_long_format(report):
    """
    Reshapes the given DataFrame from wide format (multiple quarter columns)
    to long format (one column for quarters and another for sales).

    Args:
        report (pandas.DataFrame): The DataFrame containing sales data in wide format.

    Returns:
        pandas.DataFrame: The reshaped DataFrame in long format.
    """

    melted_df = report.melt(
        id_vars="product", var_name="quarter", value_name="sales"
    )
    return melted_df


if __name__ == "__main__":
    sales_report = create_sales_report()
    print("Original Sales Report (Wide Format):")
    print(sales_report)

    print("\nReshaped Sales Report (Long Format):")
    reshaped_report = reshape_data_to_long_format(sales_report.copy())
    print(reshaped_report)