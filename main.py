from datetime import datetime
import requests
from flask import Flask, request

app = Flask(__name__)


GITHUB_API_URL = 'https://api.github.com'
GITHUB_REPOSITORY_NAME = ''
GITHUB_USER_NAME = 'dmtopp'


@app.route("/fork", methods=['POST'])
def fork_repo():
    # return f'{request.headers["githubUsername"]}, {request.headers["githubAuthToken"]}'
    response = requests.post(
        url=f'{GITHUB_API_URL}/repos/{GITHUB_USER_NAME}/{GITHUB_REPOSITORY_NAME}/forks',
        auth=(request.headers['githubUsername'], request.headers['githubAuthToken']),
        headers={
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        },
        data={
            'name': f'{GITHUB_REPOSITORY_NAME}-fork-{datetime.now()}'
        }
    )

    response.raise_for_status()
    return response.status_code
