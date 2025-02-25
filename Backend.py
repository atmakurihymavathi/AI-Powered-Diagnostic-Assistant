from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import uvicorn
import io

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["ai_diagnostic_db"]
collection = db["diagnosis_records"]

# Load AI Model
model = load_model("medical_image_model.h5")

# Preprocess Image for AI Model
def preprocess_image(image: Image.Image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    result = "Positive" if prediction[0][0] > 0.5 else "Negative"
    collection.insert_one({"type": "image", "result": result})
    return {"diagnosis": result}

@app.post("/predict/symptom")
async def predict_symptom(symptoms: str = Form(...)):
    # Mock symptom diagnosis (Replace with AI model if needed)
    result = "Flu" if "fever" in symptoms.lower() else "Unknown Condition"
    collection.insert_one({"type": "symptom", "result": result})
    return {"diagnosis": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

