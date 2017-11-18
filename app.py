#!flask/bin/python
from flask import Flask, request, jsonify
import subprocess, os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def add_user():
    # fetch informatin from request

    # print request.form['statement']
    print request.form['title']
    file_name = str(request.form['title']).lower()
    file_name = file_name.replace(' ','_') + ".cpp"
    fout = open(file_name,"w")
    fin = open("template.cpp","r")
    fout.write(str(fin.read()))
    subprocess.Popen(["subl",file_name])
    return "jsonify(request)"

if __name__ == '__main__':
    app.run(debug=True, port = 12165)