from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    ergebnis = None
    ist_gefaehrlich = False

    if request.method == 'POST':
        datei = request.files['datei']
        if datei:
            dateiname = secure_filename(datei.filename)
            pfad = os.path.join(app.config['UPLOAD_FOLDER'], dateiname)
            datei.save(pfad)

            with open(pfad, 'rb') as f:
                inhalt = f.read()
                if b"malware" in inhalt or b"trojan" in inhalt:
                    ergebnis = "⚠️ Verdächtige Datei erkannt!"
                    ist_gefaehrlich = True
                else:
                    ergebnis = "✅ Datei ist sicher"

    return render_template('index.html', ergebnis=ergebnis, ist_gefaehrlich=ist_gefaehrlich)

if __name__ == '__main__':
    app.run(debug=True)
