# import streamlit as st
# import pandas as pd
# import altair as alt
# st.header("Our First Application")
# st.write("Hello world")
# st.write("^^^^^^^^^^^^^^")
# def load(url):
#     return pd.read_json(url)

# df = load("https://cdn.jsdelivr.net/npm/vega-datasets@2/data/penguins.json")
# if st.checkbox("Show Raw Data:"):
#     st.write(df)



# st.header("Novel Coronavirus 2019 ")
# st.write("_ By MR Team")

# confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
# deaths_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
# recoveries_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
# confirmed_df = confirmed_df.drop("Province/State",axis=1)

# confirmed_df = confirmed_df.dropna()
# deaths_df = deaths_df.drop("Province/State",axis=1)
# deaths_df = deaths_df.dropna()
# recoveries_df.drop("Province/State",axis=1)
# recoveries_df = recoveries_df.dropna()

# picked= alt.selection_single(empty="none",on="mouseover")
# picked= alt.selection_interval()

# #input_dropdown= alt.binding_select(options=["Adelie","Chinstrap","Gentoo"],name="Select a species")
# #picked= alt.selection_single(encodings=["color"],bind=input_dropdown)

# st.write(confirmed_df)
# scatter= alt.Chart(df).mark_point().encode(
#     alt.X("Flipper Length (mm)",scale=alt.Scale(zero=False)),
#     alt.Y("Body Mass (g)",scale=alt.Scale(zero=False)),
#     #alt.Color("Species"),
#     color=alt.condition(picked,"Species",alt.value("lightgrey"))
# ).add_selection(picked).interactive()

# st.write(scatter)

# import altair as alt
# from vega_datasets import data

# source = alt.topo_feature(data.world_110m.url, 'countries')

# base = alt.Chart(source).mark_geoshape(
#     fill='#666666',
#     stroke='white'
# ).properties(
#     width=300,
#     height=180
# )

# projections = ['equirectangular']
# charts = [base.project(proj).properties(title=proj)
#           for proj in projections]

# c= alt.concat(*charts, columns=2)
# st.write(c)

# min_weight= st.slider("Minimum Body Mass",2500,6500)
# st.write(min_weight)

# scatter_filter= scatter.transform_filter(f"datum['Body Mass (g)'] >= {min_weight}")
# st.write(scatter_filter)

# ##########################3
# import altair as alt
# from vega_datasets import data

# # Data generators for the background
# sphere = alt.sphere()
# graticule = alt.graticule()

# # Source of land data
# source = alt.topo_feature(data.world_110m.url, 'countries')


# # Layering and configuring the components
# earth= alt.layer(
#     alt.Chart(sphere).mark_geoshape(fill='lightblue'),
#     alt.Chart(graticule).mark_geoshape(stroke='white', strokeWidth=0.5),
#     alt.Chart(source).mark_geoshape(fill='ForestGreen', stroke='black')
# ).project(
#     'naturalEarth1'
# ).properties(width=600, height=400).configure_view(stroke=None)

# points = alt.Chart(confirmed_df).mark_circle().encode(
#     longitude='long:Q',
#     latitude='lat:Q',
    
#     size=alt.value(10)
# )
# st.write(points)



import streamlit as st
import pandas as pd
import altair as alt
st.header("How is the weather in Seattle?")
st.write("~ By Mitali Potnis and Razik Singh Grewal")


st.write("Hi everyone!👋🏻")
st.write("Meet Taylor 👦🏻")
st.write("Ever since he watched a documentary on Seattle, Washington, Taylor has always wanted to visit the city. 🌆🌉")
st.write("But in order to do so, he has to preplan his trip since he needs to take a leave from his office.")
st.write("Today we will help him decide what to pack based on the weather in Seattle and assist him in knowing which months are the best to visit Seattle based on his preferences.")

df= pd.read_csv('https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv')
st.write("For this task, we will be utilizing the Seattle Weather dataset that consists of weather statistics about Precipitation, Maximum and Minimum temperature, Wind, and type of weather (Fog, Sun, Rain, Snow, Drizzle) for the years ranging 2012 - 2015.")
st.write("Let us have a look at this dataset!")
st.write(df)
st.write("As seen, it comprises the weather information for each day and month over the four years ie. 1461 total entries.")
st.write("Now let us look at the description of each column of this dataset to get a better understanding.")
st.write("- date : gives us the date of the weather observation,")
st.write("- precipitation : gives us the amount of precipitation,")
st.write("- temp_max : gives us the maximum temperature in degree Celsius,")
st.write("- temp_min : gives us the minimum temperature in degree Celsius,") 
st.write("- wind : gives us the average of speed of wind (in m/s),")
st.write("- weather : gives us the weather description") 
df["year"] =  pd.DatetimeIndex(df['date']).year
df["avg_temp"] = df["temp_min"] + df["temp_max"]
#Plot 1
st.write("Now that we have seen the dataset, let us carry out some data visualization to help our friend Taylor.")
st.write("Taylor want to know what things does he need to carry with him to Seattle depending on different months.")
st.write("Let us plot a scatter plot to observe how the average temperature of Seattle changes over the Year. The sizes of the scatter points is decided based on the amount of precipitation observed on the date.")
st.write("We have also plotted a horizontal bar chart in order to observe the frequency distribution of the weather for the data chosen in the scatter plot.")
year_dropdown = alt.binding_select(options=[2012,2013,2014,2015],name="Pick a Year")
year_selection = alt.selection_single(fields=['year'], bind=year_dropdown)
scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                  range=['#FF0000', '#808080', '#7FFFD4', '#6495ED', '#FFE4C4'])
color = alt.Color('weather:N', scale=scale, title="Weather Observed :")
choose = alt.selection_interval(encodings=['x'])
year_dropdown = alt.binding_select(options=[2012,2013,2014,2015],name="Pick a Year")
year_selection = alt.selection_single(fields=['year'], bind=year_dropdown)
click_change = alt.selection_multi(encodings=['color'])

