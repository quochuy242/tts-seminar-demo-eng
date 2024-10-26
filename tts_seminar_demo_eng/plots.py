from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from tts_seminar_demo_eng.config import FIGURES_DIR, PROCESSED_DATA_DIR

import matplotlib.pyplot as plt

from typing import Optional, List, Tuple, Dict
import numpy as np
import os


logger.info(f"Figures directory is: {FIGURES_DIR}")


def plot_mel_spec(
    mel_spec: np.ndarray,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    save_dir: Optional[Path] = None,
    save_name: Optional[str] = None,
    save_ext: Optional[str] = "png",
    show: Optional[bool] = False,
) -> None:
    plt.figure(figsize=(10, 4))
    plt.imshow(mel_spec, origin="lower")
    plt.xlabel(xlabel if xlabel else "Time")
    plt.ylabel(ylabel if ylabel else "Frequency")
    plt.title(title if title else "Mel Spectrogram")
    plt.colorbar()
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        if os.exists(save_dir / f"{save_name}.{save_ext}"):
            print("File already exists. Please choose a different name.")
        else:
            plt.savefig(save_dir / f"{save_name}.{save_ext}")
    if show:
        plt.show()

    return
