from lab_engine.formatting import format_number


# Concentration conversion tools for QuickLab Calc.
#
# This file handles common analytical chemistry concentration conversions.
# It does not perform dilution or solution preparation calculations.
#
# Internal base unit: mg/L
#
# Practical assumption:
# For dilute aqueous solutions, ppm is treated as approximately equivalent
# to mg/L, and ppb is treated as approximately equivalent to ug/L.


CONCENTRATION_UNITS = [
    "ppm",
    "ppb",
    "mg/L",
    "ug/L",
    "µg/L",
    "mg/mL",
    "ug/mL",
    "µg/mL"
]


def convert_concentration(value, from_unit, to_unit):
    # Conversion factors to the base unit: mg/L.
    concentration_to_mg_per_L = {
        "ppm": 1,
        "ppb": 0.001,
        "mg/L": 1,
        "ug/L": 0.001,
        "µg/L": 0.001,
        "mg/mL": 1000,
        "ug/mL": 1,
        "µg/mL": 1
    }

    # Concentration cannot be negative.
    if value < 0:
        return "Error: concentration cannot be negative."

    # Check if the starting unit is supported.
    if from_unit not in concentration_to_mg_per_L:
        return "Error: unsupported starting concentration unit."

    # Check if the target unit is supported.
    if to_unit not in concentration_to_mg_per_L:
        return "Error: unsupported target concentration unit."

    # Convert the original value to mg/L first.
    value_in_mg_per_L = value * concentration_to_mg_per_L[from_unit]

    # Convert from mg/L to the target unit.
    converted_value = value_in_mg_per_L / concentration_to_mg_per_L[to_unit]

    return converted_value


# Format the concentration conversion result.
def format_concentration_conversion_result(
    original_value,
    from_unit,
    converted_value,
    to_unit
):
    original_value = format_number(original_value, 4)
    converted_value = format_number(converted_value, 4)

    message = (
        f"{original_value} {from_unit} is equal to "
        f"{converted_value} {to_unit}."
    )

    return message


# Create a complete concentration conversion instruction.
def concentration_conversion_instruction(
    value,
    from_unit,
    to_unit
):
    converted_value = convert_concentration(
        value=value,
        from_unit=from_unit,
        to_unit=to_unit
    )

    if isinstance(converted_value, str):
        return converted_value

    instruction = format_concentration_conversion_result(
        original_value=value,
        from_unit=from_unit,
        converted_value=converted_value,
        to_unit=to_unit
    )

    return instruction