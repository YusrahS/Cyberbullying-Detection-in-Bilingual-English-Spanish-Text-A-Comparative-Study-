# Cyberbullying Detection in Bilingual English-Spanish Text: A Comparative Study

MSc Artificial Intelligence dissertation, University of Surrey.

A systematic comparison of six architectures for cyberbullying detection on a
purpose-built bilingual English-Spanish corpus, evaluated across five conditions:
bilingual joint training, English-only, Spanish-only, and zero-shot transfer in
both directions.

---

## Summary of results

Macro F1-score. Full results in the dissertation, Chapter 4.

| Model | Bilingual | EN-only | ES-only | EN→ES | ES→EN |
|---|---|---|---|---|---|
| BiLSTM (static embeddings) | 0.8864 | 0.9100 | 0.7691 | 0.3760 | 0.4462 |
| DistilBERT | 0.9088 | 0.9262 | 0.8684 | 0.4301 | 0.5396 |
| mBERT | 0.9103 | 0.9257 | 0.8773 | 0.4077 | 0.5456 |
| XLM-R | 0.9180 | 0.9294 | 0.8860 | 0.4942 | 0.6313 |
| BETO (monolingual Spanish) | — | — | 0.8990 | — | 0.6194 |
| Soft-voting ensemble | 0.9184 | — | — | — | — |

LoRA-adapted Mistral 7B, evaluated on a 1,000-row stratified subsample and so not
directly comparable with the above: 0.5257 zero-shot, 0.7910 few-shot after adding
500 Spanish examples.

**Main findings.** Three multilingual transformers land within 0.92 percentage
points of each other despite a twofold difference in parameter count. Zero-shot
transfer costs between 39 and 47 points, and fails the same way in every
condition, retaining non-abusive recall while recall on the abusive class
collapses. Class-weighted training recovers 3.4% to 7.0% of that cost; 500
target-language examples recover 73.7%.

---

## Repository structure

```
Datasets/
  raw/                 unmodified source Datasets, one folder per source
  processed/           reformatted to a common schema
  balanced/            class-balanced corpora (English, Spanish, bilingual)
  dataset_splits/      train/validation/test splits used by every experiment
Notebooks/             the experimental pipeline, run in numerical order
reports/
  figures/             figures used in the dissertation
  results/             metrics for every run
src/
  data/preprocessor.py text cleaning shared across notebooks
requirements.txt
data/
    pickles/             tokenised and embedded data for the BiLSTM and transformers
```

Trained model checkpoints are not included: they exceed GitHub's 100 MB limit.
Every metrics file needed to verify the reported numbers is in `reports/results/`.

---

## Data

Five publicly available sources were merged into a balanced corpus of 93,301
samples. Each `Datasets/raw/` subfolder carries its own README with the original
source and licence.

| Source | Language | Contribution |
|---|---|---|
| OffendES (Plaza-del-Arco et al., 2021) | Spanish | Primary Spanish source, three platforms |
| Colombian Twitter corpus (Guerra Saenz et al., 2025) | Spanish | Latin American Spanish |
| Spanish hate speech compilation (Tonneau et al., 2024) | Spanish | Supplementary abusive material |
| Fine-grained cyberbullying corpus (Wang et al., 2020) | English | Abusive class |
| TweetEval (Barbieri et al., 2020) | English | Non-abusive class |

**Splits.** 65,224 training, 13,980 validation, 13,984 test. Per language:
English 45,899 / 9,839 / 9,843, Spanish 19,325 / 4,141 / 4,141. Splits are
stratified by class and language and fixed across all experiments, so results
within a condition are computed on identical rows.

**Two properties of the corpus worth knowing before reusing it.** English
non-abusive material was filtered to exclude a small set of profanity keywords
during construction, so that class is not lexically representative. And the
Spanish component merges corpora annotated independently in different countries,
so a single binary label spans judgements that were never calibrated against one
another. Both are discussed in the dissertation, Sections 3.1.1 and 5.6.1.

---

## Running the experiments

The notebooks were developed in Google Colab on NVIDIA T4 GPUs and expect Google
Drive to be mounted. Run them in numerical order; each writes its outputs to the
shared results folder that later notebooks read from.

| Notebook | What it does | GPU |
|---|---|---|
| 1 | Loads and reformats the five sources, merges and balances | no |
| 2 | Corpus characterisation: platform, dialect, implicit expression | no |
| 3 | Cleaning, splits, tokenisation, embedding matrices | no |
| 4 | BiLSTM baseline, all five conditions | yes |
| 5 | DistilBERT, mBERT and XLM-R, all five conditions | yes |
| 6 | Soft-voting ensemble and the cross-model comparison tables | no |
| 7 | BETO, Spanish-only and ES→EN | yes |
| 8 | Class-weighted training across the six transfer conditions | yes |
| 9a, 9b | LoRA-adapted Mistral 7B, zero-shot and few-shot | yes |
| 10 | Error analysis, annotation and the label quality audit | no |

Notebooks 6 and 10 read saved predictions rather than retraining, so they run in
minutes on CPU. The training notebooks take roughly one to two hours each on a
T4.

```bash
pip install -r requirements.txt
```

---

## Reproducibility notes

Seeds are fixed at 42 throughout, but GPU reductions are not deterministic, so
retraining will not reproduce the reported figures exactly. Two accidental
repeats of the same configuration during development gave a spread of 1.44
percentage points on one cross-lingual condition and 0.04 on another; effect
sizes in the dissertation are reported against that noise floor.

Where a training cell would overwrite a saved checkpoint, it is guarded and left
unexecuted, with its original output retained as the record of training. The
notebooks reload saved models rather than retraining.


## Author

Umme-Yusrah Sumtally — MSc Artificial Intelligence, University of Surrey.
