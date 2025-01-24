from pathlib import Path
import pandas as pd

data_path = Path(__file__).parent

df = pd.read_csv(data_path / "athlete_events.csv")

print(df.head())
