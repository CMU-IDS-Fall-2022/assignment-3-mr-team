# Done by Mitali Potnis (mpotnis@andrew.cmu.edu) & Razik Singh Grewal (rgrewal@andrew.cmu.edu)

import streamlit as st
import pandas as pd
import altair as alt
st.title("How is the weather in Seattle?")
st.write("**********************************************************************************************************************")
st.write("~ By Mitali Potnis and Razik Singh Grewal")
st.write("**********************************************************************************************************************")

st.header("Hi everyone!👋🏻")
st.header("Meet Taylor 👦🏻")
st.write("Ever since he watched a documentary on Seattle, Washington, Taylor has always wanted to visit the city. 🌆🌉")
st.write("But in order to do so, he has to preplan his trip since he needs to take a leave from his office.")
st.write("Taylor is very picky in terms of the weather. He likes the sun and hates windy days. Today we will help him decide what to pack based on the weather in Seattle and assist him in knowing which months are the best to visit Seattle based on his preferences to make his trip experience amazing!")

df= pd.read_csv('https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv')
st.write("For this task, we will be utilizing the Seattle Weather dataset that consists of weather statistics about Precipitation, Maximum and Minimum temperature, Wind, and type of weather (Fog, Sun, Rain, Snow, Drizzle) for the years ranging 2012 - 2015.")
st.write("Let us have a look at this dataset!")
st.header("The Dataset:")
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
st.header("What things should Taylor carry for his trip to Seattle based on the weather commonly observed?")
st.write("Taylor want to know what things does he need to carry with him to Seattle depending on different months.")
st.write("Let us plot a scatter plot to observe how the average temperature of Seattle changes over the Year. The sizes of the scatter points is decided based on the amount of precipitation observed on the date.")
st.write("We have also plotted a horizontal bar chart in order to observe the frequency distribution of the weather for the data chosen in the scatter plot.")
st.write("*********************************************************************************************************************************")
st.write("Instructions:")
st.write("Feel free to hover over the data points and select the columns of the column bar chart or choose a certain area on the scatter plot using ur mouse as per your requirement!")
st.write("*********************************************************************************************************************************")
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
    alt.Y('avg_temp:Q',title='Average Temperature (in Degree Celsius)'
    ),
    
    color=alt.condition(choose, color, alt.value('lightgray')),
    size=alt.Size('precipitation:Q', scale=alt.Scale(range=[7, 200])),
    tooltip = ["avg_temp","weather"]
).add_selection(
    choose 
).transform_filter(
    click_change 
).properties(
    width=650,
    height=400,
    title = "Average Daily Temperature"
)

#plot 2

freq_column_chart = alt.Chart(df).mark_bar().encode(
     alt.X('count():Q', title='Frequency of observations'),
     alt.Y('weather:N', title='Observed Weather'),
     color=alt.condition(click_change, color, alt.value('yellow')),
     tooltip = ["weather","count()"]
).transform_filter(
     choose
).properties(
    width=650,
    height = 150,
    title = "Frequency Distribution of the Weather observations"
).add_selection(
    click_change 
).interactive()

both=alt.vconcat(
    scatter_weather,freq_column_chart,data=df,title="Weather in Seattle over the Years 2012 - 2015"
).configure_title(fontSize=27).configure_axis(
    labelFontSize=18,
    titleFontSize=18
).configure_legend(titleColor='yellow', titleFontSize=18) 
st.write(both)
st.write("Observations:")
st.write("Looking at the two plots, we can see that if Taylor visits Seattle during the months from January to April, he will majorly experience rainy days with some sunny days and ocassional snowy or foggy days. It will be best if he carries a raincoat or an umbrella☔. The temperature in such months is on an average around 10 to 25 degree Celsius.")
st.write("If Taylor ends up deciding to visit Seattle in the months April to July, it is advisable that he continues to carry an umbrella since rainy days constitute the second most oobserved weather. Along with umbrella, Taylor needs to pack light clothes since he will majorly face sunny days ☀️. The temperature is seen to rise in these months with temperature commonly falling in the range of 20 to 35 degree Celsius. The probability that it will snow or be foggy is quite less in such months so he can choose not to pack a winter coat or a thick jacket.")
st.write("The months of July to October (especially August and July) are some of the hottest months 🥵 with the highest temperature observed in such months being 53.4C and it is advisable for Taylor to carry both an umbrella as well as light clothes since such months mostly face sunny and rainy days.")
st.write("Finally, during the months from September to December the temperature begins to fall down with rainy days being observed the most and sunny days being the second highest observed days. If Taylor wants to visit Seattle during November and December, it will be beneficial for him to carry a winnter coat since these months reach some of the lowest temperatures.❄️")
#3 chart :
st.header("What Minimum Temperature should Taylor expect in Seattle?")
st.write("Now, Taylor wants to know to at what minimum temperature do the snow, drizzle, and fog weather stop to appear, since he wants to be sure what to expect in terms of Minimum Temperature of the day.")
st.write("For this task, we plot a stacked vertical bar chart for observing the the count of observations for each weather controlled by the Minimum Temperature in degree Celsius.")

st.write("*********************************************************************************************************************************")
st.write("Instructions:")
st.write("You can move the slider to control the Minimum Temperature!🎚️ The stacked bar chart will display the columns having observations above the Minimum Temperature chosen.")
st.write("*********************************************************************************************************************************")

