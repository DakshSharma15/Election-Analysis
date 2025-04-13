import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
election_data = pd.read_csv("india_election_2019.csv")

# Function to filter results by state and display top parties with visualization
def state_wise_result_with_percentage(state_name):
    # Filter election results for the given state
    state_results = election_data[election_data['State'].str.contains(state_name, case=False)]
    if state_results.empty:
        print(f"No data found for state: {state_name}")
        return

    # Aggregate winning party counts for the state
    state_party_counts = state_results['Party'].value_counts()

    # Separate top 5 parties and group the rest as "Other"
    top_5_parties_state = state_party_counts[:5]
    other_parties_state = state_party_counts[5:].sum()
    state_party_counts_top5 = pd.concat([top_5_parties_state, pd.Series({"Other": other_parties_state})])

    # Calculate percentage of seats for each party
    total_seats = state_party_counts_top5.sum()
    state_party_percentages = (state_party_counts_top5 / total_seats) * 100

    # Use default colors (no color mapping file provided in the dataset)
    colors_state = plt.cm.tab20.colors[:len(state_party_counts_top5.index)]

    # Generate the table for the state
    state_party_table = pd.DataFrame({
        "Party": state_party_counts_top5.index,
        "Seats": state_party_counts_top5.values,
        "Percentage (%)": state_party_percentages.values
    })

    # Plot the pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(state_party_counts_top5, labels=state_party_counts_top5.index, colors=colors_state,
            autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '', startangle=140)
    plt.title(f"Winning Political Parties - Election Results 2019 ({state_name})")
    plt.show()

    # Display the table
    print(f"\nNumber of Seats Won in {state_name}:\n")
    print(state_party_table.to_string(index=False))

# Input from user
if __name__ == "__main__":
    state_name_input = input("Enter the state name: ")
    state_wise_result_with_percentage(state_name_input)
