import random
import os

BASE_DIR = "/scratch/project_2011718/linyao_du/final_project/processed"

def split_corpus(name, total_train_limit, dev_size=1000, test_size=1000):
    print(f"Processing: {name} ...")
    src_path = os.path.join(BASE_DIR, f"{name}_clean.en")
    tgt_path = os.path.join(BASE_DIR, f"{name}_clean.zh")

    if not os.path.exists(src_path):
        print(f"Error: File not found {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as fs, open(tgt_path, 'r', encoding='utf-8') as ft:
        src_lines = [line.strip() for line in fs]
        tgt_lines = [line.strip() for line in ft]

    combined = list(zip(src_lines, tgt_lines))
    random.seed(42)
    random.shuffle(combined)

    # Splitting logic
    dev_set = combined[:dev_size]
    test_set = combined[dev_size : dev_size + test_size]
    train_set = combined[dev_size + test_size :]
    
    if total_train_limit and len(train_set) > total_train_limit:
        train_set = train_set[:total_train_limit]

    def save_file(data, suffix):
        out_src = os.path.join(BASE_DIR, f"{suffix}.en")
        out_tgt = os.path.join(BASE_DIR, f"{suffix}.zh")
        with open(out_src, 'w', encoding='utf-8') as f1, open(out_tgt, 'w', encoding='utf-8') as f2:
            for s, t in data:
                f1.write(s + '\n')
                f2.write(t + '\n')
        print(f"  -> Generated {suffix}: {len(data)} lines")

    save_file(dev_set,   f"dev_{name}")
    save_file(test_set,  f"test_{name}")
    save_file(train_set, f"train_{name}")

split_corpus("unpc", total_train_limit=500000)
split_corpus("ted", total_train_limit=50000)