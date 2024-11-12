import duckdb as db
import streamlit as st

con = db.connect()
con.sql("create view files as (from '~/data/fsi/git.json')")

dirs_df = con.sql("select isdir, count(*) from files group by all")
st.bar_chart(dirs_df)

extn_df = con.sql("select split(path,'.')[-1] \"extn\", count(*) from files group by all order by all")
st.bar_chart(extn_df)

st.dataframe(con.sql('summarize files').df())

st.write("hello")