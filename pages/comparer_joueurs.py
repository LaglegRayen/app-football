import streamlit as st
import pandas as pd
from database import queries

def load_player_data(player_ids):
    player_data = {}
    for player_id in player_ids:
        player_data[player_id] = queries.get_player_evaluations(player_id)
    return player_data

def display_player_comparison(player_data):
    if not player_data:
        st.warning("No player data available for comparison.")
        return

    player_ids = list(player_data.keys())
    st.header("Player Comparison")
    
    # Display general averages
    st.subheader("General Averages")
    averages = pd.DataFrame({
        "Player ID": player_ids,
        "Average Tactical": [data['moyenne_tactique'] for data in player_data.values()],
        "Average Behavioral": [data['moyenne_comportementale'] for data in player_data.values()],
        "Average Technical": [data['moyenne_technique'] for data in player_data.values()],
        "Average General": [data['moyenne_generale'] for data in player_data.values()],
    })
    st.table(averages)

    # Display detailed specifics
    st.subheader("Detailed Specifics")
    for player_id, evaluations in player_data.items():
        st.write(f"### Player ID: {player_id}")
        st.write(evaluations)

def main():
    st.title("Compare Players")
    
    player_ids = st.multiselect("Select Players to Compare", options=queries.get_all_player_ids())
    
    if st.button("Compare"):
        player_data = load_player_data(player_ids)
        display_player_comparison(player_data)

if __name__ == "__main__":
    main()