scatter_weather = alt.Chart().mark_point().encode(
    alt.X('monthdate(date):T', title='Date in months'),
    alt.Y('avg_temp:Q',title='Average Temperature Daily (in Degree Celsius)',
    ),
    color=alt.condition(choose, color, alt.value('lightgray')),
    size=alt.Size('precipitation', type="quantitative", scale=alt.Scale(range=[7, 200])),
    tooltip = ["avg_temp","weather"]
).add_selection(
    choose 
).transform_filter(
    click_change 
).properties(
    width=650,
    height=400
)

#plot 2

freq_column_chart = alt.Chart(df).mark_bar().encode(
     alt.X('count():Q', title='Frequency of observations'),
     alt.Y('weather:N', title='Observed Weather'),
     color=alt.condition(click_change, color, alt.value('yellow')),
).transform_filter(
     choose
).properties(
    width=650,
    height = 150
).add_selection(
    click_change 
)

both=alt.vconcat(
    scatter_weather,freq_column_chart,data=df,title="Weather in Seattle over the Years 2012 2015"
)
st.write(both)




#3 chart now:
st.header("Min Temp Stats")
scatter= alt.Chart(df).mark_bar().encode(
    alt.X("count()",scale=alt.Scale(zero=False)),
    alt.Y("weather:N",scale=alt.Scale(zero=False)),
    alt.Color("weather")
    #color=alt.condition(picked,"Species",alt.value("lightgrey"))
)

min_temp= st.slider("Minimum Temperature",-7.1,18.13)
st.write(min_temp)

scatter_filter= scatter.transform_filter(f"datum['temp_min'] >= {min_temp}")
st.write(scatter_filter)






#4 chart now
#picked= alt.selection_single(empty="none",on="mouseover")
# picked= alt.selection_interval()


# scatter= alt.Chart(df).mark_point().encode(
#     alt.X("temp_max",scale=alt.Scale(zero=False)),
#     alt.Y("temp_min",scale=alt.Scale(zero=False)),
#     #alt.Color("weather"),
#     color=alt.condition(picked,"weather",alt.value("lightgrey"))
# ).add_selection(picked).interactive()

# st.write(scatter)

violin= alt.Chart(df).transform_density(
    'wind',
    as_=['wind', 'density'],
    #extent=[5, 50],
    groupby=['weather']
).mark_area(orient='horizontal').encode(
    y='wind:Q',
    color='weather:N',
    tooltip = ["wind"],
    x=alt.X(
        'density:Q',
        stack='center',
        impute=None,
        title=None,
        axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
    ),
    column=alt.Column(
        'weather:N',
        header=alt.Header(
            titleOrient='bottom',
            labelOrient='bottom',
            labelPadding=0,
        ),
    )
).properties(
    width=100
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
).interactive()
st.write(violin)

#5 plot now


year_dropdown = alt.binding_select(options=[2012,2013,2014,2015],name="Select a Year")
year_selection = alt.selection_single(fields=['year'], bind=year_dropdown)
pie_df = df.groupby(['year', 'weather'],as_index = False).size()
fig_category_percent=alt.Chart(pie_df).mark_arc().encode(
     theta=alt.Theta(field="size", type="quantitative"),
     color=alt.Color(field="weather", type="nominal")).add_selection(year_selection).transform_filter(
    year_selection
)

st.write(fig_category_percent)


# bg = alt.Chart(df).encode(
#     alt.X('date:T', axis=alt.Axis(title="Date"))
# )


# line2 = bg.mark_line(stroke='#5276A7', interpolate='monotone').encode(
#     alt.Y('temp_max',
#           axis=alt.Axis(title='Maximum Temperature')),
# )

# final=alt.vconcat(
#     bg,line2,data=df,title="Seattle Temperature Distribution over the years"
# )
# st.write(final)

# st.write(confirmed_df)
# scatter= alt.Chart(df).mark_point().encode(
#     alt.X("Flipper Length (mm)",scale=alt.Scale(zero=False)),
#     alt.Y("Body Mass (g)",scale=alt.Scale(zero=False)),
#     #alt.Color("Species"),
#     color=alt.condition(picked,"Species",alt.value("lightgrey"))
# ).add_selection(picked).interactive()

# st.write(scatter)
