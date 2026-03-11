Core Problem: Data Imbalance Initial Plan was to use one Spanish dataset (3.5K) and one English dataset (47K). However, this creates a severe imbalance by a factor of 1:13 respectively and thus leading to multiple issues like:

Model Bias
Poor Spanish Performance
Invalid Cross-Lingual Evaluation (not enough Spanish data for model to train on)
Solution: A Two-Step Merge Strategy

**First**: Merge the Two Spanish Datasets First
Colombian Dataset ~3.5K OffendES ~16.5K ==> Merged Spanish corpus ~20K

**Second**: Merge English + Combined Spanish (balanced bilingual dataset) ==> Balance , Meaningful Bilingual Training

===================================================== JUSTIFICATIONS =============================================================
Justification about merging 2 Spanish Datasets:
1. Language variety - Spain Spanish & Colombian Spanish (allow different dialects, slang, and cultural expressions)
2. Nuance + Context aware - OffendES has a richer group of nuanced examples whereas the colombian dataset is context dependent
3. Data source - OffedndES data are comments posted on Instagram/Youtube & Twitter whereas the Colombian dataset consist of Tweets collected using specific keywords which will expose the model to different linguistic styles and online communication formats & thus improving the ability to generalize to "social media"
4.The corpus will captures dialectal variation, different platform styles, and both the subjective and expert-defined nature annotiation upon merging these 2 Spanish datasets which aligns with the goal of generalizable and effective model across the Spanish communities.

Justification about merging the Created Spanish Corpus and an English dataset:
goal: Bilingual cyberbullying detection
1. To Enable and Validate Cross-Lingual Learning (Zero-shot evaluation experiments.)
2. To Address the "Resource-Rich"(English) vs. "Low-Resource"(Spanish) Dynamic -- explore techniques like pre-training/fine-tuning
3. To Increase Model Robustness and Generalizability (model exposed to wider variety of linguistic phenomena, including code-switching, anglicisms, and platform-specific slang)
4.Mitigate Annotation Biases - model is forced to learn the concept of abusive language rather than overfitting to specific definitions provided by only 1 group of annotators -- the 2 Spanish Dataset annotated --> expert therapist vs. crowdsourced ++ independently annotated English dataset

Justification for Mapping to Binary Scheme:
1. Align with dissertation objective (cyberbullying detection as a binary task)
2. Consistency across dataset (using a unified binary scheme ensures consistency and avoids incompatible label representations which could lead to cross-lingual analysis impossible.)
3. Reducing complexity while retaining core information
4. To improve the models' performance (Binary classification is statistically more robust than multi-class classification, especially for imbalanced datasets)
5. Cross-Lingual Comparability (consistent binary labeling scheme to ensure cross-lingual compatibility when comparing cyberbullying patterns in English and Spanish)

Justification for keeping only 3 columns
1. Minimal Viable Data for Modeling (For BiLSTM, XLM-R, DistilBERT, mBERT, the only required inputs are the text content and the target label, everything else is noise)
2. Column Mismatch Prevention (The three original datasets had different column structures - if merged directly, it would lead to NaN values and type errors. Hence using only 3 columns to remove this issue)
3. Memory Efficiency (reduces memory footprint and speeds up data loading, preprocessing, and model training)
4. Reproducibility (a standardized dataset format ensures proper understandability for anyone else using the dataset)
5. Language-Aware Analysis ('language' column is crucial for bilingual analysis as it allows data filtering by language for monolingual experiments & separate language performance analysis & prevent a language-agnostic blob which would have made cross-lingual evaluation impossible)
6. Pipeline Simplicity (consistent 3-column format across all datasets allows a unified preprocessing and training pipeline & reduces code duplication and potential bugs)
