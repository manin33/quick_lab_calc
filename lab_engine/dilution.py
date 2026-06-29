from lab_engine.units import convert_volume
from lab_engine.formatting import format_number


# Dilution calculator based on the equation:
# C1 * V1 = C2 * V2
#
# c1 = initial concentration
# v1 = initial volume
# c2 = final concentration
# v2 = final volume
#
# One value can be left as None.
# The function will calculate the missing value.


def conc_proportion(c1=None, c2=None, v1=None, v2=None):
    # Count how many values are missing.
    missing_values = [c1, c2, v1, v2].count(None)

    # The equation can only solve for one missing value at a time.
    if missing_values != 1:
        return "Error: exactly one value must be missing."

    # Values used in the equation must be greater than zero.
    values = [c1, c2, v1, v2]

    for value in values:
        if value is not None and value <= 0:
            return "Error: values must be greater than zero."

    # If v1 is missing, calculate the initial volume needed.
    if v1 is None:
        return (c2 * v2) / c1

    # If c1 is missing, calculate the initial concentration.
    if c1 is None:
        return (c2 * v2) / v1

    # If c2 is missing, calculate the final concentration.
    if c2 is None:
        return (c1 * v1) / v2

    # If v2 is missing, calculate the final volume.
    if v2 is None:
        return (c1 * v1) / c2


# Format the dilution result as a lab instruction.
def format_dilution_result(c1, c2, v1, v2, concentration_unit, v1_unit, v2_unit):
    c1 = format_number(c1, 4)
    c2 = format_number(c2, 4)
    v1 = format_number(v1, 4)
    v2 = format_number(v2, 4)

    message = (
        f"To prepare {v2} {v2_unit} of {c2} {concentration_unit}, "
        f"take {v1} {v1_unit} of {c1} {concentration_unit} stock solution "
        f"and dilute to a final volume of {v2} {v2_unit}."
    )

    return message


# Create a dilution instruction while handling volume unit conversion.
def dilution_instruction_with_volume_units(
    c1,
    c2,
    v2,
    v2_unit,
    output_volume_unit,
    concentration_unit
):
    # In a dilution, the stock concentration must be greater than or equal to
    # the final concentration.
    if c2 > c1:
        return "Error: final concentration cannot be greater than stock concentration for a dilution."

    # If stock and final concentration are the same, no dilution is needed.
    if c1 == c2:
        v2_clean = format_number(v2, 4)
        c1_clean = format_number(c1, 4)

        return (
            f"No dilution is needed because the stock concentration and final "
            f"concentration are both {c1_clean} {concentration_unit}. "
            f"Use {v2_clean} {v2_unit} of the stock solution directly."
        )

    # Convert the final volume to mL for the calculation.
    v2_in_ml = convert_volume(v2, v2_unit, "mL")

    # Stop if the volume conversion returned an error.
    if isinstance(v2_in_ml, str):
        return v2_in_ml

    # Calculate v1 in mL.
    v1_in_ml = conc_proportion(c1=c1, c2=c2, v2=v2_in_ml)

    # Stop if the dilution calculation returned an error.
    if isinstance(v1_in_ml, str):
        return v1_in_ml

    # The initial stock volume cannot be greater than the final volume.
    if v1_in_ml > v2_in_ml:
        return "Error: initial stock volume cannot be greater than final volume."

    # Convert v1 from mL to the requested output volume unit.
    v1_output = convert_volume(v1_in_ml, "mL", output_volume_unit)

    # Stop if the output conversion returned an error.
    if isinstance(v1_output, str):
        return v1_output

    # Create the final instruction.
    instruction = format_dilution_result(
        c1,
        c2,
        v1_output,
        v2,
        concentration_unit,
        output_volume_unit,
        v2_unit
    )

    return instruction