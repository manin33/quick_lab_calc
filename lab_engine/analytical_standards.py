from lab_engine.formatting import format_number


# Analytical standard preparation tools for QuickLab Calc.
#
# This file handles HPLC-style analytical standard calculations using
# mass/volume concentration units such as mg/mL, ug/mL, mg/L, ug/L,
# ppm, and ppb.
#
# Practical assumptions for dilute aqueous-style lab calculations:
# 1 ppm ≈ 1 mg/L
# 1 ppb ≈ 1 ug/L
#
# Internal calculation bases:
# Concentration: mg/mL
# Volume: mL
# Mass: mg


ANALYTICAL_CONCENTRATION_UNITS = [
    "mg/mL",
    "ug/mL",
    "µg/mL",
    "mg/L",
    "ug/L",
    "µg/L",
    "ppm",
    "ppb"
]

ANALYTICAL_VOLUME_UNITS = [
    "mL",
    "L"
]

ANALYTICAL_MASS_UNITS = [
    "ug",
    "µg",
    "mg",
    "g"
]


def purity_fraction(purity_percent):
    if purity_percent <= 0:
        return "Error: purity must be greater than zero."

    if purity_percent > 100:
        return "Error: purity cannot be greater than 100%."

    return purity_percent / 100


def convert_concentration_to_mg_per_ml(value, unit):
    if value <= 0:
        return "Error: concentration must be greater than zero."

    conversion_factors = {
        "mg/mL": 1,
        "ug/mL": 0.001,
        "µg/mL": 0.001,
        "mg/L": 0.001,
        "ug/L": 0.000001,
        "µg/L": 0.000001,
        "ppm": 0.001,
        "ppb": 0.000001
    }

    if unit not in conversion_factors:
        return "Error: unsupported concentration unit."

    return value * conversion_factors[unit]


def convert_mg_per_ml_to_concentration(value_mg_per_ml, output_unit):
    if value_mg_per_ml <= 0:
        return "Error: concentration must be greater than zero."

    conversion_factors = {
        "mg/mL": 1,
        "ug/mL": 1000,
        "µg/mL": 1000,
        "mg/L": 1000,
        "ug/L": 1000000,
        "µg/L": 1000000,
        "ppm": 1000,
        "ppb": 1000000
    }

    if output_unit not in conversion_factors:
        return "Error: unsupported concentration unit."

    return value_mg_per_ml * conversion_factors[output_unit]


def convert_volume_to_ml(value, unit):
    if value <= 0:
        return "Error: volume must be greater than zero."

    conversion_factors = {
        "mL": 1,
        "L": 1000
    }

    if unit not in conversion_factors:
        return "Error: unsupported volume unit."

    return value * conversion_factors[unit]


def convert_volume_from_ml(value_ml, output_unit):
    if value_ml <= 0:
        return "Error: volume must be greater than zero."

    conversion_factors = {
        "mL": 1,
        "L": 0.001
    }

    if output_unit not in conversion_factors:
        return "Error: unsupported volume unit."

    return value_ml * conversion_factors[output_unit]


def convert_mass_to_mg(value, unit):
    if value <= 0:
        return "Error: mass must be greater than zero."

    conversion_factors = {
        "ug": 0.001,
        "µg": 0.001,
        "mg": 1,
        "g": 1000
    }

    if unit not in conversion_factors:
        return "Error: unsupported mass unit."

    return value * conversion_factors[unit]


def convert_mass_from_mg(value_mg, output_unit):
    if value_mg <= 0:
        return "Error: mass must be greater than zero."

    conversion_factors = {
        "ug": 1000,
        "µg": 1000,
        "mg": 1,
        "g": 0.001
    }

    if output_unit not in conversion_factors:
        return "Error: unsupported mass unit."

    return value_mg * conversion_factors[output_unit]


def mass_from_analytical_concentration(
    concentration,
    concentration_unit,
    final_volume,
    final_volume_unit,
    output_mass_unit,
    purity_percent=100
):
    concentration_mg_per_ml = convert_concentration_to_mg_per_ml(
        concentration,
        concentration_unit
    )

    if isinstance(concentration_mg_per_ml, str):
        return concentration_mg_per_ml

    final_volume_ml = convert_volume_to_ml(
        final_volume,
        final_volume_unit
    )

    if isinstance(final_volume_ml, str):
        return final_volume_ml

    purity = purity_fraction(purity_percent)

    if isinstance(purity, str):
        return purity

    pure_mass_mg = concentration_mg_per_ml * final_volume_ml
    weighed_mass_mg = pure_mass_mg / purity

    output_mass = convert_mass_from_mg(
        weighed_mass_mg,
        output_mass_unit
    )

    if isinstance(output_mass, str):
        return output_mass

    pure_mass_output = convert_mass_from_mg(
        pure_mass_mg,
        output_mass_unit
    )

    if isinstance(pure_mass_output, str):
        return pure_mass_output

    result = {
        "concentration": concentration,
        "concentration_unit": concentration_unit,
        "final_volume": final_volume,
        "final_volume_unit": final_volume_unit,
        "mass": output_mass,
        "pure_mass": pure_mass_output,
        "mass_unit": output_mass_unit,
        "pure_mass_mg": pure_mass_mg,
        "weighed_mass_mg": weighed_mass_mg,
        "purity_percent": purity_percent
    }

    return result


