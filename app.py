from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/api')
def api():
    # Extract the GET request parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if parameters are present
    if not slack_name or not track:
        return jsonify(error="slack_name and track parameters are required"), 400

    # Get the current day and UTC time
    current_day = datetime.utcnow().strftime('%A')  # E.g., 'Monday'
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')  # E.g., '2023-08-24T14:21:23Z'

    # Construct the GET response
    response = {
        "slack_name": an222n,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/An222n/flask_endpoint_project/app.py.git",
        "github_repo_url": "https://github.com/An222n/flask_endpoint_project.git",
        "status_code": 200
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
