# NUST Nodes

- **Members:** Haider Ali Malik (Lead, NUST SEECS, BSCS-2026, Abdul Areez , Abu Bakar Ayub, Sami ullah
- - **Kaggle team name:** haider malik
- **Final Kaggle public score:** 0.951

## Approach
We trained a 4-model soft-voting ensemble combining `HistGradientBoosting`, `ExtraTrees`, and two `StandardScaler`-backed `MLPClassifier` neural networks (`(64, 32)` and `(96, 48)`) on physics-based features across 44,017 training rows. Because the test set covers unseen days with severe class imbalance, we switched from `StratifiedKFold` to `GroupKFold` grouped by `day` to prevent day-level leakage and measure true unseen-day generalization. Along the way, we kept models and scalers that improved unseen-day CV (`StandardScaler` + multi-seed MLPs) and dropped changes that hurt generalization (`RandomForest` overfitting unseen days and `QuantileTransformer` distorting linear physical relationships).

## Features You Made
- **`power_per_irr`:** Normalizes electrical power output by irradiance so operating states can be compared across varying sunlight levels.
- **`voltage_ratio_expected`:** Captures expected voltage behavior relative to baseline conditions rather than raw sensor magnitudes alone.
- **`voltage_residual`:** Measures deviation between observed and expected voltage to highlight fault-driven voltage drops.
- **`v_res_x_irr`:** Multiplies voltage residual by irradiance to isolate joint high-sun/voltage-drop behavior characteristic of `degradation` vs. `normal`.
- **`v_res_per_temp`:** Scales voltage residual against panel temperature (`panel_temp + 25.0`) to separate thermal/degradation effects across unseen days.
- **`eff_to_v_ratio`:** Relates normalized power-per-irradiance to expected voltage ratio (`power_per_irr / (voltage_ratio_expected + eps)`) as a fill-factor proxy.

## Results
- **Your own validation score:** `0.92525` Unseen-Day Macro F1 (`0.94407` Unseen-Day Accuracy) using 5-fold `GroupKFold` by `day` on the V6 ensemble.
- **Which faults your model confuses most, and why:** `degradation` (F1 `0.7563`, precision `0.7955`, recall `0.7207`) is the hardest class and is confused most with `normal` (and borderline `shading`). It makes up only ~1.5% of the training set and shows gradual voltage/efficiency shifts that can look similar to normal operation or mild shading on unseen days, whereas `open_circuit` (`0.9959`), `short_circuit` (`0.9858`), `normal` (`0.9538`), and `shading` (`0.9345`) separate much more cleanly.

## AI and Tools Used
- **Languages & Libraries:** Python, scikit-learn, pandas, NumPy
- **Environment:** Google Colab
- **AI Assistance:** Gemini — used collaboratively where we provided the domain ideas, modeling logic, and feature engineering concepts, and Gemini helped write, structure, and debug the code.
- **AI chat links:** [Optional link(s)]
