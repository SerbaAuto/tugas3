import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
from bokeh.plotting import figure
import pydeck as pdk
import graphviz
import datetime
from PIL import Image
import os
import time
st.set_page_config(
    page_title="Stevanus APP",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded"
    )

tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10=st.tabs(["Write & Magic","Text Element","Data Display","Chart","Input","Media","Layout","Status","Control Flow","Utilities"])


# Using "with" notation
with st.sidebar:
    st.title("Daftar Isi | Layout Sidebar & Expander")
    with st.expander("Nomor 1"):
        st.markdown("[1. Write and Magic](#1-write-and-magic)")
    with st.expander("Nomor 2"):
        st.markdown("[2. Text Elements](#2-text-elements)")
        st.markdown("[2b. Streamlit Title](#2b-streamlit-title)")
        st.markdown("[2c. Header](#2c-header)")
        st.markdown("[2d. Sub Header](#2d-sub-header)")
        st.markdown("[2e. Caption]")
        st.markdown("[2f. Code](#2f-code)")
        st.markdown("[2g. Streamlit Text](#2g-streamlit-text)")
        st.markdown("[2h. Streamlit Latex](#2h-streamlit-latex)")
    with st.expander("Nomor 3"):
        st.markdown("[3. Data Display Element](#3-data-display-element)")
        st.markdown("[3a. Streamlit Dataframe](#3a-streamlit-dataframe)")
        st.markdown("[3b. Streamlit Table](#3b-streamlit-table)")
        st.markdown("[3c. Strealit Metric](#3c-strealit-metric)")
        st.markdown("[3d. Strealit json](#3d-strealit-json)")
    with st.expander("Nomor 4"):
        st.markdown("[4. Chart Element](#4-chart-element)")
        st.markdown("[4a. Streamlit Line Chart](#4a-streamlit-line-chart)")
        st.markdown("[4b. Streamlit Area Chart](#4b-streamlit-area-chart)")
        st.markdown("[4c. Streamlit Bar Chart](#4c-streamlit-bar-chart)")
        st.markdown("[4d. Streamlit Pyplot](#4d-streamlit-pyplot)")
        st.markdown("[4e. Streamlit Altair](#4e-streamlit-altair)")
        st.markdown("[4f. Streamlit Vega Lite Chart](#4f-streamlit-vega-kite-chart)")
        st.markdown("[4g. Streamlit Plotly Chart](#4g-streamlit-plotly-chart)")
        st.markdown("[4h. Streamlit Bokeh Chart](#4h-streamlit-bokeh-chart)")
        st.markdown("[4i. Streamlit Pydeck Chart](#4i-streamlit-pydeck-chart)")
        st.markdown("[4j. Streamlit Graphviz Chart](#4j-streamlit-graphviz-chart)")
        st.markdown("[4k. Streamlit Map Chart](#4k-streamlit-map-chart)")
    with st.expander("Nomor 5"):
        st.markdown("[5. Input Widget](#5-input-widget)")
        st.markdown("[5a. Streamlit Button](#5a-streamlit-button)")
        st.markdown("[5b. Streamlit Experimental_data_editor](#5b-streamlit-experimental-data-editor)")
        st.markdown("[5c. Streamlit Button Download](#5c-streamlit-button-download)")
        st.markdown("[5d. Streamlit CheckBox](#5d-streamlit-checkbox)")
        st.markdown("[5e. Streamlit Radio](#5e-streamlit-radio)")
        st.markdown("[5f. Streamlit Select Box](#5f-streamlit-select-box)")
        st.markdown("[5g. Streamlit Multi Select](#5g-streamlit-multi-select)")
        st.markdown("[5h. Streamlit Slider](#5h-streamlit-slider)")
        st.markdown("[5i. Streamlit Select Slider](#5i-streamlit-select-slider)")
        st.markdown("[5j. Streamlit Text Input](#5j-streamlit-text-input)")
        st.markdown("[5k. Streamlit Number Input](#5k-streamlit-number-input)")
        st.markdown("[5l. Streamlit Text Area](#5l-streamlit-text-area)")
        st.markdown("[5m. Streamlit Date Input](#5m-streamlit-date-input)")
        st.markdown("[5n. Streamlit Time Input](#5n-streamlit-time-input)")
        st.markdown("[5o. Streamlit File Uploader](#5o-streamlit-file-uploader)")
        st.markdown("[5p. Streamlit Color Picker](#5p-streamlit-color-picker)")
    with st.expander("Nomor 6"):
        st.markdown("[6. Media Element](#6-media-element)")
        st.markdown("[6a. Streamlit Image](#6a-streamlit-image)")
    with st.expander("Nomor 7"):
        st.markdown("[7. Layout And Container](#7-layout-and-container)")
        st.markdown("[7a. Sidebar](#7a-sidebar)")
        st.markdown("[7b. Column](#7b-column)")
        st.markdown("[7c. Tab](#7c-tab)")
        st.markdown("[7d. Expander](#7d-expander)")
        st.markdown("[7e. Container](#7e-container)")
        st.markdown("[7f. Empty](#7f-empty)")
    with st.expander("Nomor 8"):
        st.markdown("[8. Status Element](#8-status-element)")
        st.markdown("[8a. Progress](#8a-progress)")
        st.markdown("[8b. Spinner](#8b-spinner)")
        st.markdown("[8c. Balloons](#8c-balloons)")
        st.markdown("[8d. Snow](#8d-snow)")
        st.markdown("[8e. Error](#8e-error)")
        st.markdown("[8f. Warning](#8f-warning)")
        st.markdown("[8g. Info](#8g-info)")
        st.markdown("[8h. Success](#8h-success)")
        st.markdown("[8i. Exception](#8i-exception)")
    with st.expander("Nomor 9"):
        st.markdown("[9. Control Flow](#9-control-flow)")
        st.markdown("[9a. Stop](#9a-stop)")
        st.markdown("[9b. Form & Submit Btn](#9b-form-submit-btn)")
        st.markdown("[9c. experimental_rerun](#9c-experimental-rerun)")
        
