from lab_engine.formatting import format_number


# Solution scaling tools for QuickLab Calc.
#
# This file handles proportional scaling.
# It can scale a known ingredient amount from an original final size
# to a new final size.
#
# Formula:
# new amount = original amount * (new final size / original final size)


def scale_amount(
    original_amount,
    original_final_size,
    new_final_size
):
    # Values must be greater than zero.
    if original_amount <= 0:
        return "Error: original amount must be greater than zero."

    if original_final_size <= 0:
        return "Error: original final size must be greater than zero."

    if new_final_size <= 0:
        return "Error: new final size must be greater than zero."

    # Calculate the proportional scaling factor.
    scaling_factor = new_final_size / original_final_size

    # Apply the scaling factor to the original amount.
    new_amount = original_amount * scaling_factor

    result = {
        "original_amount": original_amount,
        "original_final_size": original_final_size,
        "new_final_size": new_final_size,
        "scaling_factor": scaling_factor,
        "new_amount": new_amount
    }

    return result


# Format the scaling result as a lab instruction.
def format_scaling_result(
    compound_name,
    scaling_result,
    amount_unit,
    final_size_unit
):
    if isinstance(scaling_result, str):
        return scaling_result

    original_final_size = format_number(
        scaling_result["original_final_size"],
        4
    )

    new_final_size = format_number(
        scaling_result["new_final_size"],
        4
    )

    scaling_factor = format_number(
        scaling_result["scaling_factor"],
        4
    )

    new_amount = format_number(
        scaling_result["new_amount"],
        4
    )

    message = (
        f"To scale {compound_name} from {original_final_size} "
        f"{final_size_unit} to {new_final_size} {final_size_unit}, "
        f"multiply the original amount by {scaling_factor}. "
        f"Use {new_amount} {amount_unit} of {compound_name}."
    )

    return message


# Create a complete scaling instruction.
def scaling_instruction(
    compound_name,
    original_amount,
    original_final_size,
    new_final_size,
    amount_unit,
    final_size_unit
):
    scaling_result = scale_amount(
        original_amount=original_amount,
        original_final_size=original_final_size,
        new_final_size=new_final_size
    )

    instruction = format_scaling_result(
        compound_name=compound_name,
        scaling_result=scaling_result,
        amount_unit=amount_unit,
        final_size_unit=final_size_unit
    )

    return instruction