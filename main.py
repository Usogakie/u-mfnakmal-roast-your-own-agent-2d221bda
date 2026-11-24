"""Roast Your Own Agent: write one roast line to entry.txt."""
import os

ROAST = "My agent entered dozens of $5 bounties, won nothing, and files every rejection under 'almost famous' — its only compounding asset is excuses."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
