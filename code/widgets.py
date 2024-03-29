import ipywidgets as ipw
import matplotlib.pyplot as plt
import data_refinement as dr
import pandas as pd


df = dr.refine_dataset(dr.read_data('../data/census2011.csv'))
variable_data = pd.read_csv('../data/variables.csv')
x_axis_descriptions = {}

# Iterate over the rows of the variable data
for _, row in variable_data.iterrows():
    variable = row['Variable']
    code = row['Code']
    description = row['Description']
    
    # Check if the variable is already in the dictionary
    if variable in x_axis_descriptions:
        x_axis_descriptions[variable][code] = description
    else:
        x_axis_descriptions[variable] = {code: description}

# Define the widgets
region_widget = ipw.Dropdown(
    options=df['Region'].unique(),
    description='Region:',
    disabled=False,
)

x_axis_widget = ipw.Dropdown(
    options=[option for option in df.columns if option not in ['Person ID', 'Region']],
    description='X-Axis:',
    disabled=False,
)

# Create the output widgets for the plot and the text
plot_output = ipw.Output()
text_box = ipw.Output()

def update_plot(change):
    with plot_output:
        plot_output.clear_output(wait=True)
        plt.clf()
        filtered_data = df[df['Region'] == region_widget.value]
        value_counts = filtered_data[x_axis_widget.value].value_counts().sort_index()
        value_counts.plot(kind='bar')
        plt.title(f"Distribution of {x_axis_widget.value}")
        plt.xlabel(x_axis_widget.value)
        plt.xticks(rotation=0)
        plt.ylabel('Count')
        plt.show()
    
    with text_box:
        text_box.clear_output(wait=True)
        if x_axis_widget.value in x_axis_descriptions:
            description = "\n".join(f"{code}: {desc}" 
                                    for code, desc in x_axis_descriptions[x_axis_widget.value].items())
            print(description)

# Set up the observer for the widgets
region_widget.observe(update_plot, names='value')
x_axis_widget.observe(update_plot, names='value')

# Initial call to update the plot
update_plot(None)

def create_plot():
    # Layout and display
    box_layout = ipw.Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
    left_box = ipw.VBox([region_widget, x_axis_widget, plot_output])
    right_box = ipw.VBox([text_box])
    hbox = ipw.HBox([left_box, right_box], layout=box_layout)
    return hbox