# st.markdown("[](#)")


with tab1:
    st.header("1. Write and Magic")
    # 1.  Write and Magic
    st.write('''
    # This is *_Magic_*
    ''')
    


with tab2:
    # 2.  Text Element
    st.header("2. Text Elements")
            
    st.markdown(" 2a. Streamlit *_Mark_down*")
    st.markdown("Warna :red[Merah] dan Biru bold **:blue[Biru]**.")

    st.title("2b. Streamlit Title")
    st.header("2c. Header")
    st.subheader("2d. Sub Header")
    st.caption("2e. Caption")

    st.header("2f. Code")
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

with tab3:
    # 3.  Data Display Element
    st.header("3. Data Display Element")
    st.header("3a. Streamlit Dataframe")
    df = pd.DataFrame(
    np.random.randn(50, 3),
    columns=('col %d' % i for i in range(3)))

    st.dataframe(df)
    st.header("3b. Streamlit Table")
    st.table(df)

    st.header("3c. Strealit Metric")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    col3.metric(label="Humidity",value="86%",delta="4%",delta_color="inverse")

    st.header("3d. Strealit json")

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

with tab4:
    # 4.  Chart Element
    st.header("4. Chart Element")
    st.header("4a. Streamlit Line Chart")
    st.line_chart(df)

    st.header("4b. Streamlit Area Chart")
    st.area_chart(df)

    st.header("4c. Streamlit Bar Chart")
    st.bar_chart(df)

    st.header("4d. Streamlit Pyplot")

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

    st.header("4e. Streamlit Altair")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(chart_data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.altair_chart(c, use_container_width=True)

    st.header("4f. Streamlit Vega Lite Chart")

    st.vega_lite_chart(chart_data, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'a', 'type': 'quantitative'},
            'y': {'field': 'b', 'type': 'quantitative'},
            'size': {'field': 'c', 'type': 'quantitative'},
            'color': {'field': 'c', 'type': 'quantitative'},
        },
    })

    st.header("4g. Streamlit Plotly Chart")

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


    st.header("4h. Streamlit Bokeh Chart")
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(
        title='simple line example',
        x_axis_label='x',
        y_axis_label='y')

    p.line(x, y, legend_label='Trend', line_width=2)

    st.bokeh_chart(p, use_container_width=True)

    st.header("4i. Streamlit Pydeck Chart")

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
    st.header("4j. Streamlit Graphviz Chart")

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

    st.header("4k. Streamlit Map Chart")

    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)

