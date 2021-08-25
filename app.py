from flask import Flask,render_template,url_for,request
import joblib

cv_sentiment = joblib.load("count_.sav")
cv_score = joblib.load("count_v2.sav")

model_sentiment = joblib.load("sentiment_prediction_model.sav")
model_score = joblib.load("score_prediction_model.sav")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]

        # for sentiment prediction
        pred = cv_sentiment.transform(data)
        y_pred = model_sentiment.predict(pred)
        if y_pred[0] == 1:
            message1 = "Positive Review"
        else:
            message1 = "Negative Review"

        # for score prediction
        pred2 = cv_score.transform(data)
        y_pred2 = model_score.predict(pred2)

        return render_template('index.html', prediction = [message1, y_pred2])

if __name__ == '__main__':
    app.run(debug=True)