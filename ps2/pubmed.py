from pymed import PubMed
import csv

pubmed = PubMed(tool="MyTool", email="my@email.address")
topics = ["COVID-19", "cancer", "cardiovascular disease", "neurology", "pediatrics"]

with open('pubmed_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Topic', 'Title', 'Abstract'])  # Write header

    for topic in topics:
        results = pubmed.query(topic, max_results=1000)
        
        for article in results:
            title = article.title
            abstract = article.abstract if article.abstract else "No abstract available"
            writer.writerow([topic, title, abstract])

print("CSV file 'pubmed_articles.csv' has been created.")
