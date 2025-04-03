import streamlit as st
import pandas as pd
from database.db_connection import get_connection
from database.queries import get_match_evaluations

def display_match_evaluations():
    st.title("Evaluations During Matches")

    # Fetch matches from the database
    conn = get_connection()
    matches_query = "SELECT id, date_match, adversaire FROM matchs ORDER BY date_match DESC"
    matches_df = pd.read_sql(matches_query, conn)

    # Dropdown to select a match
    match_id = st.selectbox("Select a Match", matches_df['id'].tolist(), format_func=lambda x: f"{matches_df[matches_df['id'] == x]['date_match'].values[0]} vs {matches_df[matches_df['id'] == x]['adversaire'].values[0]}")

    if match_id:
        # Fetch evaluations for the selected match
        evaluations = get_match_evaluations(match_id)
        
        if evaluations:
            st.subheader("Evaluations")
            st.write(evaluations)
        else:
            st.warning("No evaluations found for this match.")

    conn.close()

if __name__ == "__main__":
    display_match_evaluations()