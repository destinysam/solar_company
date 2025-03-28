from datetime import datetime, time

import frappe


def calculate_monthly_tariff(year: str, month: str):
    """
    Function to calculate customer low tariff and high
    tariff based on average low kwh and avergage high kwh for all records
    based on year and month
    """

    entries = frappe.get_all(
        "Calculation Entry",
        filters={"date": ["between", [f"{year}-{month}-01", f"{year}-{month}-31"]]},
        fields=["customer", "date", "time", "kw", "kwh"],
    )

    low_sum_kwh = high_sum_kwh = low_count = high_count = 0

    low_tariff_start = time(23, 0, 0)
    low_tariff_end = time(5, 59, 59)
    for entry in entries:
        time_ = datetime.strptime(str(entry["time"]), "%H:%M:%S").time()

        if time_ >= low_tariff_start or time_ <= low_tariff_end:
            low_sum_kwh += entry["kwh"]
            low_count += 1
        else:
            high_sum_kwh += entry["kwh"]
            high_count += 1

    # calculate average_low_kwh and high_kwh
    average_low_kwh = low_sum_kwh // low_count if low_count else 0
    average_high_kwh = high_sum_kwh // high_count if high_count else 0

    #  applying forumala
    low_tariff = 0.1 * average_low_kwh
    high_tariff = 0.3 * average_high_kwh

    return low_tariff, high_tariff
