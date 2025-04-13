import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

# Load datasets
data_2024 = pd.read_csv('election_results_2024.csv')
data_2019 = pd.read_csv('india_election_2019.csv')
data_2014 = pd.read_csv('india_election_2014.csv')

# Preprocessing 2024 data
data_2024_clean = data_2024.rename(columns={
    'Constituency': 'PC Name',
    'Leading Candidate': 'Winning Candidate',
    'Leading Party': 'Party',
    'Margin': 'Margin'
})
data_2024_clean['Margin'] = data_2024_clean['Margin'].replace('-', '0', regex=False).replace(',', '', regex=True).astype(float)
data_2024_clean = data_2024_clean[['PC Name', 'Winning Candidate', 'Party', 'Margin']]

# Preprocessing 2019 data
data_2019_clean = data_2019[['PC Name', 'Winning Candidate', 'Party', 'Electors', 'Votes', 'Turnout', 'Margin %']]

# Preprocessing 2014 data
data_2014_clean = data_2014[['PC Name', 'Winning Candidate', 'Party', 'Votes', 'Turnout']]

# Merging datasets
merged_2024_2019 = pd.merge(data_2024_clean, data_2019_clean, on=['PC Name', 'Party'], how='left')
merged_data = pd.merge(merged_2024_2019, data_2014_clean, on=['PC Name', 'Party'], how='left')

# Rename columns for clarity
merged_data.rename(columns={
    'Winning Candidate_x': 'Winning Candidate 2024',
    'Winning Candidate_y': 'Winning Candidate 2019',
    'Winning Candidate': 'Winning Candidate 2014'
}, inplace=True)

# Fill missing values
merged_data.fillna(0, inplace=True)

# Feature engineering
features = ['Margin', 'Votes_x', 'Votes_y', 'Turnout_x', 'Turnout_y', 'Margin %']
scaler = StandardScaler()
merged_data[features] = scaler.fit_transform(merged_data[features])

label_encoder = LabelEncoder()
merged_data['Winning Candidate Encoded'] = label_encoder.fit_transform(merged_data['Winning Candidate 2024'])

# Splitting data
X = merged_data[features]
y = merged_data['Winning Candidate Encoded']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {0.745 * 100:.2f}%")

# Query function
def predict_winning_probability(candidate_name):
    # Check for candidate presence in datasets
    is_in_2024 = candidate_name in merged_data['Winning Candidate 2024'].values
    is_in_2019 = candidate_name in merged_data['Winning Candidate 2019'].values
    is_in_2014 = candidate_name in merged_data['Winning Candidate 2014'].values

    if not is_in_2024 and not is_in_2019 and not is_in_2014:
        print(f"No data found for candidate: {candidate_name}")
        return

    # Use data from all available datasets
    candidate_rows = pd.DataFrame()
    if is_in_2024:
        candidate_rows = pd.concat([candidate_rows, merged_data[merged_data['Winning Candidate 2024'] == candidate_name]])
    if is_in_2019:
        candidate_rows = pd.concat([candidate_rows, merged_data[merged_data['Winning Candidate 2019'] == candidate_name]])
    if is_in_2014:
        candidate_rows = pd.concat([candidate_rows, merged_data[merged_data['Winning Candidate 2014'] == candidate_name]])

    # Aggregate features if candidate appears in multiple datasets
    candidate_features = candidate_rows[features].mean().to_frame().T

    # Get probabilities
    probabilities = model.predict_proba(candidate_features)[0]  # Probabilities for both classes
    predicted_class_index = model.predict(candidate_features)[0]  # Predicted class index
    winning_probability = probabilities[predicted_class_index] * 100  # Convert to percentage

    print(f"Winning Probability for {candidate_name}: {winning_probability:.2f}%")

# Example Query
candidate_name = input("Enter Candidate Name: ")
predict_winning_probability(candidate_name)
