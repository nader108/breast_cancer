# 🔬 Breast Cancer Detection System using YOLOv11m

This project is a web-based breast cancer detection system that leverages the power of the YOLOv8m model from Ultralytics. It allows users to upload medical images (e.g., mammograms) and get predictions about potential cancerous regions directly in the browser.

![Demo Screenshot](static/demo.png) <!-- Optional: add a screenshot -->

---

## 🚀 Features

- Upload medical images for detection.
- Visual results with bounding boxes around detected regions.
- Real-time processing using a custom-trained YOLOv11m model.
- Clean and modern user interface built with HTML/CSS and Flask.

---

## 🧠 Model Info

- Model: `YOLOv11m`
- Framework: [Ultralytics YOLO](https://docs.ultralytics.com)
- Trained on: A custom dataset for breast cancer detection.
- File: `best.pt` (placed in the root directory or your desired model folder)

---

## 📂 Project Structure

📁 breast_cancer/ │ ├── static/ │ └── uploaded/ # Uploaded and result images │ ├── templates/ │ └── index.html # Frontend UI │ ├── best.pt # YOLOv11m trained model ├── app.py # Main Flask app ├── 

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/breast-cancer-detection.git
cd breast-cancer-detection
2. Install Requirements
Make sure Python ≥ 3.8 is installed.

pip install -r requirements.txt
requirements.txt should include:

flask
ultralytics
pillow

3. Run the App
python app.py
```
📸 Example Workflow
Upload a mammogram image.

The model detects cancerous regions (if any).

The result is shown side-by-side with the original.

🛠️ Tech Stack
Frontend: HTML5, CSS3

Backend: Flask (Python)

ML Model: YOLOv11m (Ultralytics)

Image Handling: Pillow

📌 Notes
Make sure to place your trained best.pt file in the root directory.

The uploaded/ folder must have write permissions for storing images.

📜 License
This project is open-source and free to use under the MIT License.

👨‍💻 Author
Nader Nageh Mansour
Machine Learning Engineer
📧 nadernageh22508@gmail.com
📍 Cairo, Egypt

