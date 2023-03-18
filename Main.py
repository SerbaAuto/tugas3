import streamlit as st
import pandas as pd
import numpy as np


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

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)
# 4.  Chart Element
# 5.  Input Widget
# 6.  Media Element
# 7.  Layout and Container
# 8.  Status Element
# 9.  Control Flow
# 10. Utilities
