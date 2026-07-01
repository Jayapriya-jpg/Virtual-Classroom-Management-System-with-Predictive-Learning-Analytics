from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load ML Model
model = pickle.load(open("model.pkl", "rb"))

# Home Page
@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

# Student Dashboard
@app.route("/student")
def student():
    return render_template("student_dashboard.html")

# Attendance Page
@app.route("/attendance.html")
def attendance():
    return render_template("attendance.html")

# Engagement Page
@app.route("/engagement.html")
def engagement():
    return render_template("engagement.html")

# Video Class Page
@app.route("/video_class.html")
def video_class():
    return render_template("video_class.html")

# Faculty Dashboard
@app.route("/faculty_dashboard.html")
def faculty():
    return render_template("faculty_dashboard.html")

# Admin Dashboard
@app.route("/admin_dashboard.html")
def admin():
    return render_template("admin_dashboard.html")

# ML Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    result = model.predict([[
        data["attendance"],
        data["marks"],
        data["engagement"]
    ]])

    return jsonify({
        "result": int(result[0])
    })

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)