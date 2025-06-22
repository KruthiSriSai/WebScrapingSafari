import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch GitHub Trending page
url = "https://github.com/trending"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Select repo elements
repos = soup.select('article.Box-row h2 a')

# Step 3: Extract top 5 repos and their links
top_repos = []
for repo in repos[:5]:
    name = repo.text.strip().replace('\n', '').replace(' ', '')
    link = "https://github.com" + repo['href']
    top_repos.append([name, link])

# Step 4: Save to CSV
with open('trending.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Repository Name", "Link"])
    writer.writerows(top_repos)

# Step 5: Print results to terminal
print("✅ Top 5 trending repositories saved to trending.csv\n")
print("Top 5 Trending GitHub Repositories:\n")
for i, repo in enumerate(top_repos, 1):
    print(f"{i}. {repo[0]} → {repo[1]}")