def analytical_standard_from_solid_instruction(
    compound_name,
    concentration,
    concentration_unit,
    final_volume,
    final_volume_unit,
    output_mass_unit,
    purity_percent=100
):
    result = mass_from_analytical_concentration(
        concentration=concentration,
        concentration_unit=concentration_unit,
        final_volume=final_volume,
        final_volume_unit=final_volume_unit,
        output_mass_unit=output_mass_unit,
        purity_percent=purity_percent
    )

    if isinstance(result, str):
        return result

    concentration_text = format_number(
        result["concentration"],
        4
    )

    final_volume_text = format_number(
        result["final_volume"],
        4
    )

    mass_text = format_number(
        result["mass"],
        4
    )

    pure_mass_text = format_number(
        result["pure_mass"],
        4
    )

    purity_text = format_number(
        result["purity_percent"],
        4
    )

    if purity_percent == 100:
        message = (
            f"To prepare {final_volume_text} {final_volume_unit} of "
            f"{concentration_text} {concentration_unit} {compound_name} "
            f"analytical standard, weigh {mass_text} {output_mass_unit} "
            f"of {compound_name}, dissolve it in less than "
            f"{final_volume_text} {final_volume_unit} of solvent, then "
            f"bring to a final volume of {final_volume_text} "
            f"{final_volume_unit}."
        )

    else:
        message = (
            f"To prepare {final_volume_text} {final_volume_unit} of "
            f"{concentration_text} {concentration_unit} {compound_name} "
            f"analytical standard, the required pure mass is "
            f"{pure_mass_text} {output_mass_unit}. At {purity_text}% "
            f"purity, weigh {mass_text} {output_mass_unit} of "
            f"{compound_name}, dissolve it in less than "
            f"{final_volume_text} {final_volume_unit} of solvent, then "
            f"bring to a final volume of {final_volume_text} "
            f"{final_volume_unit}."
        )

    return message


def dilute_analytical_standard(
    stock_concentration,
    stock_concentration_unit,
    final_concentration,
    final_concentration_unit,
    final_volume,
    final_volume_unit,
    output_volume_unit
):
    stock_concentration_mg_per_ml = convert_concentration_to_mg_per_ml(
        stock_concentration,
        stock_concentration_unit
    )

    if isinstance(stock_concentration_mg_per_ml, str):
        return stock_concentration_mg_per_ml

    final_concentration_mg_per_ml = convert_concentration_to_mg_per_ml(
        final_concentration,
        final_concentration_unit
    )

    if isinstance(final_concentration_mg_per_ml, str):
        return final_concentration_mg_per_ml

    if final_concentration_mg_per_ml > stock_concentration_mg_per_ml:
        return (
            "Final concentration cannot be greater than stock "
            "concentration for a dilution."
        )

    if final_concentration_mg_per_ml == stock_concentration_mg_per_ml:
        return (
            "No dilution is needed because the final concentration "
            "is equal to the stock concentration."
        )

    final_volume_ml = convert_volume_to_ml(
        final_volume,
        final_volume_unit
    )

    if isinstance(final_volume_ml, str):
        return final_volume_ml

    stock_volume_ml = (
        final_concentration_mg_per_ml
        * final_volume_ml
        / stock_concentration_mg_per_ml
    )

    stock_volume = convert_volume_from_ml(
        stock_volume_ml,
        output_volume_unit
    )

    if isinstance(stock_volume, str):
        return stock_volume

    result = {
        "stock_concentration": stock_concentration,
        "stock_concentration_unit": stock_concentration_unit,
        "final_concentration": final_concentration,
        "final_concentration_unit": final_concentration_unit,
        "final_volume": final_volume,
        "final_volume_unit": final_volume_unit,
        "stock_volume": stock_volume,
        "output_volume_unit": output_volume_unit
    }

    return result


