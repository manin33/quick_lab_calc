"""Streamlit web interface for QuickLab Calc."""

import streamlit as st

from lab_engine.concentration import CONCENTRATION_UNITS, concentration_conversion_instruction
from lab_engine.dilution import dilution_instruction_with_volume_units
from lab_engine.percent_solutions import (
    percent_wv_instruction,
    percent_vv_instruction,
    percent_ww_instruction,
)
from lab_engine.scaling import scaling_instruction
from lab_engine.serial_dilution import serial_dilution_instruction
from lab_engine.solution_prep import (
    solution_prep_instruction,
    molarity_from_mass_instruction,
)
from lab_engine.units import (
    DILUTION_CONCENTRATION_UNITS,
    MASS_UNITS,
    MOLARITY_UNITS,
    VOLUME_UNITS,
)

DISCLAIMER = (
    "QuickLab Calc is a calculation aid for educational and laboratory planning "
    "purposes. Always verify results according to your laboratory SOP, method, "
    "and supervisor requirements."
)


def show_result(instruction: str) -> None:
    """Display an engine result as success or error text."""
    if instruction.startswith("Error:"):
        st.error(instruction)
    elif instruction.startswith("Warning:"):
        st.warning(instruction)
    else:
        st.success(instruction)


def positive_number(label: str, value: float = 1.0, min_value: float = 0.000000001):
    """Create a positive numeric input with a small non-zero minimum."""
    return st.number_input(label, min_value=min_value, value=value, format="%.10g")


def dilution_calculator() -> None:
    st.subheader("Dilution calculator")
    st.caption("Use this when C1 and C2 are in the same concentration unit.")

    with st.form("dilution_form"):
        c1 = positive_number("Stock concentration (C1)", 1000.0)
        c2 = positive_number("Final concentration (C2)", 50.0)
        concentration_unit = st.selectbox("Concentration unit", DILUTION_CONCENTRATION_UNITS, index=5)
        v2 = positive_number("Final volume (V2)", 100.0)
        v2_unit = st.selectbox("Final volume unit", VOLUME_UNITS, index=2)
        output_volume_unit = st.selectbox("Output stock volume unit", VOLUME_UNITS, index=2)
        submitted = st.form_submit_button("Calculate dilution")

    if submitted:
        instruction = dilution_instruction_with_volume_units(
            c1=c1,
            c2=c2,
            v2=v2,
            v2_unit=v2_unit,
            output_volume_unit=output_volume_unit,
            concentration_unit=concentration_unit,
        )
        show_result(instruction)


def solution_prep_calculator() -> None:
    st.subheader("Prepare solution from solid")
    st.caption("Calculates the mass needed from molarity, final volume, and molecular weight.")

    with st.form("solution_prep_form"):
        compound_name = st.text_input("Compound name", "NaCl")
        molarity = positive_number("Target molarity", 50.0)
        molarity_unit = st.selectbox("Molarity unit", MOLARITY_UNITS, index=3)
        volume = positive_number("Final volume", 100.0)
        volume_unit = st.selectbox("Final volume unit", VOLUME_UNITS, index=2)
        molecular_weight = positive_number("Molecular weight (g/mol)", 58.44)
        output_mass_unit = st.selectbox("Output mass unit", MASS_UNITS, index=2)
        submitted = st.form_submit_button("Calculate mass")

    if submitted:
        instruction = solution_prep_instruction(
            compound_name=compound_name.strip() or "compound",
            molarity=molarity,
            molarity_unit=molarity_unit,
            volume=volume,
            volume_unit=volume_unit,
            molecular_weight=molecular_weight,
            output_mass_unit=output_mass_unit,
        )
        show_result(instruction)


def molarity_from_mass_calculator() -> None:
    st.subheader("Molarity from weighed solid")
    st.caption("Calculates concentration from weighed mass, final volume, and molecular weight.")

    with st.form("molarity_from_mass_form"):
        compound_name = st.text_input("Compound name", "NaCl")
        mass = positive_number("Weighed mass", 292.2)
        mass_unit = st.selectbox("Mass unit", MASS_UNITS, index=2)
        volume = positive_number("Final volume", 100.0)
        volume_unit = st.selectbox("Final volume unit", VOLUME_UNITS, index=2)
        molecular_weight = positive_number("Molecular weight (g/mol)", 58.44)
        output_molarity_unit = st.selectbox("Output molarity unit", MOLARITY_UNITS, index=3)
        submitted = st.form_submit_button("Calculate molarity")

    if submitted:
        instruction = molarity_from_mass_instruction(
            compound_name=compound_name.strip() or "compound",
            mass=mass,
            mass_unit=mass_unit,
            volume=volume,
            volume_unit=volume_unit,
            molecular_weight=molecular_weight,
            output_molarity_unit=output_molarity_unit,
        )
        show_result(instruction)


