from bs4 import BeautifulSoup
import re

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
            'answers': re.findall(r'\d+', answers)[0],
            'badge': badge,
            'picture_url': full_picture_url
        })

    return directory_results


def decode_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    lawyer_list = []
    row = soup.find(id='profileTabContent').find_all('div', class_='row')[0]
    # rows = soup.find_all('div', class_='row')  # Find all rows (for multiple lawyers)

    lawyer_info = {}

    # Extract description content
    description_div = row.find('div', class_='content col-lg-9')
    if description_div:
        lawyer_info['description'] = ' '.join([p.get_text() for p in description_div.find_all('p')])

    # Extract company
    company = row.find('h5', text='Company')
    if company:
        company_list = company.find_next('ul')
        lawyer_info['company'] = company_list.li.get_text() if company_list else None

    # Extract address
    address = row.find('h5', text='Address')
    if address:
        address_list = address.find_next('ul')
        lawyer_info['address'] = ' '.join([item.get_text() for item in address_list.find_all('li')])[:-3].strip()[:-4].strip()

    # Extract areas of experience
    experience = row.find('h5', text='Areas of Experience')
    if experience:
        experience_list = experience.find_next('ul')
        lawyer_info['areas_of_experience'] = ', '.join([li.get_text() for li in experience_list.find_all('li')])

    # # Extract total answers
    # total_answers = row.find('h5', text='Total Answers')
    # if total_answers:
    #     total_answers_list = total_answers.find_next('ul')
    #     lawyer_info['total_answers'] = total_answers_list.li.get_text() if total_answers_list else None

    return lawyer_info
