import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
import spicy as s


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
''')

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])



# Plot!
st.plotly_chart(fig, use_container_width=True)

# 5.  Input Widget
# 6.  Media Element
# 7.  Layout and Container
# 8.  Status Element
# 9.  Control Flow
# 10. Utilities
