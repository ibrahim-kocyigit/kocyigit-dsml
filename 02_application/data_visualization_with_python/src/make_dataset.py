import pandas as pd
from pathlib import Path

script_dir = Path(__file__).resolve()
data_path = script_dir.parent.parent / "data" / "external" / "Canada.xlsx"

df = pd.read_excel(
    data_path,
    sheet_name="Canada by Citizenship",
    skiprows=range(20),
    skipfooter=2,
)

df = df.drop(columns=["Type", "DEV", "Coverage", "AREA", "REG", "DevName"], axis=1)

df = df.rename(
    columns={"OdName": "country", "AreaName": "continent", "RegName": "region"}
)

df["total"] = df.loc[:, 1980:2013].sum(axis=1)

df.set_index("country")

df.to_pickle(
    script_dir.parent.parent / "data" / "interim" / "immigration_to_canada_01.pkl"
)
