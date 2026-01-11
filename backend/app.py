from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io 

app = FastAPI()

# CORS (connect frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = tf.keras.models.load_model("3.keras")
class_name = ["Early Blight", "Late Blight", "Healthy"]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(io.BytesIO(data)))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = read_file_as_image(await file.read())

    img_batch = np.expand_dims(img,0)
    

    prediction = model.predict(img_batch)
    predicted_class = class_name[np.argmax(prediction[0])]
    confidence = round(float(np.max(prediction[0])) * 100, 2)

    return {
        "prediction": predicted_class,
        "confidence": confidence
    }


@app.post("/predicts")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes)).resize((224, 224))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_name[np.argmax(prediction)]
    confidence = round(float(np.max(prediction)) * 100, 2)

    return {
        "prediction": predicted_class,
        "confidence": confidence
    }
