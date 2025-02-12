# Ania Shaheed

My favorite programming language is python because I use it. 

## Example Code
'''
def bag(examples, labels):
  # TODO
  new_examples = []
  new_labels = []

  for _ in range(len(labels)):
      index = random.randrange(len(labels))
      new_examples.append(examples[index])
      new_labels.append(labels[index])

  return new_examples, new_labels
'''

### Code Explanation
The function bag() takes a list of N examples and N labels and returns a list of N examples and N corresponding labels that have been sampled with replacement from the original lists. 
