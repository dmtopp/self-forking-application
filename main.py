import requests
from requests import HTTPError
from flask import Flask, request

app = Flask(__name__)


GITHUB_API_URL = 'https://api.github.com'
GITHUB_REPOSITORY_NAME = 'self-forking-application'
GITHUB_USER_NAME = 'dmtopp'


@app.route("/fork", methods=['POST'])
def fork_repo():
    try:
        response = _call_github_api()
        return response.content, 200
    except HTTPError as e:
        return e.response.content, 500


def _call_github_api():
    response = requests.post(
        url=f'{GITHUB_API_URL}/repos/{GITHUB_USER_NAME}/{GITHUB_REPOSITORY_NAME}/forks',
        auth=(request.headers['githubUsername'], request.headers['githubAuthToken']),
        headers={
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        },
        json={
            'name': f'{GITHUB_REPOSITORY_NAME}-fork'
        }
    )

    response.raise_for_status()
    return response
