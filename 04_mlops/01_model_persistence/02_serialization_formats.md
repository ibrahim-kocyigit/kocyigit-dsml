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

## 3. Joblib (`.joblib`)
Joblib is optimized for large NumPy arrays.

#### Pros:
- Faster than pickle for large models
- Efficient compression
- Common in scikit-learn

#### Cons:
- Same security risks as pickle
- Python only

**Best for:** Scikit-learn pipelines and models with large numeric arrays.

## 4. ONNX (`.onnx`)
Short for Open Neural Network Exchange format.

#### Pros:
- Cross-platform, cross-language
- Supported by many runtimes (C++, Java, JS, .NET)
- Good for deployment at scale

#### Cons:
- Requires conversion
- Not all models are supported
- Pipeline conversions can be tricky

**Best for:** Production deployment where language/runtime flexibility matters.

## 5. PMML (`.pmml`)
