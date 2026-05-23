# 🎨 Art2Artist Recognizer

> An end-to-end deep learning image classifier that identifies the master behind any painting — spanning data collection, cleaning, model training, deployment, and API integration.

<p align="center">
  <img src="images/image.png" alt="Art2Artist Recognizer App Interface"/>
  <br/>
  <em>Art2Artist Recognizer — Web Interface</em>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/goldphish2209/art2artist-recognizer">
    <img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-FFD21E?style=for-the-badge" alt="Hugging Face"/>
  </a>
  <a href="https://naawshin.github.io/Art2Artist-Recognizer/">
    <img src="https://img.shields.io/badge/GitHub%20Pages-Website-222222?style=for-the-badge&logo=github" alt="GitHub Pages"/>
  </a>
  <img src="https://img.shields.io/badge/Accuracy-90%25-4CAF50?style=for-the-badge" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/Artists-20-blueviolet?style=for-the-badge" alt="Artists"/>
</p>


## 📦 Dataset Preparation

**Data Collection** was sourced from two places:
- **DuckDuckGo** — images scraped by artist name
- **[Kaggle WikiArt Dataset](https://www.kaggle.com/datasets/steubk/wikiart)** — curated art repository

| Stage | Image Count |
|---|---|
| Raw collected | ~20,000 |
| After cleaning | ~16,000 |

**DataLoader** — Built with the [fastai DataBlock API](https://docs.fast.ai/data.block.html).

**Data Augmentation** — fastai's default GPU-accelerated augmentation pipeline:
- Random resized crops (`min_scale=0.5`)
- Multiple augmentations with `2.0` multiplier

> See `notebooks/data_prep.ipynb` for full details.

---

## 🏋️ Training & Data Cleaning

### Training

- Transfer learning with pretrained ResNet architectures
- Fine-tuned over **3 cycles × 5 epochs each**

### Data Cleaning

The most time-consuming phase of the project. Images scraped from DuckDuckGo required extensive manual review and cleaning before being merged with the WikiArt dataset to produce high-quality, relevant training examples.

---

## 📊 Model Comparison

| Model | Architecture | Dataset Size | Accuracy |
|---|---|---|---|
| Model 1 | ResNet34 | 16,000 images | 88% |
| Model 2 | ResNet50 | 16,000 images | **90%** ✅ |

**ResNet50** was selected as the final model — its deeper architecture enables richer feature extraction, capturing the subtle stylistic signatures that distinguish each artist.

---

## 🚀 Deployment

The model is deployed as a **Gradio app on Hugging Face Spaces**.

<p align="center">
  <img src="deployment/gradio_app.png" alt="Gradio App Interface" width="700"/>
  <br/>
  <em>Gradio App — Deployed on Hugging Face Spaces</em>
</p>

🔗 **Live app:** [huggingface.co/spaces/goldphish2209/art2artist-recognizer](https://huggingface.co/spaces/goldphish2209/art2artist-recognizer)

> Implementation details in the `deployment/` folder.

---

## 🌐 API Integration (GitHub Pages)

The Gradio model API is integrated into a GitHub Pages website for browser-based access without any local setup.

<p align="center">
  <img src="images/image-1.png" alt="GitHub Pages Website" width="700"/>
  <br/>
  <em>Art2Artist — GitHub Pages Live Demo</em>
</p>

🔗 **Website:** [naawshin.github.io/Art2Artist-Recognizer](https://naawshin.github.io/Art2Artist-Recognizer/)

> Implementation details in the `docs/` folder.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Deep learning framework | fastai + PyTorch |
| Model architectures | ResNet34, ResNet50 |
| Data sources | DuckDuckGo scraping, Kaggle WikiArt |
| Deployment | Hugging Face Spaces + Gradio |
| Web integration | GitHub Pages |
| Training strategy | Transfer learning + fine-tuning |

---

## ✨ Summary

- 🧠 Built with **fastai** and **PyTorch**
- 🔁 **Transfer learning** with ResNet34 and ResNet50
- 🖼️ Curated and cleaned **20k+ images** from DuckDuckGo and Kaggle WikiArt
- 🎯 Achieved up to **90% accuracy** in artist classification
- ☁️ Deployed on **Hugging Face Spaces** with Gradio
- 🌐 Integrated via API on **GitHub Pages** for web-based access

---

## 👩‍💻 Author

**Nowshin Tabasum** — AI Engineer

[![GitHub](https://img.shields.io/badge/GitHub-Naawshin-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Naawshin)
[![Email](https://img.shields.io/badge/Email-nowshintabasum004@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nowshintabasum004@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-nowshin--tabasum-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nowshin-tabasum)