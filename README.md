# GPT Teaching Assistant - Software Engineering Intern Assignment

## 🚀 Overview
This project is a **GPT-powered Teaching Assistant** for **Data Structures and Algorithms (DSA)** problems. The application provides a chat-based interface where users can submit a **LeetCode problem link** along with their **doubts or questions**. The assistant, powered by GPT, responds with **guidance, hints, and intuition-building prompts**, ensuring users develop a deeper understanding of the problem **without receiving direct solutions**.

## 🎯 Objective
The goal of this project is to create an **interactive and user-friendly chat interface** that effectively integrates GPT to **assist users in solving DSA problems independently**. The assistant engages in meaningful dialogue, encouraging **critical thinking and problem-solving skills**.

---
## 📌 Features
### **1️⃣ User Interface**
✅ **Clean & Intuitive Chat UI**
   - Users can **submit** a LeetCode problem link.
   - Users can **ask doubts** related to the problem.
   - Users can **view responses** from the GPT-based assistant.
✅ **Modern Design with Vanilla CSS**
   - Uses **proper padding, big fonts, and a color scheme** for a visually appealing experience.
   - Messages from **users and the assistant** are visually distinguished.
   - The UI **automatically scrolls** to show the latest messages.

### **2️⃣ GPT Integration**
✅ **Backend communicates with GPT** to generate responses.
✅ **Ensures meaningful engagement** by guiding users towards the solution.
✅ **Avoids direct answers**, instead focusing on:
   - **Guiding questions**
   - **Hints and insights**
   - **Related examples** to aid understanding

### **3️⃣ Thoughtful Prompt Management**
✅ **Custom-crafted prompts** designed to encourage **deeper understanding** and **logical progression** in problem-solving.
✅ **Ensures that responses are engaging and encourage self-learning**.

---
## 🏗️ Project Architecture
```
📂 GPT-Teaching-Assistant
│── 📂 backend
│   │── app.py              # Flask server handling GPT integration
│   │── requirements.txt    # Dependencies for the backend
│
│── 📂 frontend
│   │── src
│   │   │── App.js          # React frontend with chat UI
│   │   │── App.css         # Vanilla CSS for styling
│   │   │── index.js        # React entry point
│   │── public
│   │── package.json        # Frontend dependencies
│
│── README.md               # Documentation
│── .gitignore              # Ignore unnecessary files
```

---
## 🛠️ Setup Instructions
### **1️⃣ Backend (Flask Server)**
#### **📌 Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```
#### **📌 Run the Flask server**
```bash
python app.py
```

### **2️⃣ Frontend (React Application)**
#### **📌 Install dependencies**
```bash
cd frontend
npm install
```
#### **📌 Start the React app**
```bash
npm start
```
The application will be accessible at **`http://localhost:3000`**.

---
## 📖 How to Use the Application
1. **Enter the LeetCode problem URL** in the input field.
2. **Type your doubt or question** related to the problem.
3. **Submit the form**, and the GPT assistant will generate a helpful response.
4. **The response will guide you** with hints and explanations **without revealing the direct solution**.

---
## 🤖 How GPT Integration Works
1. **User submits a LeetCode problem URL and a question.**
2. **Frontend sends the request to Flask backend.**
3. **Flask backend calls GPT API** with a **structured prompt**.
4. **GPT processes the query** and generates a meaningful response.
5. **Flask returns the response** to the frontend.
6. **User sees a structured and intuitive answer** guiding them toward the solution.

---
## 📊 Evaluation Criteria
✅ **Functionality** - The application meets all requirements and works seamlessly.
✅ **Code Quality** - Well-organized, **modular**, and **follows best practices**.
✅ **Innovative Prompts** - The assistant **engages users effectively** through meaningful and thought-provoking hints.

---
## 📌 Submission Guidelines
This project is hosted on **GitHub**. The repository contains:
- ✅ **Complete source code (Frontend & Backend)**
- ✅ **README with detailed documentation**
- ✅ **Setup instructions & architecture explanation**

---
## 🔥 Future Enhancements
🚀 **Enhance UI with animations** for a more engaging experience.
🚀 **Support for multiple problem sources** like CodeForces, CodeChef, etc.
🚀 **Improve GPT prompt engineering** for even more insightful responses.

---
## 🏆 Conclusion
This project successfully integrates **AI-powered assistance** into DSA problem-solving, providing a **structured, user-friendly, and interactive** experience that enhances learning. 🎯

💡 **Let's make problem-solving smarter, not harder!** 🚀

