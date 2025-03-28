import frappe

from solar_app.scripts.calculate_tariff import calculate_monthly_tariff


@frappe.whitelist(methods=["GET"], allow_guest=True)
def get_monthly_tariff(year: str, month: str):
    """
    Get monthly low tariff and high tariff

    Args:
        year (str): calculate tariff for the given year.
        month (str): calculcate tariff for the given month.

    Returns:
        dict: monthly low tariff and high tariff
    """

    low_tariff, high_tariff = calculate_monthly_tariff(year, month)
    return {"low_tariff": low_tariff, "high_tariff": high_tariff}
