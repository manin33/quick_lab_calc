from lab_engine.units import convert_volume, convert_mass
from lab_engine.formatting import format_number


# Calculate the mass needed for a % w/v solution.
#
# % w/v means grams of solute per 100 mL of final solution.
#
# Formula:
# mass_g = (percent / 100) * volume_mL
#
# Internally:
# volume is converted to mL
# mass is calculated in g
# mass is converted to the requested output mass unit.


def mass_from_percent_wv(
    percent,
    volume,
    volume_unit,
    output_mass_unit
):
    # Values must be greater than zero.
    if percent <= 0:
        return "Error: percent must be greater than zero."

    if volume <= 0:
        return "Error: volume must be greater than zero."

    # Convert volume to mL.
    volume_in_ml = convert_volume(volume, volume_unit, "mL")

    if isinstance(volume_in_ml, str):
        return volume_in_ml

    # Calculate mass in grams.
    mass_in_g = (percent / 100) * volume_in_ml

    # Convert mass to requested output unit.
    mass_output = convert_mass(mass_in_g, "g", output_mass_unit)

    if isinstance(mass_output, str):
        return mass_output

    return mass_output


# Format the % w/v preparation result as a lab instruction.
def format_percent_wv_result(
    compound_name,
    percent,
    volume,
    volume_unit,
    mass,
    mass_unit
):
    percent = format_number(percent, 4)
    volume = format_number(volume, 4)
    mass = format_number(mass, 4)

    message = (
        f"To prepare {volume} {volume_unit} of {percent}% w/v {compound_name}, "
        f"weigh {mass} {mass_unit} of {compound_name}, dissolve it in less than "
        f"{volume} {volume_unit} of solvent, then bring to a final volume of "
        f"{volume} {volume_unit}."
    )

    return message


# Create a complete % w/v preparation instruction.
def percent_wv_instruction(
    compound_name,
    percent,
    volume,
    volume_unit,
    output_mass_unit
):
    # Calculate the mass needed.
    mass = mass_from_percent_wv(
        percent=percent,
        volume=volume,
        volume_unit=volume_unit,
        output_mass_unit=output_mass_unit
    )

    # If the calculation returned an error message, stop and return the error.
    if isinstance(mass, str):
        return mass

    # Convert the result into a lab instruction.
    instruction = format_percent_wv_result(
        compound_name=compound_name,
        percent=percent,
        volume=volume,
        volume_unit=volume_unit,
        mass=mass,
        mass_unit=output_mass_unit
    )

    return instruction


# Calculate the solute volume needed for a % v/v solution.
#
# % v/v means mL of liquid solute per 100 mL of final solution.
#
# Formula:
# solute_volume_mL = (percent / 100) * final_volume_mL
#
# Internally:
# final volume is converted to mL
# solute volume is calculated in mL
# solute volume is converted to the requested output volume unit.


def volume_from_percent_vv(
    percent,
    final_volume,
    final_volume_unit,
    output_volume_unit
):
    # Values must be greater than zero.
    if percent <= 0:
        return "Error: percent must be greater than zero."

    if final_volume <= 0:
        return "Error: final volume must be greater than zero."

    # Convert final volume to mL.
    final_volume_in_ml = convert_volume(final_volume, final_volume_unit, "mL")

    if isinstance(final_volume_in_ml, str):
        return final_volume_in_ml

    # Calculate solute volume in mL.
    solute_volume_in_ml = (percent / 100) * final_volume_in_ml

    # Convert solute volume to requested output unit.
    solute_volume_output = convert_volume(
        solute_volume_in_ml,
        "mL",
        output_volume_unit
    )

    if isinstance(solute_volume_output, str):
        return solute_volume_output

    return solute_volume_output


