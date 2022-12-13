import requests

def filter_superheroes(superheroes: list, superheroes_names: list):
    if not isinstance(superheroes, list):
        print('Error: superheroes is not list.')
        return
    
    if not isinstance(superheroes_names, list):
        print('Error: superheroes_names is not list.')
        return
    
    filtered_superheroes = []
    filter_names = superheroes_names.copy()
    for superhero in superheroes:
        for superhero_name in filter_names:
            if superhero['name'] == superhero_name:
                filtered_superheroes.append(superhero)
                filter_names.remove(superhero_name)
    
    if len(filtered_superheroes) == 0:
        print('Error: superheroes not found.')
        return

    if len(filter_names) > 0:
        unfound_superheroes_str = ', '.join(name for name in filter_names)
        print(f'Warning: Unfounded superheroes: {unfound_superheroes_str}.')
    
    return filtered_superheroes


def get_superheroes(superheroes_names: list = None):
    api_base_url = 'https://akabab.github.io/superhero-api/api'
    api_route = '/all.json'
    url = api_base_url + api_route

    resp = requests.get(url)

    req_status_code = resp.status_code
    if req_status_code != 200:
        print(f'Error: HTTP request status code is {req_status_code}.')
        return

    superheroes = resp.json()
    if not isinstance(superheroes, list):
        print('Error: HTTP request response does not contain a list by json format.')
        return
    
    if superheroes_names == None:
        return superheroes
    
    return filter_superheroes(superheroes, superheroes_names)

def print_max_intellegence_superhero_name(superheroes_names: list = None):
    superheroes = get_superheroes(superheroes_names)
    max_intellegence_superhero = superheroes[0]
    for superhero in superheroes[1:]:
        if (superhero['powerstats']['intelligence'] >
            max_intellegence_superhero['powerstats']['intelligence']):
            max_intellegence_superhero = superhero
    
    print(max_intellegence_superhero['name'])

print_max_intellegence_superhero_name(['Hulk', 'Captain America', 'Thanos'])


