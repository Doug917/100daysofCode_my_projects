from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

#s encodes values in each cell.  Positions
#are numbered left to right, top to bottom, 1 through 9.
s = {
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": ""
}

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit'] == "Submit":
            user_x = request.form.get('X')
            user_o = request.form.get('O')
            s[user_x] = 'X'
            s[user_o] = 'O'
        elif request.form['submit'] == "Reset":
            for key in s:
                s[key] = ""
        return render_template("index.html", symbols=s)
    else:
        return render_template("index.html", symbols=s)



if __name__ == "__main__":
    app.run(debug=True)