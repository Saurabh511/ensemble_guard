from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import re



# Import the modified `ensemblePredict` file
from ensemblePredict import predict_single_pe

app = Flask(__name__, template_folder='templates', static_folder='static')

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'exe'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index_1.html')  ##login/signup only

@app.route('/index.html')
def home_return():
    return render_template('index.html')

# USER_NAME = "Pranisha@gmail.com"
# USER_MAIL = "pranisha123"

# @app.route("/login.html",  methods=['POST' , 'GET'])
# def login():
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         if email == USER_NAME and password == USER_MAIL:
#             reg = "You have successfully registered !!"
#             return render_template('index.html', reg = reg)
#         elif not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
#             err = "Invalid Email Address !!"
#             return render_template('login.html' , err = err)
#         elif not email or not password:
#             err = "Please fill out all the fields"
#             return render_template('login.html' , err = err)
#     else:
#         return render_template('login.html')
    
# @app.route("/Signup.html")
# def signup():
#     if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form:
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']

#         csv_data = [name, email, password]

#         df = pd.DataFrame(columns=['Name', 'Email', 'Password'])
#         df.loc[len(df)] = csv_data

#         df.to_csv("User_Data.csv", mode='a', index=False, header=False)
#         return render_template('index.html')
#     else:
#         return render_template('Signup.html')

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

# something = {

# }

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check for file in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Check allowed file type 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Call ensemblePredict.py with the file path and get the prediction
            result = predict_single_pe(file_path)
            predicted_class = result.get('predicted_class')
            return render_template('index.html', result=predicted_class)
        else:
            return jsonify({'error': 'Invalid file type'})

    except Exception as e:
        # Return error message in JSON format
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
