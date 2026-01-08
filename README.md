# Domain Adaptation for English-Chinese NMT 🇨🇳🇬🇧

**Course:** Machine Translation (2025)  

## Project Overview
This project explores **Domain Adaptation** techniques in Neural Machine Translation. The goal is to adapt a pre-trained multilingual model (`Helsinki-NLP/opus-mt-en-mul`) from a general formal domain (UNPC) to a specific spoken domain (TED Talks).

## Method
* **Phase 1 (General Fine-tuning):** Trained on 500k sentence pairs from the **UN Parallel Corpus (UNPC)**.
* **Phase 2 (Domain Adaptation):** Further fine-tuned on 50k sentence pairs from **TED Talks**.

## Files Structure
* `data_cleaning_config.yaml`: Configuration for OpusFilter pipeline.
* `data_split.py`: Script used to shuffle and split train/dev/test sets.
* `1_train_ UNPC.ipynb`: Notebook for Phase 1 training.
* `2_domain_adaptation_TED_and_evaluation.ipynb`: Notebook for Phase 2 training and final evaluation.
* `samples/uncleaned_random_20.txt` | 📄 Log file showing **raw data statistics** and noisy samples before filtering. 
| `samples/cleaned_random_20.txt` | 📄 Log file showing **final data statistics** and high-quality aligned samples after filtering. 
