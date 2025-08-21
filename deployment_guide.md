# 🎂 **Birthday Surprise Website - Deployment Guide**

## 🚀 **How to Set Up and Run**

### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 2: Run the App**
```bash
streamlit run birthday_surprise_app.py
```

### **Step 3: Share with Her**
The app will open at `http://localhost:8501`

To make it accessible from anywhere:
```bash
streamlit run birthday_surprise_app.py --server.port 8501 --server.address 127.0.0.1
```

## 🌐 **Deploy Online (Free Options)**

### **Option 1: Streamlit Community Cloud (Recommended)**
1. Upload your files to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Deploy instantly!

### **Option 2: Heroku (Free Tier)**
1. Create `Procfile`: 
   ```
   web: sh setup.sh && streamlit run birthday_surprise_app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [general]\n\
   email = \"your-email@domain.com\"\n\
   " > ~/.streamlit/credentials.toml
   echo "\
   [server]\n\
   headless = true\n\
   enableCORS=false\n\
   port = $PORT\n\
   " > ~/.streamlit/config.toml
   ```
3. Deploy to Heroku

### **Option 3: Railway**
1. Connect GitHub repo
2. Auto-deploy with zero configuration

## 🎁 **Features Included:**

✅ **24-Hour Countdown** to September 4th  
✅ **Bengali Song Integration** (your special 80s song)  
✅ **Love Story Timeline** with mathematical equations  
✅ **Fun Quiz** about your relationship  
✅ **Digital Art Gallery** with drawing canvas  
✅ **Dream Travel Map** with destinations  
✅ **Mathematical Love** equations and graphs  
✅ **Virtual Birthday Gifts** to unwrap  
✅ **Dark Green Theme** (her favorite color)  
✅ **Mobile-Friendly** design  

## 💚 **Personal Touches:**

- Interview-style proposal story
- Village girl + studious boy theme  
- Long-distance relationship elements
- Art and mathematics combination
- Bengali cultural references
- Your transformation from logical to romantic

## 🎵 **Background Music:**
The app includes a link to your special Bengali song. For auto-play, you might need to add browser-specific code.

## 📱 **Mobile Optimization:**
The website is fully responsive and works beautifully on phones!

---

**🎉 Your girlfriend will absolutely LOVE this personalized surprise! Every detail has been crafted with your unique love story in mind.**

*Happy Birthday to her! 💚*