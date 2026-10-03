import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def classify_sdi(id2, id1=None):
    """
    Classify rock durability based on Id2 and optional Id1.
    Returns (classification_text, label_key).
    """
    if id1 is not None:
        if id1 <= 0:
            return "Invalid Id1 (must be > 0)", None
        ratio = id2 / id1
        if ratio > 1.0:
            return "Error: Id2 cannot be greater than Id1", None
        if ratio < 0.9:
            return "Non-Durable (based on durability ratio < 0.9)", "very_low"
    # Use Id2 thresholds
    if id2 >= 98:
        return "Very High Durability", "very_high"
    elif id2 >= 95:
        return "High Durability", "high"
    elif id2 >= 85:
        return "Medium High Durability", "medium_high"
    elif id2 >= 60:
        return "Medium Durability", "medium"
    elif id2 >= 30:
        return "Low Durability", "low"
    else:
        return "Very Low Durability", "very_low"

def plot_sdi_classification(id2, id1=None):
    """
    Generate a color-coded horizontal bar chart showing the durability classes
    and the position of the given Id2 value.
    Returns a matplotlib figure.
    """
    # Thresholds (from ISRM)
    thresholds = [
        (0, 30, '#8B0000', 'Very Low'),
        (30, 60, '#FF4500', 'Low'),
        (60, 85, '#FFA500', 'Medium'),
        (85, 95, '#90EE90', 'Medium High'),
        (95, 98, '#32CD32', 'High'),
        (98, 100, '#006400', 'Very High'),
    ]
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1)
    ax.axis('off')
    # Draw colored segments
    for (lo, hi, color, label_text) in thresholds:
        ax.barh(0.5, hi - lo, left=lo, height=0.5, color=color, edgecolor='white', linewidth=1)
        mid = (lo + hi) / 2
        ax.text(mid, 0.5, f"{lo}-{hi}", ha='center', va='center', fontsize=8, color='white',
                fontweight='bold')
    # Mark Id2 with a vertical line and annotation
    ax.axvline(x=id2, ymin=0.1, ymax=0.9, color='black', linewidth=2, linestyle='--')
    ax.text(id2, 1.2, f'Id2 = {id2:.1f}%', ha='center', va='bottom', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', edgecolor='black'))
    # Optional Id1 marker
    if id1 is not None:
        ax.axvline(x=id1, ymin=0.1, ymax=0.9, color='blue', linewidth=1.5, linestyle=':')
        ax.text(id1, 0.0, f'Id1 = {id1:.1f}%', ha='center', va='top', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='lightblue', edgecolor='blue'))
    plt.tight_layout()
    return fig

def typical_rock_types(label_key):
    """
    Return HTML string with typical rock types for a given durability class label.
    """
    types = {
        "very_low": "<b>Very Low Durability:</b> Mudstones, shales, claystones, tuffs",
        "low": "<b>Low Durability:</b> Siltstones, marls, weak sandstones",
        "medium": "<b>Medium Durability:</b> Limestones, dolomites, sandstones, gypsum",
        "medium_high": "<b>Medium High Durability:</b> Granites, gneisses, quartzites (weathered)",
        "high": "<b>High Durability:</b> Fresh granites, basalts, quartzites, cherts",
        "very_high": "<b>Very High Durability:</b> Fresh quartzites, cherts, silicified rocks",
    }
    return types.get(label_key, "")
