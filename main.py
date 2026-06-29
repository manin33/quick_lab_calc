from lab_engine.scaling import scaling_instruction
from lab_engine.serial_dilution import serial_dilution_instruction
from lab_engine.concentration import (
    CONCENTRATION_UNITS,
    concentration_conversion_instruction
)
from lab_engine.percent_solutions import (
    percent_wv_instruction,
    percent_vv_instruction,
    percent_ww_instruction
)
from lab_engine.input_helpers import get_positive_float, get_unit, get_choice
from lab_engine.dilution import dilution_instruction_with_volume_units
from lab_engine.solution_prep import (
    solution_prep_instruction,
    molarity_from_mass_instruction
)
from lab_engine.units import (
    VOLUME_UNITS,
    MASS_UNITS,
    MOLARITY_UNITS,
    DILUTION_CONCENTRATION_UNITS
)


def show_menu():
    print("\nQuickLab Calc")
    print("1. Dilution calculator")
    print("2. Prepare solution from solid")
    print("3. Calculate molarity from weighed solid")
    print("4. Prepare percent w/v solution")
    print("5. Prepare percent v/v solution")
    print("6. Prepare percent w/w mixture")
    print("7. Concentration unit conversion")
    print("8. Serial dilution planner")
    print("9. Solution scaling calculator")
    print("10. Exit")


def run_dilution_calculator():
    print("\nDilution calculator")

    c1 = get_positive_float("Enter stock concentration C1: ")
    c2 = get_positive_float("Enter final concentration C2: ")
    v2 = get_positive_float("Enter final volume V2: ")

    concentration_unit = get_unit(
        "Enter concentration unit, example mM, M, ppm: ",
        DILUTION_CONCENTRATION_UNITS
    )

    v2_unit = get_unit(
        "Enter final volume unit, example uL, mL, L: ",
        VOLUME_UNITS
    )

    output_volume_unit = get_unit(
        "Enter output volume unit for V1, example uL, mL, L: ",
        VOLUME_UNITS
    )

    instruction = dilution_instruction_with_volume_units(
        c1=c1,
        c2=c2,
        v2=v2,
        v2_unit=v2_unit,
        output_volume_unit=output_volume_unit,
        concentration_unit=concentration_unit
    )

    print("\nResult:")
    print(instruction)


def run_solution_prep_calculator():
    print("\nPrepare solution from solid")

    compound_name = input("Enter compound name, example NaCl: ").strip()

    molarity = get_positive_float("Enter target molarity: ")

    molarity_unit = get_unit(
        "Enter molarity unit, example M, mM, uM: ",
        MOLARITY_UNITS
    )

    volume = get_positive_float("Enter final volume: ")

    volume_unit = get_unit(
        "Enter final volume unit, example mL, L: ",
        VOLUME_UNITS
    )

    molecular_weight = get_positive_float("Enter molecular weight in g/mol: ")

    output_mass_unit = get_unit(
        "Enter output mass unit, example g, mg: ",
        MASS_UNITS
    )

    instruction = solution_prep_instruction(
        compound_name=compound_name,
        molarity=molarity,
        molarity_unit=molarity_unit,
        volume=volume,
        volume_unit=volume_unit,
        molecular_weight=molecular_weight,
        output_mass_unit=output_mass_unit
    )

    print("\nResult:")
    print(instruction)


def run_molarity_from_mass_calculator():
    print("\nCalculate molarity from weighed solid")

    compound_name = input("Enter compound name, example NaCl: ").strip()

    mass = get_positive_float("Enter weighed mass: ")

    mass_unit = get_unit(
        "Enter mass unit, example g, mg: ",
        MASS_UNITS
    )

    volume = get_positive_float("Enter final volume: ")

    volume_unit = get_unit(
        "Enter final volume unit, example mL, L: ",
        VOLUME_UNITS
    )

    molecular_weight = get_positive_float("Enter molecular weight in g/mol: ")

    output_molarity_unit = get_unit(
        "Enter output molarity unit, example M, mM, uM: ",
        MOLARITY_UNITS
    )

    instruction = molarity_from_mass_instruction(
        compound_name=compound_name,
        mass=mass,
        mass_unit=mass_unit,
        volume=volume,
        volume_unit=volume_unit,
        molecular_weight=molecular_weight,
        output_molarity_unit=output_molarity_unit
    )

    print("\nResult:")
    print(instruction)


def run_percent_wv_calculator():
    print("\nPrepare percent w/v solution")

    compound_name = input("Enter compound name, example NaCl: ").strip()

    percent = get_positive_float("Enter percent w/v: ")

    volume = get_positive_float("Enter final volume: ")

    volume_unit = get_unit(
        "Enter final volume unit, example mL, L: ",
        VOLUME_UNITS
    )

    output_mass_unit = get_unit(
        "Enter output mass unit, example g, mg: ",
        MASS_UNITS
    )

    instruction = percent_wv_instruction(
        compound_name=compound_name,
        percent=percent,
        volume=volume,
        volume_unit=volume_unit,
        output_mass_unit=output_mass_unit
    )

    print("\nResult:")
    print(instruction)


