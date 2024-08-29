import streamlit as st

# Set the page config for dark mode
st.set_page_config(page_title="SkimLit", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for dark theme
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #f5f5f5;
    }
    .stTextInput label {
        color: #f5f5f5;
    }
    .stTextArea textarea {
        color: #f5f5f5;
        background-color: #333;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    .stMarkdown {
        color: #f5f5f5;
    }
    .message {
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .user_message {
        background-color: #3a3a3a;
        text-align: right;
    }
    .bot_message {
        background-color: #2c2c2c;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to display messages
def display_message(text, is_user=False):
    if is_user:
        st.markdown(f'<div class="message user_message">{text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot_message">{text}</div>', unsafe_allow_html=True)

# Initial messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("SkimLit")

# Display chat history
for message in st.session_state.messages:
    display_message(message['text'], message['is_user'])

# Text input
user_input = st.text_input("You:", "", key="input")

# Handle user input
if user_input:
    st.session_state.messages.append({'text': user_input, 'is_user': True})
    display_message(user_input, is_user=True)

    # Dummy bot response (you can integrate your own model here)
    bot_response = "This is a simulated response. Replace this with your model's output."
    st.session_state.messages.append({'text': bot_response, 'is_user': False})
    display_message(bot_response, is_user=False)

    # Clear input
    st.session_state.input = ""



