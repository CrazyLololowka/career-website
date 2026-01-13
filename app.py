from flask import Flask, render_template

app = Flask(__name__)

OFFERS =[
{
  "id" : 1,
  "title" : "Pinky",
  "price" : "100000 Rubles"
  },
{ 
  "id" : 2,
  "title" : "Rainbow",
  "price" : "104000 Rubles"
} 
]

@app.route('/') 
def hello_world():
  return render_template('home.html', offers=OFFERS)
  
print(__name__)  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)