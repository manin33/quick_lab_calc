# QuickLab Calc — Manual Test Checklist

This file contains manual test cases for QuickLab Calc.

Run the program from the project folder:

python main.py

---

## 1. Dilution calculator

### Test 1 — Valid dilution

Input:

Option: 1
C1: 1000
C2: 50
V2: 100
Concentration unit: ppm
Final volume unit: ml
Output volume unit: ml

Expected result:

To prepare 100 mL of 50 ppm, take 5 mL of 1000 ppm stock solution and dilute to a final volume of 100 mL.

---

### Test 2 — No dilution needed

Input:

Option: 1
C1: 100
C2: 100
V2: 50
Concentration unit: ppm
Final volume unit: ml
Output volume unit: ml

Expected result:

No dilution is needed because the stock concentration and final concentration are both 100 ppm. Use 50 mL of the stock solution directly.

---

### Test 3 — Invalid dilution

Input:

Option: 1
C1: 3
C2: 4
V2: 3
Concentration unit: ppm
Final volume unit: ml
Output volume unit: ml

Expected result:

Error: final concentration cannot be greater than stock concentration for a dilution.

---

## 2. Prepare solution from solid

### Test 1 — NaCl 50 mM, 100 mL

Input:

Option: 2
Compound name: NaCl
Target molarity: 50
Molarity unit: mm
Final volume: 100
Final volume unit: ml
Molecular weight: 58.44
Output mass unit: g

Expected result:

To prepare 100 mL of 50 mM NaCl, weigh 0.2922 g of NaCl, dissolve it in less than 100 mL of solvent, then bring to a final volume of 100 mL.

---

## 3. Calculate molarity from weighed solid

### Test 1 — NaCl reverse calculation

Input:

Option: 3
Compound name: NaCl
Weighed mass: 0.2922
Mass unit: g
Final volume: 100
Final volume unit: ml
Molecular weight: 58.44
Output molarity unit: mm

Expected result:

0.2922 g of NaCl brought to a final volume of 100 mL gives a concentration of 50 mM.

---

## 4. Percent w/v solution

### Test 1 — 5% w/v NaCl

Input:

Option: 4
Compound name: NaCl
Percent w/v: 5
Final volume: 100
Final volume unit: ml
Output mass unit: g

Expected result:

To prepare 100 mL of 5% w/v NaCl, weigh 5 g of NaCl, dissolve it in less than 100 mL of solvent, then bring to a final volume of 100 mL.

---

## 5. Percent v/v solution

### Test 1 — 70% v/v ethanol

Input:

Option: 5
Solute name: ethanol
Percent v/v: 70
Final volume: 100
Final volume unit: ml
Output solute volume unit: ml

Expected result:

To prepare 100 mL of 70% v/v ethanol, measure 70 mL of ethanol, then bring to a final volume of 100 mL.

---

## 6. Percent w/w mixture

### Test 1 — 50% w/w NaCl, 300 g

Input:

Option: 6
Compound name: NaCl
Percent w/w: 50
Final mixture mass: 300
Final mixture mass unit: g
Output solute mass unit: kg

Expected result:

To prepare 300 g of 50% w/w NaCl mixture, weigh 0.15 kg of NaCl, then add solvent or other components until the final mixture mass is 300 g.

---

## 7. Concentration unit conversion

### Test 1 — ppm to ppb

Input:

Option: 7
Concentration value: 1
Starting concentration unit: ppm
Target concentration unit: ppb

Expected result:

1 ppm is equal to 1000 ppb.

---

### Test 2 — mg/mL to mg/L

Input:

Option: 7
Concentration value: 1
Starting concentration unit: mg/ml
Target concentration unit: mg/l

Expected result:

1 mg/mL is equal to 1000 mg/L.

---

### Test 3 — ug/L to ppb

Input:

Option: 7
Concentration value: 500
Starting concentration unit: ug/l
Target concentration unit: ppb

Expected result:

500 ug/L is equal to 500 ppb.

---

### Test 4 — mgml to mgl alias

Input:

Option: 7
Concentration value: 1
Starting concentration unit: mgml
Target concentration unit: mgl

Expected result:

1 mg/mL is equal to 1000 mg/L.

---

## 8. Serial dilution planner

### Test 1 — Exact serial dilution

Input:

Option: 8
Initial concentration: 1000
Final concentration: 1
Dilution factor per step: 10
Concentration unit: ppm

Expected result:

Serial dilution plan:
Step 1: perform a 1:10 dilution to go from 1000 ppm to 100 ppm.
Step 2: perform a 1:10 dilution to go from 100 ppm to 10 ppm.
Step 3: perform a 1:10 dilution to go from 10 ppm to 1 ppm.

---

### Test 2 — Non-exact serial dilution warning

Input:

Option: 8
Initial concentration: 1000
Final concentration: 3
Dilution factor per step: 10
Concentration unit: ppm

Expected result:

Serial dilution plan:
Step 1: perform a 1:10 dilution to go from 1000 ppm to 100 ppm.
Step 2: perform a 1:10 dilution to go from 100 ppm to 10 ppm.
Step 3: perform a 1:10 dilution to go from 10 ppm to 1 ppm.

Warning: this serial dilution does not end exactly at the requested final concentration of 3 ppm. The final concentration after the last step is 1 ppm.

---

### Test 3 — Invalid serial dilution

Input:

Option: 8
Initial concentration: 100
Final concentration: 100
Dilution factor per step: 10
Concentration unit: ppm

Expected result:

Error: final concentration must be lower than initial concentration for a serial dilution.

---

## 9. Solution scaling calculator

### Test 1 — Scale NaCl solution from 100 mL to 250 mL

Input:

Option: 9
Compound name: NaCl
Original amount: 5
Amount unit: g
Original final size: 100
Final size unit: ml
New final size: 250

Expected result:

To scale NaCl from 100 mL to 250 mL, multiply the original amount by 2.5. Use 12.5 g of NaCl.

---

### Test 2 — Scale down NaCl solution from 100 mL to 50 mL

Input:

Option: 9
Compound name: NaCl
Original amount: 5
Amount unit: g
Original final size: 100
Final size unit: ml
New final size: 50

Expected result:

To scale NaCl from 100 mL to 50 mL, multiply the original amount by 0.5. Use 2.5 g of NaCl.

---

## 10. Input validation

### Test 1 — Invalid menu option

Input:

Option: hello

Expected result:

Error: invalid option. Allowed options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

---

### Test 2 — Invalid number

Input:

Enter stock concentration C1: hello

Expected result:

Error: please enter a valid number.

---

### Test 3 — Zero value

Input:

Enter stock concentration C1: 0

Expected result:

Error: value must be greater than zero.

---

### Test 4 — Negative value

Input:

Enter stock concentration C1: -5

Expected result:

Error: value must be greater than zero.

---

### Test 5 — Invalid unit

Input:

Molarity unit: molar

Expected result:

Error: unsupported unit. Allowed units: nM, uM, µM, mM, M

---

### Test 6 — Unit normalization

These inputs should work:

ml -> mL
mm -> mM
um -> uM
mg/ml -> mg/mL
mgml -> mg/mL
mg/l -> mg/L
mgl -> mg/L
ug/ml -> ug/mL
ugml -> ug/mL
ug/l -> ug/L
ugl -> ug/L
