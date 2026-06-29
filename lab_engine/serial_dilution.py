from lab_engine.formatting import format_number


# Serial dilution tools for QuickLab Calc.
#
# This file handles serial dilution planning.
# It does not perform unit conversions.
#
# Assumption:
# initial concentration and final concentration use the same unit.


def calculate_serial_dilution_steps(
    initial_concentration,
    final_concentration,
    dilution_factor
):
    # Values must be greater than zero.
    if initial_concentration <= 0:
        return "Error: initial concentration must be greater than zero."

    if final_concentration <= 0:
        return "Error: final concentration must be greater than zero."

    if dilution_factor <= 1:
        return "Error: dilution factor must be greater than one."

    # Final concentration must be lower than initial concentration.
    if final_concentration >= initial_concentration:
        return (
            "Error: final concentration must be lower than initial "
            "concentration for a serial dilution."
        )

    steps = []
    current_concentration = initial_concentration
    step_number = 1

    while current_concentration > final_concentration:
        next_concentration = current_concentration / dilution_factor

        steps.append(
            {
                "step": step_number,
                "from_concentration": current_concentration,
                "to_concentration": next_concentration,
                "dilution_factor": dilution_factor
            }
        )

        current_concentration = next_concentration
        step_number += 1

        # Safety stop to avoid infinite loops.
        if step_number > 100:
            return "Error: too many serial dilution steps."

    # Floating point calculations can create very small precision differences.
    tolerance = 1e-12
    is_exact = abs(current_concentration - final_concentration) < tolerance

    result = {
        "steps": steps,
        "requested_final_concentration": final_concentration,
        "actual_final_concentration": current_concentration,
        "is_exact": is_exact
    }

    return result


def format_serial_dilution_steps(
    serial_dilution_result,
    concentration_unit
):
    if isinstance(serial_dilution_result, str):
        return serial_dilution_result

    steps = serial_dilution_result["steps"]
    requested_final_concentration = (
        serial_dilution_result["requested_final_concentration"]
    )
    actual_final_concentration = (
        serial_dilution_result["actual_final_concentration"]
    )
    is_exact = serial_dilution_result["is_exact"]

    message = "Serial dilution plan:\n"

    for step in steps:
        step_number = step["step"]
        from_concentration = format_number(step["from_concentration"], 4)
        to_concentration = format_number(step["to_concentration"], 4)
        dilution_factor = format_number(step["dilution_factor"], 4)

        message += (
            f"Step {step_number}: perform a 1:{dilution_factor} dilution "
            f"to go from {from_concentration} {concentration_unit} "
            f"to {to_concentration} {concentration_unit}.\n"
        )

    if not is_exact:
        requested_final_concentration = format_number(
            requested_final_concentration,
            4
        )
        actual_final_concentration = format_number(
            actual_final_concentration,
            4
        )

        message += (
            "\nWarning: this serial dilution does not end exactly at the "
            f"requested final concentration of {requested_final_concentration} "
            f"{concentration_unit}. The final concentration after the last "
            f"step is {actual_final_concentration} {concentration_unit}."
        )

    return message.strip()


def serial_dilution_instruction(
    initial_concentration,
    final_concentration,
    dilution_factor,
    concentration_unit
):
    serial_dilution_result = calculate_serial_dilution_steps(
        initial_concentration=initial_concentration,
        final_concentration=final_concentration,
        dilution_factor=dilution_factor
    )

    instruction = format_serial_dilution_steps(
        serial_dilution_result=serial_dilution_result,
        concentration_unit=concentration_unit
    )

    return instruction