# RawMal-TF
This repository provides a comprehensive dataset for malware classification research, combining raw binaries with pre-extracted feature vectors. The dataset includes over **160 GB of Windows PE malware samples**, sourced from publicly available repositories such as **VirusShare**, **MalwareBazaar**, and **VX Underground**. The samples are categorized by **malware type** and **malware family**.


## 📦 Dataset Structure

The dataset consists of two main parts:

| Component               | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Raw PE files**        | Malware binaries sorted into folders by type and family.                   |
| **Feature vectors**     | Pre-extracted vectors extracted from the binaries.  |

The pre-extracted vectors are suitable for immediate use with machine learning models, and the raw binaries are available for further analysis or feature extraction.

### 🔍 Label Granularity

- **Type-based classification:** e.g., worm, trojan, ransomware
- **Family-based classification:** e.g., AgentTesla, Bladabindi, Xtrat

## 📥 Download

Due to the dataset's size and sensitivity, distribution is handled manually or via internal storage.

| Subset          | Structure         | Format        | Approx. Size |
|------------------|------------------|---------------|--------------|
| Binaries         | by type/family   | Raw PE files  | ~160 GB      |
| Feature vectors  |     .jsonl       | Vector files  | included     |

> 🔗 **Google Drive download link:** [Link](https://drive.google.com/drive/folders/1wYQPjoZ48BaFmVeW3leMVocqHbjV6TBm?usp=sharing)

## 🧠 Usage

**TODO**

The dataset can be used directly for:

- Training machine learning models for malware detection
- Benchmarking feature extraction methods
- Comparing classification at the type vs. family level
- Analyzing classification errors across malware categories


## 📁 Directory Layout

