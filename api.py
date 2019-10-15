from flask import Flask, jsonify
import scrap
from scrap import Scrap
teams = {}

Scrap()

teams = {
    'teams': Scrap()
    }
app = Flask(__name__)

all_teams = teams


@app.route('/all_teams', methods=['GET'])
def home():
    return jsonify(all_teams), 200

@app.route('/all_teams/<string:team>', methods=['GET'])
def team_per_name(team):
    #team_per_name = [dev for dev in all_teams if dev['team'] == team]
    for i in all_teams:
        if team == all_teams[i][team]:
            print(team, all_teams[i][team])
            team_per_name2 = team
    #print(f"AQUI: {all_teams}")
    return jsonify(team_per_name2), 200

if __name__ == '__main__':
    app.run(debug=True)