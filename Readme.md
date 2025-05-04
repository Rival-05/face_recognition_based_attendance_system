# ATTENDEASE - Face Recognition-based Attendance System

## 📌 Project Description

**ATTENDEASE** is an intelligent and contactless attendance system that uses facial recognition to identify individuals and record their attendance automatically. The system leverages OpenCV and machine learning (KNN classifier) to detect and recognize faces in real-time, and stores attendance in a SQLite database for persistence. It is aimed at reducing proxy attendance and manual errors while making the attendance process seamless.

---

## ⚙️ How to Run the Project

### 1. **Clone the repository**
git clone https://github.com/your-username/Attendease.git
cd Attendease

### 2. **Install Dependencies**
Make sure you have Python installed (version >= 3.7).

Install required Python packages:
pip install -r requirements.txt


### 3. **Collect Face Data**
Run the face capture script to register new users:
python faces.py

This will:
- Capture face data from the webcam.
- Save the flattened face images in data/faces_data.pkl.
- Save corresponding names in data/names.pkl.

### 4. **Run the Attendance System**
python test.py

The system will start your webcam.
- It will recognize faces and display names in real-time.
- Press m to mark attendance if the user is recognized.
- Press q to quit the application.

### 5. **How to view the attendance**

#### Steps:
- Download and install DB Browser for SQLite.
- Open attendance.db from your project folder.
- Go to the "Browse Data" tab.
- Select the attendance table.
- You’ll see all marked entries: name, date, and time.