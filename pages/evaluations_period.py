import streamlit as st
import pandas as pd
from datetime import datetime
from src.database.queries import get_evaluations_by_period

def evaluations_period():
    st.title("Evaluations Over a Period")

    # Date input for selecting the period
    start_date = st.date_input("Start Date", datetime.today())
    end_date = st.date_input("End Date", datetime.today())

    if st.button("Get Evaluations"):
        if start_date > end_date:
            st.error("Start date must be before end date.")
        else:
            # Fetch evaluations from the database
            evaluations = get_evaluations_by_period(start_date, end_date)
            if evaluations:
                # Convert to DataFrame for better display
                df = pd.DataFrame(evaluations)
                st.write(df)
            else:
                st.warning("No evaluations found for the selected period.")

if __name__ == "__main__":
    evaluations_period()