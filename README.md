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

Due to the dataset's size and sensitivity, distribution is handled manually.

| Subset          | Structure         | Format        | Approx. Size |
|------------------|------------------|---------------|--------------|
| Binaries         | by type/family   | Raw PE files  | ~160 GB      |
| Feature vectors  |     .jsonl       | Vector files  | included     |

> 🔗 **Google Drive download link:** [Link](https://drive.google.com/drive/folders/1wYQPjoZ48BaFmVeW3leMVocqHbjV6TBm?usp=sharing)


## 🧬 Feature Vectors

Each feature vector is stored as a JSON object inside a `.json` file. All samples are combined into a single JSON array. Each object contains structured metadata and statistics extracted from one Windows PE binary. This format is suitable for loading the entire dataset into memory or iterating over it for batch processing in machine learning workflows.


### 📄 Format Overview

| Field              | Description |
|--------------------|-------------|
| `sha256`           | SHA-256 hash of the binary (acts as unique identifier) |
| `label`            | Classification label |
| `histogram`        | Byte histogram (256-length array of byte value frequencies) |
| `byteentropy`      | Flattened 2D histogram of byte value vs. entropy |
| `strings`          | String metadata: total count, average length, entropy, printable distribution |
| `general`          | General binary properties (e.g., file size, virtual size, presence of resources) |
| `header`           | PE header fields, including COFF and optional header values |
| `section`          | Information about PE sections (e.g., name, size, entropy, access flags) |
| `imports`          | Dictionary of imported functions grouped by DLL |
| `exports`          | List of exported symbols (if present) |
| `datadirectories`  | PE data directories (IAT, resource table, TLS, etc.) |





