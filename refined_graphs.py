import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

def get_sorted_arrays(refinedColumn, variableColumn):
    if (len(refinedColumn.dropna().unique()) != len(variableColumn.dropna())):
        raise ValueError(f"Provided columns for codes and their corresponding variable names are not the same length.\nColumn 1: {len(refinedColumn.dropna().unique())}\nColumn 2: {len(variableColumn.dropna())}")
    
    codes = np.sort(list(map(str, refinedColumn.unique())))
    columnDict = dict(zip(codes, variableColumn.dropna()))
    sorted_column = json.loads(refinedColumn.value_counts().to_json())
    arr = []

    for k in sorted_column.keys():
        arr.append(columnDict[k])

    return (arr,sorted_column)

def get_bar_chart(refinedColumn, variableColumn, x, y, title, name):
    fig, ax = plt.subplots()
    arrTuple = get_sorted_arrays(refinedColumn, variableColumn)
    arr = arrTuple[0]
    sorted_column = arrTuple[1]
    
    ax.bar(np.array(arr), np.array([*sorted_column.values()]), color ='maroon', width = 0.4)
    plt.xlabel(x, fontsize=15, labelpad=15)
    plt.ylabel(y, fontsize=15, labelpad=15)
    fig.set_figwidth(7)
    fig.set_figheight(7)
    fig.autofmt_xdate()
    ax.set_title(title, pad=25, fontsize=25)
    plt.savefig(("images/" + name), bbox_inches='tight')

def get_pie_chart(refinedColumn, variableColumn, title, legend_title, name):
    fig, ax = plt.subplots(figsize=(4,2))
    arrTuple = get_sorted_arrays(refinedColumn, variableColumn)
    arr = arrTuple[0]
    sorted_column = arrTuple[1]
    
    ax.pie(np.array([*sorted_column.values()]), labels = arr, radius = 4, autopct='%1.1f%%')
    ax.set_title(title, pad=220, fontsize=25)
    plt.legend(title=legend_title, loc='center right', bbox_to_anchor=(6,1), fontsize='xx-large')
    plt.savefig(("images/" + name), bbox_inches='tight')

def get_table_bar_chart(dt, xlabel, ylabel, width, height):
    fig, axs = plt.subplots(len(dt.columns))
    i = 0
    for c in dt.columns:
        axs[i].bar(dt[c].index, dt[c].tolist(), color ='maroon', width = 0.4)
        axs[i].set_title(c, pad = 10, fontsize = 20)
        axs[i].set_xlabel(xlabel, fontsize=15, labelpad=5)
        axs[i].set_ylabel(ylabel, fontsize=15, labelpad=10)
        fig.set_figwidth(width)
        fig.set_figheight(height)
        fig.tight_layout(pad=5)
        axs[i].set_xticks(axs[i].get_xticks())
        axs[i].set_xticklabels(dt[c].index, rotation=30)
        i += 1
    return axs

def get_table_3d_chart(dt, xlabel, ylabel, zlabel, width, height):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    i = len(dt.columns)
    for c in dt.columns:
        ax.bar(dt[c].index, dt[c].tolist(), i, zdir='y', alpha=0.8)
        i -= 1
    ax.set_yticks(ticks = np.arange(len(dt.columns)), labels=dt.columns[::-1], ha="left", rotation=-15, va="bottom", rotation_mode="anchor")
    ax.tick_params(axis='z', which='major', pad=10)
    fig.autofmt_xdate()
    fig.set_figwidth(width)
    fig.set_figheight(height)
    ax.set_xlabel(xlabel, labelpad=110, fontsize=25)
    ax.set_ylabel(ylabel, labelpad=110, fontsize=25)
    ax.set_zlabel(zlabel, labelpad=20, fontsize=25)

if __name__ == '__main__':

    df = pd.read_csv('refined_census2011.csv')
    plt.style.use('_mpl-gallery')
    plt.rcParams['legend.title_fontsize'] = 'xx-large'
    vf = pd.read_csv('census_variables.csv')

    get_bar_chart(df.Region, vf.Region, "Region", "Number of records", "Number of records per region", "region_bar_chart.png")
    get_bar_chart(df.Occupation, vf.Occupation, "Occupation", "Number of records", "Number of records per occupation", "occupation_bar_chart.png")
    get_pie_chart(df.Age, vf.Age, "Age Distribution", "Ages", "age_pie.png")
    get_pie_chart(df['Economic Activity'], vf['Economic Activity'], "Economic Activity", "Sectors", "economic_activity_pie.png")
    print("Graphs saved to images directory.")