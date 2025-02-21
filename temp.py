import pandas as pd

df = pd.DataFrame(
    {"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]},
    index=pd.MultiIndex.from_tuples([("d", 1), ("d", 2), ("e", 2)], names=["n", "v"]),
)