with tab5:
    # 5.  Input Widget
    st.header("5. Input Widget")
    st.header("5a. Streamlit Button")

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


    st.header("5c. Streamlit Button Download")
    csv = pd.read_csv(st.secrets['public_gsheet_csv']).to_csv()

    st.download_button(label="Download File Data",data=csv,file_name="data.csv",mime='text/csv')

    st.header("5d. Streamlit CheckBox")
    agree = st.checkbox('I agree')

    if agree:
        st.write('Great!')

    st.header("5e. Streamlit Radio")
    genre = st.radio(
        "What's your favorite movie genre",
        ('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn\'t select comedy.")

    st.header("5f. Streamlit Select Box")
    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)

    st.header("5g. Streamlit Multi Select")
    options = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

    st.write('You selected:', options)

    st.header("5h. Streamlit Slider")
    values = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

    st.header("5i. Streamlit Select Slider")
    color = st.select_slider(
        'Select a color of the rainbow',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('My favorite color is', color)

    st.header("5j. Streamlit Text Input")
    text = st.text_input('Title Write', 'Text')
    st.write('Your Text is', text)

    st.header("5k. Streamlit Number Input")
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)

    st.header("5l. Streamlit Text Area")
    txt = st.text_area('Text to analyze', '''
        It was the best of times, it was the worst of times, it was
        the age of wisdom, it was the age of foolishness, it was
        the epoch of belief, it was the epoch of incredulity, it
        was the season of Light, it was the season of Darkness, it
        was the spring of hope, it was the winter of despair, (...)
        ''')
    st.write(txt)

    st.header("5m. Streamlit Date Input")
    d = st.date_input(
        "When\'s your birthday",
        datetime.date(2023, 3, 19))
    st.write('Your birthday is:', d)

    st.header("5n. Streamlit Time Input")
    t = st.time_input('Set an alarm for', datetime.time(8, 45))
    st.write('Alarm is set for', t)


    st.header("5o. Streamlit File Uploader")
    uploaded_file = st.file_uploader("Choose a file CSV")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.table(dataframe)


    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)


    st.header("5p. Streamlit Color Picker")
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('The current color is', color)
with tab6:
    # 6.  Media Element
    st.header("6. Media Element")
    st.header("6a. Streamlit Image")
    dir = os.getcwd()
    st.write(dir)
    image = Image.open('./Thumnail Paladin #2.png')

    st.image(image, caption='Channel Youtube : EVAN141')


# 7.  Layout and Container
with tab7:
    st.header("7. Layout And Container")
    
    st.header("7a. Sidebar")
    st.write("👈 is SideBar")
    st.header("7b. Column")
    col1,col2= st.columns(2)
    with col1:
        st.write("This is column 1")

    with col2:
        st.write("This is column 2")

    st.header("7c. Tab")
    st.write("👆 Top Web is Tab")

    st.header("7d. Expander")
    st.write("👈 Inside Sidebar")

    st.header("7e. Container")
    with st.container():
        st.write("This is Container")

    st.header("7f. Empty")
    st.write("10 Seconds to Destroy")
    holder = st.empty()
    with holder:
        for seconds in range(10):
            text = st.write(f"⏳ {seconds} seconds have passed")
            time.sleep(1)
        holder.empty()
# 8.  Status Element
with tab8:
    st.header("8. Status Element")
    st.header("8a. Progress")
    
    if(st.button("Start Progress")):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.2)
            my_bar.progress(percent_complete + 1, text=progress_text)

    st.header("8b. Spinner")
    if(st.button("Start Spinner")):
        with st.spinner('Wait for it...'):
            time.sleep(5) 
            st.success('Done!')

    st.header("8c. Balloons")
    if(st.button("Start Balloons")):
        st.balloons()
    st.header("8d. Snow")
    if(st.button("Start Snow")):
        st.snow()
    st.header("8e. Error")
    if(st.button("Start Error")):
        st.error('This is an error', icon="🚨")
    st.header("8f. Warning")
    if(st.button("Start Warning")):
        st.warning('This is a warning', icon="⚠️")
    st.header("8g. Info")
    if(st.button("Start Info")):
        st.info('This is a purely informational message', icon="ℹ️")
    st.header("8h. Success")
    if(st.button("Start Success")):
        st.success('This is a success message!', icon="✅")
    st.header("8i. Exception")
    if(st.button("Start Exception")):
        e = RuntimeError('This is an exception of type RuntimeError')
        st.exception(e)

# 9.  Control Flow
with tab9:
    st.header("9. Control Flow")
    st.header("9a. Stop")
    st.title("Empty Text to Stop")
    name = st.text_input('Name',"Name")
    if not name:
        st.warning('Please input a name.')
        st.stop()
        st.success('Thank you for inputting a name.')
    
    st.header("9b. Form & Submit Btn")
    with st.form("my_form"):
        st.write("Form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.header("9c. experimental_rerun")
    if(st.button("Start Experimental Rerun")):
        st.experimental_rerun()

# 10. Utilities
with tab10:
    st.header("10. Utilities")
    st.header("10a. Set Page Config")
    st.write("Already build")
    
    st.header("10b. Echo")
    with st.echo():
        st.write('This code will be printed')

    st.header("10c. Help")
    with st.expander("Help Dataframe"):
        st.help(pd.DataFrame)
    
    st.header("10d. Experimental Show")
    dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    })
    st.experimental_show(dataframe)

    st.header("10e. Experimental Get Query Params")
    st.experimental_get_query_params()
    {"show_map": ["True"], "selected": ["asia", "america"]}

    st.header("10f. Experimental Set Query Params")
    st.experimental_set_query_params(
    show_map=True,
    selected=["asia", "america"],
    )
    
    
    