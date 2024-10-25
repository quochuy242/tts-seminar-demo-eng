from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from tts_seminar_demo_eng.config import FIGURES_DIR, PROCESSED_DATA_DIR

import matplotlib.pyplot as plt

from typing import Optional, List, Tuple, Dict


logger.info(f"Figures directory is: {FIGURES_DIR}")

def plot_spectrogram(spectrogram)