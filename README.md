# ✍️ Signature Matching System (Flask + OpenCV)

A simple web-based application that allows users to upload two signature images and compare them using image processing techniques.

---

## 🚀 Features

* Upload two signature images
* Automatic image preprocessing (grayscale + resize)
* Similarity calculation using SSIM (Structural Similarity Index)
* Result display with match / no match decision

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Image Processing:** OpenCV
* **Similarity Algorithm:** SSIM (scikit-image)
* **Frontend:** HTML (Jinja Templates)

---

## 📂 Project Structure

```
signature_match/
│── app.py
│── templates/
│     └── index.html
│── static/
│     └── uploads/
```

---

## ⚙️ Installation

### 1. Clone Repository

```
git clone https://github.com/your-username/signature-match.git
cd signature-match
```

### 2. Install Dependencies

```
pip install flask opencv-python scikit-image numpy
```

---

## ▶️ Run the Application

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User uploads two images
2. Images are converted to grayscale
3. Images are resized to the same dimensions
4. SSIM algorithm calculates similarity score
5. Result is displayed:

   * **> 0.7** → Signatures Match ✅
   * **≤ 0.7** → Signatures Do Not Match ❌

---

## ⚠️ Limitations

* Basic image comparison only
* Sensitive to image quality, rotation, and noise
* Not suitable for real-world authentication systems

---

## 🔥 Future Improvements

* Deep Learning-based signature verification (CNN / Siamese Network)
* Image preprocessing (noise removal, edge detection)
* Database integration for storing signatures
* User authentication system
* Admin dashboard

---

## 📸 Demo

(Add screenshots here)

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
