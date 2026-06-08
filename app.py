import streamlit as st

# অ্যাপের সাইডবারে বা মূল পেজে নমুনা প্রশ্নের সেকশন
st.sidebar.markdown("### 💡 স্যারদের টেস্ট করার জন্য নমুনা প্রশ্ন (Sample Questions)")
st.sidebar.write("যেকোনো একটি বাটনে ক্লিক করে পরীক্ষা করুন:")

# ১. বাংলা প্রশ্ন
if st.sidebar.button("১. ধান গাছের পাতা হলুদ হলে কী করব?"):
    st.info("**প্রশ্ন:** ধান গাছের পাতা হলুদ হলে কী করব?")
    st.success("**কৃষক বন্ধু AI:** ধান গাছের পাতা মূলত নাইট্রোজেনের অভাবে হলুদ হতে পারে। এর সমাধান হলো সঠিক নিয়মে ইউরিয়া সার উপরিপ্রয়োগ করা। এছাড়া দস্তা বা জিংকের অভাব হলেও এমন হতে পারে। নিশ্চিত হতে আপনি গাছের পাতার একটি ছবি আপলোড করতে পারেন।")

# ২. বাংলিশ প্রশ্ন
if st.sidebar.button("২. Poka domon korbo kemne?"):
    st.info("**Question:** Poka domon korbo kemne?")
    st.success("**কৃষক বন্ধু AI:** ফসলের পোকা দমনের জন্য প্রাথমিক অবস্থায় নিম পাতার রস বা নিম তেল স্প্রে করতে পারেন (জৈব পদ্ধতি)। আক্রমণ বেশি হলে কৃষি কর্মকর্তার পরামর্শ অনুযায়ী সঠিক কীটনাশক পরিমাণমতো স্প্রে করতে হবে।")

# ৩. ইংরেজি প্রশ্ন
if st.sidebar.button("৩. What is the purpose of this website?"):
    st.info("**Question:** What is the purpose of this website?")
    st.success("**Krishok Bondhu AI:** The purpose of this AI project is to assist our local farmers in identifying crop diseases, managing pests, and getting expert fertilizer recommendations instantly using AI, Image, and Audio tools.")

# ৪. প্রজেক্ট নিয়ে আরেকটি বাংলিশ প্রশ্ন
if st.sidebar.button("৪. Ei website ti ke banayeche?"):
    st.info("**Question:** Ei website ti ke banayeche?")
    st.success("**কৃষক বন্ধু AI:** এই ওয়েবসাইটটি আমি (আপনার নাম ও ক্লাস লিখবে) আমার স্কুলের বিজ্ঞান মেলার প্রজেক্ট হিসেবে তৈরি করেছি। এটি তৈরিতে Python, Streamlit এবং AI প্রযুক্তি ব্যবহার করা হয়েছে।")