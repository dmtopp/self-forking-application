# self-forking-application

### How to run
- Create & activate a python virtual environment (I prefer to use `python3 -m venv venv` but there are many ways)
- Install dependencies using `pip install -r requirements.txt`
- Run the application: `flask --app main run`

### Invoking the app
- This application has a single endpoint: `/fork`
- To call this endpoint, send a POST request to `http://localhost:5000/fork`
- This requests requires two headers:
  - `githubUsername`: the username of the account to fork the application
  - `githubAuthToken`: a personal access token for the account to fork the application.  Tokens can be generated [here](https://github.com/settings/tokens/new)
- Successful requests should return a 200 along with data from github about the forked repository
- Failed requests should return an error code along with some response data
- It is not possible to fork this repository more than once with the same account

### Approach
This application is a simple wrapper around the Github API.  There's probably some scenarios
where it's not ideal to send personal access tokens in request headers, but I decided not to spend time
on other ways of authenticating to github for this tests.

If someone wanted to invoke this app by clicking a link, they'd need to have their github username
and token available to the front end application -- this should be done by authenticating the user and sending the credentials
in a separate api request.  It would not be advisable to include tokens in application source code.

