# AI-Powered Diagnostic Assistant

## Overview
The AI-Powered Diagnostic Assistant is a **machine learning-based application** that assists in medical diagnosis by analyzing **medical images** and **symptoms**. It provides automated insights and stores results in a database for future reference.

## Features
✅ **Upload Medical Images** for AI-based disease detection  
✅ **Enter Symptoms** to receive AI-generated diagnoses  
✅ **Store and Retrieve** past diagnosis records from MongoDB  
✅ **FastAPI Backend** for seamless data processing  
✅ **React.js Frontend** for an intuitive user experience  

## Technologies Used
- **Frontend**: React.js (Axios for API calls)
- **Backend**: FastAPI (Python, TensorFlow, Keras, MongoDB)
- **Database**: MongoDB (Local instance)

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo-link.git
cd ai-diagnostic-assistant
```

### 2. Set Up Backend (FastAPI)
#### Install dependencies
```sh
pip install fastapi uvicorn pymongo tensorflow keras numpy pillow python-multipart
```
#### Run MongoDB locally (Ensure MongoDB is installed)
```sh
mongod --dbpath /path/to/mongodb/data
```
#### Start the FastAPI server
```sh
uvicorn backend_setup:app --reload
```

### 3. Set Up Frontend (React.js)
#### Install dependencies
```sh
cd frontend
npm install
```
#### Start React.js
```sh
npm start
```

---

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/predict/image` | Upload an image for AI-based medical diagnosis |
| POST | `/predict/symptom` | Enter symptoms for AI-based diagnosis |

---

## Folder Structure
```
/ai-diagnostic-assistant
 ├── backend_setup.py    # FastAPI Backend
 ├── frontend_app.jsx    # React.js Frontend
 ├── README.md           # Documentation
 ├── medical_image_model.h5  # AI Model (Pretrained)
 ├── temp/               # Temporary storage for uploaded images
```

---

## Notes
- The **AI model (`medical_image_model.h5`)** must be pre-trained and stored in the backend directory.
- Ensure that the **MongoDB server** is running before starting the backend.
- Modify API endpoints in the **frontend** if hosting the backend separately.

## Contributors
- A.Hymavathi

## License
This project is open-source under the MIT License.

