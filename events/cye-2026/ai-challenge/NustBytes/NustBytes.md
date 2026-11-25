# Team:  NustBytes

All this info would facilitate the judges to rank you but is optional

- Members: Anum Fatima, Raihana Walizada, Fatima Sajjad
- Kaggle team name: [NustBytes]
- Final Kaggle public score: [0.947]

## Approach
ExtraTrees classifier (500 trees, class-balanced weights) on the four sensor readings plus engineered features. I dropped `day` and `id` as inputs, since the final test comes from different days. I validated by holding out whole days (train on some days, score on days the model never saw) instead of random splits, because a random split gave a misleadingly high 0.99. ExtraTrees was chosen because its random splits regularize well: it scored about 0.85 on held-out days, vs about 0.64 for LightGBM, which overfit to the specific training days.

## Features you made
- power (voltage × current) and efficiency (power / irradiance): healthy panels convert light to power at a steady rate, and faults break that.
- current / irradiance: current should scale with sunlight, so a low ratio signals shading.
- resistance (voltage / current): separates open circuit (huge) and short circuit (tiny).
- temperature-adjusted voltage: voltage drops as panels heat up, so this stops hot days from looking like faults.
- healthy-panel residuals (current and voltage vs what a normal panel gives at the same irradiance and temperature, learned from normal rows only): faults show up as a clear gap from expected.

## Results
- Your own validation score: 0.848 macro-F1 on held-out days (Kaggle public score: 0.947)
- Which faults your model confuses most, and why: normal vs shading, which accounts for about 91% of all errors. About 46% of shading rows have current that looks normal for their irradiance (75-99% below 400 W/m², where both are near zero), so they can't be told apart. Degradation is the next weakest (F1 about 0.58) because it looks like normal at high irradiance, differing only by a small voltage drop. Open circuit (0.996) and short circuit (0.976) are easy because their voltage and current readings are extreme.

## AI and tools used
- claude 
