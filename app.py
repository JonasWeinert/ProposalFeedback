# Initialise project
import streamlit as st
import docx2txt
from docxlatex import Document
from util import test, overviewfb, detailedfb

# Start Front End interface
st.set_page_config(page_title='ProposalTutor', page_icon="🧡", layout="wide")

llm="gpt-4-1106-preview",
#llm = "gpt-3.5-turbo-0125"

# Set Styles
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
load_css('style.css')
# Supress streamlit branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title('Reserach Proposal Feedback Generator') # Title
st.markdown('You will get feedback on clarity, feasability, novelty, as well as your chosen methods and cases. You can also paste specific criteria that you would like to get feedback on the left.') # First paragraph

upload, criteria = st.columns(2)

with upload:
    st.subheader('Upload your Proposal') # Upload prompt
    uploaded_file = st.file_uploader('Choose your DocX file', type='docx') # Save file to memory for duration of session
    if uploaded_file:
        doc = Document(uploaded_file)
        proposal = doc.get_text()
        text = docx2txt.process(uploaded_file)
    else:
        proposal = ""
        text =""

    

with criteria:
    st.subheader('Get your feedback')
    st.markdown('Make sure to specify your case details in the sidebar to get better feedback! Otherwise the default values might obscure the feedback clarity if not applicable to your case.')
    if uploaded_file:
        if st.button("Submit!"):
            run = 1
        else:
            run = 0    
    else:
        run = 0

    # st.markdown("Eg 'Analytical: Does the proposed research analyse a phenomenon, or just describe it?")
    # extrac1 = st.text_input("Add your first extra criterion", key = "crit1")
    # extrac2 = st.text_input("Add your second extra criterion", key = "crit2")
#st.markdown('---')

# Custom Input
with st.sidebar:
    st.header('Settings')
    st.subheader('General')
    institution = st.text_input(key = "inst", label= "Academic Institution", value = "University College London")
    department = st.text_input(key = "department", label= "Academic Departemnt/ Field", value = "Economics")
    program = st.text_input(key = "program", label= "PhD program name", value = "Development Economics")
    st.subheader('Extra criteria')
    st.markdown('If applicable, add aditional criteria that will be used to evaluate your proposal. Make sure to follow this format:')
    st.markdown("Eg 'Analytical: Does the proposed research analyse a phenomenon, or just describe it?'")
    extrac1 = st.text_input("Add your first extra criterion", placeholder = "Leave blank if not applicable", key = "crit1")
    extrac2 = st.text_input("Add your second extra criterion", placeholder = "Leave blank if not applicable", key = "crit2")




from prompts import literature, custom_, hypotheses, methods_, novelty_feasbility

## Results
if run == 1:
    # placeholder = st.empty()
    # # Replace the placeholder with some text:
    # placeholder.text("Generating Feedback. Please wait!")    
    # output = overviewfb(department, institution, program, proposal)
    # with placeholder.container():
    #     st.markdown(output)
    overview, lit, hyp, methods, novelty, custom = st.tabs(["💡 Overview", "📖 Literature", "🔀 Hypotheses", "🔬 Methods", "🆕 Novelty & Feasability", "🧐 Your custom criteria"])

    overview.subheader('General Feedback Overview')
    with st.spinner("Generating Feedback Overview. Please wait!"):
        output = overviewfb(department, institution, program, proposal)

    overview.markdown(output)

    with st.spinner("Generating Literature Feedback. Please wait!"):
        lit_out = detailedfb(department, institution, program, proposal, literature)
        lit.subheader('Literature')
        lit.markdown(lit_out)

    with st.spinner("Generating Hypotheses Feedback. Please wait!"):
        hyp_out = detailedfb(department, institution, program, proposal, hypotheses)
        hyp.subheader('Hypotheses')
        hyp.markdown(hyp_out)

    with st.spinner("Generating Methods Feedback. Please wait!"):
        met_out = detailedfb(department, institution, program, proposal, methods_)
        methods.subheader('Methods')
        methods.markdown(met_out)

    with st.spinner("Generating Feasability & Novelty Feedback. Please wait!"):
        nov_out = detailedfb(department, institution, program, proposal, novelty_feasbility)
        novelty.subheader('Feasability & Novelty')
        novelty.markdown(nov_out)

    if extrac1 or extrac2:
        with st.spinner("Generating custom Feedback. Please wait!"):
            cust_out = detailedfb(department, institution, program, proposal, custom_(extrac1, extrac2))
            custom.subheader('Your own criteria')
            custom.markdown(cust_out)




    



