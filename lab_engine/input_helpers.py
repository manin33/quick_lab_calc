# Input helper tools for QuickLab Calc.
#
# This file should handle user input validation only.
# It should not perform chemistry calculations.


def get_float(prompt):
    while True:
        user_input = input(prompt).strip()

        try:
            value = float(user_input)
            return value

        except ValueError:
            print("Error: please enter a valid number.")


def get_positive_float(prompt):
    while True:
        value = get_float(prompt)

        if value > 0:
            return value

        print("Error: value must be greater than zero.")


def get_choice(prompt, allowed_choices):
    while True:
        user_input = input(prompt).strip()

        if user_input in allowed_choices:
            return user_input

        print(f"Error: invalid option. Allowed options: {', '.join(allowed_choices)}")


def normalize_unit(unit):
    # Remove spaces before and after the unit.
    unit = unit.strip()

    # Normalize the Greek letter mu to the micro sign used in the program.
    unit = unit.replace("μ", "µ")

    # Use lowercase so common uppercase/lowercase variants are accepted.
    unit_key = unit.lower()

    # Common unit aliases.
    unit_aliases = {
        # Volume
        "ul": "uL",
        "µl": "µL",
        "ml": "mL",
        "l": "L",

        # Mass
        "ug": "ug",
        "µg": "µg",
        "mg": "mg",
        "g": "g",
        "kg": "kg",

        # Molarity
        "nm": "nM",
        "um": "uM",
        "µm": "µM",
        "mm": "mM",
        "m": "M",

        # ppm / ppb
        "ppm": "ppm",
        "ppb": "ppb",

        # Concentration mass/volume: mg/L
        "mg/l": "mg/L",
        "mgl": "mg/L",

        # Concentration mass/volume: ug/L
        "ug/l": "ug/L",
        "ugl": "ug/L",

        # Concentration mass/volume: µg/L
        "µg/l": "µg/L",
        "µgl": "µg/L",

        # Concentration mass/volume: mg/mL
        "mg/ml": "mg/mL",
        "mgml": "mg/mL",

        # Concentration mass/volume: ug/mL
        "ug/ml": "ug/mL",
        "ugml": "ug/mL",

        # Concentration mass/volume: µg/mL
        "µg/ml": "µg/mL",
        "µgml": "µg/mL"
    }

    if unit_key in unit_aliases:
        return unit_aliases[unit_key]

    return unit


def get_unit(prompt, allowed_units):
    while True:
        user_input = input(prompt)

        normalized_unit = normalize_unit(user_input)

        if normalized_unit in allowed_units:
            return normalized_unit

        print(f"Error: unsupported unit. Allowed units: {', '.join(allowed_units)}")