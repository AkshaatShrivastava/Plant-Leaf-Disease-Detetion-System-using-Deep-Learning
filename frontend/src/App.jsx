import React, { useState, useRef, useEffect } from 'react';
import { 
  Sprout, 
  UploadCloud, 
  Image as ImageIcon, 
  X, 
  RefreshCw, 
  AlertTriangle, 
  CheckCircle2, 
  Layers, 
  Grid, 
  Maximize2,
  Loader2,
  BarChart3,
  AlertCircle,
  Award,
  ClipboardCheck,
  ShieldAlert,
  ShieldCheck,
  Info
} from 'lucide-react';

const API_BASE_URL = 'http://127.0.0.1:8002';
const ALLOWED_TYPES = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];

// Helper to extract plant name and clean condition from class name
function parseClassDetails(className, displayName) {
  if (!className) return { plant: 'Unknown Plant', condition: 'Unknown Condition', isHealthy: false };
  
  const parts = className.split('___');
  const rawPlant = parts[0] || 'Unknown Plant';
  const rawCondition = parts[1] || '';

  const plantName = rawPlant
    .replace('Pepper,_bell', 'Bell Pepper')
    .replace('Corn_(maize)', 'Corn (Maize)')
    .replace('Cherry_(including_sour)', 'Cherry')
    .replace(/_/g, ' ');

  const isHealthy = rawCondition.toLowerCase().includes('healthy');
  
  let conditionName = rawCondition
    .replace(/_/g, ' ')
    .trim();
  
  if (isHealthy) {
    conditionName = 'Healthy Plant';
  } else if (!conditionName) {
    conditionName = displayName || 'Disease Detected';
  }

  return {
    plant: plantName,
    condition: conditionName,
    isHealthy
  };
}

