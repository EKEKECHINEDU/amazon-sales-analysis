import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AmazonDataAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Loads the dataset from the specified file path."""
        self.df = pd.read_csv(self.file_path)

    def clean_data(self):
        """Cleans the dataset by converting data types and removing unwanted characters."""
        self.df['discounted_price'] = self.df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)
        self.df['actual_price'] = self.df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)
        self.df['discount_percentage'] = self.df['discount_percentage'].str.replace('%', '').astype(float)
        self.df['rating'] = pd.to_numeric(self.df['rating'], errors='coerce')
        self.df['rating_count'] = self.df['rating_count'].str.replace(',', '').astype(float)

    def plot_top_categories(self):
        """Plots the top 10 product categories."""
        category_counts = self.df['category'].value_counts().head(10)
        plt.figure(figsize=(10, 5))
        sns.barplot(y=category_counts.index, x=category_counts.values, palette='viridis')
        plt.xlabel("Number of Products")
        plt.ylabel("Category")
        plt.title("Top 10 Product Categories")
        plt.show()

    def plot_top_products(self):
        """Plots the top 10 best-selling products by review count."""
        top_products = self.df[['product_name', 'rating_count']].sort_values(by='rating_count', ascending=False).head(10)
        plt.figure(figsize=(10, 5))
        sns.barplot(y=top_products['product_name'], x=top_products['rating_count'], palette='coolwarm')
        plt.xlabel("Number of Reviews")
        plt.ylabel("Product Name")
        plt.title("Top 10 Best-Selling Products")
        plt.show()

    def plot_discount_vs_rating(self):
        """Plots the relationship between discount percentage and rating."""
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=self.df, x='discount_percentage', y='rating', alpha=0.5)
        plt.xlabel("Discount Percentage")
        plt.ylabel("Average Rating")
        plt.title("Discount vs. Rating")
        plt.show()

    def show_summary(self):
        """Displays summary insights from the dataset."""
        print("Average Discount Percentage:", self.df['discount_percentage'].mean())
        print("Average Product Rating:", self.df['rating'].mean())
        print("Top 5 Categories by Product Count:")
        print(self.df['category'].value_counts().head())
        print("Top 10 Best-Selling Products by Review Count:")
        print(self.df[['product_name', 'rating_count']].sort_values(by='rating_count', ascending=False).head(10))
        print("Relationship between Discount and Rating:")
        print(self.df[['discount_percentage', 'rating']].corr())

    def save_cleaned_data(self, output_file):
        """Saves the cleaned dataset to a CSV file."""
        self.df.to_csv(output_file, index=False)

# Example usage
if __name__ == "__main__":
    analysis = AmazonDataAnalysis("data/amazon.csv")
    analysis.load_data()
    analysis.clean_data()
    analysis.plot_top_categories()
    analysis.plot_top_products()
    analysis.plot_discount_vs_rating()
    analysis.show_summary()
    analysis.save_cleaned_data("cleaned_amazon.csv")

    print("Data analysis completed. Cleaned data saved to cleaned_amazon.csv.");