import requests
import streamlit as st

caption = '''
**Dr. Andrew Huberman, Ph.D.** - is a neuroscientist and professor at Stanford, who entered the podcast world by making neuroscience fun and easy to understand.

He shares on a weekly base awesome, science-based tips to boost your health and happiness.

The podcast is frequently ranked in the top 10 of all podcasts globally. '''

st.sidebar.image("https://yt3.googleusercontent.com/5ONImZvpa9_hYK12Xek2E2JLzRc732DWsZMX2F-AZ1cTutTQLBuAmcEtFwrCgypqJncl5HrV2w=s900-c-k-c0x00ffffff-no-rj", use_column_width=True)
st.sidebar.markdown(caption)

st.sidebar.markdown("[HubermanLab - visit website](https://www.hubermanlab.com/)")
st.sidebar.markdown('''
    <a href="https://www.youtube.com/@hubermanlab" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/2560px-Logo_of_YouTube_%282015-2017%29.svg.png" style="width: 80px; margin-right: 30px;">
    </a>
    <a href="https://open.spotify.com/show/79CkJF3UJTHFV8Dse3Oy0P" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/2048px-Spotify_logo_without_text.svg.png" style="width: 50px;">
    </a>
''', unsafe_allow_html=True)


st.sidebar.markdown('<br><br>', unsafe_allow_html=True)  # Add space before the buttons
def create_button_with_link(label, link, color):
    return f'<a href="{link}" target="_blank" style="background-color: {color}; color: white; text-decoration: none; padding: 10px 15px; border-radius: 5px; display: inline-block;">{label}</a>'

# Buttons with links and colors
button1 = create_button_with_link("Mental Health and Addictions", "https://www.hubermanlab.com/topics/mental-health-and-addictions", "SkyBlue")
button2 = create_button_with_link("Fitness and Recovery", "https://www.hubermanlab.com/topics/fitness-and-recovery", "	LightBlue")
button3 = create_button_with_link("Sleep Hygiene", "https://www.hubermanlab.com/topics/sleep-hygiene", "SkyBlue")
button4 = create_button_with_link("ADHD, Drive and Motivation", "https://www.hubermanlab.com/topics/adhd-drive-and-motivation", "LightBlue")

# Add buttons to the sidebar
st.sidebar.markdown(button1, unsafe_allow_html=True)
st.sidebar.markdown(button2, unsafe_allow_html=True)
st.sidebar.markdown(button3, unsafe_allow_html=True)
st.sidebar.markdown(button4, unsafe_allow_html=True)

# Set avatars for roles
querier_avatar = 'https://as2.ftcdn.net/v2/jpg/05/53/97/13/1000_F_553971391_58CnJ3qSdxmrOFUp6eojyVhZ9khKq2Et.jpg'
assistant_avatar = 'https://yt3.googleusercontent.com/5ONImZvpa9_hYK12Xek2E2JLzRc732DWsZMX2F-AZ1cTutTQLBuAmcEtFwrCgypqJncl5HrV2w=s900-c-k-c0x00ffffff-no-rj'

# Streamlit app title and introduction
st.title("Ask Andrew")
st.subheader("Your personal podcast assistant 🚀 ")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    role = message["role"]
    avatar = querier_avatar if role == "user" else assistant_avatar

    with st.chat_message(role, avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input('Just ask me'):
    # Display user message in chat message container
    st.chat_message("user", avatar=querier_avatar).markdown(prompt)

    # Make a request to the FastAPI server
    fastapi_url = "http://127.0.0.1:8000/chat"  # Adjust the URL based on your FastAPI server location
    response = requests.get(fastapi_url, params={"question": prompt}).json()

    llm_answer = response['response']['result']
    source_documents = response['response']['source_documents']
    sources = [doc['metadata']['source'] for doc in source_documents]
    cleaned_sources = set(source.replace('/Users/larshofferbert/code/hofferBERT/askandrew_langchain/docs/', '').replace('.txt', '') for source in sources)
    sources_list = ', '.join(cleaned_sources)

    final_answer = f"{llm_answer}\n\n**Find more in episode:** {sources_list}"

    # Display assistant response in chat message container
    with st.chat_message("Andrew", avatar=assistant_avatar):
        st.markdown(final_answer)

    # Only append the relevant information to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "Andrew", "content": final_answer})


# if prompt := st.chat_input('Just ask me'):
#     # Display user message in chat message container
#     st.chat_message("user", avatar=querier_avatar).markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     # Make a request to the FastAPI server
#     fastapi_url = "http://127.0.0.1:8000/chat"  # Adjust the URL based on your FastAPI server location
#     response = requests.get(fastapi_url, params={"question": prompt}).json()

#     source_documents = response['response']['source_documents']
#     sources = [doc['metadata']['source'] for doc in source_documents]
#     cleaned_sources = set(source.replace('/Users/larshofferbert/code/hofferBERT/askandrew_langchain/docs/', '').replace('.txt', '') for source in sources)
#     sources_list = ', '.join(cleaned_sources)

#     llm_answer = response['response']['result']
#     final_answer = f"{llm_answer} \n\n**Find more in episode:** \n{sources_list}"

#     # Display assistant response in chat message container
#     with st.chat_message("Andrew", avatar=assistant_avatar):
#         st.markdown(final_answer) # Use final_answer instead of response["response"]

#     st.session_state.messages.append({"role": "Andrew", "content": response["response"]})
