import requests
from pprint import pprint


class SuperHero:
    def __init__(self):
        self.heros = {}

    def our_request(self, names):
        url = ' https://superheroapi.com/api/2619421814940190/search/'
        for hero in names:
            response = requests.get(url + hero)
            json_to_dict = response.json()
            for item in json_to_dict['results']:
                if item['name'] == hero:
                    self.heros[hero] = {'intelligence': item['powerstats']['intelligence']}


if __name__ == '__main__':
    heros_name = ['Hulk', 'Captain America', 'Thanos']

    super_hero = SuperHero()
    super_hero.our_request(heros_name)

#поиск максимального значения
    super_max_name = ''
    max_value = 0
    for key, item in super_hero.heros.items():
        if int(item['intelligence']) > max_value:
            super_max_name = key
            max_value = int(item['intelligence'])

    pprint(super_max_name + '--->' + str(max_value))



