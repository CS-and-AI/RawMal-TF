# RawMal-TF
This repository provides a comprehensive dataset for malware classification research, combining raw binaries with pre-extracted feature vectors. The dataset includes over **160 GB of Windows PE malware samples**. The data files were obtained from various sources, including **EMBER, VirusShare, MalwareBazaar**, and **VX Underground**, and are governed by their respective licensing terms. The samples are categorized by **malware type** and **malware family**.



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

Each feature vector is stored as a JSON object inside a `.jsonl` file. All samples are combined into a single JSON array. Each object contains structured metadata and statistics extracted from one Windows PE binary. This format is suitable for loading the entire dataset into memory or iterating over it for batch processing in machine learning workflows.

The feature vectors include both **malicious samples** and **clean (benign) binaries** prepared for direct use in machine learning experiments. This allows straightforward training of binary classifiers without additional preprocessing.

### 📄 Format Overview

| Field              | Description |
|--------------------|-------------|
| `sha256`           | SHA-256 hash of the binary (acts as unique identifier) |
| `label`            | Classification label (`1` = malicious, `0` = benign) |
| `histogram`        | Byte histogram (256-length array of byte value frequencies) |
| `byteentropy`      | Flattened 2D histogram of byte value vs. entropy |
| `strings`          | String metadata: total count, average length, entropy, printable distribution |
| `general`          | General binary properties (e.g., file size, virtual size, presence of resources) |
| `header`           | PE header fields, including COFF and optional header values |
| `section`          | Information about PE sections (e.g., name, size, entropy, access flags) |
| `imports`          | Dictionary of imported functions grouped by DLL |
| `exports`          | List of exported symbols (if present) |
| `datadirectories`  | PE data directories (IAT, resource table, TLS, etc.) |

> 💡 **Note:** The dataset combines malicious and benign samples, enabling immediate use for training and evaluating binary classifiers.


## 📈 Loading Data

The loading logic is based on the **original Ember reference Jupyter notebook**, which demonstrates how to generate vectorized features and load them for training. To make this process straightforward, we have preserved the **directory structure expected by the Ember code**, but extracted and simplified everything into a standalone script so you can integrate it into your own pipelines more easily.

You can find this example script [here](scripts/load.py).

After running the script successfully, you should see an output similar to:
```
    Dataset loaded successfully!
    - Training set size: (13468, 2381)
    - Test set size: (3368, 2381)
    - Labels distribution in train: clean=6711, malware=6757
    - Labels distribution in test: clean=1707, malware=1661

```

> **Note:**  This output corresponds to the example path specified in the script.



## 🫆 Citing
If you use this dataset in your research or publications, please reference the following [paper](https://arxiv.org/abs/2506.23909).

```
@misc{balik2025rawmaltfrawmalwaredataset,
      title={RawMal-TF: Raw Malware Dataset Labeled by Type and Family}, 
      author={B{\'a}lik, David and Jure{\v{c}}ek, Martin and Stamp, Mark},
      year={2025},
      eprint={2506.23909},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2506.23909}
}
```









