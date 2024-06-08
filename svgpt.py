import streamlit as st
import psycopg2
import pandas as pd

# Function to create a connection to the Redshift database
def create_redshift_connection():
    conn = psycopg2.connect(
        dbname='your_db_name',
        user='your_username',
        password='your_password',
        host='your_redshift_endpoint',
        port='5439'
    )
    return conn

# Function to query the Redshift database
def query_redshift(query):
    conn = create_redshift_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit UI
st.title('Chat with Redshift')

# Create an input text box for user queries
user_query = st.text_input("Enter your query:", "")

# Button to submit the query
if st.button("Submit"):
    if user_query:
        try:
            # Execute the query and fetch results
            result_df = query_redshift(user_query)
            st.write(result_df)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query.")

