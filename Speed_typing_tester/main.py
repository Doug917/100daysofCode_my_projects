from flask import Flask, request, render_template, redirect, url_for
import time

app = Flask(__name__)

test_text = '''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth; 
Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,
And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.
I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference.
'''

speed = 0
accuracy = 0
user_text = " "
is_visible = False
@app.route('/', methods =["GET", "POST"])
def home():
    global t0, speed, accuracy, user_text, is_visible
    if request.method == "POST":
        if request.form['button'] == 'Start_Button':
            t0 = time.time()
            is_visible = True
        elif request.form['button'] == 'Stop_Button':
            t = time.time() - t0
            user_text = request.form.get('users_text')
            word_count = len(user_text.split(" "))
            if word_count > 0:
                speed = 60 * (word_count / t)
                correct_chars = 0
                for i in range(len(user_text)):
                    print(test_text[i], user_text[i])
                    if test_text[i] == user_text[i]:
                        correct_chars += 1

                accuracy = 100 * (correct_chars/len(user_text))

                speed = round(speed, 2)
                accuracy = round(accuracy, 2)
            
            

    return render_template('index.html', speed=speed, accuracy=accuracy, test_text_visibility=is_visible, test_text=test_text)


if __name__ == "__main__":
    app.run(debug=True)