def percent_wv_calculator() -> None:
    st.subheader("Percent w/v solution")
    st.caption("% w/v = grams of solute per 100 mL of final solution.")

    with st.form("percent_wv_form"):
        compound_name = st.text_input("Compound name", "NaCl")
        percent = positive_number("Percent w/v", 1.0)
        volume = positive_number("Final volume", 100.0)
        volume_unit = st.selectbox("Final volume unit", VOLUME_UNITS, index=2)
        output_mass_unit = st.selectbox("Output mass unit", MASS_UNITS, index=3)
        submitted = st.form_submit_button("Calculate % w/v")

    if submitted:
        instruction = percent_wv_instruction(
            compound_name=compound_name.strip() or "compound",
            percent=percent,
            volume=volume,
            volume_unit=volume_unit,
            output_mass_unit=output_mass_unit,
        )
        show_result(instruction)


def percent_vv_calculator() -> None:
    st.subheader("Percent v/v solution")
    st.caption("% v/v = mL of liquid solute per 100 mL of final solution.")

    with st.form("percent_vv_form"):
        solute_name = st.text_input("Solute name", "ethanol")
        percent = st.number_input("Percent v/v", min_value=0.000000001, max_value=100.0, value=70.0, format="%.10g")
        final_volume = positive_number("Final volume", 100.0)
        final_volume_unit = st.selectbox("Final volume unit", VOLUME_UNITS, index=2)
        output_volume_unit = st.selectbox("Output solute volume unit", VOLUME_UNITS, index=2)
        submitted = st.form_submit_button("Calculate % v/v")

    if submitted:
        instruction = percent_vv_instruction(
            solute_name=solute_name.strip() or "solute",
            percent=percent,
            final_volume=final_volume,
            final_volume_unit=final_volume_unit,
            output_volume_unit=output_volume_unit,
        )
        show_result(instruction)


def percent_ww_calculator() -> None:
    st.subheader("Percent w/w mixture")
    st.caption("% w/w = grams of solute per 100 g of final mixture.")

    with st.form("percent_ww_form"):
        compound_name = st.text_input("Compound name", "NaCl")
        percent = st.number_input("Percent w/w", min_value=0.000000001, max_value=100.0, value=5.0, format="%.10g")
        final_mass = positive_number("Final mixture mass", 100.0)
        final_mass_unit = st.selectbox("Final mixture mass unit", MASS_UNITS, index=3)
        output_mass_unit = st.selectbox("Output solute mass unit", MASS_UNITS, index=3)
        submitted = st.form_submit_button("Calculate % w/w")

    if submitted:
        instruction = percent_ww_instruction(
            compound_name=compound_name.strip() or "compound",
            percent=percent,
            final_mass=final_mass,
            final_mass_unit=final_mass_unit,
            output_mass_unit=output_mass_unit,
        )
        show_result(instruction)


def concentration_conversion_calculator() -> None:
    st.subheader("Concentration unit conversion")
    st.caption("For dilute aqueous solutions, ppm is treated approximately as mg/L and ppb as µg/L.")

    with st.form("concentration_conversion_form"):
        value = positive_number("Concentration value", 1.0)
        from_unit = st.selectbox("Starting concentration unit", CONCENTRATION_UNITS, index=0)
        to_unit = st.selectbox("Target concentration unit", CONCENTRATION_UNITS, index=2)
        submitted = st.form_submit_button("Convert concentration")

    if submitted:
        instruction = concentration_conversion_instruction(
            value=value,
            from_unit=from_unit,
            to_unit=to_unit,
        )
        show_result(instruction)
        if from_unit in {"ppm", "ppb"} or to_unit in {"ppm", "ppb"}:
            st.info("Note: ppm/ppb conversions are approximate for dilute aqueous solutions.")


def serial_dilution_calculator() -> None:
    st.subheader("Serial dilution planner")
    st.caption("Plans repeated equal-factor dilutions from an initial concentration to a target concentration.")

    with st.form("serial_dilution_form"):
        initial_concentration = positive_number("Initial concentration", 1000.0)
        final_concentration = positive_number("Requested final concentration", 1.0)
        dilution_factor = positive_number("Dilution factor per step", 10.0, min_value=1.000000001)
        concentration_unit = st.selectbox("Concentration unit", DILUTION_CONCENTRATION_UNITS, index=5)
        submitted = st.form_submit_button("Plan serial dilution")

    if submitted:
        instruction = serial_dilution_instruction(
            initial_concentration=initial_concentration,
            final_concentration=final_concentration,
            dilution_factor=dilution_factor,
            concentration_unit=concentration_unit,
        )
        show_result(instruction)


