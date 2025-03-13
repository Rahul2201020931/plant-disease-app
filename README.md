# plant-disease-app- Setup Guide

## Setup for Python

### 1. Install Python
Follow the official Python installation guide: [Python Setup](https://www.python.org/downloads/)

### 2. Install Required Python Packages
Run the following commands to install dependencies:
```sh
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt
```

### 3. Install TensorFlow Serving
Follow the official TensorFlow Serving installation guide: [TensorFlow Serving Setup](https://www.tensorflow.org/tfx/serving/setup)

---

## Setup for ReactJS

### 1. Install Node.js
Follow the official Node.js installation guide: [Node.js Setup](https://nodejs.org/)

### 2. Install NPM
NPM comes with Node.js, but if needed, update it:
```sh
npm install -g npm
```

### 3. Install Dependencies
```sh
cd frontend
npm install --from-lock-json
npm audit fix
```

### 4. Configure Environment Variables
```sh
cp .env.example .env
```
Edit `.env` and update the API URL.

---

## Setup for React-Native App

### 1. Install React Native CLI
Follow the React Native setup guide: [React Native Setup](https://reactnative.dev/docs/environment-setup)

### 2. Install Dependencies
```sh
cd mobile-app
yarn install
```

### 3. (For Mac Users Only)
```sh
cd ios && pod install && cd ../
```

### 4. Configure Environment Variables
```sh
cp .env.example .env
```
Edit `.env` and update the API URL.

---

## Training the Model

### 1. Download Dataset
- Download the dataset from Kaggle.
- Keep only folders related to **Potatoes**.

### 2. Run Jupyter Notebook
```sh
jupyter notebook
```

### 3. Open Notebook & Train the Model
- Open `training/potato-disease-training.ipynb` in Jupyter Notebook.
- Update the dataset path in **Cell #2**.
- Run all cells sequentially.

### 4. Save the Model
- Copy the generated model and save it with a version number in the `models` folder.

---

## Running the API

### **1. Using FastAPI**
```sh
cd api
uvicorn main:app --reload --host 0.0.0.0
```
Your API is now running at: **http://0.0.0.0:8000**

### **2. Using FastAPI & TensorFlow Serving**
#### **Step 1: Configure Model Serving**
```sh
cd api
cp models.config.example models.config
```
Update paths in `models.config`.

#### **Step 2: Run TensorFlow Serving**
```sh
docker run -t --rm -p 8501:8501 -v C:/Code/potato-disease-classification:/potato-disease-classification tensorflow/serving --rest_api_port=8501 --model_config_file=/potato-disease-classification/models.config
```

#### **Step 3: Run FastAPI Server**
```sh
uvicorn main-tf-serving:app --reload --host 0.0.0.0
```
Your API is now running at: **http://0.0.0.0:8000**

---

## Running the Frontend

### 1. Navigate to Frontend Folder
```sh
cd frontend
```

### 2. Configure Environment Variables
```sh
cp .env.example .env
```
Update `REACT_APP_API_URL` to match your API URL.

### 3. Start the Frontend
```sh
npm run start
```

---

## Contribution
Feel free to fork this repository, open issues, and submit pull requests. Happy coding!
