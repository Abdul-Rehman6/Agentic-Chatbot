import streamlit as st
import os
from src.langgrapgagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
            # GETTING OPTIONS FROM THE CONFIG CLASS THROUGH SELF.CONFIG
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM OPTIONS
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "OPEN AI":
                # MODEL SELECTION
                model_options = self.config.get_openai_model_options()
                self.user_controls["selected_openai_model"] = st.selectbox("Select Model", model_options)

                # API Key
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"] = st.text_input("API Key", type="password")
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("Please enter your OPEN AI API Key to proceed. Don't have? refer : https://platform.openai.com/api-keys")
                
                # usecase selection
                self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)

                if self.user_controls["selected_usecase"] == "Chatbot with Web Tool":
                    self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily Api Key", type="password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily Api Key to proceed. Don't have? refer : https://app.tavily.com/home")

            return self.user_controls

