#!/usr/bin/env python
# coding: utf-8

# In[251]:


#importing Libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[252]:


#Reading CSV File
data = pd.read_csv(r'D:\project 2\lung cancer data.csv')
#returning the first 10 rows of the data
data.head(10)


# In[253]:


data.describe()


# In[254]:


data.shape


# In[255]:


data.info()


# In[256]:


#replace 2s with 1 and 1s with 0
data = data.replace({1:0, 2:1})
data.head(5)


# In[257]:


below_50_age = data[data['AGE'] <= 50]
below_50_age


# In[258]:


fig = px.histogram(data, x="AGE", color="GENDER", barmode="group", title="<b>Count of Ages by Gender</b>",opacity = 0.7, height = 600,
                   color_discrete_sequence=["#fe5454", "#54c5fe"])
fig.update_layout(xaxis_title="Age", yaxis_title="Count")
fig.update_layout(title={'x': 0.5})

fig.show()


# In[259]:


# Replace values for Alcohol Consumption
data['ALCOHOL CONSUMING'] = data['ALCOHOL CONSUMING'].replace({0: 'NO', 1: 'YES'})
fig_alcohol = px.histogram(
    data,
    x="AGE",
    color="ALCOHOL CONSUMING",
    facet_row = "ALCOHOL CONSUMING",
    title="<b>Count of Ages by Alcohol Consumption</b>",
    opacity=0.6,
    height=600,
    color_discrete_sequence=["#6e2c00", "#2ecc71"]
)

fig_alcohol.update_layout(xaxis_title="Age", yaxis_title="Count")
fig_alcohol.update_layout(title={'x': 0.5})

fig_alcohol.show()

# Replace values for Fatigue
if 'COUGHING' in data.columns:  # Check if the FATIGUE column exists
    data['COUGHING'] = data['COUGHING'].replace({0: 'NO', 1: 'YES'})
    fig_fatigue = px.histogram(
        data,
        x="AGE",
        color="COUGHING",
        facet_row = "COUGHING",
        title="<b>Count of Ages by COUGHING</b>",
        opacity=0.6,
        height=600,
        color_discrete_sequence=["#5dade2", "#5b2c6f"]
    )

    fig_fatigue.update_layout(xaxis_title="Age", yaxis_title="Count")
    fig_fatigue.update_layout(title={'x': 0.5})

    fig_fatigue.show()
else:
    print("Column 'COUGHING' not found in the DataFrame.")


# In[260]:


fig = px.histogram(
    data, 
    x="AGE",                # Counts ages
    color="GENDER",         # Color by gender
    facet_col="LUNG_CANCER",
    title="<b>Count of Ages by Gender and Lung Cancer Status</b>",
    opacity=0.7,
    height=500,
    barmode="group",
    color_discrete_sequence=["#000000", "#f05fff"])

# Update layout for better clarity
fig.update_layout(
    xaxis_title="Age",
    yaxis_title="Count",
    legend_title="Gender"
)
fig.update_layout(title={'x': 0.5})

fig.show()


# In[261]:


data_encoded = pd.get_dummies(data, drop_first=True)

# Calculate correlation matrix
corr_matrix = data_encoded.corr()

# Create heatmap
fig = px.imshow(corr_matrix, 
                text_auto=True,         # Show values in each cell
                color_continuous_scale='RdBu_r',  # Color scale
                title="<b>Correlation Heatmap</b>")

# Customize layout
fig.update_layout(
    xaxis_title="Features",
    yaxis_title="Features",
    height = 1000
)
fig.update_layout(title={'x': 0.5})

fig.show()


# In[262]:


fig = px.histogram(
    data, 
    x="AGE",                # Counts ages
    color="GENDER",         # Color by gender
    facet_col="SMOKING",
    title="<b>Count of Ages by Gender and Smoking Status</b>",
    opacity=0.6,
    height=500,
    barmode="group",
    color_discrete_sequence=["#FF7F50", "#800080"]
)

