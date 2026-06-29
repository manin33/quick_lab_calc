# Unit conversion tools for QuickLab Calc.
#
# This file should handle unit conversions only.
# It should not perform dilution calculations.


VOLUME_UNITS = ["uL", "µL", "mL", "L"]
MASS_UNITS = ["ug", "µg", "mg", "g", "kg"]
MOLARITY_UNITS = ["nM", "uM", "µM", "mM", "M"]

# For dilution, C1 and C2 only need to use the same concentration unit.
DILUTION_CONCENTRATION_UNITS = ["nM", "uM", "µM", "mM", "M", "ppm"]


def convert_volume(value, from_unit, to_unit):
    # Conversion factors to the base unit: mL.
    volume_to_ml = {
        "uL": 0.001,
        "µL": 0.001,
        "mL": 1,
        "L": 1000
    }

    # Volume cannot be negative.
    if value < 0:
        return "Error: volume cannot be negative."

    # Check if the starting unit is supported.
    if from_unit not in volume_to_ml:
        return "Error: unsupported starting volume unit."

    # Check if the target unit is supported.
    if to_unit not in volume_to_ml:
        return "Error: unsupported target volume unit."

    # Convert the original value to mL first.
    value_in_ml = value * volume_to_ml[from_unit]

    # Convert from mL to the target unit.
    converted_value = value_in_ml / volume_to_ml[to_unit]

    return converted_value


def convert_mass(value, from_unit, to_unit):
    # Conversion factors to the base unit: g.
    mass_to_g = {
        "ug": 0.000001,
        "µg": 0.000001,
        "mg": 0.001,
        "g": 1,
        "kg": 1000
    }

    # Mass cannot be negative.
    if value < 0:
        return "Error: mass cannot be negative."

    # Check if the starting unit is supported.
    if from_unit not in mass_to_g:
        return "Error: unsupported starting mass unit."

    # Check if the target unit is supported.
    if to_unit not in mass_to_g:
        return "Error: unsupported target mass unit."

    # Convert the original value to g first.
    value_in_g = value * mass_to_g[from_unit]

    # Convert from g to the target unit.
    converted_value = value_in_g / mass_to_g[to_unit]

    return converted_value


def convert_molarity(value, from_unit, to_unit):
    # Conversion factors to the base unit: M.
    molarity_to_M = {
        "nM": 0.000000001,
        "uM": 0.000001,
        "µM": 0.000001,
        "mM": 0.001,
        "M": 1
    }

    # Molarity cannot be negative.
    if value < 0:
        return "Error: molarity cannot be negative."

    # Check if the starting unit is supported.
    if from_unit not in molarity_to_M:
        return "Error: unsupported starting molarity unit."

    # Check if the target unit is supported.
    if to_unit not in molarity_to_M:
        return "Error: unsupported target molarity unit."

    # Convert the original value to M first.
    value_in_M = value * molarity_to_M[from_unit]

    # Convert from M to the target unit.
    converted_value = value_in_M / molarity_to_M[to_unit]

    return converted_value