def run_percent_vv_calculator():
    print("\nPrepare percent v/v solution")

    solute_name = input("Enter solute name, example ethanol: ").strip()

    percent = get_positive_float("Enter percent v/v: ")

    final_volume = get_positive_float("Enter final volume: ")

    final_volume_unit = get_unit(
        "Enter final volume unit, example mL, L: ",
        VOLUME_UNITS
    )

    output_volume_unit = get_unit(
        "Enter output solute volume unit, example mL, L: ",
        VOLUME_UNITS
    )

    instruction = percent_vv_instruction(
        solute_name=solute_name,
        percent=percent,
        final_volume=final_volume,
        final_volume_unit=final_volume_unit,
        output_volume_unit=output_volume_unit
    )

    print("\nResult:")
    print(instruction)


def run_percent_ww_calculator():
    print("\nPrepare percent w/w mixture")

    compound_name = input("Enter compound name, example NaCl: ").strip()

    percent = get_positive_float("Enter percent w/w: ")

    final_mass = get_positive_float("Enter final mixture mass: ")

    final_mass_unit = get_unit(
        "Enter final mixture mass unit, example g, kg: ",
        MASS_UNITS
    )

    output_mass_unit = get_unit(
        "Enter output solute mass unit, example g, mg: ",
        MASS_UNITS
    )

    instruction = percent_ww_instruction(
        compound_name=compound_name,
        percent=percent,
        final_mass=final_mass,
        final_mass_unit=final_mass_unit,
        output_mass_unit=output_mass_unit
    )

    print("\nResult:")
    print(instruction)


def run_concentration_conversion_calculator():
    print("\nConcentration unit conversion")

    value = get_positive_float("Enter concentration value: ")

    from_unit = get_unit(
        "Enter starting concentration unit, example ppm, ppb, mg/L: ",
        CONCENTRATION_UNITS
    )

    to_unit = get_unit(
        "Enter target concentration unit, example ppm, ppb, mg/L: ",
        CONCENTRATION_UNITS
    )

    instruction = concentration_conversion_instruction(
        value=value,
        from_unit=from_unit,
        to_unit=to_unit
    )

    print("\nResult:")
    print(instruction)


def run_serial_dilution_calculator():
    print("\nSerial dilution planner")

    initial_concentration = get_positive_float("Enter initial concentration: ")
    final_concentration = get_positive_float("Enter final concentration: ")
    dilution_factor = get_positive_float(
        "Enter dilution factor per step, example 10: "
    )

    concentration_unit = get_unit(
        "Enter concentration unit, example ppm, mM, mg/L: ",
        DILUTION_CONCENTRATION_UNITS
    )

    instruction = serial_dilution_instruction(
        initial_concentration=initial_concentration,
        final_concentration=final_concentration,
        dilution_factor=dilution_factor,
        concentration_unit=concentration_unit
    )

    print("\nResult:")
    print(instruction)


def run_scaling_calculator():
    print("\nSolution scaling calculator")

    compound_name = input("Enter compound name, example NaCl: ").strip()

    original_amount = get_positive_float("Enter original amount: ")

    amount_unit = get_unit(
        "Enter amount unit, example mg, g, kg: ",
        MASS_UNITS
    )

    original_final_size = get_positive_float("Enter original final size: ")

    final_size_unit = get_unit(
        "Enter final size unit, example mL, L: ",
        VOLUME_UNITS
    )

    new_final_size = get_positive_float("Enter new final size: ")

    instruction = scaling_instruction(
        compound_name=compound_name,
        original_amount=original_amount,
        original_final_size=original_final_size,
        new_final_size=new_final_size,
        amount_unit=amount_unit,
        final_size_unit=final_size_unit
    )

    print("\nResult:")
    print(instruction)


while True:
    show_menu()

    choice = get_choice(
        "\nChoose an option: ",
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    )

    if choice == "1":
        run_dilution_calculator()

    elif choice == "2":
        run_solution_prep_calculator()

    elif choice == "3":
        run_molarity_from_mass_calculator()

    elif choice == "4":
        run_percent_wv_calculator()

    elif choice == "5":
        run_percent_vv_calculator()

    elif choice == "6":
        run_percent_ww_calculator()

    elif choice == "7":
        run_concentration_conversion_calculator()

    elif choice == "8":
        run_serial_dilution_calculator()

    elif choice == "9":
        run_scaling_calculator()

    elif choice == "10":
        print("Exiting QuickLab Calc.")
        break