"""
Stock Market Analysis Dashboard - Main Entry Point
====================================================
Run this file to start the Streamlit dashboard.
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    import streamlit as st
    from app.dashboard import main
    main()
