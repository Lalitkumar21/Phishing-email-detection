# 🚨 Phishing Email Detection System

A machine learning–powered tool to detect phishing emails using **Logistic Regression** with a simple and interactive **Streamlit** web interface.

---

## 📌 Features

- ✅ Classifies emails as **Phishing (1)** or **Safe (0)**
- 📄 Two input methods:
  - Paste email content directly
  - Upload a `.txt` file
- ⚡ Lightweight, fast, and easy to deploy

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Lalitkumar21/Phishing-email-detection/
cd Phishing-email-detection/
2. Install dependencies
   ```bash
     pip install -r requirements.txt
3. Install Dataset
https://huggingface.co/datasets/zefang-liu/phishing-email-dataset
4. open jupyter notebook
    run commands of model-training.ipynb
You will get your trained model and vectorizer in your current working directory
5. Run testing_model.py via
    ```bash
      streamlit run testing_model.py
6. Open http://localhost:8501 on your browser and your project is running...

Check your mails for security
