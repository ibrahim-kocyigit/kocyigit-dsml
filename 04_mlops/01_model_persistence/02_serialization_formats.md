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
Short for Predictive Model Markup Language (XML-based).

#### Pros:
- Language-agnostic
- Human-readable
- Used in enterprise settings

#### Cons:
- Limited support for modern models
- Complex pipelines can be hard to represent

**Best for:** Traditional ML models in enterprise systems.

## 6. TensorFlow / PyTorch Formats

- **TensorFlow:** `.h5` or SavedModel
- **PyTorch:** `.pt` or `pth`

**Best for**: Deep learning models trained in these frameworks.

## 7. Choosing the Right Format

| Use Case | Recommended Format |
|---------|--------------------|
| scikit-learn prototype | `joblib` |
| Python-only deployment | `joblib` or `pickle` |
| Cross-language deployment | `onnx` |
| Enterprise legacy systems | `pmml` |
| Deep learning models | framework-native format |

### ⚠️ Security Reminders
- Never load serialized model files from untrusted sources.  
- Formats like **pickle** and **joblib** can execute arbitrary code during loading.

---

**Next**: [Saving and Loading Models](./03_saving_and_loading_models.md)