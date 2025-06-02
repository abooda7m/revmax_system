import streamlit as st
from scipy.stats import ttest_ind, f_oneway


def render(df_filtered):
    st.subheader("\U0001F4C9 T-Test: South vs West")
    south = df_filtered[df_filtered["Region"] == "South"]["Sales"]
    west = df_filtered[df_filtered["Region"] == "West"]["Sales"]
    if len(south) > 1 and len(west) > 1:
        t_stat, p_val = ttest_ind(south, west)
        st.write(f"**T-statistic:** {t_stat:.3f}, **P-value:** {p_val:.3f}")
        st.success(" Significant difference" if p_val < 0.05 else "ℹ️ No significant difference")
    else:
        st.warning(" Not enough data for South and West.")

    st.subheader("\U0001F4CA ANOVA: Across All Regions")
    groups = [df_filtered[df_filtered["Region"] == r]["Sales"] for r in df_filtered["Region"].unique()]
    if len(groups) > 1 and all(len(g) > 1 for g in groups):
        f_stat, p_val = f_oneway(*groups)
        st.write(f"**F-statistic:** {f_stat:.3f}, **P-value:** {p_val:.3f}")
        st.success(" Regions differ significantly" if p_val < 0.05 else "ℹ No significant difference")
    else:
        st.warning(" Need at least two regions with data for ANOVA.")
