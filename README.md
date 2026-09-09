# 🌿 Plant Leaf Disease Detection Using Deep Learning

> An AI-powered plant disease detection system that identifies plant diseases from leaf images using **Deep Learning, Transfer Learning, Computer Vision, FastAPI, and React**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?logo=keras)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv)
![Accuracy](https://img.shields.io/badge/Test%20Accuracy-95.93%25-success)

---

## 📌 About the Project

Plant diseases can significantly affect crop health and agricultural productivity. Early identification of diseases can help farmers and agricultural professionals take appropriate action before diseases spread.

This project uses **deep learning and transfer learning** to automatically classify plant leaf images into different disease categories.

The current system uses a **VGG16 model pretrained on ImageNet**, combined with the **PlantVillage dataset containing 38 classes**.

The trained machine learning model is integrated into a complete web application using:

* 🧠 VGG16 Transfer Learning
* 🐍 Python
* ⚡ FastAPI
* 👁️ OpenCV
* ⚛️ React
* ⚡ Vite
* 🔢 TensorFlow / Keras

The current M1 baseline model achieves approximately **95.93% test accuracy** on the PlantVillage test dataset.

---

# ✨ Key Features

### 🧠 AI Disease Detection

Upload a plant leaf image and let the trained deep learning model predict the most likely disease.

### 📊 Prediction Confidence

The system displays the model's confidence for the predicted class.

### 🥇 Top-3 Predictions

The application provides the top three classes predicted by the model.

### 📈 Model Accuracy

The application displays the overall test accuracy of the deployed model.

### 💡 Disease Recommendations

A structured recommendation layer provides guidance related to the detected disease.

### 🌱 38 PlantVillage Classes

The current M1 model supports 38 plant/disease categories.

### 🖥️ Full-Stack Application

The ML model is connected to a React frontend through a FastAPI backend.

---

# 🚀 How It Works

The complete system follows this pipeline:

```text
                USER
                  │
                  ▼
          React Frontend
                  │
                  ▼
        Upload Leaf Image
                  │
                  ▼
          FastAPI Backend
                  │
                  ▼
          OpenCV Processing
                  │
                  ▼
        VGG16 M1 Model
                  │
                  ▼
        Disease Prediction
                  │
          ┌───────┴────────┐
          ▼                ▼
      Confidence        Top-3 Results
          │                │
          └───────┬────────┘
                  ▼
        Disease Recommendation
                  │
                  ▼
          Results Interface
```

---

# 🧪 Machine Learning Pipeline

The machine learning workflow consists of:

```text
Kaggle Dataset
      ↓
Dataset Exploration
      ↓
Image Preprocessing
      ↓
Train / Validation / Test Split
      ↓
VGG16 Transfer Learning
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Classification Report
      ↓
Confusion Matrix
      ↓
Error Analysis
      ↓
Model Deployment
```

---

# 📚 Dataset

The primary dataset used for the current model is the **PlantVillage Splits dataset**.

### Dataset Information

| Property          |               Value |
| ----------------- | ------------------: |
| Dataset           | PlantVillage Splits |
| Total Images      |              54,305 |
| Training Images   |              37,997 |
| Validation Images |              10,859 |
| Test Images       |               5,449 |
| Number of Classes |                  38 |
| Image Size        |           224 × 224 |
| Image Channels    |                 RGB |

The dataset contains predefined training, validation, and testing splits.

---

# 🌿 Supported Plant Diseases

The current M1 model classifies images into 38 PlantVillage classes:

|  # | Class                                           |
| -: | ----------------------------------------------- |
|  1 | Apple — Apple Scab                              |
|  2 | Apple — Black Rot                               |
|  3 | Apple — Cedar Apple Rust                        |
|  4 | Apple — Healthy                                 |
|  5 | Blueberry — Healthy                             |
|  6 | Cherry — Powdery Mildew                         |
|  7 | Cherry — Healthy                                |
|  8 | Corn — Cercospora Leaf Spot / Gray Leaf Spot    |
|  9 | Corn — Common Rust                              |
| 10 | Corn — Northern Leaf Blight                     |
| 11 | Corn — Healthy                                  |
| 12 | Grape — Black Rot                               |
| 13 | Grape — Esca / Black Measles                    |
| 14 | Grape — Leaf Blight / Isariopsis Leaf Spot      |
| 15 | Grape — Healthy                                 |
| 16 | Orange — Huanglongbing / Citrus Greening        |
| 17 | Peach — Bacterial Spot                          |
| 18 | Peach — Healthy                                 |
| 19 | Pepper Bell — Bacterial Spot                    |
| 20 | Pepper Bell — Healthy                           |
| 21 | Potato — Early Blight                           |
| 22 | Potato — Late Blight                            |
| 23 | Potato — Healthy                                |
| 24 | Raspberry — Healthy                             |
| 25 | Soybean — Healthy                               |
| 26 | Squash — Powdery Mildew                         |
| 27 | Strawberry — Leaf Scorch                        |
| 28 | Strawberry — Healthy                            |
| 29 | Tomato — Bacterial Spot                         |
| 30 | Tomato — Early Blight                           |
| 31 | Tomato — Late Blight                            |
| 32 | Tomato — Leaf Mold                              |
| 33 | Tomato — Septoria Leaf Spot                     |
| 34 | Tomato — Spider Mites / Two-Spotted Spider Mite |
| 35 | Tomato — Target Spot                            |
| 36 | Tomato — Tomato Mosaic Virus                    |
| 37 | Tomato — Tomato Yellow Leaf Curl Virus          |
| 38 | Tomato — Healthy                                |

---

# 🧠 Model Architecture

## M1 — PlantVillage Baseline

The current deployed model is called:

**M1 — PlantVillage Baseline**

It uses **VGG16 pretrained on ImageNet** as the feature extraction backbone.

The convolutional layers of VGG16 are frozen, while a new classification head is trained for the 38 PlantVillage classes.

### Architecture

```text
Input Image
224 × 224 × 3
      │
      ▼
VGG16
ImageNet Pretrained
      │
      ▼
Frozen Convolutional Layers
      │
      ▼
Global Average Pooling
      │
      ▼
Dense Layer
256 Neurons + ReLU
      │
      ▼
Dropout
0.5
      │
      ▼
Dense Layer
38 Classes
      │
      ▼
Softmax
      │
      ▼
Prediction
```

### Classification Head

```text
GlobalAveragePooling2D
        ↓
Dense(256, ReLU)
        ↓
Dropout(0.5)
        ↓
Dense(38, Softmax)
```

The model also includes the VGG16 `preprocess_input` operation internally.

---

# 📊 Model Parameters

| Parameter Type           |      Count |
| ------------------------ | ---------: |
| Total Parameters         | 14,855,782 |
| Trainable Parameters     |    141,094 |
| Non-Trainable Parameters | 14,714,688 |

Most of the parameters belong to the pretrained and frozen VGG16 feature extractor.

---

# ⚙️ Training Configuration

| Configuration      | Value                           |
| ------------------ | ------------------------------- |
| Backbone           | VGG16                           |
| Pretrained Weights | ImageNet                        |
| Input Size         | 224 × 224 × 3                   |
| Batch Size         | 32                              |
| Maximum Epochs     | 10                              |
| Optimizer          | Adam                            |
| Learning Rate      | 0.001                           |
| Loss               | Sparse Categorical Crossentropy |
| Metric             | Accuracy                        |
| Random Seed        | 42                              |

### Training Callbacks

The following callbacks were used:

* ModelCheckpoint
* EarlyStopping
* ReduceLROnPlateau

The best validation-loss model was saved as:

```text
plantvillage_m1_baseline.keras
```

---

# 🏆 Model Performance

The M1 model achieved the following results:

| Metric                   |     Result |
| ------------------------ | ---------: |
| Best Validation Accuracy | **96.28%** |
| Test Accuracy            | **95.93%** |
| Test Loss                | **0.1268** |
| Macro Precision          |     0.9549 |
| Macro Recall             |     0.9341 |
| Macro F1                 |     0.9424 |
| Weighted Precision       |     0.9602 |
| Weighted Recall          |     0.9593 |
| Weighted F1              |     0.9590 |

### ⭐ Main Result

> **M1 PlantVillage Test Accuracy: 95.93%**

This means the model correctly classified approximately 95.93% of images in the PlantVillage test dataset.

---

# 📈 Model Evaluation

The model was evaluated using multiple metrics rather than accuracy alone.

Evaluation included:

* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report
* Confusion Matrix
* Per-class performance
* Error analysis
* Class imbalance analysis
* External image testing

---

# 🔍 Error Analysis

The confusion matrix was analyzed to understand where the model makes mistakes.

Some visually similar diseases created more confusion.

Examples include:

```text
Corn Gray Leaf Spot
        ↓
Corn Northern Leaf Blight
```

and:

```text
Tomato Spider Mites
        ↓
Tomato Target Spot
```

Other tomato diseases also showed confusion:

```text
Tomato Early Blight
       ↓
 ┌─────┼─────┬─────┐
 ▼     ▼     ▼     ▼
Bacterial  Target  Late  Septoria
Spot       Spot    Blight Leaf Spot
```

These errors are understandable because several plant diseases can produce visually similar symptoms on leaves.

---

# ⚠️ Dataset Class Imbalance

The PlantVillage dataset does not contain the same number of images for every class.

For example:

```text
Smallest training class:
Potato Healthy
106 images

Largest training class:
Orange Huanglongbing
3,854 images
```

This produces an approximate largest-to-smallest class ratio of:

**36.36 : 1**

Therefore, high overall accuracy does not necessarily mean that every class performs equally well.

Future versions can investigate:

* Class weighting
* Oversampling
* Targeted augmentation
* Balanced batches
* Additional data collection

---

# 🌎 Real-World Testing & Domain Shift

One important finding from the project was the difference between benchmark performance and real-world performance.

The model achieved:

> **95.93% accuracy on the PlantVillage test set**

However, an external real-world image of **Apple Cedar Apple Rust** was incorrectly classified as **Grape Black Rot** with approximately **92.08% confidence**.

This demonstrates an important machine learning concept:

## Domain Shift

```text
PlantVillage Images
       ↓
Training Distribution
       ↓
High Test Accuracy
```

versus:

```text
Real-World Images
       ↓
Different Distribution
       ↓
Potential Performance Drop
```

Real-world images can differ in:

* Background
* Lighting
* Camera quality
* Leaf position
* Image composition
* Distance
* Disease severity
* Environmental conditions

Therefore:

> **High PlantVillage test accuracy does not guarantee perfect real-world generalization.**

This limitation is an important part of the project's evaluation.

---

# 💻 Web Application

The trained M1 model has been integrated into a full-stack web application.

### Frontend

The frontend is built using:

* React
* Vite
* JavaScript
* HTML
* CSS

The frontend allows users to:

1. Upload a plant leaf image
2. Preview the image
3. Select the available model
4. Send the image for prediction
5. View the predicted disease
6. View prediction confidence
7. View top-3 predictions
8. View model test accuracy
9. View disease recommendations

---

# ⚡ Backend

The backend is built using:

* Python
* FastAPI
* Uvicorn
* TensorFlow
* Keras
* OpenCV
* NumPy
* Pillow

The backend handles:

* Model loading
* Image upload
* Image preprocessing
* Disease prediction
* Class mapping
* Confidence calculation
* Top-3 predictions
* Model accuracy information
* Recommendations

---

# 🔌 API Endpoints

## `GET /`

Health/status endpoint used to verify that the backend is running.

## `GET /model-status`

Returns information about the currently loaded model.

It can be used to verify:

* Model availability
* Model name
* Number of classes
* Model status

## `POST /predict`

Main prediction endpoint.

It accepts an uploaded plant leaf image and returns:

```text
Predicted Class
Confidence
Top-3 Predictions
Model Test Accuracy
Recommendation
```

---

# 🖼️ Image Processing Pipeline

The uploaded image is processed using OpenCV.

```text
Uploaded Image
      ↓
FastAPI
      ↓
OpenCV
      ↓
Color Conversion
      ↓
Resize to 224 × 224
      ↓
TensorFlow / Keras
      ↓
VGG16 preprocess_input
      ↓
M1 Model
      ↓
Prediction
```

### Important

The M1 model already contains the VGG16 `preprocess_input` operation.

Therefore, preprocessing should **not be applied twice** before prediction.

---

# 📊 Prediction Confidence vs Accuracy

The application displays both prediction confidence and model test accuracy.

These values have different meanings.

### Prediction Confidence

Confidence represents how strongly the model favors a particular class for one image.

For example:

```text
Prediction:
Tomato Early Blight

Confidence:
91.4%
```

This means the model assigned approximately 91.4% softmax probability to that class.

It does **not** mean the model is 91.4% accurate overall.

### Model Test Accuracy

The M1 model achieved:

```text
95.93%
```

test accuracy on the PlantVillage test set.

In simple terms:

```text
Confidence
= Model's belief about ONE image

Accuracy
= Model's performance across the TEST DATASET
```

A model can therefore produce a highly confident incorrect prediction.

---

# 💡 Recommendation System

After predicting a disease, the application provides structured guidance.

The recommendation pipeline is:

```text
Detected Disease
       ↓
Disease Information
       ↓
Suggested Action
       ↓
Preventive Guidance
```

The current recommendation system is a **rule-based / structured recommendation layer**.

It is not presented as a separately trained NLP model.

---

# 🔬 Four-Model Development Strategy

The project is designed around four machine learning experiments.

| Model  | Dataset                       | Classes | VGG16 Strategy        | Status      |
| ------ | ----------------------------- | ------: | --------------------- | ----------- |
| **M1** | PlantVillage                  |      38 | Frozen                | ✅ Completed |
| **M2** | PlantVillage                  |      38 | Blocks 4–5 Fine-Tuned | 🔄 Planned  |
| **M3** | PlantVillage + Rice + Cassava |      51 | Frozen                | 🔄 Planned  |
| **M4** | PlantVillage + Rice + Cassava |      51 | Blocks 4–5 Fine-Tuned | 🔄 Planned  |

This strategy allows comparison of two major variables:

1. Dataset size and class coverage
2. Transfer learning vs fine-tuning

---

# 🧪 M2 — Fine-Tuned VGG16

M2 will use the same 38 PlantVillage classes but fine-tune deeper VGG16 layers.

Planned configuration:

```text
VGG16 Blocks 1–3
        ↓
     Frozen

VGG16 Blocks 4–5
        ↓
    Trainable
```

The purpose is to allow deeper feature representations to adapt to plant disease-specific visual patterns.

---

# 🌾 Dataset Expansion — 38 → 51 Classes

A major future goal is to expand the system beyond the original 38 PlantVillage classes.

Two additional datasets are planned:

### Rice Leaf Diseases

Additional classes:

**8**

### Cassava Leaf Disease Classification

Additional classes:

**5**

Therefore:

```text
PlantVillage
38 classes
      +
Rice
8 classes
      +
Cassava
5 classes
      ↓
51 Classes
```

This creates the planned:

# 🌱 38 → 51 Class Expansion

The goal is to increase crop and disease coverage and move toward a broader plant disease recognition system.

---

# 🚀 Future Work

## 1. VGG16 Fine-Tuning

Complete M2 by fine-tuning VGG16 Blocks 4 and 5.

## 2. Expand Dataset

Integrate:

```text
PlantVillage → 38
Rice → 8
Cassava → 5
----------------
Total → 51
```

## 3. Train M3

Train the 51-class model using a frozen VGG16 backbone.

## 4. Train M4

Train the 51-class model with VGG16 Blocks 4 and 5 fine-tuned.

## 5. Compare All Four Models

Compare:

```text
M1 → 38 classes + Frozen VGG16

M2 → 38 classes + Fine-Tuned VGG16

M3 → 51 classes + Frozen VGG16

M4 → 51 classes + Fine-Tuned VGG16
```

Metrics will include:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Per-class performance
* Generalization performance

## 6. Improve Class Imbalance

Investigate:

* Class weights
* Oversampling
* Data augmentation
* Balanced batches
* Additional training data

## 7. Improve Real-World Generalization

Collect and train with images captured under:

* Different lighting conditions
* Different backgrounds
* Different cameras
* Different leaf orientations
* Different distances
* Natural agricultural environments

## 8. Webcam Detection

A future version could support real-time detection:

```text
Webcam
  ↓
Live Frame
  ↓
OpenCV
  ↓
Model
  ↓
Real-Time Prediction
```

## 9. Advanced Recommendation System

Future versions could include:

* Natural-language explanations
* Disease severity descriptions
* Treatment guidance
* Preventive measures
* Follow-up questions
* Farmer-oriented explanations

## 10. Better Confidence Handling

Future research could include:

* Confidence calibration
* Confidence thresholds
* Unknown-class detection
* Out-of-distribution detection

---

# 📁 Project Structure

```text
Plant-Disease/
│
├── backend/
│   ├── main.py
│   ├── plant_disease.py
│   ├── requirements.txt
│   └── plantvillage_m1_baseline.keras
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── plant_disease.py
│
├── plantvillage_m1_baseline.keras
│
└── README.md
```

> The exact project structure may evolve as additional models and datasets are integrated.

---

# 📦 Model File

### Current Model

```text
plantvillage_m1_baseline.keras
```

### Configuration

| Property      | Value                    |
| ------------- | ------------------------ |
| Model         | M1 PlantVillage Baseline |
| Backbone      | VGG16                    |
| Pretrained On | ImageNet                 |
| Classes       | 38                       |
| Input         | 224 × 224 × 3            |
| VGG16         | Frozen                   |
| Test Accuracy | 95.93%                   |
| File Size     | ~57.84 MB                |

The model is below GitHub's standard 100 MB individual file limit.

For larger future models or multiple model versions, **Git LFS** may be preferable.

---

# 🛠️ Installation

## Prerequisites

Make sure you have installed:

* Python 3.x
* Node.js
* npm
* Git

---

# 🐍 Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8002
```

Backend:

```text
http://127.0.0.1:8002
```

FastAPI documentation:

```text
http://127.0.0.1:8002/docs
```

---

# ⚛️ Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The Vite development server normally runs at:

```text
http://localhost:5173
```

---

# ▶️ Running the Application

### Step 1 — Start Backend

```bash
cd backend
uvicorn main:app --reload --port 8002
```

### Step 2 — Start Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

### Step 3 — Open the Application

Open the frontend URL provided by Vite.

### Complete Workflow

```text
Open Application
      ↓
Upload Plant Leaf Image
      ↓
Select M1 Model
      ↓
Click Predict
      ↓
Image Sent to FastAPI
      ↓
OpenCV Processes Image
      ↓
VGG16 M1 Performs Classification
      ↓
Prediction Returned
      ↓
Confidence + Top-3 Displayed
      ↓
Model Accuracy Displayed
      ↓
Recommendation Displayed
```

---

# 🧰 Technologies Used

## Machine Learning

* Python
* TensorFlow
* Keras
* VGG16
* ImageNet Transfer Learning
* NumPy
* Scikit-learn

## Computer Vision

* OpenCV
* Image preprocessing
* Image resizing
* RGB/BGR conversion

## Backend

* FastAPI
* Uvicorn
* Python
* TensorFlow / Keras

## Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

## Dataset

* PlantVillage Splits
* Rice Leaf Diseases Dataset — planned
* Cassava Leaf Disease Classification — planned

## Development Tools

* Google Colab
* VS Code
* Git
* GitHub

---

# 📌 Current Project Status

| Component                   | Status         |
| --------------------------- | -------------- |
| PlantVillage Dataset        | ✅ Completed    |
| Dataset Exploration         | ✅ Completed    |
| Class Imbalance Analysis    | ✅ Completed    |
| 38-Class Classification     | ✅ Completed    |
| VGG16 M1 Model              | ✅ Completed    |
| M1 Training                 | ✅ Completed    |
| M1 Evaluation               | ✅ Completed    |
| Classification Report       | ✅ Completed    |
| Confusion Matrix Analysis   | ✅ Completed    |
| Error Analysis              | ✅ Completed    |
| FastAPI Backend             | ✅ Completed    |
| React Frontend              | ✅ Completed    |
| Image Upload Prediction     | ✅ Completed    |
| Recommendation Layer        | ✅ Completed    |
| Model Accuracy Display      | ✅ Completed    |
| M2 Fine-Tuning              | 🔄 Planned     |
| Rice Dataset Integration    | 🔄 Planned     |
| Cassava Dataset Integration | 🔄 Planned     |
| 51-Class M3                 | 🔄 Planned     |
| 51-Class M4                 | 🔄 Planned     |
| Webcam Detection            | 🔮 Future Work |
| Advanced NLP Recommendation | 🔮 Future Work |

---

# 📈 Development Roadmap

```text
                    CURRENT
                       │
                       ▼
              M1 — 38 Classes
              Frozen VGG16
                       │
                       ▼
              M2 — 38 Classes
             Fine-Tuned VGG16
                       │
                       ▼
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
     Rice Dataset              Cassava Dataset
       +8 classes                 +5 classes
        │                             │
        └──────────────┬──────────────┘
                       ▼
              M3 — 51 Classes
              Frozen VGG16
                       │
                       ▼
              M4 — 51 Classes
             Fine-Tuned VGG16
                       │
                       ▼
          Improved Generalization
                       │
                       ▼
             Real-World Detection
```

---

# 🎯 Key Achievements

### Machine Learning

* 🌱 54,305 images
* 🌿 38 plant/disease classes
* 🧠 VGG16 transfer learning
* ⚙️ 14.86M total parameters
* 🏆 95.93% test accuracy

### Model Analysis

The project includes:

* Validation evaluation
* Test evaluation
* Classification report
* Precision
* Recall
* F1 Score
* Confusion matrix
* Error analysis
* Class imbalance analysis
* Domain-shift testing

### Application

The trained model has been integrated into:

```text
React
   ↓
FastAPI
   ↓
OpenCV
   ↓
TensorFlow / Keras
   ↓
VGG16
   ↓
Prediction
```

---

# 💡 Why This Project Matters

Plant disease detection is a practical application of artificial intelligence in agriculture.

This project demonstrates how a deep learning model can move from:

```text
Dataset
   ↓
Machine Learning Model
   ↓
Evaluation
   ↓
API
   ↓
Web Application
   ↓
End User
```

Rather than focusing only on model accuracy, the project also investigates:

* Dataset imbalance
* Similar disease classes
* Model confidence
* Domain shift
* Real-world generalization
* Model deployment
* Future dataset expansion

---

# 🔮 Long-Term Vision

The long-term objective is to develop a broader and more robust plant disease detection platform capable of recognizing diseases across a wider range of crops.

The planned evolution is:

```text
38 Classes
     ↓
51 Classes
     ↓
More Crops
     ↓
More Real-World Images
     ↓
Better Generalization
     ↓
Real-Time Detection
     ↓
Smarter Recommendations
```

---

# ⚠️ Limitations

The current system has several limitations:

### 1. Dataset Diversity

The primary model is trained on PlantVillage images, which may differ from real-world agricultural images.

### 2. Class Imbalance

The number of training images varies significantly between classes.

### 3. Similar Disease Appearance

Some diseases have visually similar symptoms, making classification difficult.

### 4. Limited Model Coverage

The current deployed model supports 38 PlantVillage classes.

### 5. No Webcam

The current application supports image upload only.

### 6. Confidence Does Not Guarantee Correctness

A model can produce a high-confidence prediction that is still incorrect.

### 7. Recommendation Layer

The current recommendation system is structured/rule-based rather than a separately trained NLP model.

---

# 📜 Disclaimer

This project is an **educational and experimental machine learning project**.

Predictions and recommendations should **not** be treated as professional agricultural or plant pathology advice.

The current model is trained primarily on the PlantVillage dataset and may perform differently on real-world images due to differences in:

* Image quality
* Lighting
* Background
* Plant varieties
* Disease severity
* Camera conditions
* Environmental conditions

For important agricultural decisions, predictions should be verified by a qualified agricultural or plant pathology professional.

---

# 👨‍💻 Project Status

**Current Version:** M1 — PlantVillage Baseline

**Model:** VGG16 Transfer Learning

**Dataset:** PlantVillage

**Classes:** 38

**Test Accuracy:** **95.93%**

**Application:** React + FastAPI

**Status:** 🚀 Working Prototype

---

# ⭐ Future Goal

> **Build a robust AI-powered plant disease detection platform that can identify diseases across multiple crops, generalize to real-world images, and provide useful, understandable guidance to users.**

---

## ⭐ If You Find This Project Useful

If you find this project interesting or useful, consider giving the repository a ⭐ **Star** on GitHub!