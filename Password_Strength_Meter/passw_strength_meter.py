import re
import random
import string
import streamlit as st

# Blacklist of common passwords
COMMON_PASSWORDS = {"password", "123456", "12345678", "qwerty", "abc123", "password1", "123456789"}

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    feedback = []
    
    if password in COMMON_PASSWORDS:
        return "❌ Weak Password - This is a commonly used password!", 0, ["Choose a more unique password."]
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", score, []
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", score, feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions below:", score, feedback

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
st.title("🔐 Password Strength Meter")
st.markdown("## Check the strength of your password or get the strong password suggestions!")

password = st.text_input("Enter your password:", type="password")
if password:
    message, score, suggestions = check_password_strength(password)
    st.progress(score / 4)
    st.subheader(f"**Score:** {score}/4")
    if score == 4:
        st.success(message)
    elif score == 3:
        st.warning(message)
    else:
        st.error(message)

    
    if suggestions:
        st.markdown("### Suggestions to Improve Your Password:")
        for suggestion in suggestions:
            st.write("📍", suggestion)

# Password Generator Feature
if st.button("Generate a Strong Password"):
    new_password = generate_strong_password()
    st.text_input("Suggested Strong Password:", value=new_password, disabled=True)

st.markdown("---")
st.write("A Journey of Learning & Creativity 🚀 | Built by Ume-Farwa")