# QuickLab Calc

QuickLab Calc is a practical laboratory calculator for routine analytical chemistry and solution-preparation calculations.

Current version:

```text
V1 web beta + terminal app
```

The project includes a modular Python calculation engine, a terminal interface, and a Streamlit web interface.

---

## Calculators included

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

---

## Important disclaimer

QuickLab Calc is a calculation aid for educational and laboratory planning purposes. Always verify results according to your laboratory SOP, method, and supervisor requirements.

---

## Web app

Run the Streamlit web version locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The web version is the recommended interface for normal users.

---

## Terminal app

Run the terminal version:

```bash
python main.py
```

The terminal version is useful for development and testing.

---

## Project structure

```text
quick_lab_calc/
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── manual_tests.md
└── lab_engine/
    ├── concentration.py
    ├── dilution.py
    ├── formatting.py
    ├── input_helpers.py
    ├── percent_solutions.py
    ├── scaling.py
    ├── serial_dilution.py
    ├── solution_prep.py
    └── units.py
```

---

## File responsibilities

### app.py

Streamlit web interface for the product-facing version of QuickLab Calc.

### main.py

Terminal menu interface. It collects user input and sends values to the calculation modules.

### lab_engine/units.py

Handles unit definitions and unit conversions.

Supported volume units:

```text
uL, µL, mL, L
```

Supported mass units:

```text
ug, µg, mg, g, kg
```

Supported molarity units:

```text
nM, uM, µM, mM, M
```

### lab_engine/dilution.py

Handles single-step dilution calculations based on:

```text
C1 * V1 = C2 * V2
```

### lab_engine/solution_prep.py

Handles molarity-based solution preparation and molarity from weighed solid.

### lab_engine/percent_solutions.py

Handles percentage-based solution and mixture calculations:

```text
% w/v = grams solute per 100 mL final solution
% v/v = mL solute per 100 mL final solution
% w/w = grams solute per 100 g final mixture
```

### lab_engine/concentration.py

Handles common concentration conversions using mg/L as the internal base unit.

For dilute aqueous solutions, ppm is treated approximately as mg/L and ppb as µg/L.

### lab_engine/serial_dilution.py

Plans repeated equal-factor serial dilutions and warns when the requested final concentration is not reached exactly.

### lab_engine/scaling.py

Scales a known recipe amount proportionally to a new final size.

---

## Example outputs

Dilution:

```text
To prepare 100 mL of 50 ppm, take 5 mL of 1000 ppm stock solution and dilute to a final volume of 100 mL.
```

Solution from solid:

```text
To prepare 100 mL of 50 mM NaCl, weigh 292.2 mg of NaCl, dissolve it in less than 100 mL of solvent, then bring to a final volume of 100 mL.
```

Concentration conversion:

```text
1 mg/mL is equal to 1000 mg/L.
```

---

## Deployment to Streamlit Community Cloud

1. Push this project to GitHub.
2. Go to Streamlit Community Cloud.
3. Create a new app from the GitHub repository.
4. Set the main file path to:

```text
app.py
```

5. Deploy.

---

## Current product status

```text
Ready for web beta publication.
```

Recommended public positioning:

```text
QuickLab Calc — free beta laboratory calculator for routine solution preparation.
```

Suggested next improvements:

```text
- Add automated pytest tests
- Add downloadable result reports
- Add compound molecular-weight presets
- Add serial dilution volume planning
- Add a landing page and support/donation link
```
