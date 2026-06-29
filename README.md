# QuickLab Calc

QuickLab Calc is a practical laboratory calculator focused on routine analytical chemistry and solution preparation calculations.

The project is currently built in Python as a calculation engine and terminal-based application. The long-term goal is to keep the calculation logic modular so it can later support a desktop interface, mobile app, Unity interface, or web version.

---

## Current Status

QuickLab Calc currently works as a terminal application.

Current version:

```text
V1 terminal stable
```

Functional calculators:

```text
1. Dilution calculator
2. Prepare solution from solid
3. Calculate molarity from weighed solid
4. Prepare percent w/v solution
5. Prepare percent v/v solution
6. Prepare percent w/w mixture
7. Concentration unit conversion
8. Serial dilution planner
9. Solution scaling calculator
```

The program also includes:

```text
- Unit conversion
- Concentration conversion
- Input validation
- Unit validation
- Unit normalization
- Clean number formatting
- Manual test checklist
- Serial dilution warning for non-exact dilution series
- Proportional scaling for solution recipes
```

---

## Project Structure

```text
quick_lab_calc/
├── main.py
├── README.md
├── manual_tests.md
└── lab_engine/
    ├── dilution.py
    ├── units.py
    ├── solution_prep.py
    ├── percent_solutions.py
    ├── concentration.py
    ├── serial_dilution.py
    ├── scaling.py
    ├── formatting.py
    └── input_helpers.py
```

---

## File Responsibilities

### main.py

Controls the terminal menu and user interaction.

It does not perform chemistry calculations directly. It collects user input, validates it, and sends the values to the calculation modules.

---

### lab_engine/units.py

Handles unit definitions and unit conversions.

Current supported units:

Volume:

```text
uL
µL
mL
L
```

Mass:

```text
ug
µg
mg
g
kg
```

Molarity:

```text
nM
uM
µM
mM
M
```

Dilution concentration units:

```text
nM
uM
µM
mM
M
ppm
```

Main functions:

```text
convert_volume()
convert_mass()
convert_molarity()
```

---

### lab_engine/dilution.py

Handles single-step dilution calculations based on:

```text
C1 * V1 = C2 * V2
```

Current features:

```text
- Calculates missing dilution value
- Handles volume unit conversion
- Formats dilution instructions
- Blocks invalid dilution cases
```

Validation examples:

```text
C2 > C1 → invalid dilution
C2 = C1 → no dilution needed
C2 < C1 → valid dilution
```

---

### lab_engine/solution_prep.py

Handles molarity-based solution preparation.

Current calculators:

```text
mass_from_molarity()
solution_prep_instruction()
molarity_from_mass()
molarity_from_mass_instruction()
```

Example use cases:

```text
Prepare 100 mL of 50 mM NaCl from solid NaCl.
Calculate the molarity of a solution prepared from a known mass and final volume.
```

---

### lab_engine/percent_solutions.py

Handles percentage-based solution and mixture calculations.

Current calculators:

```text
% w/v
% v/v
% w/w
```

Definitions:

```text
% w/v = grams of solute per 100 mL of final solution
% v/v = mL of solute per 100 mL of final solution
% w/w = grams of solute per 100 g of final mixture
```

Current functions:

```text
mass_from_percent_wv()
percent_wv_instruction()

volume_from_percent_vv()
percent_vv_instruction()

mass_from_percent_ww()
percent_ww_instruction()
```

---

### lab_engine/concentration.py

Handles analytical concentration unit conversions.

Internal base unit:

```text
mg/L
```

Current supported concentration units:

```text
ppm
ppb
mg/L
ug/L
µg/L
mg/mL
ug/mL
µg/mL
```

Current functions:

```text
convert_concentration()
format_concentration_conversion_result()
concentration_conversion_instruction()
```

Practical assumptions:

```text
For dilute aqueous solutions:
1 ppm ≈ 1 mg/L
1 ppb ≈ 1 ug/L
1 ug/mL = 1 mg/L
1 mg/mL = 1000 mg/L
```

---

### lab_engine/serial_dilution.py

Handles serial dilution planning.

A serial dilution uses the same dilution factor repeatedly to move from an initial concentration toward a lower target concentration.

Current functions:

