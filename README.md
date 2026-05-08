# 💧 Water Quality Predictor

This project uses **Machine Learning** to classify whether water is safe for human consumption (**Potable**) or not, based on various water quality metrics.

## 📌 Project Overview
Water quality is a critical factor for health and environmental safety. This tool provides a data-driven approach to predicting water potability using chemical properties. The model is trained on a dataset containing parameters like pH, Hardness, Solids, and more.

## 🚀 Features
* **Exploratory Data Analysis (EDA):** Visualizations showing how different factors affect water safety.
* **Classification Model:** A trained ML model (using Scikit-Learn) that achieves high accuracy in predicting potability.
* **User Input Support:** Easily test the model with custom water quality values.

## 📊 Key Features (Dataset Columns)
The model analyzes the following attributes:
* **pH:** Acidic or basic nature of the water.
* **Hardness:** Concentration of calcium and magnesium.
* **Solids:** Total dissolved solids (TDS) in ppm.
* **Chloramines:** Amount of Chloramines in ppm.
* **Sulfate:** Concentration of sulfates.
* **Conductivity:** Electrical conductivity of the water.
* **Organic Carbon:** Measure of organic matter.
* **Trihalomethanes:** Concentration of THMs.
* **Turbidity:** Measure of water clarity.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn


## 📈 Model Performance
The model was evaluated using accuracy, precision, and recall.
* **Best Model:** Random Forest Classifier (or whichever you used)
* **Accuracy:** 71% (Update with your actual score)
* **Key Finding:** pH and Sulfate levels were the most significant predictors of potability in this dataset.
