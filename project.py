#mcandrew

import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import streamlit as st
import scipy

if __name__ == "__main__":

    ili_data = pd.read_csv("./ilidata.csv")

    ili_data["year"] = ili_data["epiweek"].astype(str).str[:4]
    ili_data["week"] = ili_data["epiweek"].astype(str).str[-2:]

    def pick_state(state):
        pa = ili_data.loc[ili_data.state==state]
        weeks                   = np.arange(len(pa))
        pa["weeks"] = weeks

        return pa
    
    option = st.selectbox("Select State", ili_data.state.unique() )

    #option = "pa"
    all_state_data = pick_state(option)

    st.line_chart(data = all_state_data, x="weeks",y=["ili"])


    
    fig,ax = plt.subplots()
    plt.hist( all_state_data.ili.values, density=True, bins=20)
    est_rate = 1./np.mean(all_state_data.ili)

    dom  = np.linspace(0.05,7,50)
    cdfs = scipy.stats.expon( 0, est_rate ).pdf(dom)

    plt.plot(dom,cdfs)

    st.pyplot( fig )
    
    
    



    
    

