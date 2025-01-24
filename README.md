---

# **Spam Email Classifier**

### **Overview**
The **Spam Email Classifier** is a machine learning project designed to identify whether an email or text message is spam or not. It utilizes a Naive Bayes classifier trained on a preprocessed dataset and employs TF-IDF vectorization for feature extraction. The project is deployed as an interactive web application using Streamlit.

---

### **Features**
- Preprocesses and cleans raw text data.
- Extracts numerical features from text using TF-IDF.
- Classifies messages as either **Spam** or **Not Spam**.
- Interactive web application for real-time classification.

---

### **Technologies Used**
- **Programming Language:** Python
- **Machine Learning Library:** Scikit-learn
- **Text Processing:** NLTK
- **Deployment:** Streamlit
- **Serialization:** Joblib

---

### **Dataset**
The dataset used is the **SMS Spam Collection Dataset**, which contains labeled messages as either "ham" (not spam) or "spam."

---

### **Model Performance**
The Naive Bayes model achieved the following results:
- **Accuracy:** 96.68%
- **Precision:** _[Insert precision for spam class]_
- **Recall:** _[Insert recall for spam class]_

---

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Keepkirui/spam-email-classifier.git
   cd spam-email-classifier
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

### **How to Use**
1. Launch the application using the steps above.
2. Enter the email or text message you want to classify in the text area.
3. Click the **Classify** button to get the result: **Spam** or **Not Spam**.

---

### **Project Structure**
```
Spam-Email-Classifier/
├── data/
│   └── spam.csv                # Dataset
├── app.py                      # Streamlit app script
├── spam_classifier_model.pkl   # Saved Naive Bayes model
├── tfidf_vectorizer.pkl        # Saved TF-IDF vectorizer
├── README.md                   # Project documentation
└── requirements.txt            # Dependencies file
```

---

### **Results**
Below is an example screenshot of the web application:

![image](https://github.com/user-attachments/assets/2c04cd17-70dc-4597-bc70-2f042f418d6f)


---

### **Future Enhancements**
- Include support for multilingual datasets.
- Improve accuracy with advanced models like Support Vector Machines or deep learning.
- Add additional preprocessing techniques like named entity recognition (NER).

---

### **Contributions**
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/spam-email-classifier/issues).

---

### **License**
This project is licensed under the [MIT License](LICENSE).

---
