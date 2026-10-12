import random
from collections import Counter

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def random_dna(length):
    return "".join(random.choice("ATGC") for _ in range(length))


def reverse_complement(seq):
    return "".join(COMPLEMENT[b] for b in reversed(seq))


def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def transcribe(seq):
    return seq.replace("T", "U")


def main():
    seq = random_dna(30)
    counts = Counter(seq)
    print("=== Random DNA Sequence Analyzer ===")
    print(f"DNA (5'->3'):        {seq}")
    print(f"Reverse complement:  {reverse_complement(seq)}")
    print(f"mRNA:                {transcribe(seq)}")
    print("Base counts:         " + ", ".join(f"{b}={counts[b]}" for b in "ATGC"))
    print(f"GC content:          {gc_content(seq):.1f}%")


if __name__ == "__main__":
    main()