def dilute_analytical_standard_instruction(
    stock_concentration,
    stock_concentration_unit,
    final_concentration,
    final_concentration_unit,
    final_volume,
    final_volume_unit,
    output_volume_unit
):
    result = dilute_analytical_standard(
        stock_concentration=stock_concentration,
        stock_concentration_unit=stock_concentration_unit,
        final_concentration=final_concentration,
        final_concentration_unit=final_concentration_unit,
        final_volume=final_volume,
        final_volume_unit=final_volume_unit,
        output_volume_unit=output_volume_unit
    )

    if isinstance(result, str):
        return result

    stock_volume_text = format_number(
        result["stock_volume"],
        4
    )

    stock_concentration_text = format_number(
        result["stock_concentration"],
        4
    )

    final_volume_text = format_number(
        result["final_volume"],
        4
    )

    final_concentration_text = format_number(
        result["final_concentration"],
        4
    )

    message = (
        f"To prepare {final_volume_text} {final_volume_unit} of "
        f"{final_concentration_text} {final_concentration_unit} "
        f"working standard, take {stock_volume_text} "
        f"{output_volume_unit} of {stock_concentration_text} "
        f"{stock_concentration_unit} stock solution and dilute to "
        f"a final volume of {final_volume_text} {final_volume_unit}."
    )

    return message


def practical_analytical_standard_plan(
    compound_name,
    target_concentration,
    target_concentration_unit,
    working_final_volume,
    working_final_volume_unit,
    stock_pure_mass,
    stock_pure_mass_unit,
    purity_percent,
    stock_final_volume,
    stock_final_volume_unit,
    minimum_pipetting_volume,
    minimum_pipetting_volume_unit,
    output_stock_concentration_unit,
    output_stock_volume_unit
):
    target_concentration_mg_per_ml = convert_concentration_to_mg_per_ml(
        target_concentration,
        target_concentration_unit
    )

    if isinstance(target_concentration_mg_per_ml, str):
        return target_concentration_mg_per_ml

    working_final_volume_ml = convert_volume_to_ml(
        working_final_volume,
        working_final_volume_unit
    )

    if isinstance(working_final_volume_ml, str):
        return working_final_volume_ml

    stock_final_volume_ml = convert_volume_to_ml(
        stock_final_volume,
        stock_final_volume_unit
    )

    if isinstance(stock_final_volume_ml, str):
        return stock_final_volume_ml

    stock_pure_mass_mg = convert_mass_to_mg(
        stock_pure_mass,
        stock_pure_mass_unit
    )

    if isinstance(stock_pure_mass_mg, str):
        return stock_pure_mass_mg

    purity = purity_fraction(purity_percent)

    if isinstance(purity, str):
        return purity

    minimum_pipetting_volume_ml = convert_volume_to_ml(
        minimum_pipetting_volume,
        minimum_pipetting_volume_unit
    )

    if isinstance(minimum_pipetting_volume_ml, str):
        return minimum_pipetting_volume_ml

    direct_pure_mass_mg = (
        target_concentration_mg_per_ml
        * working_final_volume_ml
    )

    direct_weighed_mass_mg = direct_pure_mass_mg / purity

    stock_weighed_mass_mg = stock_pure_mass_mg / purity

    stock_concentration_mg_per_ml = (
        stock_pure_mass_mg
        / stock_final_volume_ml
    )

    stock_concentration_output = convert_mg_per_ml_to_concentration(
        stock_concentration_mg_per_ml,
        output_stock_concentration_unit
    )

    if isinstance(stock_concentration_output, str):
        return stock_concentration_output

    required_stock_volume_ml = (
        target_concentration_mg_per_ml
        * working_final_volume_ml
        / stock_concentration_mg_per_ml
    )

    required_stock_volume_output = convert_volume_from_ml(
        required_stock_volume_ml,
        output_stock_volume_unit
    )

    if isinstance(required_stock_volume_output, str):
        return required_stock_volume_output

    pipetting_is_comfortable = (
        required_stock_volume_ml >= minimum_pipetting_volume_ml
    )

    result = {
        "compound_name": compound_name,
        "target_concentration": target_concentration,
        "target_concentration_unit": target_concentration_unit,
        "working_final_volume": working_final_volume,
        "working_final_volume_unit": working_final_volume_unit,
        "stock_final_volume": stock_final_volume,
        "stock_final_volume_unit": stock_final_volume_unit,
        "stock_pure_mass": stock_pure_mass,
        "stock_pure_mass_unit": stock_pure_mass_unit,
        "stock_weighed_mass_mg": stock_weighed_mass_mg,
        "direct_pure_mass_mg": direct_pure_mass_mg,
        "direct_weighed_mass_mg": direct_weighed_mass_mg,
        "purity_percent": purity_percent,
        "stock_concentration": stock_concentration_output,
        "stock_concentration_unit": output_stock_concentration_unit,
        "required_stock_volume": required_stock_volume_output,
        "required_stock_volume_unit": output_stock_volume_unit,
        "minimum_pipetting_volume": minimum_pipetting_volume,
        "minimum_pipetting_volume_unit": minimum_pipetting_volume_unit,
        "pipetting_is_comfortable": pipetting_is_comfortable
    }

    return result


