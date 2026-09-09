from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from model import load_trained_model, get_model_info, predict_image

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler to load the model once on startup."""
    print("Application startup: Loading trained model...")
    load_trained_model()
    yield
    print("Application shutdown.")

# Initialize FastAPI application
app = FastAPI(
    title="Plant Disease Classification API",
    description="API for classifying plant leaf diseases using deep learning",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Root health check endpoint."""
    return {
        "status": "online",
        "message": "Plant Disease Classification API is running"
    }

@app.get("/model-status")
def model_status():
    """Endpoint to check the status and metadata of the loaded model."""
    return get_model_info()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Accepts an uploaded plant leaf image and returns the predicted disease class
    along with Top-3 probability rankings.
    """
    # 1. Validate file presence
    if not file or not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No image file provided. Please upload an image."
        )

    # 2. Read image bytes
    try:
        image_bytes = await file.read()
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to read uploaded file: {str(e)}"
        )

    if not image_bytes or len(image_bytes) == 0:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty. Please upload a valid image file."
        )

    # 3. Perform prediction using OpenCV pipeline and trained model
    try:
        result = predict_image(image_bytes)
        return result
    except ValueError as val_err:
        raise HTTPException(
            status_code=400,
            detail=str(val_err)
        )
    except Exception as err:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction encountered an internal error: {str(err)}"
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)
