from flask import Flask, request
from ceasar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

content = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>

    <body>

      <form action="/" method="POST">
        <label> Rotate by
            <input type = "text" name = "rot" value = "0"/><br><br>
        </label>
        
        <textarea name="text" rows="5" cols="50">
        {text_to_show}
        </textarea> <br><br>

        <input type="submit" name= "submit" value = "Submit Query" />
      </form>

    </body>
</html>
'''

@app.route("/")
def index():
    return content.format(text_to_show = "")

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])

    changed_text = rotate_string(text, rot)

    #form = '<h1>' + changed_text + '</h1>'

    return content.format(text_to_show = changed_text)

app.run()