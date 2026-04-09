@echo off
cd /d "%~dp0"
conda run -n fmea streamlit run app.py
