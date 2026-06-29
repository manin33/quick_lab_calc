from lab_engine.units import convert_volume, convert_molarity, convert_mass
from lab_engine.formatting import format_number


# Calculate the mass needed to prepare a solution from a solid.
#
# Formula:
# mass = molarity * volume * molecular_weight
#
# Internally:
# molarity is converted to M
# volume is converted to L
# molecular_weight is assumed to be g/mol
# mass is calculated in g, then converted to the requested mass unit.


def mass_from_molarity(
    molarity,
    molarity_unit,
    volume,
    volume_unit,
    molecular_weight,
    output_mass_unit
):
    # Values must be greater than zero for this calculation.
    if molarity <= 0:
        return "Error: molarity must be greater than zero."

    if volume <= 0:
        return "Error: volume must be greater than zero."

    if molecular_weight <= 0:
        return "Error: molecular weight must be greater than zero."

    # Convert molarity to M.
    molarity_in_M = convert_molarity(molarity, molarity_unit, "M")

    if isinstance(molarity_in_M, str):
        return molarity_in_M

    # Convert volume to L.
    volume_in_L = convert_volume(volume, volume_unit, "L")

    if isinstance(volume_in_L, str):
        return volume_in_L

    # Calculate mass in grams.
    mass_in_g = molarity_in_M * volume_in_L * molecular_weight

    # Convert mass to requested output unit.
    mass_output = convert_mass(mass_in_g, "g", output_mass_unit)

    if isinstance(mass_output, str):
        return mass_output

    return mass_output


# Format the solution preparation result as a lab instruction.
def format_solution_prep_result(
    compound_name,
    mass,
    mass_unit,
    molarity,
    molarity_unit,
    volume,
    volume_unit
):
    message = (
        f"To prepare {volume} {volume_unit} of {molarity} {molarity_unit} "
        f"{compound_name}, weigh {mass} {mass_unit} of {compound_name}, "
        f"dissolve it in less than {volume} {volume_unit} of solvent, "
        f"then bring to a final volume of {volume} {volume_unit}."
    )

    return message


# Create a complete solution preparation instruction.
def solution_prep_instruction(
    compound_name,
    molarity,
    molarity_unit,
    volume,
    volume_unit,
    molecular_weight,
    output_mass_unit
):
    # Calculate the mass needed.
    mass = mass_from_molarity(
        molarity=molarity,
        molarity_unit=molarity_unit,
        volume=volume,
        volume_unit=volume_unit,
        molecular_weight=molecular_weight,
        output_mass_unit=output_mass_unit
    )

    # If the calculation returned an error message, stop and return the error.
    if isinstance(mass, str):
        return mass

    # Format the values for a cleaner lab instruction.
    mass = format_number(mass, 4)
    molarity = format_number(molarity, 4)
    volume = format_number(volume, 4)

    # Convert the calculated result into a lab instruction.
    instruction = format_solution_prep_result(
        compound_name=compound_name,
        mass=mass,
        mass_unit=output_mass_unit,
        molarity=molarity,
        molarity_unit=molarity_unit,
        volume=volume,
        volume_unit=volume_unit
    )

    return instruction


# Calculate molarity from a weighed solid mass.
#
# Formula:
# moles = mass / molecular_weight
# molarity = moles / volume
#
# Internally:
# mass is converted to g
# volume is converted to L
# molecular_weight is assumed to be g/mol
# molarity is calculated in M, then converted to the requested molarity unit.


def molarity_from_mass(
    mass,
    mass_unit,
    volume,
    volume_unit,
    molecular_weight,
    output_molarity_unit
):
    # Values must be greater than zero for this calculation.
    if mass <= 0:
        return "Error: mass must be greater than zero."

    if volume <= 0:
        return "Error: volume must be greater than zero."

    if molecular_weight <= 0:
        return "Error: molecular weight must be greater than zero."

    # Convert mass to g.
    mass_in_g = convert_mass(mass, mass_unit, "g")

    if isinstance(mass_in_g, str):
        return mass_in_g

    # Convert volume to L.
    volume_in_L = convert_volume(volume, volume_unit, "L")

    if isinstance(volume_in_L, str):
        return volume_in_L

    # Calculate moles.
    moles = mass_in_g / molecular_weight

    # Calculate molarity in M.
    molarity_in_M = moles / volume_in_L

    # Convert molarity to requested output unit.
    molarity_output = convert_molarity(molarity_in_M, "M", output_molarity_unit)

    if isinstance(molarity_output, str):
        return molarity_output

    return molarity_output


# Format the molarity calculation result as a lab instruction.
def format_molarity_from_mass_result(
    compound_name,
    mass,
    mass_unit,
    volume,
    volume_unit,
    molarity,
    molarity_unit
):
    message = (
        f"{mass} {mass_unit} of {compound_name} brought to a final volume of "
        f"{volume} {volume_unit} gives a concentration of "
        f"{molarity} {molarity_unit}."
    )

    return message


# Create a complete molarity-from-mass instruction.
def molarity_from_mass_instruction(
    compound_name,
    mass,
    mass_unit,
    volume,
    volume_unit,
    molecular_weight,
    output_molarity_unit
):
    # Calculate molarity from mass.
    molarity = molarity_from_mass(
        mass=mass,
        mass_unit=mass_unit,
        volume=volume,
        volume_unit=volume_unit,
        molecular_weight=molecular_weight,
        output_molarity_unit=output_molarity_unit
    )

    # If the calculation returned an error message, stop and return the error.
    if isinstance(molarity, str):
        return molarity

    # Format the values for a cleaner lab instruction.
    molarity = format_number(molarity, 4)
    mass = format_number(mass, 4)
    volume = format_number(volume, 4)

    # Convert the calculated result into a lab instruction.
    instruction = format_molarity_from_mass_result(
        compound_name=compound_name,
        mass=mass,
        mass_unit=mass_unit,
        volume=volume,
        volume_unit=volume_unit,
        molarity=molarity,
        molarity_unit=output_molarity_unit
    )

    return instruction