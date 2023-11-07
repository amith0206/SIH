from datasets import load_dataset
import pandas as pd

# # Load the dataset
dataset = load_dataset("sKushagra/NewsArticles")

# # Access the dataset split you want to save (e.g., 'train')
split_name = 'train'
data = dataset[split_name]

# # Convert the dataset to a Pandas DataFrame
df = pd.DataFrame(data)

# # Specify the path where you want to save the CSV file
csv_file_path = 'news_articles.csv'

# Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False)
print("Dataset downloaded")