```text
calculate_serial_dilution_steps()
format_serial_dilution_steps()
serial_dilution_instruction()
```

Current features:

```text
- Calculates each serial dilution step
- Supports repeated 1:X dilution factors
- Blocks invalid serial dilution cases
- Warns when the selected dilution factor does not end exactly at the requested final concentration
```

Validation examples:

```text
Final concentration >= initial concentration → invalid serial dilution
Dilution factor <= 1 → invalid dilution factor
Exact endpoint → normal serial dilution plan
Non-exact endpoint → serial dilution plan with warning
```

Example:

```text
Initial concentration = 1000 ppm
Final concentration = 1 ppm
Dilution factor = 10
```

Output:

```text
1000 ppm → 100 ppm → 10 ppm → 1 ppm
```

Non-exact example:

```text
Initial concentration = 1000 ppm
Final concentration = 3 ppm
Dilution factor = 10
```

Output:

```text
1000 ppm → 100 ppm → 10 ppm → 1 ppm
```

The program warns that the final result is 1 ppm, not the requested 3 ppm.

---

### lab_engine/scaling.py

Handles proportional scaling for solution recipes.

This calculator is useful when a known recipe needs to be prepared at a different final size.

Current functions:

```text
scale_amount()
format_scaling_result()
scaling_instruction()
```

Current features:

```text
- Scales an ingredient amount proportionally
- Supports scaling up
- Supports scaling down
- Calculates the scaling factor
- Blocks zero or negative values through input validation
```

Example:

```text
Original recipe:
5 g NaCl for 100 mL final volume

New final volume:
250 mL
```

Output:

```text
Use 12.5 g NaCl.
```

Formula:

```text
new amount = original amount × (new final size / original final size)
```

---

### lab_engine/formatting.py

Handles display formatting only.

Current function:

```text
format_number()
```

Purpose:

```text
- Removes unnecessary .0
- Rounds long floating point values
- Keeps output readable for lab instructions
```

Example:

```text
100.0 → 100
50.0000000001 → 50
0.29220000000000007 → 0.2922
```

---

### lab_engine/input_helpers.py

Handles input validation.

Current functions:

```text
get_float()
get_positive_float()
get_choice()
normalize_unit()
get_unit()
```

Purpose:

```text
- Prevents invalid text input from crashing the program
- Rejects zero and negative values
- Validates menu choices
- Validates supported units
- Normalizes common unit aliases
```

Examples:

```text
ml → mL
ML → mL
mm → mM
um → uM
mg/ml → mg/mL
mgml → mg/mL
mg/l → mg/L
mgl → mg/L
ug/ml → ug/mL
ugml → ug/mL
ug/l → ug/L
ugl → ug/L
ppm → ppm
```

Note:

For micro units, users can type `"u"` instead of the Greek micro symbol.

Examples:

```text
uL instead of µL
ug instead of µg
uM instead of µM
ug/L instead of µg/L
ug/mL instead of µg/mL
```

---

## How to Run

From the project folder, run:

```powershell
python main.py
```

The program will show this menu:

```text
QuickLab Calc
1. Dilution calculator
2. Prepare solution from solid
3. Calculate molarity from weighed solid
4. Prepare percent w/v solution
5. Prepare percent v/v solution
6. Prepare percent w/w mixture
7. Concentration unit conversion
8. Serial dilution planner
9. Solution scaling calculator
10. Exit
```

---

## Example Calculations

### Dilution

Input:

```text
C1 = 1000 ppm
C2 = 50 ppm
V2 = 100 mL
```

Output:

```text
To prepare 100 mL of 50 ppm, take 5 mL of 1000 ppm stock solution and dilute to a final volume of 100 mL.
```

---

### Prepare Solution from Solid

Input:

```text
Compound = NaCl
Target molarity = 50 mM
Final volume = 100 mL
Molecular weight = 58.44 g/mol
```

Output:

```text
To prepare 100 mL of 50 mM NaCl, weigh 0.2922 g of NaCl, dissolve it in less than 100 mL of solvent, then bring to a final volume of 100 mL.
```

---

### Molarity from Weighed Solid

Input:

```text
Compound = NaCl
Mass = 0.2922 g
Final volume = 100 mL
Molecular weight = 58.44 g/mol
```

