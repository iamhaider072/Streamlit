import streamlit as st

st.text("Hello  World")
st.write("Write text demo")
st.title("My title")

"# Pakistan"


st.success("Success")
st.error("Error")
# success
st.info("Information")
 
# success
st.warning("Warning")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
status = st.radio("Select Gender: ", ('Male', 'Female'))