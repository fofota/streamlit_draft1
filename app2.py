import streamlit as st
import pandas as pd

st. set_page_config(layout="wide")

# Streamlit app to read and display DataFrame from CSV
def main():
    st.title("Read CSV App v1")

    # Load DataFrame from the CSV file saved by the first app
    df = pd.read_csv("parsed_data.csv")

    # Function to map positions to the desired values
    def map_position(position):
        if position.startswith('GK'):
            return 1
        elif position.startswith('DM'):
            return 3
        elif position.startswith('WB'):
            return 2.5  # You can use any value between 2 and 3
        elif position.startswith('D'):
            return 2
        elif position.startswith('M'):
            return 4
        elif position.startswith('A'):
            return 5
        elif position.startswith('S'):
            return 6
        else:
            return 7

    # Add a new column 'MappedPosition' based on the mapping function
    df['MappedPosition'] = df['Position'].apply(map_position)

    # Sort the DataFrame by 'MappedPosition'
    df.sort_values(by='MappedPosition', inplace=True)

    # Select only the desired columns
    selected_columns = ['Inf', 'Name', 'Age', 'Wage', 'Transfer Value', 'Nat', 'Position', 'Av Rat', 'Mins', 'Gls', 'Ast', 'NP-xG/90', 'xA/90']
    selected_df = df[selected_columns]

    # Use st.columns to create two columns
    col1, col2 = st.columns([2, 1])  # Adjust the ratios as needed

    # Display the table in the left column
    with col1:
        st.dataframe(selected_df.style.set_table_styles([{'selector': 'table', 'props': [('width', '100%')]}]), height=(len(selected_df) + 1) * 35)

    # Print 'hello world' in the right column
    with col2:
        st.write("Hello World")

if __name__ == "__main__":
    main()
