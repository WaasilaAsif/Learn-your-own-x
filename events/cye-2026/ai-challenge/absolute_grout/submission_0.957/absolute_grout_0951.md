# Team: absolute_grout

- Members: Adyaan Ahmed (479556); Abdul Moiz (464853); Muhammad Hamdan Ishfaq (455881)
- Kaggle team name: absolute_grout
- Final Kaggle public score: **0.951**

## Approach
A class-weighted **Extra Trees** ensemble (3 seeds × 500 trees, `min_samples_leaf=5`, `class_weight="balanced_subsample"`) classifies how each reading deviates from a *healthy plant* at the same irradiance and temperature. The healthy plant is a set of polynomial Ridge models fitted only on `normal` rows and refitted inside every fold. A hard rule handles open circuit. Validation is **leave-one-day-out** (13 folds, pooled out-of-fold macro F1), because `test.csv` comes from unseen days. Larger leaves (≥ 5) stop the trees memorising single days.

## Features you made
- **Healthy-plant expectation:**
  - Cubic-polynomial Ridge models predict healthy voltage (`Ve`) and current (`Ie`) from irradiance and temperature.
  - A quadratic model predicts healthy voltage from irradiance, temperature **and** current.
  - All are fitted per fold on `normal` rows only.
- **`Vr` = V / Ve:** open circuit ≈ 0.50, short circuit ≈ 0.87, degradation ≈ 0.95, normal ≈ 1.00.
- **`Ir` = I / Ie:** shading < 1 (mean 0.91 in strong sun), open circuit ≈ 0.52.
- **`Vres` = V − Ve and `Ires` = I − Ie:** absolute deviations, which matter more at high power.
- **`Pr` = Vr · Ir:** power relative to healthy.
- **`Vr2` = V / expected V given G, T and current:** separates a resistive drop (degradation) from a normal change in operating point.
- **Open-circuit rule:** `Vr < 0.65` and irradiance > 800 W/m². One string disconnected halves the voltage, which is unambiguous.

## Results
- **Own validation score:** **0.925** leave-one-day-out macro F1.
- **Per-class F1:** normal 0.950, shading 0.929, degradation 0.769, short circuit 0.982, open circuit 0.996.
- **Which faults the model confuses most, and why:**
  1. **Normal vs. shading (1,419 normal → shading, 901 shading → normal).** When shading is mild, current and voltage look healthy, so no single-reading feature separates them.
  2. **Degradation vs. normal (176 normal → degradation, 139 degradation → normal).** Degradation's voltage factor (about 0.945) is close to normal, while healthy voltage drifts about ±1.5% between days. On test, the degradation cluster is well separated (only about 15 ambiguous rows).
  3. Short circuit and open circuit are almost solved, thanks to large, fixed voltage signatures.
- **Test sanity check:** in strong sun, test `Vr` falls into the same clusters as train (360 rows < 0.65, 359 in 0.8–0.9, 357 in 0.92–0.97). Open-circuit predictions exactly match the 360 open-circuit-like rows.
- **Tried and rejected on validation:** self-training on test, prior re-weighting, dedicated low-irradiance models and temperature residuals (no gain). The validation score is slightly optimistic, since a few configurations were compared on it.

## AI and tools used
- **Claude (Anthropic)** and **ChatGPT (OpenAI):** [describe what each was used for]
- **Libraries:** scikit-learn (ExtraTreesClassifier, Ridge, PolynomialFeatures), pandas, NumPy
- AI chat links: [link 1], [link 2]
