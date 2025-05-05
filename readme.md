# 🦙 Bujji — Chat with Llama 2

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Gradio-orange)
![Model](https://img.shields.io/badge/Model-Ollama-9cf)

**Bujji** is a conversational AI assistant powered by **Llama 2**, featuring a lightweight **Gradio** interface for real-time interaction.  
Whether you're experimenting with large language models or building your own chatbot, Bujji provides a ready-to-use, customizable framework.

---

## 🚀 Features

✅ Chat live with a Llama 2 model  
✅ Simple, intuitive Gradio web interface  
✅ Easy customization for your own needs  
✅ Lightweight and quick to deploy  

---

## 📦 Installation

### Prerequisites

- Python 3.9 or higher  
- (Optional) Docker, if you want containerized deployment

---

### Setup Steps

1️⃣ Clone the repository:

```bash
git clone https://github.com/your-username/bujji.git
cd bujji
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Run the app:

```bash
python app.py
```

This will **launch the Gradio web UI** in your browser where you can chat live with Bujji!

---

## 🛠 Example Usage

Once running, open the provided local Gradio URL (usually shown as `http://127.0.0.1:7860` in the terminal) and start chatting.

Example prompt:

```
🦙 Bujji: Hi there! How can I help you today?
👤 You: Tell me a fun fact about space.
```

---

## 🐳 Docker (Optional)

If you prefer running Bujji in a container:

```bash
docker build -t bujji .
docker run -p 7860:7860 bujji
```

---

## 📝 License

This project is licensed under the MIT License — see the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- **Meta (Llama 2)** for providing the powerful language model  
- **Gradio** for the easy-to-use web interface  
- **Ollama** for integration support

---

## 📬 Contact

Have questions or suggestions?  
Feel free to open an issue or reach out by email!

💡 **Happy chatting with Bujji! 🚀**
