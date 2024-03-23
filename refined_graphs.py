import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Returns a tuple containing a column with the value counts of the column containing alphanumeric codes sorted in order of index name and the column containing the textual representation of the codes as a tuple
#Checks if both columns are the same length, as there should be a textual representation for every alphanumeric code
def get_sorted_columns(rc, vc):
    if (len(rc.dropna().unique()) != len(vc.dropna())):
        raise ValueError(f"Provided columns for codes and their corresponding variable names are not the same length.\nColumn 1: {len(rc.dropna().unique())}\nColumn 2: {len(vc.dropna())}")
    return (rc.value_counts().sort_index(), vc.dropna())

#Creates a bar chart using the value counts of a given census dataframe variable as the y axis, and the x axis labels as the textual representation of the variable's codes
#Calls get_sorted_columns() to return a tuple containing the sorted value counts of the variable, and to check that there is a textual representation for every code
#Graph is saved into the images directory using savefig()
def get_bar_chart(refinedColumn, variableColumn, x, y, title, name):
    c = get_sorted_columns(refinedColumn, variableColumn)
    fig, ax = plt.subplots()
    ax.bar(c[1], c[0], color ='maroon', width = 0.4)
    plt.xlabel(x, fontsize=15, labelpad=15)
    plt.ylabel(y, fontsize=15, labelpad=15)
    fig.set_figwidth(7)
    fig.set_figheight(7)
    fig.autofmt_xdate()
    ax.set_title(title, pad=25, fontsize=25)
    plt.savefig(("images/" + name), bbox_inches='tight')

#Creates a pie chart using the value counts of a given census dataframe variable as the sectors of the pie, and the labels as the textual representation of the variable's codes
#Calls get_sorted_columns() to return a tuple containing the sorted value counts of the variable, and to check that there is a textual representation for every code
#Graph is saved into the images directory using savefig()
def get_pie_chart(refinedColumn, variableColumn, title, legend_title, name):
    c = get_sorted_columns(refinedColumn, variableColumn)
    fig, ax = plt.subplots(figsize=(4,2))
    ax.pie(c[0], labels = c[1], radius = 4, autopct='%1.1f%%')
    ax.set_title(title, pad=220, fontsize=25)
    plt.legend(title=legend_title, loc='center right', bbox_to_anchor=(6,1), fontsize='xx-large')
    plt.savefig(("images/" + name), bbox_inches='tight')

#Creats a set of bar charts from a groupby table by iterating through every column and making a bar chart for each one
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

#Creats a 3D bar chart from a groupby table by iterating through each column in the table, adding the values to the 3D bar chart and then using axis functions to assign relevant values and settings to the axis labels
def get_table_3d_chart(dt, xlabel, ylabel, zlabel, width, height):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    i = (len(dt.columns)-1)
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
    ax.set_zlabel(zlabel, labelpad=40, fontsize=25)

#Automatically generates the bar and pie charts detailed in the basic specification
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