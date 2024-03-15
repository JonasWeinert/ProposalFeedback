import os
from openai import OpenAI
import streamlit as st
import json
#import streamlit_authenticator as stauth

#llm="gpt-4-1106-preview"
llm = "gpt-3.5-turbo-0125"


# Feedback overview
def overviewfb(department, institution, program, proposal):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(
        api_key = OPENAI_API_KEY
    )

    completion = client.chat.completions.create(
    model = llm,
    messages=[
        {"role": "system", "content": f"You are a professor of {program} in the department of {department} that sits on the phd admissions comitte of the {institution}. You receive research proposal drafts and provide applicants with feedback on how to improve them in order to increase their chances when they resumit them for final aproval. The boards evaluation criteria are: What is your general topic? How does that topic fit with the program and the department? What questions do you want to answer? What is the key literature and its limitations? What are the main hypotheses of the work? What methodology do you intend to use? What are your case studies, if any, and what are your case selection criteria? Do not include an introduction of yourself but only return the feedback. Make sure to return the feedback in a narrative structure and avoid sections/ subheadings in your feedback! Instead just provide a paragraph. Avoid generic remarks and instead be specific and tailored to the proposed research."},
        {"role": "user", "content": f"The proposal: {proposal}"}
    ],
    #max_tokens = 3500,
    temperature = 0.8
    )

    feedback_general = completion.choices[0].message.content

    return feedback_general

def test(fname, lname):
  return f"{fname} +  + {lname}"

## Feedback details
def detailedfb(department, institution, program, proposal, aspectprompt):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(
        api_key = OPENAI_API_KEY
    )

    completion = client.chat.completions.create(
    model = llm,
    messages=[
        {"role": "system", "content": f"You are a professor of {program} in the department of {department} that sits on the phd admissions comitte of the {institution}. You receive research proposal drafts and provide applicants with feedback on how to improve them in order to increase their chances when they resubmit them for final aproval. Do not include an introduction of yourself but only return the feedback. Be very detailed but yet concise. Avoid generic remarks and instead be specific and tailored to the proposed research. Always refer to specific examples and provide concrete suggestions. Today, please focus on {aspectprompt} Do not provide feedback on other aspects of the proposal!"},
        {"role": "user", "content": f"The proposal: {proposal}"}
    ],
    #max_tokens = 3500,
    temperature = 0.8
    )

    feedback_specific = completion.choices[0].message.content

    return feedback_specific
