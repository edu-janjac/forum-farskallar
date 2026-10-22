from flask import Flask, request, render_template_string, jsonify

import json, os
app = Flask(__name__)
JSON_FILE = 'data.json'

HTML = '''
    <body>
        <form method="POST" action="/write-json">
        <label for="user">User:</label>
        <input type="text" name="user" id="user" required>
        <label for"passwd">Password:</label>
        <input type="password" name="passwd" id="passwd" required>
        <button type="submit">Login</button>
    </body>
'''

def load_posts():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return []


@app.route('/')
def json_demo():
    return render_template_string(HTML)

@app.route('/write-json', methods=['POST'])
def write_json():
    posts = load_posts()
    posts.append({
        'user': request.form.get('user'),
        'passwd': request.form.get('passwd')
    })
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)
    return render_template_string(HTML)

app.run(debug=True)