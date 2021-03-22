from flask import Flask,jsonify,request,render_template,url_for,redirect
import requests,json,sys


app=Flask(__name__) 

url = 'https://swapi.dev/api/people/'

def apiimp(i):
	r = requests.get(url + str(i))
	data = r.json()
	return data

pic={'1':'https://upload.wikimedia.org/wikipedia/en/9/9b/Luke_Skywalker.png','2':'https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/C-3PO_droid.png/220px-C-3PO_droid.png','3':'https://upload.wikimedia.org/wikipedia/en/3/39/R2-D2_Droid.png','4':'https://upload.wikimedia.org/wikipedia/en/7/76/Darth_Vader.jpg','5':'https://upload.wikimedia.org/wikipedia/en/1/1b/Princess_Leia%27s_characteristic_hairstyle.jpg'}

picurl=pic['1']

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		sele=request.form.get("haha").strip()
		print(sele)
		name=[]
		height=[]
		mass=[]
		hair_color=[]
		eye_color=[]
		skin_color=[]
		gender=[]
		birth_year=[]
		imgg=[]
		for i in sele:
			print(i)
			name.append(apiimp(i)['name'])
			height.append(apiimp(i)['height'])
			mass.append(apiimp(i)['mass']) 
			hair_color.append (apiimp(i)['hair_color']) 
			eye_color.append (apiimp(i)['eye_color']) 
			skin_color.append (apiimp(i)['skin_color']) 
			gender.append (apiimp(i)['gender']) 
			birth_year.append (apiimp(i)['birth_year']) 
			imgg.append(pic[i])
		if 'fetch' in request.form:
			return render_template('temp.html',name=name,height=height,mass=mass,hair_color=hair_color,eye_color=eye_color,skin_color=skin_color,gender=gender,birth_year=birth_year,pi=imgg,len=len(sele))
	elif request.method=='GET':
		return render_template('store.html')

if __name__ == "__main__":
	app.run(debug=True)