# Format the % v/v preparation result as a lab instruction.
def format_percent_vv_result(
    solute_name,
    percent,
    final_volume,
    final_volume_unit,
    solute_volume,
    solute_volume_unit
):
    percent = format_number(percent, 4)
    final_volume = format_number(final_volume, 4)
    solute_volume = format_number(solute_volume, 4)

    message = (
        f"To prepare {final_volume} {final_volume_unit} of {percent}% v/v "
        f"{solute_name}, measure {solute_volume} {solute_volume_unit} of "
        f"{solute_name}, then bring to a final volume of "
        f"{final_volume} {final_volume_unit}."
    )

    return message


# Create a complete % v/v preparation instruction.
def percent_vv_instruction(
    solute_name,
    percent,
    final_volume,
    final_volume_unit,
    output_volume_unit
):
    # Calculate the solute volume needed.
    solute_volume = volume_from_percent_vv(
        percent=percent,
        final_volume=final_volume,
        final_volume_unit=final_volume_unit,
        output_volume_unit=output_volume_unit
    )

    # If the calculation returned an error message, stop and return the error.
    if isinstance(solute_volume, str):
        return solute_volume

    # Convert the result into a lab instruction.
    instruction = format_percent_vv_result(
        solute_name=solute_name,
        percent=percent,
        final_volume=final_volume,
        final_volume_unit=final_volume_unit,
        solute_volume=solute_volume,
        solute_volume_unit=output_volume_unit
    )

    return instruction


# Calculate the solute mass needed for a % w/w mixture.
#
# % w/w means grams of solute per 100 g of final mixture.
#
# Formula:
# solute_mass_g = (percent / 100) * final_mixture_mass_g
#
# Internally:
# final mixture mass is converted to g
# solute mass is calculated in g
# solute mass is converted to the requested output mass unit.


def mass_from_percent_ww(
    percent,
    final_mass,
    final_mass_unit,
    output_mass_unit
):
    # Values must be greater than zero.
    if percent <= 0:
        return "Error: percent must be greater than zero."

    if final_mass <= 0:
        return "Error: final mixture mass must be greater than zero."

    # Convert final mixture mass to g.
    final_mass_in_g = convert_mass(final_mass, final_mass_unit, "g")

    if isinstance(final_mass_in_g, str):
        return final_mass_in_g

    # Calculate solute mass in g.
    solute_mass_in_g = (percent / 100) * final_mass_in_g

    # Convert solute mass to requested output unit.
    solute_mass_output = convert_mass(
        solute_mass_in_g,
        "g",
        output_mass_unit
    )

    if isinstance(solute_mass_output, str):
        return solute_mass_output

    return solute_mass_output


# Format the % w/w preparation result as a lab instruction.
def format_percent_ww_result(
    compound_name,
    percent,
    final_mass,
    final_mass_unit,
    solute_mass,
    solute_mass_unit
):
    percent = format_number(percent, 4)
    final_mass = format_number(final_mass, 4)
    solute_mass = format_number(solute_mass, 4)

    message = (
        f"To prepare {final_mass} {final_mass_unit} of {percent}% w/w "
        f"{compound_name} mixture, weigh {solute_mass} {solute_mass_unit} "
        f"of {compound_name}, then add solvent or other components until "
        f"the final mixture mass is {final_mass} {final_mass_unit}."
    )

    return message


# Create a complete % w/w preparation instruction.
def percent_ww_instruction(
    compound_name,
    percent,
    final_mass,
    final_mass_unit,
    output_mass_unit
):
    # Calculate the solute mass needed.
    solute_mass = mass_from_percent_ww(
        percent=percent,
        final_mass=final_mass,
        final_mass_unit=final_mass_unit,
        output_mass_unit=output_mass_unit
    )

    # If the calculation returned an error message, stop and return the error.
    if isinstance(solute_mass, str):
        return solute_mass

    # Convert the result into a lab instruction.
    instruction = format_percent_ww_result(
        compound_name=compound_name,
        percent=percent,
        final_mass=final_mass,
        final_mass_unit=final_mass_unit,
        solute_mass=solute_mass,
        solute_mass_unit=output_mass_unit
    )

    return instruction