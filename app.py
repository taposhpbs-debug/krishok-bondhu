import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page configuration
st.set_page_config(page_title="Krishok Bondhu AI", page_icon="🌾", layout="wide")

# Title and Top Section
st.title("🌾 কৃষক বন্ধু AI (Krishok Bondhu AI)")
st.write("An AI-powered agricultural assistant for Bangladeshi farmers to detect crop diseases and get instant solutions.")

# Gemini API key configuration with safe fallback
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    model = None

# Expanded Q&A List (Bangla, English, and Banglish)
faqs = [
    {
        "btn": "১. ধান গাছের পাতা হলুদ হলে কী করব?", 
        "q": "ধান গাছের পাতা হলুদ হলে কী করব?", 
        "a": "ধান গাছের পাতা মূলত নাইট্রোজেনের অভাবে হলুদ হতে পারে। এর সমাধান হলো সঠিক নিয়মে ইউরিয়া সার উপরিপ্রয়োগ করা। এছাড়া দস্তা বা জিংকের অভাব হলেও এমন হতে পারে। নিশ্চিত হতে আপনি গাছের পাতার একটি ছবি আপলোড করতে পারেন।"
    },
    {
        "btn": "২. Poka domon korbo kemne?", 
        "q": "Poka domon korbo kemne?", 
        "a": "Fosler poka domon korar jonne prathmik bhabe neem pata ba neem tel spray korte paren (joibo poddhoti). Akromon beshi hole krishi kormokortar poramorsho naye sothik kitnashok porimanmoto spray korun."
    },
    {
        "btn": "৩. What is the purpose of this website?", 
        "q": "What is the purpose of this website?", 
        "a": "The purpose of this AI project is to assist our local farmers in identifying crop diseases, managing pests, and getting expert fertilizer recommendations instantly using AI and Image analysis tools."
    },
    {
        "btn": "৪. Ei website ti ke banayeche?", 
        "q": "Ei website ti ke banayeche?", 
        "a": "Ei website ti ami amar school er science project hisebe baniyechi (Class 9). Eti toirite Python, Streamlit ebong Gemini AI projukti bhabohar kora hoyeche."
    },
    {
        "btn": "৫. আলুর মড়ক রোগ (Late Blight) হলে কী করণীয়?", 
        "q": "আলুর মড়ক রোগ (Late Blight) হলে কী করণীয়?", 
        "a": "আলুর মড়ক বা লেট ব্লাইট একটি মারাত্মক ছত্রাকজনিত রোগ। প্রতিকারের জন্য ম্যানকোজেব গ্রুপের ছত্রাকনাশক (যেমন: ডাইথেন এম-৪৫) প্রতি লিটার পানিতে ২ গ্রাম মিশিয়ে ৭-১০ দিন পর পর স্প্রে করতে হবে।"
    },
    {
        "btn": "৬. Tomato pata kokeye gele ki korbo?", 
        "q": "Tomato pata kokeye gele ki korbo?", 
        "a": "Tomato pata kokeye jaoa (Leaf Curl) hoche ekta virus jonito rog, jaha mukhoto Shada Makhi (Whitefly) dara choraye. Er jonne kitnashok spray kore Shada Makhi domon kore hobe."
    },
    {
        "btn": "৭. How to get better soil fertility?", 
        "q": "How to get better soil fertility?", 
        "a": "To improve soil fertility, practice crop rotation, use organic compost like cow dung or vermicompost, avoid excessive chemical fertilizers, and test your soil pH regularly."
    },
    {
        "btn": "৮. খরা বা অনাবৃষ্টিতে ফসলের যত্ন কীভাবে নেব?", 
        "q": "খরা বা অনাবৃষ্টিতে ফসলের যত্ন কীভাবে নেব?", 
        "a": "খরা परिस्थितियों মাটির আর্দ্রতা ধরে রাখতে গাছের গোড়ায় খড়, শুকনা পাতা বা মালচিং পেপার ব্যবহার করা অত্যন্ত কার্যকরী। এতে সেচ কম লাগে।"
    }
]

# Sidebar layout
st.sidebar.markdown("### 💡 স্যারদের টেস্ট করার জন্য নমুনা প্রশ্ন (Sample Questions)")
st.sidebar.write("Jekono ekta bhatone click kore porikkha korun:")

selected_q = None
selected_a = None

# Generate Sidebar Buttons
for faq in faqs:
    if st.sidebar.button(faq["btn"]):
        selected_q = faq["q"]
        selected_a = faq["a"]

# Main Interface split into 2 columns (Left for Image, Right for Chat)
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 ফসলের রোগ নির্ণয় (Image Upload)")
    uploaded_file = st.file_uploader("Fosler ba gacher patar chobi upload korun...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button("রোগ সনাক্ত করুন (Analyze Image)"):
            if model:
                with st.spinner("AI chobi ti porikkha korche..."):
                    try:
                        response = model.generate_content(["Identify the plant disease and provide a solution in Bengali language.", image])
                        st.success(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.info("**কৃষক বন্ধু AI (Demo):** ছবি সফলভাবে আপলোড হয়েছে। ডেমো মোডে সম্পূর্ণ কাজ দেখানোর জন্য দয়া করে সাইডবারের বাটনগুলো ব্যবহার করুন।")

with col2:
    st.header("💬 চ্যাটবট সহকারী (Ask AI)")
    
    # If a sidebar button is clicked, show the answer instantly
    if selected_q and selected_a:
        st.info(f"**Question:** {selected_q}")
        st.success(f"**কৃষক বন্ধু AI:** {selected_a}")
    
    # Text input for manual typing
    user_input = st.text_input("Apnar prosno ti eikhane likhun (Type your question):")
    if st.button("Send 🚀") and user_input:
        st.info(f"**You:** {user_input}")
        if model:
            with st.spinner("AI chinta korche..."):
                try:
                    response = model.generate_content(user_input + " (Answer in short and clean Bengali)")
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.success(f"**কৃষক বন্ধু AI (Demo Mode):** আপনার প্রশ্নটি পেয়েছি: '{user_input}'। স্কুলের বিজ্ঞান মেলার প্রদর্শনের জন্য সাইডবারের বাটনগুলো ব্যবহার করতে পারেন!")