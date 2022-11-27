from flask import Flask, Response, request, render_template
#from cryptography.fernet import Fernet
import logging
import urllib

app = Flask(__name__)
#app.logging.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
logging.basicConfig(level=logging.FATAL)
log.setLevel(logging.ERROR)

@app.route("/")
def hellopage():
    return render_template('index.html')

@app.route("/home")
def mainpage():
    return render_template('main_page.html')

@app.route("/createnft")
def create_nft():
    return render_template('make_NFT.html')

@app.route("/profile")
def profile():
    return render_template('my_pes.html')

@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/trading")
def trade():
    return render_template('torg_plosh.html')

@app.route("/collection")
def collection():
    return render_template('my_collection.html')

@app.route("/", methods=['POST'])
def auth():
    print("GET INFORMATION")
    status_code = 200
    return render_template('main_page.html')

@app.route("/createnft", methods=['POST'])
def create_nft_post():
    print("GET INFORMATION")
    status_code = 200
    return mainpage()

if __name__ == "__main__":
    app.run(host='185.87.48.157', port=9999)
