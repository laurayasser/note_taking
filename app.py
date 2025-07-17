from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)
notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form['note']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        notes.insert(0, (note, timestamp))

    return render_template_string('''
    <html>
    <head>
        <title>Note-Taking App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }

            h1 {
                color: #2c3e50;
                font-size: 50px;
                margin-bottom: 20px;
            }

            .container {
                background-color: white;
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
            }

            textarea {
                width: 100%;
                padding: 12px;
                font-size: 16px;
                border: 1px solid #ddd;
                border-radius: 8px;
                resize: vertical;
                margin-bottom: 20px;
            }

            input[type=submit] {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                padding: 12px 24px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                width: 100%;
                transition: background-color 0.3s ease;
            }

            input[type=submit]:hover {
                background-color: #2980b9;
            }

            .note {
                background-color: #ecf0f1;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 15px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }

            .timestamp {
                color: #7f8c8d;
                font-size: 14px;
                margin-bottom: 10px;
            }

            .content {
                font-size: 18px;
                color: #2c3e50;
            }

            /* Responsive Design */
            @media (max-width: 600px) {
                body {
                    padding: 10px;
                }
                .container {
                    padding: 20px;
                    width: 100%;
                }
                textarea {
                    font-size: 14px;
                }
                input[type=submit] {
                    font-size: 14px;
                }
            }

        </style>
    </head>
    <body>
        <h1>📝 My Notes</h1>
        <div class="container">
            <form method="post">
                <textarea name="note" placeholder="Write your note here..." rows="4"></textarea><br>
                <input type="submit" value="Save Note">
            </form>
            {% for note in notes %}
                <div class="note">
                    <div class="timestamp">🕒 {{ note[1] }}</div>
                    <div class="content">📌 {{ note[0] }}</div>
                </div>
            {% endfor %}
        </div>
    </body>
    </html>
    ''', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
