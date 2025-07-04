# asm2c-transformer

A minimal transformer-based decompiler that learns to convert **assembly code** back into **C source code** using a sequence-to-sequence model.

> This project was inspired by [RevEng.AI](https://blog.reveng.ai/training-an-llm-to-decompile-assembly-code/) and serves as a hands-on starting point for training and evaluating AI-based decompilers.
> Special thanks to Russell for the reverse engineering inspiration.

---

## Project Structure

asm2c-transformer/
├── data/ # Assembly ↔ C function pairs
├── scripts/ # Model, dataset, and training scripts
├── tokenizer/ # Placeholder for custom tokenization
├── saved_model/ # Folder created after training
├── test_the_model.ipynb # Jupyter notebook for inference
├── requirements.txt
└── README.md

---

## How to Use

1. **Install dependencies**  
   pip install -r requirements.txt

2. Train the model
   From the root directory:
   python scripts/train.py

3. Test it out
   Open `test_the_model.ipynb` in Jupyter or VS Code.
   You can paste in assembly and see the generated C code.

## Notes

* The dataset is tiny - just 3 examples - and easily expandable.
* Uses `t5-small` from HuggingFace for fast experimentation.
* Model and tokenizer will be saved to `saved_model/` after training.

## Contribute or Fork

This project is designed to be a launchpad for deeper exploration. Feel free to fork, improve, or ping me if you'd like to collaborate on a larger dataset or model!