# =========================================
# IPL Analytics Project
# analysis.py
# =========================================

# Import Libraries
import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------------------
# Create visuals folder if not exists
# -----------------------------------------

os.makedirs("../visuals", exist_ok=True)

# -----------------------------------------
# Extract ZIP File
# -----------------------------------------

zip_path = "../archive.zip"

extract_path = "../data"

# Create data folder if not exists
os.makedirs(extract_path, exist_ok=True)
