# Algo Trading System with Google Sheet + Angel One API

This repository is designed for building a fully automated Algo Trading system using:
- **Google Sheets** as the control center
- **Angel One SmartAPI** for placing trades
- **Python scripts** for indicator logic and signal generation

## Features

- Auto Fetch Live Market Data (LTP, RSI, EMA, OI)
- Generate Buy/Sell signals based on technical indicators
- Auto Update signals in Google Sheet
- Auto Place Orders in Angel One account
- Uses `.gitignore` to protect sensitive info (API keys, creds)

## Technologies Used

- Python 3
- Google Sheets API
- Angel One SmartAPI
- GitHub Actions (for auto-running the script from cloud)

## Folder Structure

main.py                 -> Main Python script sheet_config.json       -> Google Sheet config .env / creds.json       -> API keys (ignored by Git) .gitignore              -> Protects secrets README.md               -> This file

## Setup Guide

1. Clone this repo
2. Setup `.env` file with Angel One & Sheet API keys
3. Edit `sheet_config.json` with your Google Sheet ID
4. Run `main.py` or set GitHub Actions for automation

## Note

- Do not share your `.env` or credentials publicly
- Keep your `.gitignore` updated for safety

## Author

Created with love by [Your Name]  
Maintained with blessings from Bhagwan & Algo Passion
