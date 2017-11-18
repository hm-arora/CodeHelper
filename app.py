#!flask/bin/python
from flask import Flask, request, jsonify
import subprocess, os

app = Flask(__name__)   
@app.route("/", methods=["POST"])
def add_user():
    # fetch informatin from request

    # print request.form['statement']
    path = '/media/himanshu/Local Disk/Programs/C++/'
    # print request.form['title']
    file_name = str(request.form['title']).lower()
    file_name = file_name.replace(' ','_') + ".cpp"
    fout = open(path + file_name,"w")
    fin = open("template.cpp","r")
    fout.write(str(fin.read()))
    # open sublime (open any text editor with command i.e vscode -> code app.py)
    subprocess.Popen(["subl",path + file_name])
    return "true"

if __name__ == '__main__':
    app.run(debug=True, port = 12165)