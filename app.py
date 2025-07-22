from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to insecure demo app!"

@app.route("/run", methods=["POST"])
def run_code():
    user_input = request.form.get("code")
    ### --- eval() executes any code passed to it. 
    ### If user input isn't validated, 
    ### an attacker can execute arbitrary Python code on your server.

    try:
        result = eval(user_input)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
