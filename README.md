
# 📊 Heart Rate Monitoring & Stress Analysis System using ML and Arduino

This project integrates **Arduino-based heart rate sensing** with **machine learning-driven stress level analysis**, **real-time visualization**, and **LCD display feedback**. It combines hardware-based data collection with software-based prediction and visualization, offering a complete biofeedback system for stress detection.

---

## 🔌 Arduino Components & Libraries

Used to collect and process raw heart rate signals:

- `Arduino.h`
- `DFRobot_Heartrate.h`
- `Wire.h`
- `LiquidCrystal_I2C.h`

🔧 **Functionality**:  
The Arduino setup collects 2000 heart rate samples via an analog sensor, filters out noisy values, scales the BPM appropriately, and sends the processed data to Python over serial communication for machine learning-based evaluation.

---

## 🧠 Machine Learning Libraries & Packages

Install the required Python packages:

```bash
pip install -U scikit-learn
pip install seaborn==0.11.0
pip install -q ptitprince
```

### Python Libraries Used:
- **Pandas** (`pd`) – Data processing and analysis
- **NumPy** (`np`) – Numerical computations
- **Seaborn** (`sns`) – Statistical plots
- **Matplotlib** (`plt`) – Graphical visualizations
- **Scipy.stats** – Statistical testing and analysis
- **Scikit-Learn** (`sklearn`):
  - `train_test_split` – Splits dataset for training/testing
  - `PCA` – Principal Component Analysis for dimensionality reduction
  - `LogisticRegression` – Classifier for stress prediction
  - `brier_score_loss`, `confusion_matrix` – Evaluation metrics

---

## 🖥️ System Communication Libraries (Python)

Used for real-time serial communication between Arduino and PC:

- `serial` – From `pyserial`, handles serial communication
- `serial.tools.list_ports` – Detects available COM ports
- `time` – Manages delays and synchronization

---

## ⚙️ Functional Modules

### 1. **Sensor Data Collection**
- Captures real-time heart rate via `analogRead()`.
- Filters out weak/noisy signals (<800).
- Scales raw values to BPM (60–180 range).
- Sends data to Python via serial.

### 2. **Data Processing & Storage**
- Python receives up to 2000 samples.
- Applies **Z-score normalization**.
- Saves normalized data as `heart_rate_data.csv`.

### 3. **ML Model Training & Evaluation**
- Uses PCA for feature reduction.
- Trains a Logistic Regression model to predict stress levels.
- Evaluates using:
  - **Confusion Matrix**
  - **Brier Score**

### 4. **LCD Display Integration**
- LCD shows:
  - BPM (Heart Rate)
  - HRV (Heart Rate Variability)
  - Stress Level
  - Recovery Status
- Display output is updated live via serial from the PC.

---

## 💡 Example Output Format

```
HR: 95 BPM | HRV: 30 ms | Stress: Moderate Stress | Recovery: Partial Recovery
```

---

## 📁 Project Structure

```
keerti/
├── Arduino_Sensor/              # Code to read HR and send via serial
├── LCD_Display/                 # Code to display HR & stress levels on LCD
├── Stress_Levels/              # Enhanced analysis: HRV, stress, recovery
├── csvprocees.py               # Reads serial data, normalizes and stores it
├── photoplethysmograph-pca-prediction-brierscore-0-03.ipynb  # Main ML notebook
├── Required Libraries.txt       # List of required Arduino libraries
```

---

## ✅ How to Run

### 1. **Upload Arduino Code**
- Upload files from `Arduino_Sensor/` and `LCD_Display/` to your Arduino board using the Arduino IDE.

### 2. **Run Python Script**
- Ensure Arduino is connected (check COM port).
- Run `csvprocees.py` to collect and save normalized HR data.
- Open the Jupyter notebook and run `photoplethysmograph-pca-prediction-brierscore-0-03.ipynb` for ML analysis.

---

## 📜 License

*You can add a license like MIT or Apache 2.0 depending on your sharing preferences.*

---

## 🙋‍♀️ Author

**Keerti** – [NIT Andhra]  
*Built with Arduino, Python, and ML to promote health tech innovation.*
