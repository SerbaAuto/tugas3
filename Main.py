import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
from bokeh.plotting import figure
import pydeck as pdk
import graphviz

# 1.  Write and Magic
st.write('''
# 1. Write and Magic

This is a _magic_.
''')


# 2.  Text Element
st.write('''
# 2. Text Elements
''')
         
st.markdown(" 2a. Streamlit *_Mark_down*")
st.markdown("Warna :red[Merah] dan Biru bold **:blue[Biru]**.")

st.title("2b. Streamlit Title")

st.header("2c. Header")
st.subheader("2d. Sub Header")
st.caption("2e. Caption")

#2f. st.code
code = '''
    def HelloWorld():
        print("2f. Streamlit Code")
        print("Hello World")
'''

st.code(code,language="python")

st.text("2g. Streamlit Text")

st.write('''
# 2h. Streamlit Latex
''')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k =  a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


# 3.  Data Display Element
st.write('''
# 3a. Streamlit Dataframe
''')
df = pd.DataFrame(
   np.random.randn(50, 3),
   columns=('col %d' % i for i in range(3)))

st.dataframe(df)
st.write('''
# 3b. Streamlit Table
''')
st.table(df)

st.write('''
# 3c. Strealit Metric
''')

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col3.metric(label="Humidity",value="86%",delta="4%",delta_color="inverse")

st.write('''
# 3d. Strealit json
''')

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

# 4.  Chart Element

st.write('''
# 4a. Strealit Line Chart
''')
st.line_chart(df)

st.write('''
# 4b. Strealit Area Chart
''')
st.area_chart(df)

st.write('''
# 4c. Strealit Bar Chart
''')
st.bar_chart(df)

st.write('''
# 4d. Strealit Pyplot
''')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.write('''
# 4e. Streamlit Altair
''')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

st.write('''
# 4f. Streamlit Vega Lite Chart
''')

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

st.write('''
# 4f. Streamlit Plotly Chart
# ''')

# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)


st.write('''
# 4g. Streamlit Bokeh Chart
''')
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

st.write('''
# 4h. Streamlit Pydeck Chart
''')

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
st.write('''
# 4i. Streamlit Graphviz Chart
''')

graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

st.write('''
# 4j. Streamlit Map Chart
''')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
# 5.  Input Widget
st.header("5 Input Widget")
st.write('''
# 5a. Streamlit Button
''')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.header("5b. Streamlit Experimental_data_editor")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 3, "is_widget": True},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

edited_df = st.experimental_data_editor(df)


favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


st.header("5c. Streamlit Button Download ")
csv = pd.read_csv(st.secrets['public_gsheet_csv']).to_csv()

st.download_button(label="Download File Data",data=csv,file_name="data.csv",mime='text/csv')

st.header("5d. Streamlit CheckBox ")
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

st.header("5e. Streamlit Radio ")
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

st.header("5e. Streamlit Select Box ")
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.header("5f. Streamlit Multi Select ")
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.header("5g. Streamlit Slider ")
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.header("5g. Streamlit Select Slider ")
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

st.header("5h. Streamlit Text Input ")
text = st.text_input('Title Write', 'Text')
st.write('Your Text is', text)

st.header("5i. Streamlit Number Input ")
number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.header("5j. Streamlit Text Area ")
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', run_sentiment_analysis(txt))

# 6.  Media Element
# 7.  Layout and Container
# 8.  Status Element
# 9.  Control Flow
# 10. Utilities
    