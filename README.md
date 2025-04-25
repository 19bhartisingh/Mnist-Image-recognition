# Mnist-Image-recognition

Perfect, Bharti! Here's a clean and clear **README-style explanation** for your MNIST digit recognizer project workflow:

---

## 🖋️ MNIST Handwritten Digit Recognizer Project

This project allows you to **draw digits on the screen**, and a trained model will recognize and classify the digit (0–9) in real-time.

---

### ✅ Workflow Overview

1. **Train the Model (on Google Colab)**
2. **Launch the GUI for Drawing and Prediction**

---

### 📌 Step 1: Train the Model (Google Colab)

1. Open the `train_model.ipynb` Colab file.
2. Run all cells. This will:
   - Load and preprocess the MNIST dataset.
   - Build and train a Convolutional Neural Network (CNN).
   - Save the trained model as `mnist.h5`.

3. After training, download the `mnist.h5` file.

> 💡 Tip: Make sure to place `mnist.h5` in the same folder as your GUI script (`gui.py`).

---

### 📌 Step 2: Run the GUI App

1. Open a terminal or your Python environment.
2. Run the GUI script:

```bash
python gui.py
```

3. A window will appear where you can:
   - Draw digits using your mouse.
   - Click **"Recognize"** to predict the digit.
   - Click **"Clear"** to draw a new digit.

---

### 🧠 Behind the Scenes

- The canvas drawing is mirrored to a `PIL` image buffer.
- The drawn digit is preprocessed to match MNIST format:
  - Converted to grayscale.
  - Inverted (black digit on white).
  - Resized to 28×28.
  - Centered and normalized.
- The `mnist.h5` model predicts the digit with confidence.

---

### ✅ Requirements

Install these Python libraries if you haven't:


pip install tensorflow keras pillow matplotlib numpy


