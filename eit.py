#!/usr/bin/python3

import numpy as np
import streamlit as st

from matplotlib import pyplot as plt

A = st.sidebar.number_input('A', value=1.0, min_value=0.0, max_value=10000.0)
B = st.sidebar.number_input('B', value=1.0, min_value=0.0, max_value=10000.0)
D = st.sidebar.number_input('D', value=1.0, min_value=0.0, max_value=10000.0)
c_min = st.sidebar.number_input('c_min', value=1, min_value=-10000, max_value=10000)
c_max = st.sidebar.number_input('c_max', value=1, min_value=-10000, max_value=10000)
c_step = st.sidebar.number_input('c_step', value=1.0, min_value=0.0, max_value=10000.0)
C = np.arange(c_min, c_max, c_step)
re = (C*(D**2 - 4*C**2 - 4*B**2)) / ((4*(B*A-C**2)+D**2)**2 + 16*C*C*(A+B)**2)
im = (4*A*(B**2+C**2)+D*D*B) / ((4*(B*A-C**2)+D**2)**2 + 16*C*C*(A+B)**2)

fig, ax = plt.subplots()
ax.plot(C, im, label='Imaginary')
ax.plot(C, re, label='Real')
ax.set_xlabel("Detuning $\Delta_1$ (arbitrary units)")
ax.set_ylabel("Susceptibility $\chi$ (arbitrary units)")
ax.legend()
st.pyplot(fig)

fn = "eit.png"
plt.savefig(fn)
with open(fn, "rb") as img:
    btn = st.download_button(
        label="Download Graph",
        data=img,
        file_name=fn,
        mime="image/png"
    )
