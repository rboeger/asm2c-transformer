import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer
from dataset import AsmCDataset
from model import load_model
from tqdm import tqdm
from torch.optim import AdamW

tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = load_model("t5-small")
model.train()

dataset = AsmCDataset("data/asm_c_pairs.tsv", tokenizer)
loader = DataLoader(dataset, batch_size=4, shuffle=True)

optimizer = AdamW(model.parameters(), lr=5e-5)

for epoch in range(3):
    for batch in tqdm(loader):
        outputs = model(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            labels=batch["labels"]
        )
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    print(f"Epoch {epoch+1} loss: {loss.item()}")

# Save the model and tokenizer
model.save_pretrained("saved_model")
tokenizer.save_pretrained("saved_model")
