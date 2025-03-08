# import streamlit as st
# import re
# # Optionally: import zxcvbn if you want advanced password analysis

# def calculate_strength(password):
#     score = 0
#     suggestions = []
    
#     if len(password) >= 8:
#         score += 1
#     else:
#         suggestions.append(" Use at least 8 characters - 🏗️🔢")
    
#     if re.search(r"[A-Z]", password):
#         score += 1
#     else:
#         suggestions.append(" Add uppercase letters - 🔠💪")
    
#     if re.search(r"[a-z]", password):
#         score += 1
#     else:
#         suggestions.append(" Add lowercase letters - 🔡✨")
    
#     if re.search(r"[0-9]", password):
#         score += 1
#     else:
#         suggestions.append(" Include numbers - 🔢🔒")
    
#     if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         score += 1
#     else:
#         suggestions.append(" Include symbols - 🔣⚡")
    
#     return score, suggestions

# st.title("Password Strength Meter")

# # Password input field
# st.markdown("""
#         <style>
#             body {
#                 font-family: 'Roboto', sans-serif;
#                 font-size: 20px !important;
#             }
#             input {
#                 font-size: 20px !important;
#             }
#         </style>
# """, unsafe_allow_html=True)
# password = st.text_input("Enter your password", type="password")

# if password:
#     score, suggestions = calculate_strength(password)
#     st.write(f"Password Strength Score: {score} out of 5")
#     st.progress(score / 5)
    
#     if suggestions:
#         st.info("🎯 Suggestions to improve your password:")
#         for suggestion in suggestions:
#             st.write("- " + suggestion)

import streamlit as st
import re
import random
import string

st.set_page_config(page_title="Password Fortress", page_icon="🔐", layout="centered")

# Custom CSS for more dynamic styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

.title {
    font-family: 'Poppins', sans-serif;
    font-size: 46px;
    font-weight: 700;
    color: #3498db;
    margin-bottom: 30px;
}

.password-input-label {
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    font-weight: 600;
}

.strength-label {
    font-family: 'Poppins', sans-serif;
    font-size: 20px;
    font-weight: 600;
    margin-top: 10px;
}

.suggestion-box {
    padding-left: 5px;
    margin-top: 20px;
    margin-bottom: 15px;
    border-left: 5px solid #3498db;
}

.suggestion-header {
    font-family: 'Poppins', sans-serif;
    font-size: 22px;
    font-weight: 600;
    color: #3498db;
}

.suggestion-item {
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    margin-bottom: 14px;
}

.stButton>button {
    display: block;
    font-family: 'Poppins', sans-serif;
    background-color:#3498db;
    color: white;
}
.stButton>button:hover {
    font-family: 'Poppins', sans-serif;
    display: block;
    box-shadow: 20px;
    color:#3498db;
    border:2px solid #3498db;
    background-color: white
}
.stButton>button:active {
    font-family: 'Poppins', sans-serif;
    display: block;
    box-shadow: 20px;
    color:#3498db;
    border:2px solid #3498db;
    background-color: white
}

