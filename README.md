# IT Sector Portfolio VaR & Expected Shortfall Analysis

## Overview

This project is a market risk analytics application designed to measure and evaluate the downside risk of an equally/user-weighted portfolio of Indian IT sector stocks.

The project implements multiple Value at Risk (VaR) and Expected Shortfall (ES) methodologies and evaluates VaR performance using historical backtesting and the Kupiec Proportion of Failures (POF) test.

A Streamlit dashboard is included to allow users to enter portfolio investments and interactively analyse portfolio risk.

## Portfolio

The analysis uses 10 Indian IT sector stocks:

- TCS
- Infosys
- HCL Technologies
- Wipro
- Tech Mahindra
- LTIMindtree
- L&T Technology Services
- Mphasis
- Persistent Systems
- Coforge

The underlying historical data covers approximately five years.

## Risk Measures

### Value at Risk (VaR)

VaR estimates the potential portfolio loss at a specified confidence level over a given holding period.

The project calculates:

- Historical VaR
- Parametric VaR

Confidence levels:

- 95%
- 99%

Holding periods:

- 1 Day
- 5 Days
- 30 Days
- 90 Days

### Expected Shortfall (ES)

Expected Shortfall measures the average portfolio loss beyond the VaR threshold.

The project calculates:

- Historical Expected Shortfall
- Parametric Expected Shortfall

## Backtesting

VaR estimates are evaluated using historical portfolio returns.

The project performs:

### VaR Breach Analysis

A breach occurs when the realized portfolio return falls below the estimated VaR threshold.

The observed breach frequency is compared with the expected frequency:

- 95% VaR → approximately 5% expected exceptions
- 99% VaR → approximately 1% expected exceptions

### Kupiec POF Test

The Kupiec Proportion of Failures test evaluates whether the observed number of VaR exceptions is consistent with the expected exception probability.

The test is performed for:

- Historical VaR
- Parametric VaR
- 95% confidence level
- 99% confidence level
- 1D, 5D, 30D and 90D horizons

## Key Findings

The backtesting results showed that:

- Historical VaR passed the Kupiec POF test across all tested confidence levels and horizons.
- Parametric VaR passed the Kupiec POF test at the 95% confidence level.
- Parametric VaR failed the Kupiec POF test at the 99% confidence level across the tested horizons.

This indicates that the normal-distribution assumption used in the parametric approach may have difficulty capturing extreme-tail behaviour in this portfolio.

These results should be interpreted as evidence from the current historical sample rather than proof that one VaR methodology is universally superior.

## Portfolio Analytics

The dashboard also provides:

- Portfolio weights
- Total investment
- Portfolio mean return
- Portfolio variance
- Portfolio standard deviation
- Annualized volatility
- Correlation matrix
- Covariance matrix
- Portfolio returns across multiple horizons

## Technology Stack

- Python
- Pandas
- NumPy
- SciPy
- OpenPyXL
- Streamlit
- Git / GitHub

## Project Structure

```text
var es project/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── Portfolio_Returns_Merged.xlsx
│
└── src/
    ├── combine_excel.py
    ├── correl.py
    ├── excel.py
    ├── merge.py
    └── stats.py