export default function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [isDragActive, setIsDragActive] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [predictionData, setPredictionData] = useState(null);
  const fileInputRef = useRef(null);
  const resultsRef = useRef(null);

  // Clean up object URLs to prevent memory leaks
  useEffect(() => {
    return () => {
      if (previewUrl) {
        URL.revokeObjectURL(previewUrl);
      }
    };
  }, [previewUrl]);

  // Scroll to results when prediction completes
  useEffect(() => {
    if (predictionData && resultsRef.current) {
      resultsRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }, [predictionData]);

  const processFile = (file) => {
    setError(null);
    setPredictionData(null);

    if (!file) return;

    // Validate file type
    if (!ALLOWED_TYPES.includes(file.type.toLowerCase())) {
      setError('Unsupported file type. Please select a valid JPG, JPEG, PNG, or WEBP image.');
      return;
    }

    // Clean up previous URL
    if (previewUrl) {
      URL.revokeObjectURL(previewUrl);
    }

    const objectUrl = URL.createObjectURL(file);
    setSelectedFile(file);
    setPreviewUrl(objectUrl);
  };

  const handleFileInput = (e) => {
    if (e.target.files && e.target.files[0]) {
      processFile(e.target.files[0]);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragActive(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragActive(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      processFile(e.dataTransfer.files[0]);
    }
  };

  const handleRemoveImage = () => {
    if (previewUrl) {
      URL.revokeObjectURL(previewUrl);
    }
    setSelectedFile(null);
    setPreviewUrl(null);
    setError(null);
    setPredictionData(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const triggerFileInput = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  const handleAnalyze = async () => {
    if (!selectedFile) {
      setError('Please select or upload a plant leaf image first.');
      return;
    }

    setError(null);
    setIsLoading(true);

    try {
      const formData = new FormData();
      formData.append('file', selectedFile);

      const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        let errorMessage = 'An error occurred during prediction.';
        try {
          const errorData = await response.json();
          errorMessage = errorData.detail || errorMessage;
        } catch {
          errorMessage = `Server returned status code ${response.status} (${response.statusText})`;
        }
        throw new Error(errorMessage);
      }

      const data = await response.json();
      if (!data.success || !data.prediction) {
        throw new Error('Invalid prediction format received from server.');
      }

      setPredictionData(data);
    } catch (err) {
      console.error('Prediction request failed:', err);
      if (err.name === 'TypeError' && err.message.includes('fetch')) {
        setError('Unable to connect to the backend prediction API at http://127.0.0.1:8002. Please ensure the FastAPI server is running.');
      } else {
        setError(err.message || 'Failed to analyze the leaf image. Please try again.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const topPredictionDetails = predictionData?.prediction 
    ? parseClassDetails(predictionData.prediction.class_name, predictionData.prediction.display_name) 
    : null;

  const recommendation = predictionData?.recommendation;
  const modelInfo = predictionData?.model_info;

  return (
    <div className="app-container">
      {/* Header */}
      <header className="header">
        <div className="header-content">
          <div className="brand">
            <div className="brand-icon">
              <Sprout size={24} />
            </div>
            <div className="brand-text">
              <h1>Plant Disease Detection</h1>
              <p>Deep Learning Project</p>
            </div>
          </div>
          <div className="college-badge">
            <Layers size={14} />
            <span>VGG16 Model</span>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="main-content">
        {/* Hero Section */}
        <section className="hero-section">
          <div className="hero-pill">
            <Sprout size={15} />
            <span>Plant Disease Detection</span>
          </div>
          <h2 className="hero-title">
            Detect Plant Leaf Diseases with <span>Deep Learning</span>
          </h2>
          <p className="hero-subtitle">
            Upload a plant leaf image to identify the plant and its potential disease or health condition using deep learning.
          </p>
        </section>

        {/* Main Card: Image Upload & Preview */}
        <section className="app-card">
          {error && (
            <div className="alert-banner alert-error" style={{ marginBottom: '1.25rem' }}>
              <AlertTriangle size={20} style={{ flexShrink: 0 }} />
              <div>{error}</div>
            </div>
          )}

          <input 
            type="file" 
            ref={fileInputRef} 
            onChange={handleFileInput} 
            accept="image/jpeg,image/png,image/jpg,image/webp" 
            style={{ display: 'none' }} 
          />

          {!previewUrl ? (
            /* Drag and Drop Zone */
            <div 
              className={`dropzone ${isDragActive ? 'drag-active' : ''}`}
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
              onClick={triggerFileInput}
            >
              <div className="dropzone-icon">
                <UploadCloud size={32} />
              </div>
              <h3 className="dropzone-title">
                {isDragActive ? 'Drop your leaf image here' : 'Click to select or drag & drop leaf image'}
              </h3>
              <p className="dropzone-desc">
                Supports clear images of crop and plant leaves
              </p>
              <span className="file-types-badge">
                JPG • JPEG • PNG • WEBP
              </span>
            </div>
          ) : (
            /* Selected Image Preview */
            <div className="preview-card">
              <div className="preview-media-container">
                <img 
                  src={previewUrl} 
                  alt="Selected plant leaf preview" 
                  className="preview-image" 
                />
                <div className="preview-overlay-badge">
                  <CheckCircle2 size={14} color="#34d399" />
                  <span>Image Loaded</span>
                </div>
              </div>

              <div className="preview-details">
                <div className="file-info">
                  <span className="file-name" title={selectedFile?.name}>
                    {selectedFile?.name}
                  </span>
                  <span className="file-size">
                    {selectedFile && formatFileSize(selectedFile.size)}
                  </span>
                </div>

                <div className="preview-actions">
                  <button 
                    type="button" 
                    className="btn-secondary" 
                    onClick={triggerFileInput}
                    disabled={isLoading}
                  >
                    <RefreshCw size={15} />
                    <span>Change Image</span>
                  </button>
                  <button 
                    type="button" 
                    className="btn-danger" 
                    onClick={handleRemoveImage}
                    disabled={isLoading}
                  >
                    <X size={15} />
                    <span>Remove</span>
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Primary Action Button */}
          <div className="action-area">
            <button 
              type="button" 
              className="btn-primary"
              disabled={!selectedFile || isLoading}
              onClick={handleAnalyze}
            >
              {isLoading ? (
                <>
                  <Loader2 size={18} className="spinner" />
                  <span>Analyzing image...</span>
                </>
              ) : (
                <>
                  <ImageIcon size={18} />
                  <span>Analyze Image</span>
                </>
              )}
            </button>
          </div>

          {/* Results Display */}
          {predictionData && topPredictionDetails && (
            <div className="result-container" ref={resultsRef}>
              
              {/* 1. Main Classification Result */}
              <div className={`result-main-card ${topPredictionDetails.isHealthy ? 'healthy' : 'disease'}`}>
                <div className="result-header-row">
                  <div className="plant-pill">
                    <Sprout size={14} />
                    <span>Plant: {topPredictionDetails.plant}</span>
                  </div>

                  <div className={`status-badge ${topPredictionDetails.isHealthy ? 'healthy' : 'disease'}`}>
                    {topPredictionDetails.isHealthy ? (
                      <>
                        <ShieldCheck size={15} />
                        <span>HEALTHY PLANT</span>
                      </>
                    ) : (
                      <>
                        <ShieldAlert size={15} />
                        <span>DISEASE DETECTED</span>
                      </>
                    )}
                  </div>
                </div>

                <div className="result-title-row">
                  <div className="result-label">Prediction Result</div>
                  <h3 className="result-condition">
                    {predictionData.prediction.display_name}
                  </h3>
                </div>

                <div className="result-confidence-box">
                  <div className="confidence-header">
                    <span className="confidence-title">Prediction Confidence</span>
                    <span className="confidence-value">
                      {predictionData.prediction.confidence}%
                    </span>
                  </div>
                  <div className="confidence-bar-bg">
                    <div 
                      className="confidence-bar-fill" 
                      style={{ width: `${Math.min(predictionData.prediction.confidence, 100)}%` }}
                    />
                  </div>
                </div>
              </div>

              {/* 2. Top 3 Predictions Breakdown */}
              {predictionData.top_3 && predictionData.top_3.length > 0 && (
                <div className="top3-container">
                  <div className="top3-header">
                    <BarChart3 size={18} color="#059669" />
                    <span>Top 3 Predictions</span>
                  </div>

                  <div className="top3-list">
                    {predictionData.top_3.map((item, index) => (
                      <div key={item.class_name} className={`top3-item ${index === 0 ? 'rank-1' : ''}`}>
                        <div className="top3-row">
                          <div className="top3-left">
                            <span className="top3-rank-badge">{index + 1}</span>
                            <span className="top3-name">{item.display_name}</span>
                          </div>
                          <span className="top3-confidence">{item.confidence}%</span>
                        </div>
                        <div className="top3-bar">
                          <div 
                            className="top3-bar-fill" 
                            style={{ width: `${Math.min(item.confidence, 100)}%` }}
                          />
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* 3. Model Performance Card */}
              <div className="performance-card">
                <div className="perf-score-box">
                  <span className="perf-value">
                    {modelInfo?.test_accuracy ? `${modelInfo.test_accuracy}%` : '95.93%'}
                  </span>
                  <span className="perf-sublabel">Test Accuracy</span>
                </div>
                <div className="perf-details">
                  <h4 className="perf-title">
                    <Award size={18} color="#059669" />
                    <span>Model Test Accuracy</span>
                  </h4>
                  <p className="perf-desc">
                    Evaluated on the {modelInfo?.test_dataset || 'PlantVillage'} test dataset across {modelInfo?.num_classes || 38} distinct plant disease categories using transfer learning.
                  </p>
                  <p className="perf-note">
                    * Note: This benchmark metric reflects overall test-set accuracy and is separate from the individual prediction confidence shown above.
                  </p>
                </div>
              </div>

              {/* 4. Disease Recommendation & Care Guidance */}
              {recommendation && (
                <div className="recommendation-card">
                  <div className="rec-header">
                    <div className="rec-header-icon">
                      <ClipboardCheck size={20} />
                    </div>
                    <h3 className="rec-header-title">
                      {topPredictionDetails.isHealthy ? 'Plant Care & Maintenance Guidance' : 'What You Can Do (Recommended Guidance)'}
                    </h3>
                  </div>

                  <div className="rec-overview">
                    <h4 className="rec-disease-title">{recommendation.title}</h4>
                    <p className="rec-description">{recommendation.description}</p>
                  </div>

                  {recommendation.recommendations && recommendation.recommendations.length > 0 && (
                    <div>
                      <h4 className="rec-section-title">
                        <CheckCircle2 size={16} color="#059669" />
                        <span>Recommended Actions:</span>
                      </h4>
                      <ul className="rec-list">
                        {recommendation.recommendations.map((action, idx) => (
                          <li key={idx} className="rec-list-item">
                            <span className="rec-bullet">•</span>
                            <span>{action}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {recommendation.prevention && recommendation.prevention.length > 0 && (
                    <div>
                      <h4 className="rec-section-title">
                        <ShieldCheck size={16} color="#059669" />
                        <span>Prevention & Long-Term Management:</span>
                      </h4>
                      <ul className="rec-list">
                        {recommendation.prevention.map((tip, idx) => (
                          <li key={idx} className="rec-list-item">
                            <span className="rec-bullet">•</span>
                            <span>{tip}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {recommendation.caution && (
                    <div className="rec-caution-box">
                      <Info size={16} style={{ flexShrink: 0, marginTop: '2px' }} />
                      <span>{recommendation.caution}</span>
                    </div>
                  )}
                </div>
              )}

            </div>
          )}
        </section>

        {/* Model Information Section */}
        <section className="info-grid">
          <div className="info-card">
            <div className="info-icon">
              <Layers size={22} />
            </div>
            <div className="info-details">
              <h4>Model Architecture</h4>
              <p>VGG16 Transfer Learning</p>
            </div>
          </div>

          <div className="info-card">
            <div className="info-icon">
              <Grid size={22} />
            </div>
            <div className="info-details">
              <h4>Classification Classes</h4>
              <p>38 PlantVillage Classes</p>
            </div>
          </div>

          <div className="info-card">
            <div className="info-icon">
              <Maximize2 size={22} />
            </div>
            <div className="info-details">
              <h4>Input Resolution</h4>
              <p>224 × 224 pixels</p>
            </div>
          </div>
        </section>

        {/* Disclaimer Card */}
        <section className="disclaimer-card">
          <AlertTriangle size={20} className="disclaimer-icon" />
          <div className="disclaimer-text">
            <h5>Dataset & Prediction Notice</h5>
            <p>
              Predictions are based on the PlantVillage-trained model and may be less reliable for images captured in different real-world conditions.
            </p>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="footer">
        <p>Plant Disease Classification Using Deep Learning • College Project Demonstration</p>
      </footer>
    </div>
  );
}
