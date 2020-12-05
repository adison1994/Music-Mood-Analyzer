import requests
import json
from watson_developer_cloud import ToneAnalyzerV3

class ToneAnalyzer(object) :
    def __init__(self, key = "phww3vCRE3yOHNB5jgRvypsJzSM0B6cEIpRgQ2H-0JYr") :
        self.key = key;

    def analyze(self, track) :
        tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            iam_apikey=self.key,
            url='https://gateway.watsonplatform.net/tone-analyzer/api'
        )
        tone_analysis = tone_analyzer.tone( {'text': track.lyrics}, 'application/json').get_result()
        
        return [self.remapTones(k['tone_name'].lower()) for k in tone_analysis["document_tone"]["tones"]];

    def remapTones(self, tone) :
        if "anger" in tone or "fear" in tone or "sadness" in tone :
            return "Sad :("
        return "Happy :)"
# emojis give uicode error 😎 😞