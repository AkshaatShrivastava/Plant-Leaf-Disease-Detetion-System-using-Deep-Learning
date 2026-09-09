import os
import cv2
import numpy as np
import keras
from keras.applications.vgg16 import preprocess_input

from classes import CLASS_NAMES, get_display_name
from recommendations import get_recommendation

# Path to the trained .keras model
MODEL_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "models", "plantvillage_m1_baseline.keras")
)

# Verified Model Metadata from M1 experiment
MODEL_METADATA = {
    "name": "VGG16 Transfer Learning",
    "test_accuracy": 95.93,
    "test_dataset": "PlantVillage",
    "num_classes": 38,
    "input_size": "224x224"
}

# Global model instance stored in memory
_model = None

def load_trained_model():
    """
    Loads the trained Keras 3 model once into memory.
    Handles Lambda(preprocess_input) deserialization safely.
    """
    global _model
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

    print(f"Loading trained model from {MODEL_PATH}...")
    _model = keras.models.load_model(
        MODEL_PATH,
        custom_objects={"preprocess_input": preprocess_input},
        safe_mode=False
    )
    print("Trained model successfully loaded into memory!")
    return _model

def get_model():
    """Returns the loaded model instance."""
    global _model
    if _model is None:
        return load_trained_model()
    return _model

def get_model_info():
    """Returns model metadata and status."""
    global _model
    if _model is None:
        return {
            "loaded": False,
            "status": "Model not loaded",
            "model_path": MODEL_PATH,
            **MODEL_METADATA
        }

    return {
        "loaded": True,
        "status": "Trained model is loaded and ready",
        "model_file": os.path.basename(MODEL_PATH),
        "input_shape": list(_model.input_shape) if hasattr(_model, "input_shape") else None,
        "output_classes": len(CLASS_NAMES),
        "total_parameters": _model.count_params() if hasattr(_model, "count_params") else None,
        **MODEL_METADATA
    }

def predict_image(image_bytes: bytes) -> dict:
    """
    Inference pipeline for uploaded plant leaf images:
    1. Decode image bytes using OpenCV (BGR).
    2. Validate decoded image.
    3. Convert BGR to RGB.
    4. Resize to exactly 224x224.
    5. Cast to float32 NumPy array and expand batch dimension (1, 224, 224, 3).
    6. Pass directly to model.predict() without external preprocess_input.
    7. Return Top-1, Top-3, Disease Recommendations, and Model Test Metadata.
    """
    model = get_model()

    # 1. Decode raw bytes with OpenCV
    nparr = np.frombuffer(image_bytes, np.uint8)
    image_bgr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 2. Validation
    if image_bgr is None or image_bgr.size == 0:
        raise ValueError("Image decoding failed. The provided file is corrupted or not a valid image format.")

    # 3. Convert OpenCV BGR to RGB
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # 4. Resize to expected model input dimensions (224, 224)
    image_resized = cv2.resize(image_rgb, (224, 224), interpolation=cv2.INTER_AREA)

    # 5. Format tensor: float32, range [0, 255], batch shape (1, 224, 224, 3)
    image_batch = np.expand_dims(image_resized.astype(np.float32), axis=0)

    # 6. Model prediction (internal Lambda layer performs VGG16 preprocess_input)
    probabilities = model.predict(image_batch, verbose=0)[0]

    # 7. Extract Top-3 indices sorted by confidence descending
    top_indices = np.argsort(probabilities)[::-1][:3]

    top_3 = []
    for idx in top_indices:
        class_name = CLASS_NAMES[idx]
        confidence = float(probabilities[idx] * 100.0)
        top_3.append({
            "class_name": class_name,
            "display_name": get_display_name(class_name),
            "confidence": round(confidence, 2)
        })

    top_prediction = top_3[0]
    recommendation_data = get_recommendation(top_prediction["class_name"])

    return {
        "success": True,
        "prediction": top_prediction,
        "top_3": top_3,
        "recommendation": recommendation_data,
        "model_info": MODEL_METADATA
    }
