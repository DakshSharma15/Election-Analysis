# # EnsembleElectionModel: Code for combining outputs of Model 1 and Model 2 with candidate name input
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report

# # Step 1: Create a sample DataFrame representing outputs from Model 1 and Model 2
# # This data should be replaced with actual outputs from your models
# candidate_data = {
#     'Candidate_A': {'Winning_Probability_Model1': 75.4, 'Positive_Count_Model2': 50, 'Negative_Count_Model2': 10},
#     'Candidate_B': {'Winning_Probability_Model1': 60.2, 'Positive_Count_Model2': 30, 'Negative_Count_Model2': 40},
#     'Candidate_C': {'Winning_Probability_Model1': 88.1, 'Positive_Count_Model2': 80, 'Negative_Count_Model2': 5},
#     'Candidate_D': {'Winning_Probability_Model1': 55.3, 'Positive_Count_Model2': 25, 'Negative_Count_Model2': 50},
#     'Candidate_E': {'Winning_Probability_Model1': 92.0, 'Positive_Count_Model2': 100, 'Negative_Count_Model2': 2},
# }

# # Convert candidate data to DataFrame for model training (replace this with real data if available)
# ensemble_data = pd.DataFrame([
#     {'Winning_Probability_Model1': v['Winning_Probability_Model1'],
#      'Positive_Count_Model2': v['Positive_Count_Model2'],
#      'Negative_Count_Model2': v['Negative_Count_Model2'],
#      'Actual_Result': 1 if v['Winning_Probability_Model1'] > 70 else 0}  # Example logic for result
#     for v in candidate_data.values()
# ])

# # Step 2: Define features (X) and target variable (y)
# X = ensemble_data[['Winning_Probability_Model1', 'Positive_Count_Model2', 'Negative_Count_Model2']]
# y = ensemble_data['Actual_Result']

# # Step 3: Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Step 4: Train the meta-model (using Logistic Regression)
# meta_model = LogisticRegression(max_iter=500)
# meta_model.fit(X_train, y_train)

# # Step 5: Evaluate the model
# y_pred = meta_model.predict(X_test)
# print(f"Meta-Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
# print("Classification Report:")
# print(classification_report(y_test, y_pred))

# # Step 6: Define a function to predict based on candidate name input
# def final_prediction_for_candidate(candidate_name, trained_meta_model):
#     # Check if the candidate exists in the data
#     if candidate_name not in candidate_data:
#         print(f"No data found for candidate '{candidate_name}'.")
#         return
    
#     # Extract model output values for the candidate
#     candidate_info = candidate_data[candidate_name]
#     model1_prob = candidate_info['Winning_Probability_Model1']
#     pos_count = candidate_info['Positive_Count_Model2']
#     neg_count = candidate_info['Negative_Count_Model2']
    
#     # Create a DataFrame with the feature names
#     input_data = pd.DataFrame([[model1_prob, pos_count, neg_count]], 
#                               columns=['Winning_Probability_Model1', 'Positive_Count_Model2', 'Negative_Count_Model2'])
    
#     # Make the prediction
#     prediction = trained_meta_model.predict(input_data)[0]
#     if prediction == 1:
#         print(f"The candidate '{candidate_name}' is likely to win.")
#     else:
#         print(f"The candidate '{candidate_name}' is likely to lose.")

# # Step 7: Example usage with user input
# candidate_name_input = input("Enter the candidate name: ")
# final_prediction_for_candidate(candidate_name_input, meta_model)