# Update layout for better clarity
fig.update_layout(
    xaxis_title="Age",
    yaxis_title="Count",
    legend_title="Gender"
)

fig.update_layout(title={'x': 0.5})


fig.show()


# In[263]:


exclude_columns = ['LUNG_CANCER', 'AGE', 'GENDER']
health_factors = [col for col in data.columns if col not in exclude_columns]

# Step 2: Convert relevant columns to numeric, forcing errors to NaN
for factor in health_factors:
    data[factor] = pd.to_numeric(data[factor], errors='coerce')

# Step 3: Check unique values for 'Alcohol Consuming' and 'Coughing'
print("Unique values for Alcohol Consuming:", data['ALCOHOL CONSUMING'].unique())
print("Unique values for Coughing:", data['COUGHING'].unique())

# Step 4: Calculate average percentages using a for loop
average_percentages = {}

for factor in health_factors:
    average_percentages[factor] = data[factor].mean() * 100

# Step 5: Convert the average percentages to a DataFrame for better visualization
avg_df = pd.DataFrame(list(average_percentages.items()), columns=['Health Factor', 'Average Percentage'])

# Step 6: Create a pie chart to show average percentages of health factors
fig_avg = px.pie(avg_df, names='Health Factor', values='Average Percentage', 
                  title='<b>Average Percentage of Health Factors</b>', height = 650)

# Update pie chart layout with a legend title
fig_avg.update_traces(textinfo='percent+label')
fig_avg.update_layout(
    title={'x': 0.5},
    legend_title_text='Health Factors'  # Add legend title here
)

fig_avg.show()


# In[264]:


data['SHORTNESS OF BREATH'] = data['SHORTNESS OF BREATH'].replace({0: 'NO', 1: 'YES'})
# Create the histogram
fig = px.histogram(
    data,
    x="AGE",
    color="SHORTNESS OF BREATH",
    facet_row="SHORTNESS OF BREATH",
    title="<b>Count of Ages by Shortness Of Breath</b>",
    height=700,
    opacity=0.7,
    color_discrete_sequence=["#fe5454", "#54d5fe"]
)

# Update axis labels and legend title
fig.update_layout(
    yaxis_title="Count",
    xaxis_title="AGE",
    legend_title="Shortness Of Breath",
    title={'x': 0.5}
)


# In[265]:


# Plot the area chart with vertical orientation
fig = px.area(
    data,
    y="AGE",                # Set y-axis to "AGE" for vertical orientation
    color="LUNG_CANCER",    # Color by lung cancer status
    facet_row="LUNG_CANCER", # Keep facet_col for side-by-side layout
    title="<b>Count of Ages by Lung Cancer Status</b>",
    height=600,
    color_discrete_sequence=["#fe5454", "#54d5fe"]
)

# Update layout for clarity
fig.update_layout(
    yaxis_title="AGE",       # Label the y-axis as "Age"
    xaxis_title="Count",     # Label the x-axis as "Count"
    legend_title="Lung Cancer Status",
    title={'x': 0.5} )

fig.show()

data['SMOKING'] = data['SMOKING'].replace({0: 'NO', 1: 'YES'})

# Plot the area chart with vertical orientation
fig = px.area(
    data,
    y="AGE",                # Set y-axis to "AGE" for vertical orientation
    color="SMOKING",    # Color by lung cancer status
    facet_row="SMOKING", # Keep facet_col for side-by-side layout
    title="<b>Count of Ages by Smoking Status</b>",
    height=600,
    color_discrete_sequence=["#47d994", "#4642cb"]
)

# Update layout for clarity
fig.update_layout(
    yaxis_title="AGE",       # Label the y-axis as "Age"
    xaxis_title="Count",     # Label the x-axis as "Count"
    legend_title="Smoking Status",
    title={'x': 0.5} )

fig.show()

