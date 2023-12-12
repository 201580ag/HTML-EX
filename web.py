from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Get the client's IP address
    client_ip = request.remote_addr
    
    # Get the user agent
    user_agent = request.headers.get('User-Agent')

    return render_template('index.html', ip_address=client_ip, user_agent=user_agent)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
