from flask import Flask, render_template

from utills import *

app = Flask(__name__)

JSON_NAME = 'candidates.json'
data = load_candidates_from_json(JSON_NAME)


@app.route('/')
def show_all_candidates():
    return render_template('index.html', data=data)


@app.route('/candidate/<int:id>')
def show_candidate_profile(id):
    item = get_candidate(id, data)
    return render_template('single.html', candidate=item)


@app.route('/search/<name>')
def search_for_name(name):
    candidates_list = get_candidates_by_name(name, data)
    return render_template('search.html', candidates_list=candidates_list, count=len(candidates_list))


@app.route('/skill/<skill_name>')
def search_for_skill(skill_name):
    candidates_have_skill = get_candidates_by_skill(skill_name, data)
    return render_template('skill.html', candidates_list=candidates_have_skill, count=len(candidates_have_skill))


if __name__ == '__main__':
    app.run()