scatter= alt.Chart(df).mark_bar().encode(
    alt.X("weather:N",scale=alt.Scale(zero=False),title="Weather Type"),
    alt.Y("count()",scale=alt.Scale(zero=False),title="Count of Weather observations"),
    alt.Color("year",scale=alt.Scale(zero=False)),
    tooltip = ["weather","count()","year"]
).properties(
    width=600,
    height = 500,
    title = "Weather observations on the basis of Minimum Temperature"
).configure_title(fontSize=20).configure_axis(
    labelFontSize=18,
    titleFontSize=18
).configure_legend(titleColor='yellow', titleFontSize=18)

min_temp= st.slider("Minimum Temperature",-7.1,18.13)

scatter_filter= scatter.transform_filter(f"datum['temp_min'] >= {min_temp}")
st.write(scatter_filter)
st.write("Observations:")
st.write("From the plot we can assert that once the minimum temperature goes above 5.59C it stops snowing or it usually does not snow in Seattle. Thus, if Taylor wants to observe snow🌨️, he should expect atleast a Minimum Temperature to be 5.6 degree Celsius.")
st.write("The drizzle weather stops to get observed after a Minimum Temperature around 16.12C. Thus on a day when it is drizzling, Taylor can expect the Minimum Temperature to be up to 16.12C at maximum.")
st.write("The foggy weather does not get observed once Minimum Temperature crosses 17.8C. Thus on a foggy day the maximum temperature that Taylor can face in Seattle is17.8 degree Celsius.")
st.write("One interesting observation is that Taylor will still have a chance experience Sunny Days irrespective of the Minimum Temperature. Which is great because Taylor loves the sun!🌞🌞")

#4 chart now
st.header("Which weather is the windiest?🍃")
st.write("Taylor does not like windy days 🌬️. He wants to know how windy is it going to be during different weather observations so that he can avoid visiting Seattle in those months wherein such observations with high wind sspeed occur most frequently.")
st.write("We have employed a box plot to lok at the maximum, minimum and the median values of average speed of the wind for each weather type.")
st.write("*********************************************************************************************************************************")
st.write("Instructions:")
st.write("Do try choosing a weather using the rectangular buttons on the left! Each chosen weather will display its corresponding boxplot.")
st.write("*********************************************************************************************************************************")

df2 = pd.DataFrame({'weather':['sun', 'fog', 'drizzle', 'rain', 'snow']})
selection = alt.selection_multi(fields=['weather'])
color = alt.condition(selection, alt.Color('weather:N'), alt.value('lightgray'))
weather_selection = alt.Chart(df2).mark_rect().encode(y='weather', color=color).add_selection(selection)
boxplot = alt.Chart(df).mark_boxplot(size=40).encode(
	alt.Y('wind:Q'),
    alt.X('weather:N',scale=alt.Scale(zero=False)),
    color=("weather:N")
).properties(width=550,height=500).transform_filter(selection).interactive()

both2=alt.vconcat(
    weather_selection,boxplot,data=df,title="Average Speed of Wind in different Weathers"
).configure_title(fontSize=20).configure_axis(
    labelFontSize=18,
    titleFontSize=18
).configure_legend(titleColor='yellow', titleFontSize=18) 
st.write(both2)
st.write("Observations:")
st.write("As observed, during drizzle days, the wind speed is quite less ie. between 0.6 to 4.7 m/s, with its median value being 2.1 m/s.")
st.write("The wind speed increases during Foggy days wherein it lies between 0.8 to 6.6 m/s and its median speed being 2.4 m/s")
st.write("During Rainy days, the wind spped even increases more to a range between 0.5 to 9.5 m/s with a 3.4 m/s median speed of wind.")
st.write("Compared to rainy days, snowy days tend to have higher average speed of wind with a 4.95 m/s median wind speed and the wind usually being in between the range 1.6 to 7 m/s. ")
st.write("Finally, for sunny days, the wind speed is again low with a median speed of 2.8 m/s.")
st.write("From this, we can deduce that if Taylor wants to avoid windy days, he needs to visit Seattle in the months wherein there is no snowfall. From the previous plots, we observed that the phenomena of snow is less commonly observed during the months from April to November. So this time is a good fit for Taylor to visit Seattle!")

#5 plot now

st.header("Does it snow much in Seattle?")
st.write("Oh no! we just got to know from the above chart that Taylor must not visit Seattle during the snowy months. Taylor is sad because his friend told him it is pretty snowy in Seattle! ☹️☹️")
st.write("We will now be seeing if this fact is true or not and if it is false, is there a good chance that Taylor can visit Seattle based on the percentage of other weather observations?")
st.write("To answer this question, we have employed a pie chart which allows us to compare the quantity of different weather observations.")
st.write("*********************************************************************************************************************************")
st.write("Instructions:")
st.write("Try playing around with choosing different Year values from the dropdown menu to observe the pie distribution for different years.")
st.write("*********************************************************************************************************************************")

year_dropdown = alt.binding_select(options=[2012,2013,2014,2015],name="Select a Year")
year_selection = alt.selection_single(fields=['year'], bind=year_dropdown)
pie_df = df.groupby(['year', 'weather'],as_index = False).size()
pie_chart=alt.Chart(pie_df).mark_arc().encode(
     theta=alt.Theta(field="size", type="quantitative"),
     color=alt.Color(field="weather", type="nominal")).add_selection(year_selection).transform_filter(
    year_selection
)
st.write(pie_chart)
st.write("Observations:")
st.write("After looking at the pie chart for different years, we can see that snowy days constitute one of the smallest if not least percentage in terms of observations. One interesting observation is that it did not even snow in 2015! So Taylor should be good to visit Seattle since he will have atleast some months wherein it will not snow and the amount of snowy days is less throughout the year.")

st.write("Awesome Job! Now Taylor knows what clothes to carry on his vacation and can easily choose what months are the best to visit the city of Seattle!")

