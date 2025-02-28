from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import numpy as np
from io import BytesIO
from PIL import Image
import uvicorn
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load model with absolute path
Model = tf.keras.models.load_model(r"D:\ml\PlantVillage\models\model_1.h5", compile=False)

# Class labels
class1 = ["Early Blight", "Late Blight", "Healthy"]

def read(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).convert("RGB")  # Convert to RGB
    return np.array(image)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    print("Received file:", file.filename)
    
    image = read(await file.read())
    img_batch = np.expand_dims(image, 0)

    print("Image shape:", img_batch.shape)

    predictions = Model.predict(img_batch)
    print("Predictions:", predictions)

    predicted_class = class1[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    print("Predicted Class:", predicted_class, "Confidence:", confidence)

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
