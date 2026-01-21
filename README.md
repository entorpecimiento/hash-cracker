# ⚡ Cryptographic Hash Decoder

A specialized Python utility engineered for reverse-engineering SHA-256 hashes through dictionary-based analysis. This tool is designed for security auditing and educational exploration of cryptographic vulnerabilities.

---

## 🛠️ Functional Logic

The decoder operates by processing potential candidates through a high-speed comparison engine:

### 🧩 Core Methodology
- **Hash Reconstruction:** Utilizes the `hashlib` library to generate deterministic SHA-256 signatures for each wordlist entry.
- **Matching Engine:** Performs real-time bitwise comparison between the target hash and calculated values.

### ⚙️ Operational Flow
- **Input Handling:** Dynamically loads external `.txt` dictionaries for large-scale wordlist processing.
- **Optimization:** Features a break-on-match logic to maximize efficiency once the original string is identified.

---

## 💎 Technical Specifications
- **Algorithm:** SHA-256 (Secure Hash Algorithm 2).
- **Security Context:** Demonstrates the risks of weak password entropy and the necessity of salting hashes.
- **I/O Management:** Implements robust file stream handling for local dictionary integration.

---

## 📂 Project Structure
- hashcracker.py      # Main cryptographic analysis script.
- diccionario.txt     # Sample wordlist for initial testing and validation.
- README.md           # Technical documentation and usage guide.

---

## 📋 Prerequisites
- **Python 3.10+**
- A standard wordlist or dictionary file (e.g., `rockyou.txt`).

---

## 👤 Developer
[GitHub – entorpecimiento](https://github.com/entorpecimiento)
