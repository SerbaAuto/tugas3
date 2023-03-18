import streamlit as st
import pandas as pd


# 1.  Write and Magic
st.write("Magic Appear")

df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart


# 2.  Text Element
# 3.  Data Display Element
# 4.  Chart Element
# 5.  Input Widget
# 6.  Media Element
# 7.  Layout and Container
# 8.  Status Element
# 9.  Control Flow
# 10. Utilities
