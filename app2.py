from flask import Flask, request, render_template
import pywhatkit

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/contact')
def contact():
  return render_template('contactus.html')


#####
#this is form 2 whatsapp message sender handler
#####
"""
@app.route('/whatsappsender', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    whatsapp_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    try:
      pywhatkit.sendwhatmsg_instantly(
          phone_no=
          "+919945351110",  # Replace with the recipient's number including country code
          message=whatsapp_message)
      return "Message sent successfully!"
    except Exception as e:
      return f"Error sending message: {e}"

  return render_template('form.html')

"""


#####
#this is 404 error page handler
#####
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
