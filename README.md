# Amazon Fine Food Reviews End To End

📝 Build a model to help identify the
- Scoring(Rating) pattern (model-1)
- And classify whether the review is Positive or Negative review.(model-2)



## ⏳ Steps to the project
1. Load the dataset:
    <ul>
    <li>Import data and Explore shape and size.</li>
    </ul>

2. Data cleaning:
    <ul>
    <li>Missing value treatment</li>
    <li>Drop attribute/s if required using relevant functional knowledge</li>
    <li>Automate all the above steps/li>
    </ul>

3. Data analysis & visualisation:
    <ul>
    <li>Perform detailed statistical analysis on the data.</li>
    <li>Perform a detailed univariate, bivariate and multivariate analysis with appropriate detailed comments after each analysis.</li>
    </ul>
 
4. Data pre-processing:
    <ul>
    <li>Segregate predictors vs target attributes</li>
    <li>Check for target balancing and fix it if found imbalanced.</li>
    <li>Convert text into vector formate using(countvectorize & tfidf)</li>
    <li>Perform text cleaning & remove stopwords</li>
    <li>Perform stemming and lemmatization</li>
    <li>Perform train-test split.</li>
    </ul>
    
5. Model training, testing and tuning:
    <ul>
    <li>Train and test models taught in the learning module.</li>
    <li>Display the classification accuracies for train and test data.</li>
    <li>Expirement with diffrent algorithms</li>
    <li>Use all possible hyper parameter for tuning and select best parameter</li>
    <li>Select the final best trained model along with your detailed comments for selecting this model.</li>
    <li>Save best model for future use</li>
    </ul>

6. Web App:
    <ul>
    <li>Create web app</li>
    <li>Deploy on webserver</li>
    </ul>
 ## :desktop_computer: Deploy - <a href = "https://amazon-finefood-review.herokuapp.com/" target="/blank" style="color:blue;">Heroku</a>
 ## :gear: Setup
 1. First clone the repo locally.
 ```bash
 git clone https://github.com/mihir3030/AmazonFine-Food-Reviews.git
 ```
 
 2. While in the virtual environment, install required dependencies from `requirements.txt`.
 ```bash
 pip install -r ./requirements.txt
 ```
 3.Now we can run the web application via
 ```bash
python app.py
```
and navigate to `http://127.0.0.1:5000/` to see it live.

## 🎯 Demo
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/45241759/130909376-7e5bf799-8a41-4ae9-b655-2e62b2bcf797.gif)

## :book: Project Structure:
~~~ 
amazon-finefood reviews
├── static
│   ├── styles
│       └── style.css
├── templates
│   └── index.html
│   └── index2.html
├── app.py
├── requirements.txt
├── Procfile
├── AmazonReviews.ipynb
├── count_.sav(countvectorize save for sentiment)
├── count_v2.sav(countvectorize save for score)
├── sentiment_prediction_model.sav
├── score_prediction_model.sav
├── bst_model.pkl
└── README.md
~~~


<!-- ## Contributors <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25>
- Mihir Dholakiya<br><br>
      <a href="https://www.linkedin.com/in/mihir-dholakia-362171162/" target="/blank"><img src="https://user-images.githubusercontent.com/45241759/130904923-143e3e99-02e3-47b5-935a-86fb1eb1476e.png" width=25, height=25></a>
   
 -->