.very-weak { color: #e74c3c; }
.weak { color: #e67e22; }
.moderate { color: #f1c40f; }
.strong { color: #2ecc71; }
.very-strong { color: #27ae60; }

.footer { text-align: center; padding: 20px; color: #3498db; margin-top: 80px; font-family: 'Poppins'; }

</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title" style="color:#3498db;"> 🔐🛡️ Password Fortress</h1>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Password Analyser", "Password Generator", "Security Tips", "FAQ"])
with tab1:
    st.markdown('<h1 class="title" style="color:#3498db;"> Password Analyser 🚀</h1>', unsafe_allow_html=True)


    # Security tips content

    st.markdown('<p class="password-input-label">Forge your password below:</p>', unsafe_allow_html=True)
    password = st.text_input("", type="password")


    strength_messages = {
        0: "Critically Vulnerable",
        1: "Highly Insecure",
        2: "Moderately Protected",
        3: "Well Fortified",
        4: "Virtually Impenetrable",
        5: "Fort Knox Certified"
    }

    # Calculate password strength
    def calculate_password_strength(password):
        score = 0
        
        if len(password) >= 8:
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[0-9]', password):
            score += 1
        if re.search(r'[^A-Za-z0-9]', password):
            score += 1
        if len(password) >= 12:
            score += 1
            
        return score

    if st.button("Analyze") or password:
        score = calculate_password_strength(password)
        
        # Determine CSS class based on score
        strength_class = ""
        if score <= 1:
            strength_class = "very-weak"
        elif score == 2:
            strength_class = "weak"
        elif score == 3:
            strength_class = "moderate"
        elif score == 4:
            strength_class = "strong"
        else:
            strength_class = "very-strong"
        
        st.markdown(f'<p class="strength-label">Security Rating: <span class="{strength_class}">{strength_messages[score]}</span> ({score} out of 5)</p>', unsafe_allow_html=True)
        
        st.progress(score/5)
        
        if score < 5 :
            st.markdown('<div class="suggestion-box"> <p class="suggestion-header">🛡️ Security Enhancement Recommendations:</p> </div>', unsafe_allow_html=True)
            
            
            if len(password) < 8:
                st.markdown('<p class="suggestion-item">• Extend your password to at least 8 characters - longer passwords are exponentially harder to crack</p>', unsafe_allow_html=True)
            
            if not re.search(r'[A-Z]', password):
                st.markdown('<p class="suggestion-item">• Fortify with uppercase letters - adding capitalization increases complexity</p>', unsafe_allow_html=True)
            
            if not re.search(r'[0-9]', password):
                st.markdown('<p class="suggestion-item">• Reinforce with numbers - numerical digits significantly strengthen your defense</p>', unsafe_allow_html=True)
            
            if not re.search(r'[^A-Za-z0-9]', password):
                st.markdown('<p class="suggestion-item">• Deploy special characters - symbols like @, #, ! create an additional layer of security</p>', unsafe_allow_html=True)
            
            if len(password) < 12:
                st.markdown('<p class="suggestion-item">• Aim for 12+ characters - maximum protection comes with length</p>', unsafe_allow_html=True)
        else:
            st.balloons() 
            st.markdown('<div class="suggestion-box"> <p class="suggestion-header">🔒 Your password is secured.</p> </div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<h1 class="title" style="color:#3498db;"> Password Generator 🚀</h1>', unsafe_allow_html=True)


    def generate_password(length, use_uppercase, use_numbers, use_symbols):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password


    st.markdown('<p class="password-input-label">Select password length::</p>', unsafe_allow_html=True)
    length = st.slider('', min_value=6, max_value=32, value=12)

    use_uppercase = st.checkbox('Include uppercase letters')
    use_numbers = st.checkbox('Include numbers')
    use_symbols = st.checkbox('Include symbols')

    # Generate password button
    if st.button('Generate Password'):
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        st.text_input('Generated Password:', value=password)

with tab3:
    st.markdown('<h1 class="title" style="color:#3498db;"> 🔒 Security Best Practices</h1>', unsafe_allow_html=True)

    st.markdown('<div class="suggestion-box"> <p class="suggestion-header">1️⃣ Use Strong Passwords</p> </div>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• Use at least 12+ characters (longer passwords are stronger).', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• Mix uppercase & lowercase letters (A-Z, a-z).', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• Include numbers (0-9) and special symbols (!@#$%^&*).', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• Avoid dictionary words or personal information (e.g., birthdays, names).', unsafe_allow_html=True)

    
    st.markdown('<div class="suggestion-box"> <p class="suggestion-header">2️⃣ Avoid Reusing Passwords</p> </div>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• Use different passwords for each account.', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• If one account gets hacked, others remain safe.', unsafe_allow_html=True)
    
    st.markdown('<div class="suggestion-box"> <p class="suggestion-header">3️⃣ Use a Password Manager</p> </div>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• Store complex passwords securely in a password manager (Bitwarden, 1Password, LastPass).', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">• This helps generate and manage strong passwords without memorizing them.', unsafe_allow_html=True)

with tab4:
    st.markdown('<h1 class="title" style="color:#3498db;">❓ Frequently Asked Questions (FAQ)</h1>', unsafe_allow_html=True)

    st.markdown('<p class="suggestion-header" style="margin-top:30px;">🔹 Why is having a strong password important?</p> ', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">A strong password protects your accounts from hackers and cybercriminals. Weak passwords make it easier for attackers to:</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Guess your credentials using common words or patterns.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Break into your accounts with brute-force attacks.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Steal sensitive data, including emails, bank details, and personal information.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">With a strong password, you reduce the risk of identity theft, hacking, and financial loss.</p>', unsafe_allow_html=True)

    st.markdown('<p class="suggestion-header" style="margin-top:30px;">🔹 Why should I add symbols, numbers, and mixed case letters in my password?</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">Adding symbols, numbers, and uppercase/lowercase letters makes passwords much harder to crack. Here\'s why:</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Symbols (&, @, %, !, #) add complexity, making it difficult for brute-force attacks.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Numbers (0-9) prevent common word-based attacks.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Mixing uppercase and lowercase letters increases the number of possible password combinations.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item"><b>For example:</b></p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">❌ Weak password: ilovecats (easy to guess)</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✅ Strong password: iL0v3C@ts!2 (much harder to crack)</p>', unsafe_allow_html=True)

    st.markdown('<p class="suggestion-header" style="margin-top:30px;">🔹 What happens if I use a weak password?</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">Weak passwords can be easily guessed, leading to:</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">❌ Hacked accounts (social media, banking, email).</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">❌ Identity theft (stealing your personal information).</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">❌ Financial loss (bank fraud, credit card theft).</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">❌ Loss of privacy (leaked emails, private messages, and photos).</p>', unsafe_allow_html=True)

    st.markdown('<p class="suggestion-header" style="margin-top:30px;">🔹 How do hackers steal passwords?</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">Hackers use different techniques to steal passwords, such as:</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Brute force attacks – Guessing passwords by trying millions of combinations.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Phishing – Tricking users into entering passwords on fake websites.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Keyloggers – Recording keystrokes to capture your password.</p>', unsafe_allow_html=True)
    st.markdown('<p class="suggestion-item">✔ Data breaches – Leaked passwords from hacked websites.</p>', unsafe_allow_html=True)



st.markdown("<div class='footer'> © 2025 Aqsa Saeed. All rights reserved. </div>", unsafe_allow_html=True)
