from flask import Flask, render_template
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

app = Flask(__name__)

credentials_file = 'credentials/credentials.json'

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/start-vm')
def startVM():
    url = 'https://us-central1-cf-start-and-stop-vms.cloudfunctions.net/vm-start'

    creds = service_account.IDTokenCredentials.from_service_account_file(
           credentials_file, target_audience=url)

    authed_session = AuthorizedSession(creds)

    resp = authed_session.post(url)
    return render_template('start-vm.html', the_start_result=resp.text)


@app.route('/stop-vm')
def stopVM():
    url = 'https://us-central1-cf-start-and-stop-vms.cloudfunctions.net/stop-vm'

    creds = service_account.IDTokenCredentials.from_service_account_file(
           credentials_file, target_audience=url)

    authed_session = AuthorizedSession(creds)
    resp = authed_session.post(url)
    return render_template('stop-vm.html', the_stop_result=resp.text)


if __name__ == '__main__':
    app.debug == True
    app.run()