def scaling_calculator() -> None:
    st.subheader("Solution scaling calculator")
    st.caption("Scales a known recipe amount to a new final size.")

    with st.form("scaling_form"):
        compound_name = st.text_input("Compound name", "NaCl")
        original_amount = positive_number("Original amount", 1.0)
        amount_unit = st.selectbox("Amount unit", MASS_UNITS, index=3)
        original_final_size = positive_number("Original final size", 100.0)
        final_size_unit = st.selectbox("Final size unit", VOLUME_UNITS, index=2)
        new_final_size = positive_number("New final size", 250.0)
        submitted = st.form_submit_button("Scale recipe")

    if submitted:
        instruction = scaling_instruction(
            compound_name=compound_name.strip() or "compound",
            original_amount=original_amount,
            original_final_size=original_final_size,
            new_final_size=new_final_size,
            amount_unit=amount_unit,
            final_size_unit=final_size_unit,
        )
        show_result(instruction)


st.set_page_config(page_title="QuickLab Calc", page_icon="🧪", layout="centered")

st.title("🧪 QuickLab Calc")
st.write("A practical calculator for routine lab solution-preparation calculations.")
st.info(DISCLAIMER)

calculator_options = [
    "Dilution calculator",
    "Prepare solution from solid",
    "Molarity from weighed solid",
    "Percent w/v solution",
    "Percent v/v solution",
    "Percent w/w mixture",
    "Concentration unit conversion",
    "Serial dilution planner",
    "Solution scaling calculator",
    "About / Privacy",
]

calculator = st.radio(
    "Choose calculator",
    calculator_options,
    index=0,
)

if calculator == "Dilution calculator":
    dilution_calculator()
elif calculator == "Prepare solution from solid":
    solution_prep_calculator()
elif calculator == "Molarity from weighed solid":
    molarity_from_mass_calculator()
elif calculator == "Percent w/v solution":
    percent_wv_calculator()
elif calculator == "Percent v/v solution":
    percent_vv_calculator()
elif calculator == "Percent w/w mixture":
    percent_ww_calculator()
elif calculator == "Concentration conversion":
    concentration_conversion_calculator()
elif calculator == "Serial dilution planner":
    serial_dilution_calculator()
elif calculator == "Solution scaling calculator":
    scaling_calculator()
elif calculator == "About / Privacy":
    st.header("About QuickLab Calc")

    st.write(
        "QuickLab Calc is a practical laboratory calculator for routine "
        "solution-preparation calculations, including dilutions, molarity, "
        "percent solutions, concentration conversions, serial dilutions, "
        "and scaling."
    )

    st.subheader("Important disclaimer")

    st.warning(
        "QuickLab Calc is a calculation aid for educational and laboratory "
        "planning purposes. Always verify calculations according to your "
        "laboratory SOP, method, supervisor requirements, and applicable "
        "regulations."
    )

    st.subheader("Internet connection")

    st.write(
        "The web and Android versions of QuickLab Calc require an internet "
        "connection because the app runs through the hosted web application."
    )

    st.subheader("Privacy")

    st.write(
        "QuickLab Calc does not ask users to create an account, does not ask "
        "for names, emails, passwords, phone numbers, payment information, "
        "location, contacts, photos, files, or health information."
    )

    st.write(
        "The app only uses the numerical values entered into the calculator "
        "fields to display calculation results. Do not enter confidential, "
        "proprietary, regulated, or patient-related information."
    )

    st.write(
        "Because the app is hosted online, basic technical information may be "
        "processed by the hosting platform as part of normal web service "
        "operation, such as IP address, browser information, device information, "
        "and usage logs."
    )

    st.subheader("Contact")

    st.write(
        "For feedback, questions, or correction requests, contact the developer "
        "through the GitHub repository or the contact email listed in the "
        "privacy policy."
    )

with st.expander("Example calculations"):
    st.markdown(
        """
- **Dilution:** Prepare 100 mL of 50 ppm from a 1000 ppm stock.
- **Solution from solid:** Prepare 100 mL of 50 mM NaCl using MW 58.44 g/mol.
- **Percent w/v:** Prepare 100 mL of 1% w/v NaCl.
- **Concentration conversion:** Convert 1 mg/mL to mg/L.
        """
    )
