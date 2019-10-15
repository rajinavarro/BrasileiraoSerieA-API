from bs4 import BeautifulSoup
import requests


def Strip(team):
    return team.get_text().replace('>', '').replace(' ', '').strip()
    
def Scrap():
    base_url = 'https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/'
    r = requests.get(base_url)

    soup = BeautifulSoup(r.text, "html.parser")
    all_teams = soup.find('tbody')


    teams = {}

    for i in all_teams:
        team_name = i.find(class_="main team-name")
        team_name = Strip(team_name)
        team_points = i.find(class_="points")
        team_points = Strip(team_points)
        team_position = i.find(class_='main position')
        team_position = Strip(team_position)
        team_matches = i.find(title="Jogos")
        team_matches = Strip(team_matches)
        team_victories = i.find(title="Vitórias")
        team_victories = Strip(team_victories)
        team_defeats = i.find(title="Derrotas")
        team_defeats = Strip(team_defeats)
        team_draws = i.find(title="Empates")
        team_draws = Strip(team_draws)
        
        teams[team_name] = {
                'team': team_name,
                'points': int(team_points),
                'position': int(team_position),
                'matches': int(team_matches),
                'victories': int(team_victories),
                'defeats': int(team_defeats),
                'draws': int(team_draws)
            }
    '''
    for i in teams:
        print(i,"=",teams[i],'\n')'''
    #print(teams)
    
    return teams