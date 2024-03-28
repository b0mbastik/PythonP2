import pandas as pd


def getTable(df, vf, rows, columns):
    """
    Returns a groupby table by taking dataframes containing the census and
    census variable names, and the variable names to use as rows and columns

    Uses value_counts on the rows so that they represented the number of
    records, and unstack to format the given variable for the columns properly
    Using the data from the groupby table, another dataframe table is created
    with the same values but column names modified to match the textual
    represenations of the alphanumeric values
    """
    if (rows in df and columns in df and rows in vf and columns in vf) == False:
        raise ValueError("Invalid variable data given.")
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
