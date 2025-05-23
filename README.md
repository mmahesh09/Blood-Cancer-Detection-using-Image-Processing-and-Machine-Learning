![Image](https://github.com/mmahesh09/Blood-Cancer-Detection-using-Image-Processing-and-Machine-Learning/blob/1a58101479ecb0139b6623d22c539222015b67f3/images/Credit-Card%20fraud%20detection%20(1).png)

 
# Blood Cancer Detection using Image Processing and Machine Learning 🩸
>"Blood cancer is the fifth most common cancer in the world, with an estimated 1.24 million new cases annually. In India, it's the third most common cancer, with about 80,000 new cases per year"





## Index

* What is Blood Cancer?
* Problem Statement
* Blood Cancer Types (e.g., Leukemia, Lymphoma, Myeloma)
* Current Detection Techniques
* Methodology
* Implementation
* Technologies used
* Results and Analysis
* Conclusion and Future Work
* Contributions

##  What is Blood Cancer?🩸
Blood cancer, or hematologic cancer, is a group of cancers that affect the blood, bone marrow, or lymphatic system. It occurs when abnormal blood cells grow uncontrollably, disrupting the production and function of normal blood cells. The main types are leukemia (affecting white blood cells), lymphoma (affecting the lymphatic system), and myeloma (targeting plasma cells in bone marrow). These cancers impair the body’s ability to fight infections, carry oxygen, and stop bleeding. Symptoms may include fatigue, fever, infections, bruising, or swollen lymph nodes. Treatment often involves chemotherapy, radiation, targeted therapy, or stem cell transplants, depending on the type and severity.


## Problem Statement
Blood cancer detection is a critical challenge in the medical field, as early diagnosis significantly improves treatment outcomes. Traditional diagnostic methods, such as blood tests and manual examination of blood samples, can be time-consuming and prone to human error. This project aims to develop an automated system for blood cancer detection using image processing and machine learning techniques. By analyzing microscopic images of blood samples, the system will identify and classify abnormal cell patterns indicative of blood cancers like leukemia, lymphoma, or myeloma. The goal is to provide a faster, more accurate, and reliable method for early blood cancer detection, assisting healthcare professionals in making timely and informed decisions.


## Blood Cancer Types :

![Image](https://www.lls.org/sites/default/files/styles/large/public/2024-09/Facts%202023-2024%20Figure%201.jpg?itok=6_ftxGkU)

![Image](https://github.com/user-attachments/assets/3f9b1485-1672-458b-bffe-40527039cd71)


There are three main types of blood cancer: **Leukemia**, **Lymphoma**, and **Myeloma**. Here’s a brief description of each:

 ### Leukemia:
 
>"In 2024, 62,770 people are expected to be diagnosed with Leukemia."

   - **Description**: Leukemia is cancer of the blood and bone marrow, primarily affecting white blood cells. It leads to the rapid production of abnormal white blood cells that interfere with the body’s ability to fight infections and produce normal blood cells.
   - **Types**: 
     - *Acute lymphocytic leukemia (ALL)*: Affects lymphoid cells and progresses rapidly.
     - *Acute myeloid leukemia (AML)*: Affects myeloid cells, also aggressive.
     - *Chronic lymphocytic leukemia (CLL)*: Affects lymphocytes, progresses slowly.
     - *Chronic myeloid leukemia (CML)*: Affects myeloid cells, progresses more slowly.


 ### Lymphoma:
 
   >"About 89,190 people in the US are expected to be diagnosed with lymphoma in 2024 (8,570 cases of HL and 80,620 cases of NHL)."
   
   - **Description**: Lymphoma is cancer of the lymphatic system, which includes lymph nodes, spleen, and bone marrow. It begins in the lymphocytes (a type of white blood cell) and can affect various parts of the body.
   - **Types**:
     - *Hodgkin lymphoma (HL)*: Characterized by the presence of Reed-Sternberg cells, usually starts in lymph nodes.
     - *Non-Hodgkin lymphoma (NHL)*: A diverse group of blood cancers affecting lymphocytes, can start in lymph nodes or other organs.

 ### Myeloma:
 
   >"An estimated 35,780 new cases of myeloma (19,520 males and 16,260 females) are expected to be diagnosed in the US in 2024"

   - **Description**: Multiple myeloma is a cancer of plasma cells in the bone marrow. Plasma cells are a type of white blood cell responsible for producing antibodies. In myeloma, abnormal plasma cells grow uncontrollably, leading to weakened bones, kidney problems, and a weakened immune system.
   - **Symptoms**: Bone pain, fractures, fatigue, and recurrent infections are common in myeloma.

These cancers disrupt normal blood cell production and function, often causing symptoms like fatigue, infections, bleeding, and organ damage. Early diagnosis and treatment are key to improving outcomes for patients with blood cancers.

## Current Detection Techniques :
Here are two current detection techniques for blood cancer:

 **Blood Tests (Complete Blood Count - CBC)**:
   - A CBC test measures the number and types of blood cells, including red blood cells, white blood cells, and platelets. Abnormal levels or unusual cell characteristics can indicate the presence of blood cancer. For example, leukemia may cause an elevated number of white blood cells or the presence of immature cells.

 **Bone Marrow Biopsy**:
   - A bone marrow biopsy involves extracting a sample of bone marrow (usually from the hip bone) to examine for abnormal cell growth. This test helps in diagnosing various blood cancers like leukemia and lymphoma, providing detailed insights into the type of cancer and its stage.

## Methodology:

![image](https://github.com/user-attachments/assets/3a437221-fbd8-4c28-b20e-35b9bd217055)

## Dataset📂

As a highly prevalent cancer, the definitive diagnosis of acute lymphoblastic leukemia (ALL) requires invasive, expensive, and time-consuming diagnostic tests. ALL diagnosis using peripheral blood smear (PBS) images plays a vital role in the initial cancer screening from non-cancer cases. The examination of these PBS images by laboratory users is riddled with problems such as diagnostic error because the non-specific nature of ALL signs and symptoms often leads to misdiagnosis.

The images of this dataset were prepared in the bone marrow laboratory of Taleqani Hospital (Tehran, Iran). This dataset consisted of 3256 PBS images from 89 suspected patients whose blood samples were prepared and stained by skillful laboratory staff. This dataset is divided into two classes benign and malignant. The former comprises hematogenous; the latter is the ALL group with three subtypes of malignant lymphoblasts: Early Pre-B, Pre-B, and Pro-B ALL. All the images were taken using a Zeiss camera in a microscope with 100x magnification and saved as JPG files. A specialist using the flow cytometry tool made the definitive determination of the types and subtypes of these cells. We also provide segmented images after color thresholding-based segmentation in the HSV color space.


## Data Augmentation💻

Data augmentation is a technique used in machine learning and deep learning to artificially increase the size of a dataset by applying transformations or modifications to existing data. It is particularly common in computer vision, natural language processing (NLP), and speech recognition tasks.

The main goal of data augmentation is to improve the generalization ability of a machine learning model by exposing it to variations of the data, thereby reducing overfitting and enhancing performance.

## **Feature Extraction**  ♻️
Feature extraction transforms raw data into a set of meaningful, informative attributes for machine learning models. It reduces data dimensionality while retaining essential information. Techniques like Principal Component Analysis (PCA), Fourier Transform, and word embeddings are often used, depending on data types (e.g., text, image, or numerical). Well-extracted features improve model accuracy and performance by enabling the algorithm to recognize patterns effectively, remove noise, and focus on the most relevant data attributes.

## **Training the Data**  📂
Training involves using labeled data to teach a machine-learning model to predict outputs. The model adjusts its parameters by minimizing the loss function, often using optimization techniques like gradient descent. Data is fed into the model in batches or iteratively, refining predictions through backpropagation. Training uses a larger portion of the dataset to learn patterns and relationships between input features and target outputs, ensuring the model generalizes well for unseen data.

## **Testing the Data**  🌐
Testing evaluates a machine learning model's performance on unseen data. After training, the test dataset (a separate portion of the original data) assesses how well the model generalizes. Metrics such as accuracy, precision, recall, and F1-score are calculated to measure performance. Testing helps identify overfitting or underfitting, ensuring the model isn’t biased toward training data. It objectively evaluates the model's ability to make reliable predictions on real-world or new input data.


## Implementation💻

Blood cancer detection using machine learning and image processing involves analyzing microscopic blood smear images to identify abnormalities. Preprocessing techniques like noise reduction, image segmentation, and feature extraction (e.g., color, shape, and texture) are applied to isolate and highlight relevant cell characteristics. Machine learning models, such as convolutional neural networks (CNNs), are then trained on labeled datasets of healthy and cancerous cells. These models automatically learn patterns to classify and predict blood cancer subtypes (e.g., leukemia). Advanced techniques like transfer learning and ensemble methods improve accuracy. This approach enables early detection, aiding diagnosis and treatment planning with high precision and efficiency.


## Technologies Used ⚙️

| Title | Description |
|--------|-------------|
| Google Colab | Google Colab is a cloud-based platform that allows users to write, execute, and share Python code seamlessly. It supports machine learning, data analysis, and collaboration with free GPU/TPU access. |
| Python | A widely used and open-source programming language with high efficiency and easily understandable |

  ### Libraries used 
  | Library Name | Description |
  |--------------|-------------|
  | Numpy| NumPy is a Python library for numerical computations, offering powerful tools for handling arrays, matrices, and mathematical operations. In my project, it processes image data and supports feature extraction efficiently. |
  | Pandas | Pandas is a Python library for data manipulation and analysis. In your project, it can process structured data, manage datasets, and create visualizations, aiding feature extraction for blood cancer detection models. |
  | Matplotlib | Matplotlib is a powerful Python library for creating visualizations like line graphs, histograms, and scatter plots. In my project, it's used to visualize blood smear image data and analysis results. | 
  | Scikit-Learn | Scikit-learn is a powerful Python machine-learning library offering classification, regression, and clustering tools. In my project, it enables efficient model training, evaluation, and hyperparameter tuning for blood cancer detection. |
  | Tensorflow | TensorFlow is an open-source machine learning framework ideal for image processing tasks. In my project, TensorFlow facilitates training a CNN to detect blood cancer by analyzing microscopic blood smear images.
  | Keras | Keras is a high-level neural network API that simplifies building and training deep learning models. In my project, Keras is used to implement and train machine learning models for blood cancer detection. |
  | Pickle | Pickle is a Python module used for serializing and deserializing objects. In my project, it can store trained machine learning models or image data, enabling easy saving, loading, and sharing across sessions. |
  | Flask | Flask is a lightweight Python web framework used to build web applications. In my project, Flask can serve as the backend, handling image processing requests and integrating machine learning models for blood cancer detection. |

![image](https://github.com/mmahesh09/Blood-Cancer-Detection-using-Image-Processing-and-Machine-Learning/blob/4c626d20014b976e484e35161e0508e52b3a7b28/Code%20Snippets/Modules.png)


## Result and Analysis📈

The results in the model can be tabulated :

| Parameter | Score |
|-----------|-------|
| Accuracy | 84.3% |
| Precision | 84.5% |
| Recall | 84.32% |
| F1-score | 84.24 % |

![image](https://github.com/mmahesh09/Blood-Cancer-Detection-using-Image-Processing-and-Machine-Learning/blob/727aecf83c743ff82a094ca004214feb19d2045b/Graphs/download%20(1).png)

![image](https://github.com/mmahesh09/Blood-Cancer-Detection-using-Image-Processing-and-Machine-Learning/blob/727aecf83c743ff82a094ca004214feb19d2045b/Graphs/download%20(1).png)

![image](https://github.com/mmahesh09/Blood-Cancer-Detection-using-Image-Processing-and-Machine-Learning/blob/727aecf83c743ff82a094ca004214feb19d2045b/Graphs/download%20(2).png)

![image](https://github.com/mmahesh09/Blood-Cancer-Detection-using-Image-Processing-and-Machine-Learning/blob/727aecf83c743ff82a094ca004214feb19d2045b/Graphs/graph2.png)


### Alogrithms used :📊
**Support Vector Machines (SVM)** are supervised machine learning algorithms used for classification and regression. They find the optimal hyperplane separating classes, maximizing margins, and can handle non-linear data using kernels.

**Random Forest** is an ensemble machine learning algorithm combining multiple decision trees. It improves accuracy, reduces overfitting, and handles missing data by averaging predictions for regression or voting for classification.

**K-Nearest Neighbors (KNN)** is a simple, non-parametric machine learning algorithm that classifies data points based on the majority class of their closest neighbors in feature space.

| Algorithm | Accuracy | 
|-----------|-------|
| Random Forest | 75.38 | 
| Support Vector Machine |69.49 |
| K-nearest NeighBours | 30.28 | 

![image](https://github.com/mmahesh09/Blood-Cancer-Detection-using-Image-Processing-and-Machine-Learning/blob/727aecf83c743ff82a094ca004214feb19d2045b/Graphs/output.png)

## Conclusion and Future Work

### **Conclusion**  
Machine learning and image processing have proven to be effective tools for early and accurate detection of blood cancer. Techniques such as feature extraction, segmentation, and classification enable automated analysis of blood smear images, reducing manual effort and increasing diagnostic accuracy. Algorithms like CNNs, SVMs, and KNN have shown promising results in identifying abnormalities in white blood cells. While these methods improve diagnostic efficiency and consistency, challenges remain in handling data imbalance and ensuring model generalizability across diverse populations. Integrating expert knowledge with machine learning can create robust tools to assist clinicians in making faster and more precise diagnoses.

---

### **Future Work**  
Future research on blood cancer detection can focus on improving the robustness and scalability of machine-learning models. Incorporating_large, diverse datasets with varied demographic and genetic information can enhance model generalization. Advanced deep learning architectures, such as transformer models, can be explored to improve image analysis capabilities. Real-time blood cancer detection systems integrated with wearable devices or automated microscopes could revolutionize point-of-care diagnostics. Furthermore, explainable AI techniques can help clinicians interpret predictions, fostering trust in automated systems. Combining image processing with multi-omics data (e.g., genomics and proteomics) could offer even more precise, personalized blood cancer detection and treatment.

## Contributors

| Name | Roll Number |
|-------|------------|
| M.Mahesh Babu | 21711A0434 |
| SK.Yasin | 21711A0453|
| T.V Adithya | 21711A0460 |
| U.Venkat Ajay | 21711A0462 |
