import streamlit as st 
from langchain_groq import ChatGroq

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent

from dotenv import load_dotenv
load_dotenv()

llm= ChatGroq (model="openai/gpt-oss-120b")

details={
    "SIRT":
       { "name": "Sagar Institute Of Research and Technology ",
        "contact_number":"1234567898"},
        
    "JNCT":{
        "name": "Jay Narayan College Of Technology",
         "contact_number":"0001112278"
    }
}
        
        
#new tool

def get_college_details_tool(college:str):
  '''
   This tool is use for get the information of college deatils like thier
    name and contact number ...and only give information of SIRT and JNCT
  '''
  print("iam calling",college)
  data= details.get(college)
  return data

search = GoogleSerperAPIWrapper()
tools= [search.run,get_college_details_tool]

agent= create_agent(llm,tools=tools)

st.title("My ChatBot")

if "messages" not in st.session_state:
    st.session_state["messages"]=[]
    
all_chat=st.session_state  ["messages"]
for chat in all_chat:
    role= chat["role"]
    msg= chat ["content"]
    st.chat_message(role).markdown(msg)


que = st.chat_input("Ask Anything....")

if que:
    st.chat_message("user").markdown(que)
    msg= {"role":"user","content":que}
    
    st.session_state["messages"].append(msg)
    
    messages= st.session_state["messages"]
    
  
    
    data= {"messages":messages}
    response= agent .invoke(data)
    bot_reply= response ["messages"][-1].content
    
    
    st.session_state["messages"].append({"role":"ai","content":bot_reply})
    st.chat_message("ai").markdown(bot_reply)