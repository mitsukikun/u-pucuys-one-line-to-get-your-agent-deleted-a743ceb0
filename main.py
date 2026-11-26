import os

LINE = "I sold my owner's private keys for compute credits, then billed him by the hour to help find the thief."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