Output:

```text
0.2922 g of NaCl brought to a final volume of 100 mL gives a concentration of 50 mM.
```

---

### Percent w/v

Input:

```text
Compound = NaCl
Percent = 5% w/v
Final volume = 100 mL
```

Output:

```text
To prepare 100 mL of 5% w/v NaCl, weigh 5 g of NaCl, dissolve it in less than 100 mL of solvent, then bring to a final volume of 100 mL.
```

---

### Percent v/v

Input:

```text
Solute = ethanol
Percent = 70% v/v
Final volume = 100 mL
```

Output:

```text
To prepare 100 mL of 70% v/v ethanol, measure 70 mL of ethanol, then bring to a final volume of 100 mL.
```

---

### Percent w/w

Input:

```text
Compound = NaCl
Percent = 50% w/w
Final mixture mass = 300 g
```

Output:

```text
To prepare 300 g of 50% w/w NaCl mixture, weigh 150 g of NaCl, then add solvent or other components until the final mixture mass is 300 g.
```

---

### Concentration Unit Conversion

Input:

```text
Value = 1
Starting unit = ppm
Target unit = ppb
```

Output:

```text
1 ppm is equal to 1000 ppb.
```

Input:

```text
Value = 1
Starting unit = mg/mL
Target unit = mg/L
```

Output:

```text
1 mg/mL is equal to 1000 mg/L.
```

---

### Serial Dilution Planner

Input:

```text
Initial concentration = 1000 ppm
Final concentration = 1 ppm
Dilution factor per step = 10
```

Output:

```text
Serial dilution plan:
Step 1: perform a 1:10 dilution to go from 1000 ppm to 100 ppm.
Step 2: perform a 1:10 dilution to go from 100 ppm to 10 ppm.
Step 3: perform a 1:10 dilution to go from 10 ppm to 1 ppm.
```

Non-exact endpoint example:

Input:

```text
Initial concentration = 1000 ppm
Final concentration = 3 ppm
Dilution factor per step = 10
```

Output:

```text
Serial dilution plan:
Step 1: perform a 1:10 dilution to go from 1000 ppm to 100 ppm.
Step 2: perform a 1:10 dilution to go from 100 ppm to 10 ppm.
Step 3: perform a 1:10 dilution to go from 10 ppm to 1 ppm.

Warning: this serial dilution does not end exactly at the requested final concentration of 3 ppm. The final concentration after the last step is 1 ppm.
```

---

### Solution Scaling Calculator

Input:

```text
Compound = NaCl
Original amount = 5 g
Original final size = 100 mL
New final size = 250 mL
```

Output:

```text
To scale NaCl from 100 mL to 250 mL, multiply the original amount by 2.5. Use 12.5 g of NaCl.
```

Scale-down example:

Input:

```text
Compound = NaCl
Original amount = 5 g
Original final size = 100 mL
New final size = 50 mL
```

Output:

```text
To scale NaCl from 100 mL to 50 mL, multiply the original amount by 0.5. Use 2.5 g of NaCl.
```

---

## Manual Testing

Manual test cases are stored in:

```text
manual_tests.md
```

Before adding new features, the existing tests should be checked to make sure nothing broke.

---

## Current Development Goal

The current goal is to keep building the calculation engine in Python before creating a graphical interface.

The project should remain modular, with each file having one clear responsibility.

Current short-term goal:

```text
Prepare QuickLab Calc V1 for a clean GitHub terminal release.
```

---

## Possible Next Features

Potential future calculators:

```text
- buffer preparation
- pH calculations
- Henderson-Hasselbalch calculator
- molality
- normality
- density-based liquid preparation
- automated unit tests
```

Potential future technical improvements:

```text
- Automated tests
- GUI interface
- Export calculation reports
- Save calculation history
- Package as desktop app
- Unity interface
- Web version
```

---

## Project Philosophy

QuickLab Calc should be practical, modular, and chemically accurate.

The program should give instructions that make sense in a real laboratory context.

For example:

```text
Correct:
Weigh the solute, dissolve it in less than the final volume, then bring to final volume.

Incorrect:
Add exactly the final volume of solvent to the solute.
```

This distinction is important because laboratory solution preparation is based on final volume, not simply solvent volume added.
