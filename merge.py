import pandas as pd

# Load the CSV files with the provided paths
final_results_path = '/Users/sahibk/Documents/3401/ML/archive/final_results.csv'
shootouts_path = '/Users/sahibk/Documents/3401/ML/archive/shootouts.csv'

final_results = pd.read_csv(final_results_path, encoding='ISO-8859-1')
shootouts = pd.read_csv(shootouts_path, encoding='ISO-8859-1')

# Merge the DataFrames on common columns
merged_df = pd.merge(final_results, shootouts, on=['date', 'home_team', 'away_team'], how='left')

# Function to determine the winner
def determine_winner(row):
    if row['home_score'] == row['away_score']:  # Check if the match is a tie
        return row['winner'] if pd.notnull(row['winner']) else 'TIE'
    else:
        # Determine the winner based on scores
        return row['home_team'] if row['home_score'] > row['away_score'] else row['away_team']

# Apply the function to each row
merged_df['winner'] = merged_df.apply(determine_winner, axis=1)

# Save the updated DataFrame to a new CSV file
output_csv_path = '/Users/sahibk/Documents/3401/ML/archive/updated_final_results.csv'
merged_df.to_csv(output_csv_path, index=False)

print("Updated CSV file saved at:", output_csv_path)
