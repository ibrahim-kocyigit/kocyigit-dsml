# Serialization Formats

## 1. Why Formats Matter
Serialization formats determine:
- **Portability:** Can you load the model in another language/environment?
- **Performance:** Speed and size of saved artifacts
- **Security:** Risk of arbitrary code execution
- **Compatibility:** Works across library versions or not

## 2. Pickle (`.pkl`)
This is Python's native serialization format.

#### Pros:
- Easy to use
- Works with most Python objects
- Common in ML workflows

#### Cons:
- **Not secure:** Unpickling untrusted files can execute code
- **Python-only:** Cannot be used in other languages
- Fragile across versions of libraries

**Best for:** Quick experiments and internal workflows where artifacts are trusted.

