# BTC-USD
BTC-USD Statistical Analysis is a Python-based data analysis tool that loads historical Bitcoin price data, computes descriptive statistics (min, max, mean, variance, std), and visualizes price trends across Open, High, Low, Close, and Volume columns using Matplotlib.

# 📈 BTC-USD Statistical Analysis

A Python script for statistical analysis and visualization of Bitcoin (BTC-USD) price data.

## 📋 Overview

This project loads historical BTC-USD market data from a CSV file, computes key statistical metrics across price and volume columns, and generates a multi-panel chart with mean reference lines.

## 🗂️ Project Structure

```
├── btc_analysis.py       # Main analysis script
├── BTC-USD.csv           # Input dataset (historical BTC-USD data)
└── BTC-USD.png           # Output chart (auto-generated)
```

## 📦 Requirements

- Python 3.7+
- numpy
- pandas
- matplotlib

Install dependencies:

```bash
pip install numpy pandas matplotlib
```

## 🚀 Usage

1. Place your `BTC-USD.csv` file in the same directory as the script.
2. Run the script:

```bash
python btc_analysis.py
```

## 📊 Input Data Format

The CSV file must contain the following columns:

| Column   | Description              |
|----------|--------------------------|
| `Date`   | Date of the record       |
| `Open`   | Opening price (USD)      |
| `High`   | Highest price (USD)      |
| `Low`    | Lowest price (USD)       |
| `Close`  | Closing price (USD)      |
| `Volume` | Trading volume           |

## 🔢 Statistical Metrics

For each numeric column, the script calculates:

- **Min** — Minimum value
- **Max** — Maximum value
- **Mean** — Average value
- **Variance** — Statistical variance
- **Standard Deviation** — Spread around the mean

Results are printed as a formatted DataFrame in the console.

## 📉 Output Charts

A 2×3 subplot figure (`BTC-USD.png`) is saved with the following panels:

| Panel | Column  | Color  |
|-------|---------|--------|
| 1     | Close   | Red    |
| 2     | High    | Blue   |
| 3     | Low     | Green  |
| 4     | Open    | Black  |
| 5     | Volume  | Yellow |

Each panel includes a **dashed mean reference line** for quick visual reference.

## 📌 Notes

- Numeric columns are cast to `float32` to reduce memory usage.
- The output image is saved at 150 DPI for high clarity.
