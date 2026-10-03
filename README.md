![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Slake Durability Index Classifier
 
*For engineering geologists and geotechnical engineers: enter the second-cycle slake durability index (Id2) to instantly classify rock durability and visualize the durability class.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Engineering Geology
 
a) Inputs: User provides the slake durability index after the second cycle (Id2) as a percentage (0–100) via a number input slider (step 0.1). An optional second input allows the first-cycle index (Id1) if available. b) Core logic: Validate Id2 is between 0 and 100. Apply standard ISMR classification thresholds: Id2 ≥ 98 → Very High Durability; 95–98 → High; 85–95 → Medium High; 60–85 → Medium; 30–60 → Low; <30 → Very Low. If Id1 is provided, compute the durability ratio = Id2 / Id1 (must be ≤ 1). If ratio < 0.9, classify rock as 'Non-Durable' regardless of Id2. Otherwise classification is by Id2 alone. Output includes text label, a color-coded bar chart (matplotlib) that marks the Id2 value against the threshold ranges, and a small reference table of typical rock types per class. c) Gradio UI: Vertical layout with title and brief instructions. Inputs: Number input for Id2, optional number input for Id1. A 'Classify' button. Outputs: (1) Text label with classification, (2) color bar plot image, (3) expanding box with typical rock type examples for the class. d) Output: Classification text, bar chart, and optional info. No file download. e) No AI/ML component; pure rule-based expert classification.
 
## Run it
 
```bash
docker build -t slake-durability-index-classifier .
docker run -p 7860:7860 slake-durability-index-classifier
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-10-03.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
