# Team: absolute_grout

- Members: Adyaan Ahmed (479556); Abdul Moiz (464853); Muhammad Hamdan Ishfaq (455881)
- Kaggle team name: absolute_grout
- Final Kaggle public score: **0.953**

## Approach
Class-balanced **CatBoost** classifies how far each reading deviates from a *healthy plant* at the same irradiance and temperature. The healthy plant is a Huber regression fitted only on `normal` rows of the training days, refitted inside every fold. Training adds synthetic degradation rows. After prediction, a deterministic open-circuit guard is applied, and probabilities are smoothed over each row's 40 nearest neighbours in raw-sensor space. Validation is **leave-one-day-out** (13 folds, pooled out-of-fold macro F1), cross-checked with **BLOCK3** folds that hold out 3 days at once, because `test.csv` comes from unseen days and has no `day` column.

## Features you made
- **Healthy-plant expectation**, fitted per fold on `normal` rows only: `v_exp = f(T, ln G, G)` and `i_exp = a·G + b·G·T`. Every feature below is a deviation from it, which removes day-to-day weather.
- **`v_ratio` = V / v_exp:** open circuit ≈ 0.50, short circuit ≈ 0.87, degradation ≈ 0.95, normal ≈ 1.00.
- **`i_ratio` = I / i_exp:** shading < 1, and open circuit ≈ 0.5 (one string lost).
- **`v_res` = V − v_exp:** short circuit is about −35 V and degradation about −15 V.
- **`r_app` = −v_res / I** (apparent extra series resistance): degradation is extra wiring resistance, so its voltage loss grows with current.
- **`irr_c` = irradiance capped at 800 W/m²:** faults were only seen in strong sun. Capping stops "very sunny" itself from acting as a fault signal.
- **Open-circuit guard:** `v_ratio < 0.65` and `0.35 < i_ratio < 0.70`. Half voltage with half current means a disconnected string, which is unambiguous physics.
- **Synthetic degradation rows** (training only): a voltage drop of R·I is applied to healthy high-sun rows, with R sampled from the fold's real degradation rows. The model learns the physical signature rather than the 4 days degradation appeared on.
- **Temporal neighbour smoothing** (k = 40, post-processing, no labels):
  - Readings are 10 s apart and nearly identical between neighbours, so a row's nearest neighbours in the 4 raw signals are mostly its neighbours in time.
  - Averaging each row's probabilities with its 40 neighbours (inside each held-out set, or the test set) restores the time context the shuffle removed.
  - It was kept only because it beat the unsmoothed model on **both** validation splits.

## Results
- **Own validation score:** **0.951** leave-one-day-out, 0.954 BLOCK3. Without smoothing: 0.935 / 0.937.
- **Per-class F1 (leave-one-day-out):** normal 0.950, shading 0.921, degradation 0.903, short circuit 0.988, open circuit 0.996.
- **Which faults the model confuses most, and why:**
  1. **Normal vs. shading (about 1,200 / 1,350 rows).** Mild shading, especially at low irradiance, leaves current and voltage looking healthy, so no single-reading feature separates them. Smoothing helps because shading comes in continuous stretches.
  2. **Degradation vs. normal (84 normal rows called degradation, 43 missed).** Degradation lowers voltage by only about 5% (ratio about 0.945), while healthy voltage drifts about ±1.5% between days.
  3. Short circuit and open circuit are almost solved, because their voltage signatures are large, fixed fractions.
- **Tried and rejected on validation:** a shading/normal probability bias (gain under 0.003), simple ratio features (VI, I/G, VI/G, V/I, log G), LightGBM (overfit to training days), self-training on test, and prior re-weighting.

## AI and tools used
- **Claude (Anthropic)** and **ChatGPT (OpenAI):** [describe what each was used for]
- **Libraries:** CatBoost, scikit-learn (HuberRegressor, NearestNeighbors, StandardScaler), pandas, NumPy, Matplotlib
- AI chat links: [link 1], [link 2]
