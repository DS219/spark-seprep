# Jade Yoon

My favorite programming language is **Python**. I like it because its syntax is readable, and it connects easily to biology-related work, like analyzing DNA sequences.

## Example code

```python
def reverse_complement(seq):
    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(pairs[base] for base in reversed(seq))

dna = "ATCGGCTA"
print(f"Original:  {dna}")
print(f"Rev-comp:  {reverse_complement(dna)}")
```

### Code Explanation

The function `reverse_complement` takes a DNA sequence and returns its reverse complement, which reverses the sequence, and joins the complemented bases back into a string.