import pandas as pd 
import streamlit as st
import numpy as np

df_goals = pd.read_csv("databases/goal_scorers_2024_processed.csv")
print(df_goals.head())
print("===================================")
df_stats = pd.read_csv("databases/stats_FLA2024_processed.csv")
print(df_stats.head())
print("===================================")
df_matches = pd.read_csv("databases/matches_FLA2024_processed.csv")
print(df_matches.head())

grafico = st.line_chart(df_goals)