from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from bs4 import BeautifulSoup

'''
Create a view in the app's views.py file to handle the API request and perform the scraping. 
You can use the requests and BeautifulSoup libraries to make an HTTP request to the Wikipedia page and parse the HTML response.
'''


@api_view(['GET'])
def country_info(request, country_name):
    # Make an HTTP request to the Wikipedia page for the country
    r = requests.get(f'https://en.wikipedia.org/wiki/{country_name}')

    # Parse the HTML response

    soup = BeautifulSoup(r.text, 'html.parser')

    # Find the infobox element
    infobox = soup.find('table', class_='infobox')

    # Extract the desired information from the infobox
    flag_link = infobox.find('img', alt='Flag')['src']
    capital_element = infobox.find('th', text='Capital')
    capital = []
    if capital_element:
        capital_list = capital_element.find_next_sibling('td').find_all('a')
        for city in capital_list:
            capital.append(city.text)
    largest_city_element = infobox.find('th', text='Largest city')
    largest_city = largest_city_element.find_next_sibling(
        'td').text if largest_city_element else None
    official_languages_element = infobox.find('th', text='Official languages')
    official_languages = []
    if official_languages_element:
        official_languages_list = official
