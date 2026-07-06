from lab_engine.concentration import concentration_conversion_instruction
from lab_engine.dilution import dilution_instruction_with_volume_units
from lab_engine.percent_solutions import percent_vv_instruction, percent_ww_instruction
from lab_engine.solution_prep import solution_prep_instruction


def test_dilution_instruction():
    result = dilution_instruction_with_volume_units(1000, 50, 100, "mL", "mL", "ppm")
    assert "take 5 mL" in result
    assert "final volume of 100 mL" in result


def test_solution_prep_instruction():
    result = solution_prep_instruction("NaCl", 50, "mM", 100, "mL", 58.44, "mg")
    assert "292.2 mg" in result
    assert "bring to a final volume" in result


def test_concentration_conversion_instruction():
    result = concentration_conversion_instruction(1, "mg/mL", "mg/L")
    assert result == "1 mg/mL is equal to 1000 mg/L."


def test_percent_vv_rejects_over_100():
    result = percent_vv_instruction("ethanol", 120, 100, "mL", "mL")
    assert result == "Error: percent v/v cannot be greater than 100."


def test_percent_ww_rejects_over_100():
    result = percent_ww_instruction("NaCl", 120, 100, "g", "g")
    assert result == "Error: percent w/w cannot be greater than 100."
