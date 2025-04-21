from flask import Flask

app = Flask(__name__, template_folder='apartment_reviews/templates')

if not os.environ.get("SESSION_SECRET"):
    os.environ["SESSION_SECRET"] = "apartment-reviews-secret-key"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
