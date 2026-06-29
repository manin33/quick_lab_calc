# Formatting tools for QuickLab Calc.
#
# This file should handle display formatting only.
# It should not perform chemistry calculations.


def format_number(value, decimal_places=4):
    # If the value is not a number, return it unchanged.
    if not isinstance(value, (int, float)):
        return value

    # Round the number before formatting.
    rounded_value = round(value, decimal_places)

    # If the rounded number is a whole number, show it without .0.
    if rounded_value == int(rounded_value):
        return str(int(rounded_value))

    # Otherwise, remove unnecessary trailing zeros.
    formatted_value = str(rounded_value).rstrip("0").rstrip(".")

    return formatted_value