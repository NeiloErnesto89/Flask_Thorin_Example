import os #from standard Py library
import json #import data coming from Json file
from flask import Flask, render_template, request, flash # captial F indicates class name

app = Flask(__name__) # instances for the class, convention dictates the name of the var is "app"
app.secret_key = "some_secret" #Flask needs secret key for flash messages, must be string. 


@app.route('/') # route decorator to tell flask what URL should trigger the function
def index():
    return render_template("index.html") 
    # could type html e.g. <h1> Hello! </h1> etc. 

@app.route('/about')
def about():
    data = [] #initalise an empty array called data(json)
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
    #list_of_numbers= [1, 2, 3] 
    #second argument to return view
    
@app.route('/about/<member_name>')
def about_member(member_name):
    member = {} #empty object used to store data in later
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data: # for loop to iterate
            if obj["url"] == member_name:
                member = obj
                    
    return render_template("member.html", member=member) # how we refer to it inside our template
    

@app.route('/contact', methods=["GET", "POST"]) # array to allow methods
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact ")
        
    """
    call flash instead of print
    print(request.form["name"]) access of key because it's dictionary using Python method
    """

@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)