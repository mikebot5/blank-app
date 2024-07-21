from bs4 import BeautifulSoup
import requests

def extract_filtered_links(search_term, num_links=3):
    url = 'https://www.google.com/search'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': search_term}

    content = requests.get(url, headers=headers, params=parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    # Find all search result links
    search_results = soup.find_all('a', href=True)

    # Filter out /search and Google-related links
    filtered_links = [link['href'] for link in search_results if '/search' not in link['href'] and 'google.com' not in link['href']]

    # Return the top filtered links
    return filtered_links[:num_links]

if __name__ == '__main__':
    search_term = input("Enter your search term: ")
    filtered_dog_links = extract_filtered_links(search_term, num_links=3)

    print("Top 3 filtered links related to '{}':".format(search_term))
    for link in filtered_dog_links:
        print(link)