def practical_analytical_standard_plan_instruction(
    compound_name,
    target_concentration,
    target_concentration_unit,
    working_final_volume,
    working_final_volume_unit,
    stock_pure_mass,
    stock_pure_mass_unit,
    purity_percent,
    stock_final_volume,
    stock_final_volume_unit,
    minimum_pipetting_volume,
    minimum_pipetting_volume_unit,
    output_stock_concentration_unit,
    output_stock_volume_unit
):
    result = practical_analytical_standard_plan(
        compound_name=compound_name,
        target_concentration=target_concentration,
        target_concentration_unit=target_concentration_unit,
        working_final_volume=working_final_volume,
        working_final_volume_unit=working_final_volume_unit,
        stock_pure_mass=stock_pure_mass,
        stock_pure_mass_unit=stock_pure_mass_unit,
        purity_percent=purity_percent,
        stock_final_volume=stock_final_volume,
        stock_final_volume_unit=stock_final_volume_unit,
        minimum_pipetting_volume=minimum_pipetting_volume,
        minimum_pipetting_volume_unit=minimum_pipetting_volume_unit,
        output_stock_concentration_unit=output_stock_concentration_unit,
        output_stock_volume_unit=output_stock_volume_unit
    )

    if isinstance(result, str):
        return result

    target_concentration_text = format_number(
        result["target_concentration"],
        4
    )

    working_volume_text = format_number(
        result["working_final_volume"],
        4
    )

    stock_volume_text = format_number(
        result["stock_final_volume"],
        4
    )

    stock_pure_mass_text = format_number(
        result["stock_pure_mass"],
        4
    )

    stock_weighed_mass_text = format_number(
        result["stock_weighed_mass_mg"],
        4
    )

    direct_pure_mass_text = format_number(
        result["direct_pure_mass_mg"],
        4
    )

    direct_weighed_mass_text = format_number(
        result["direct_weighed_mass_mg"],
        4
    )

    purity_text = format_number(
        result["purity_percent"],
        4
    )

    stock_concentration_text = format_number(
        result["stock_concentration"],
        4
    )

    required_stock_volume_text = format_number(
        result["required_stock_volume"],
        4
    )

    minimum_pipetting_volume_text = format_number(
        result["minimum_pipetting_volume"],
        4
    )

    message = (
        f"Direct preparation check:\n"
        f"To prepare {working_volume_text} "
        f"{working_final_volume_unit} of {target_concentration_text} "
        f"{target_concentration_unit} {compound_name}, the required "
        f"pure mass is {direct_pure_mass_text} mg. At {purity_text}% "
        f"purity, this would require weighing {direct_weighed_mass_text} "
        f"mg of material.\n\n"
        f"Suggested practical stock preparation:\n"
        f"Weigh {stock_weighed_mass_text} mg of {compound_name} "
        f"reference material, equivalent to {stock_pure_mass_text} "
        f"{result['stock_pure_mass_unit']} pure {compound_name}. "
        f"Dissolve it in less than {stock_volume_text} "
        f"{stock_final_volume_unit} of solvent, then bring to a final "
        f"volume of {stock_volume_text} {stock_final_volume_unit}.\n\n"
        f"Stock concentration:\n"
        f"{stock_concentration_text} "
        f"{result['stock_concentration_unit']}.\n\n"
        f"Working standard preparation:\n"
        f"Take {required_stock_volume_text} "
        f"{result['required_stock_volume_unit']} of the "
        f"{stock_concentration_text} {result['stock_concentration_unit']} "
        f"stock standard and dilute to a final volume of "
        f"{working_volume_text} {working_final_volume_unit}."
    )

    if result["pipetting_is_comfortable"]:
        message += (
            f"\n\nPipetting check:\n"
            f"The required stock volume is above the selected minimum "
            f"comfortable pipetting volume of "
            f"{minimum_pipetting_volume_text} "
            f"{minimum_pipetting_volume_unit}."
        )

    else:
        message += (
            f"\n\nPipetting warning:\n"
            f"The required stock volume is below the selected minimum "
            f"comfortable pipetting volume of "
            f"{minimum_pipetting_volume_text} "
            f"{minimum_pipetting_volume_unit}. Consider using a lower "
            f"stock concentration or an intermediate dilution."
        )

    return message