from flask import jsonify, Flask, request
from sentiment_analysis_spanish import sentiment_analysis


appFlask = Flask(__name__)
sentiment = sentiment_analysis.SentimentAnalysisSpanish()


@appFlask.route('/')
def home():
    return "API - Sentiment Analysis"

@appFlask.route('/api', methods=['POST'])
def api():
    data = request.get_json(force=True)
    input=data["text"]
    return jsonify(text=input ,sentiment=sentiment.sentiment(input))
    
if __name__ == "__main__":
    appFlask.run(debug=False,host="0.0.0.0", port= 8080,threaded=True)
