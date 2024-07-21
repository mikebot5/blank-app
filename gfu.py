def get_first_url(url):
    import efl
    import requests
    from bs4 import BeautifulSoup

    # Check if the URL has a valid schema (http or https)
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url  # Add http:// as the default schema

    # Get the filtered links
    urls = efl.extract_filtered_links(url)

    if urls:
        # Ensure there are at least two URLs
        if len(urls) >= 2:
            response = requests.get(urls[0])
            response2 = requests.get(urls[1])
            soup = BeautifulSoup(response.content, 'html.parser')
            soup2 = BeautifulSoup(response2.content, 'html.parser')
            text_content = soup.get_text()
            text_content2 = soup2.get_text()

            # Print the actual text content
            return text_content + text_content2
        else:
            print("Not enough filtered links found.")
    else:
        print("No filtered links found.")

if __name__ == '__main__':
    print(get_first_url('dogs'))
