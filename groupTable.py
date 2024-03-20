import pandas as pd

def getTable(df, vf, rows, columns):
    dt = df.groupby([rows, columns], observed=True)[rows].value_counts().unstack(columns).fillna(0)
    vrows = vf[rows].dropna()
    vcolumns = vf[columns]
    dt2 = pd.DataFrame()
    dt = dt.set_index(vrows)
    i = 0
    for c in dt.columns:
        dt2.insert(i, vcolumns[i], dt.get(c).tolist(), True)
        i += 1
    
    return dt2.set_index(vrows)