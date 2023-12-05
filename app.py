from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__,static_url_path='/static')

@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)

