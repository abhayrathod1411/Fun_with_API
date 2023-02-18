import json
import requests
import configparser
from pprint import pprint
from operator import itemgetter
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep

#Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read("/Users/abhayrathod/Desktop/Python/Github/Fun_with_API/configuration.ini")
pokemon_api_link = config_obj['POKEMON']['API_LINK']

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def ask_input(pokemon_api_link):
    #ask for input
    queryLink = f'{pokemon_api_link}pokemon/?offset=&limit=10000'

    payload={}
    headers = {}

    response = requests.request("GET", queryLink, headers=headers, data=payload)

    json_resp = response.json()
    results = json_resp['results']
    names = list(map(itemgetter('name'), results))

    clear()

    sty = Style.from_dict({
        'w': '#44ff00 bold'
    })
    print_formatted_text (HTML('<w> Hello and welcome to the world of <u>Pokemons!</u> </w>'), style=sty)

    pokemon_names = WordCompleter(names)
    text = prompt('Enter Name of Pokemon : ', completer=pokemon_names)
    print('Alright, lets talk about %s' % text)




def get_basic_info(pokemon_api_link, pokemon_name):
    """
    Docstring
    """
    queryLink = f'{pokemon_api_link}pokemon/{pokemon_name}'
    payload={}
    headers = {}

    response = requests.request("GET", queryLink, headers=headers, data=payload)

    json_resp = response.json()

    name = json_resp['name']
    weight = json_resp['weight']
    height = json_resp['height']

    print()




