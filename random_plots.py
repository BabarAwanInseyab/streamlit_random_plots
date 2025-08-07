import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Random Plots Dashboard", layout="wide")

# Title
st.title("Random Data Visualization Dashboard")
usr=st.text_input("User name")
passwrd=st.text_input("Password")
if usr=="admin" and passwrd=="admin":
    # Sidebar controls
    with st.sidebar:
        st.header("Controls")
        num_points = st.slider("Number of data points", 10, 100, 200)
        noise_level = st.slider("Noise level", 0.1, 5.0, 1.0)
        show_3d = st.checkbox("Show 3D plot", True)
        color_theme = st.selectbox("Color theme", 
                                ["plotly", "ggplot2", "seaborn", "simple_white"])

    # Generate random data
    np.random.seed(42)
    x = np.linspace(0, 10, num_points)
    y = np.sin(x) + np.random.normal(0, noise_level, num_points)
    categories = np.random.choice(['Group A', 'Group B', 'Group C'], num_points)
    values = np.random.uniform(1, 100, num_points)

    # Create DataFrame
    df = pd.DataFrame({
        'X': x,
        'Y': y,
        'Category': categories,
        'Value': values
    })

    # Layout columns
    col1, col2 = st.columns(2)

    # Plot 1: Interactive Plotly Line Plot
    with col1:
        st.subheader("Interactive Line Plot")
        fig1 = px.line(df, x='X', y='Y', color='Category',
                    title="Sine Wave with Random Noise",
                    template=color_theme)
        st.plotly_chart(fig1, use_container_width=True)

    # Plot 2: Scatter Plot
    with col2:
        st.subheader("Scatter Plot")
        fig2 = px.scatter(df, x='X', y='Y', color='Category',
                        size='Value', hover_data=['Value'],
                        title="Bu bble Chart by Category",
                        template=color_theme)
        st.plotly_chart(fig2, use_container_width=True)

    # Plot 3: Bar Chart
    st.subheader("Animated Bar Chart")
    fig3 = px.bar(df, x='Category', y='Value', color='Category',
                animation_frame=np.floor(df['X']).astype(int),
                range_y=[0, df['Value'].max()*1.1],
                title="Value Distribution by Category Over Time",
                template=color_theme)
    st.plotly_chart(fig3, use_container_width=True)

    # Plot 4: 3D Scatter (conditional)
    if show_3d and num_points <= 200:
        st.subheader("3D Scatter Plot")
        z = np.cos(x) + np.random.normal(0, noise_level/2, num_points)
        fig4 = px.scatter_3d(
            pd.DataFrame({'X': x, 'Y': y, 'Z': z, 'Category': categories}),
            x='X', y='Y', z='Z', color='Category',
            title="3D Random Scatter",
            template=color_theme)
        st.plotly_chart(fig4, use_container_width=True)
    elif show_3d:
        st.warning("⚠️ 3D plot disabled for more than 200 points (performance)")

    # Plot 5: Histogram
    st.subheader("Distribution Histogram")
    fig5 = px.histogram(df, x='Y', color='Category',
                    marginal="box", nbins=30,
                    title="Value Distribution",
                    template=color_theme)
    st.plotly_chart(fig5, use_container_width=True)

    # Footer
    st.markdown("---")
    st.caption(" All data is randomly generated in real-time")


