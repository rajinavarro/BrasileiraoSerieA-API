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
    return jsonify(all_teams[i][team]), 200

if __name__ == '__main__':
    app.run(debug=True)