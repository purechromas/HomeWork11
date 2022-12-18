from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def home_page():
    data = utils.load_candidates_from_json()
    return render_template('list.html', data=data)


@app.route("/candidate/<int:id>")
def candidate(id):
    data = utils.get_candidate(id)
    return render_template('single.html', data=data)


@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill_name>")
def get_candidate_by_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skills.html', candidates=candidates, count_candidates=len(candidates))


if __name__ == '__main__':
    app.run()
