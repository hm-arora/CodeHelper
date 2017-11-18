## Code Helper
This is a chrome extension that links with various text editors ( Sublime text, Atom, Bracket, Vscode etc) to different competitive and coding interview preparation sites like codechef, hackerearth, hackerrank, geeksforgeeks, codeforces etc.

This extension is use to open the file with the file name as question name and loads your template or library that has been written any language ( c++, java , python etc) because these templates are widely use in competitive sites.

## About
This is one of the problem that I faced when we practise coding questions on above mention websites or when we participated in any competitive contest, after understanding the problem and came up with solution then we create a file and copy & paste our template to this file and then finally start to code.

Why don't just started typing code that matters at the time after came up with solution it reduces the effort to create files with particular name, manage input and output files associated with this file and it also helps to organise the final solution.

## Requirements

- Python3 (Grab the latest version of Python from https://www.python.org/downloads/ )
- **Flask** (Microframework for python) for creating server, for more information http://flask.pocoo.org/docs/0.12/installation/

## Usage
- Clone the repository or download it.
- Change the path according to where you want to save files.
- Now run the Flask server with python app.py if there is no error go ahead otherwise take a look at http://flask.pocoo.org/docs/0.12/installation/ .
- Now load the extenstion on chrome by going to this chrome://extensions .
- Mark the developer mode then click on load unpack extension then select the folder **chromeExtension** .

## Demo

![out](https://user-images.githubusercontent.com/23010645/32980948-8e483634-cc95-11e7-9e68-1a0deeb82246.gif)

## Future Development

- Provide question and other details ( Best for practise ) in a file with just one click and user select whether to include this details or not (details don't matter in case of contest )
- Provide interface in chrome to customize the location of file to be saved, whether question consists with multiple testcases or not, copy input & output then create their seperate files.
- create seprate folder for different websites and automatically provide the location to save a file it helps to organise final solutions.


