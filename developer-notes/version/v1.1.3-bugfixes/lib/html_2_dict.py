from bs4 import BeautifulSoup

def decode_directory(html):
    base_url = "https://www.eb5investors.com"
    soup = BeautifulSoup(html, 'html.parser')

    # List to hold all the information
    directory_results = []

    # Find all directory-result divs
    results = soup.find_all('div', class_='directory-result')

    for result in results:
        profile_url = result.find('a')['href']
        picture_url = result.find('img')['src']
        name = result.find('h3').text
        location = result.find('span', class_='location').text
        answers = result.find('div', class_='answers').text.strip()
        badge = result.find('span', class_='badge').text.strip() if result.find('span', class_='badge') else None
        
        full_picture_url = base_url + picture_url

        directory_results.append({
            'name': name,
            'profile_url': profile_url,
            'location': location,
            'answers': answers,
            'badge': badge,
            'picture_url': full_picture_url
        })

    return directory_results