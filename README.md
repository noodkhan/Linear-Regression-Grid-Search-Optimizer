# 📈 Pure Python Linear Regression & Grid Search Optimizer

A lightweight, dependency-free implementation of single-variable Linear Regression written in pure Python. This project demonstrates core machine learning mechanics—including forward prediction, error computation (MSE), parameter mathematical derivation, and parameter estimation via Grid Search optimization—without using external libraries like NumPy or PyTorch.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Neural Network](https://img.shields.io/badge/Neural%20Network-From%20Scratch-purple?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Not%20Used-success?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-Not%20Used-success?style=for-the-badge)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Not%20Used-success?style=for-the-badge)

---

## ✨ Features

* 🧠 **Zero External Dependencies:** Built using standard Python functions and basic arithmetic operators.
* 🧮 **Explicit Mathematical Foundations:** Manual implementations of $y = wx + b$, parameter inversion, and error measurement.
* 🔍 **Grid Search Optimization:** Brute-force parameter search to discover optimal weights ($w$) and biases ($b$) by minimizing Mean Squared Error (MSE).
* 📐 **Loss Tracking:** Calculates squared residuals across datasets to find the best-fitting line.
<img width="5167" height="3445" alt="aaron-lefler-Vs6ip7fsld8-unsplash" src="https://github.com/user-attachments/assets/cf98518b-512d-4cf8-8627-7d4435e49da6" />

---

## 🧮 Mathematical Model

The model fits a straight line to input data using the standard slope-intercept form:

$$\hat{y} = w \cdot x + b$$

Where:
* **$x$**: Input feature vector
* **$w$**: Weight (Slope)
* **$b$**: Bias (Y-intercept)
* **$\hat{y}$**: Predicted output

### Error Metric (Mean Squared Error)
To evaluate model performance, the optimization algorithm minimizes the Mean Squared Error (MSE):

$$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$

---

## 🚀 Quick Start

### Prerequisites
* Python 3.x installed.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/noodkhan/linear-regression-grid-search.git](https://github.com/noodkhan/linear-regression-grid-search.git)
   cd linear-regression-grid-search

```

2. **Run the script:**
```bash
python main.py

```



---

## 💻 Code Example

```python
# Input features and ground-truth values
x = [1, 2, 3, 4, 5]
actual = [3, 5, 7, 9, 11]

# Discover optimal w and b within search space [-10, 10]
w, b = find_best_parameters(x, actual)

print(f"Learned Parameters: w = {w}, b = {b}")
# Output: Learned Parameters: w = 2, b = 1

```

---

## 📂 Key Functions

| Function | Description | Formula / Logic |
| --- | --- | --- |
| `predict(x, w, b)` | Computes predicted output $\hat{y}$ | $y = wx + b$ |
| `find_weight(x, y, b)` | Solves for target weight given $y$ and $b$ | $w = \frac{y - b}{x}$ |
| `find_bias(x, y, w)` | Solves for target bias given $y$ and $w$ | $b = y - wx$ |
| `prediction_error(...)` | Calculates single point residual error | $e = y_{\text{pred}} - y_{\text{actual}}$ |
| `mean_squared_error(...)` | Computes average squared error over dataset | $\frac{1}{N} \sum (y - \hat{y})^2$ |
| `find_best_parameters(...)` | Grid search algorithm for optimal parameters | Sweeps $w \in [-10, 10]$, $b \in [-10, 10]$ |
<img width="543" height="520" alt="1_dkpb3XSLslX9IjIAGrSYsA" src="https://github.com/user-attachments/assets/be64a60f-0960-48fd-8e55-1dd9490f2d96" />

---

## 👤 Credits

Designed and developed with care by:

* **Navin Kanthawong** ([@noodkhan](https://github.com/noodkhan))
* *Role:* Software Engineering

---

## 📄 License

This project is licensed under the **MIT License** — see below for details:

```text
MIT License

Copyright (c) 2026 Navin Kanthawong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
