import streamlit as st
import pandas as pd
from pathlib import Path

baseline_ai_file = Path("results/baseline_vs_ai_summary.csv")
incident_file = Path("results/incident_summary.csv")
rl_file = Path("results/medium_rl_check_summary.csv")
rl_plot = Path("results/plots/medium_rl_check_waiting_time.png")
incident_reroute_file = Path("results/incident_reroute_summary.csv")

st.set_page_config(page_title="Predictive Urban Infrastructure Dashboard", layout="wide")

st.title("Predictive Urban Infrastructure Management Dashboard")
st.write("This dashboard presents baseline, predictive ML, and RL-controlled traffic performance across multiple scenarios.")

st.sidebar.title("Dashboard Controls")
view = st.sidebar.radio(
    "Choose view",
    ["Overview", "Scenario Comparison", "Incident Analysis", "RL Analysis"]
)

if baseline_ai_file.exists():
    df = pd.read_csv(baseline_ai_file)

    avg_wait = df["avg_waiting_time"].mean()
    avg_loss = df["avg_time_loss"].mean()
    avg_completed = df["vehicles_completed"].mean()

    c1, c2, c3 = st.columns(3)
    c1.metric("Avg Waiting Time", f"{avg_wait:.2f}")
    c2.metric("Avg Time Loss", f"{avg_loss:.2f}")
    c3.metric("Vehicles Completed", f"{avg_completed:.0f}")

# File paths
baseline_ai_file = Path("results/baseline_vs_ai_summary.csv")
incident_file = Path("results/incident_summary.csv")

# Section 1: Overview
if view == "Overview":
    st.header("System Overview")

    st.markdown("""
    - **Baseline system:** fixed-time traffic signals  
    - **Predictive ML system:** model-driven adaptive controller  
    - **RL system:** Q-learning traffic signal controller  
    - **Scenarios:** low, medium, high, incident  
    """)

    st.header("Controller Modes")
    st.markdown("""
    **Baseline mode**
    - Fixed-time traffic signal control
    - No prediction
    - No adaptive behaviour

    **Predictive ML mode**
    - Uses machine learning prediction
    - Adjusts phase durations based on predicted congestion
    - Evaluated across normal and incident scenarios

    **RL mode**
    - Uses Q-learning to learn traffic signal timing policies
    - Selects actions based on learned reward optimisation
    - Evaluated as an advanced AI extension against baseline and predictive ML control
    """)

# Section 2: Baseline vs AI summary
elif view == "Scenario Comparison":
    st.header("Baseline vs AI Comparison")

    if baseline_ai_file.exists():
        df = pd.read_csv(baseline_ai_file)
        st.dataframe(df, use_container_width=True)

        scenario = st.selectbox("Select scenario", sorted(df["scenario"].unique()))
        filtered = df[df["scenario"] == scenario]

        st.subheader(f"Metrics for scenario: {scenario}")
        st.dataframe(filtered, use_container_width=True)

        st.subheader("Plots")

        plot1 = Path("results/plots/baseline_vs_ai_waiting_time.png")
        plot2 = Path("results/plots/baseline_vs_ai_time_loss.png")

        col1, col2 = st.columns(2)

        with col1:
            if plot1.exists():
                st.image(str(plot1), caption="Waiting Time Comparison")

        with col2:
            if plot2.exists():
                st.image(str(plot2), caption="Time Loss Comparison")

# Section 3: Incident summary
elif view == "Incident Analysis":
    st.header("Incident Scenario")

    if incident_file.exists():
        incident_df = pd.read_csv(incident_file)
        st.dataframe(incident_df, use_container_width=True)
    else:
        st.warning("incident_summary.csv not found.")

    plot3 = Path("results/plots/incident_reroute_waiting_time_comparison.png")

    if plot3.exists():
        st.image(str(plot3), caption="Incident Comparison")
    if incident_reroute_file.exists():
        st.subheader("Incident Reroute Comparison")
        reroute_df = pd.read_csv(incident_reroute_file)
        st.dataframe(reroute_df, use_container_width=True)
    else:
        st.info("incident_reroute_summary.csv not found.")

# Section 3+: RL

elif view == "RL Analysis":
    st.header("Reinforcement Learning Analysis")

    st.markdown("""
    This section compares:
    - **Baseline (medium scenario)**
    - **Old RL controller**
    - **Improved RL controller**
    """)

    if rl_file.exists():
        rl_df = pd.read_csv(rl_file)
        st.dataframe(rl_df, use_container_width=True)

        best_rl = rl_df.loc[rl_df["avg_waiting_time"].idxmin()]
        worst_rl = rl_df.loc[rl_df["avg_waiting_time"].idxmax()]

        st.subheader("RL Comparison Summary")
        st.markdown(f"""
- **Best waiting time in RL comparison:** {best_rl['system']} ({best_rl['avg_waiting_time']:.2f})
- **Worst waiting time in RL comparison:** {worst_rl['system']} ({worst_rl['avg_waiting_time']:.2f})
        """)
    else:
        st.warning("medium_rl_check_summary.csv not found.")

    if rl_plot.exists():
        st.image(str(rl_plot), caption="Baseline vs Old RL vs Improved RL")
    else:
        st.info("RL comparison plot not found.")

# Section 4: Plots

# Section 5: Key findings
st.header("Key Findings")

if baseline_ai_file.exists():
    df = pd.read_csv(baseline_ai_file)

    best_wait = df.loc[df["avg_waiting_time"].idxmin()]
    worst_wait = df.loc[df["avg_waiting_time"].idxmax()]

    st.markdown(f"""
- **Lowest average waiting time (baseline vs AI):** {best_wait['system']} in {best_wait['scenario']} scenario ({best_wait['avg_waiting_time']:.2f})
- **Highest average waiting time (baseline vs AI):** {worst_wait['system']} in {worst_wait['scenario']} scenario ({worst_wait['avg_waiting_time']:.2f})
""")

if rl_file.exists():
    rl_df = pd.read_csv(rl_file)

    best_rl = rl_df.loc[rl_df["avg_waiting_time"].idxmin()]
    worst_rl = rl_df.loc[rl_df["avg_waiting_time"].idxmax()]

    st.markdown(f"""
- **Best RL comparison result:** {best_rl['system']} ({best_rl['avg_waiting_time']:.2f})
- **Worst RL comparison result:** {worst_rl['system']} ({worst_rl['avg_waiting_time']:.2f})
- The RL section helps evaluate whether reinforcement learning improves traffic control relative to the baseline and earlier RL versions.
""")