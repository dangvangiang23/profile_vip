from flask import Flask, render_template
import json

app = Flask(__name__)

# Hàm đọc dữ liệu từ file data.json
def get_profile_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    data = get_profile_data()
    return render_template('index.html', profile=data)

if __name__ == '__main__':
    app.run(debug=True)