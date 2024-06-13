from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3
from langchain.chains import create_sql_query_chain


from langchain_community.chat_models import ChatOllama

db_user = "root"
db_password = "1532"
db_host = "localhost"
db_name = "classicmodels"
from langchain_community.utilities.sql_database import SQLDatabase
# db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=1,include_tables=['customers','orders'],custom_table_info={'customers':"customer"})
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

def get_gemini_response(question):
    llm = ChatOllama(model="sqlcoder", temperature=0.8)
    write_query = create_sql_query_chain(llm, db)
    query = write_query.invoke({"question": f"{question}"})
    return query

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("LLM App To Retrieve SQL Data")
st.subheader("Table from database: ['customers', 'employees', 'offices', 'orderdetails', 'orders', 'payments', 'productlines', 'products']")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit and question!=None:
    response=get_gemini_response(question)
    st.subheader("The Sql query is:")
    st.subheader(f"sql query is: {response}")
    try:
        response1=db.run(response)
        st.subheader("Response from database:")
        st.markdown(f"<span style='color: green; font-size:2rem;'>{response1}</span>", unsafe_allow_html=True)
    except:
        # st.subheader("query input wrong")
        st.markdown(":red[query input wrong]")
    # for row in response1:
    #     print(row)
    #     st.header(row)









