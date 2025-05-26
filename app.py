from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000',
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000',
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000',
}]


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/contact')
def contact():
  return render_template('contactus.html')


@app.route('/career')
def career():
  return render_template('career.html', jobs=JOBS, company_name='Jovian')


#####
#this is form 2 whatsapp message sender handler
#####


@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
