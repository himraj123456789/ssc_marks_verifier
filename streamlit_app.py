import streamlit as st
import string

# 26 emojis for 26 English letters
emojis = [
    "😀", "😁", "😂", "🤣", "😃", "😄",
    "😅", "😆", "😉", "😊", "😋", "😎",
    "😍", "😘", "🥰", "😗", "😙", "😚",
    "🙂", "🤗", "🤩", "🤔", "🤨", "😐",
    "😑", "😶"
]

# Create mapping dictionary
letter_to_emoji = {letter: emoji for letter, emoji in zip(string.ascii_lowercase, emojis)}
letter_to_emoji[" "] = " "  # space maps to space
emoji_to_letter = {emoji: letter for letter, emoji in letter_to_emoji.items()}

# Encrypt function
def encrypt(text: str) -> str:
    return "".join(letter_to_emoji.get(ch.lower(), ch) for ch in text)

# Decrypt function
def decrypt(emoji_text: str) -> str:
    return "".join(emoji_to_letter.get(ch, ch) for ch in emoji_text)

# Streamlit App
st.title("🔐 Emoji Encryptor & Decryptor")

# Text input
user_input = st.text_area("Enter your text or emoji message:")

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Encrypt"):
        if user_input.strip():
            encrypted = encrypt(user_input)
            st.success(f"🔒 Encrypted: {encrypted}")
        else:
            st.warning("⚠️ Please enter some text to encrypt.")

with col2:
    if st.button("Decrypt"):
        if user_input.strip():
            decrypted = decrypt(user_input)
            st.success(f"🔓 Decrypted: {decrypted}")
        else:
            st.warning("⚠️ Please enter some emoji text to decrypt.")
