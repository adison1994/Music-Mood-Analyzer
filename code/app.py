from flask import Flask, flash, redirect, render_template, request, session, abort
from pipeline import Pipeline
from musixmatch.api import Musix, Track;
from ibm.tone import ToneAnalyzer;
import pandas as pd
from argparse import ArgumentParser

FILE_NAME = "";

app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Classifier Function
@app.route('/classify', methods=['POST'])
def handle_data():
    # Get Lyrics
    lyrics = request.form['lyrics']

    if not lyrics :
        return "No Lyrics Found!"
    # Convert to list if it is not.
    if type(lyrics) == type("") :
        lyrics = [lyrics]

    # Instantiate a pipeline object
    pipeline = Pipeline(lyrics);

    # Get the results.
    return pipeline.vectorize()


@app.route("/musixmatch",methods=['POST'])
def musixmatch() :
    j = 0
    k = int(request.form['k'])
    country = request.form['country']
    musix = Musix(country)
    tracks = musix.get_top_lyrics(k)
    f = open(FILE_NAME,"w");
    f.write("song\ttone-analyzer\tibm\n");
    f.close();
    result = ""
    for i, track in enumerate(tracks) :
        j += 1
        try :
            pipeline = Pipeline([track.lyrics])
            track.label(pipeline.vectorize())

            ibm = ToneAnalyzer();
            ibm_results = ibm.analyze(track);

            result = result + ("<b>" + str(j) + ". " + "</b>" + track.name + " by <i>" + track.artist + "</i> : <b>" + track.mood + "</b> || IBM's Results <b><u>" + ', '.join(ibm_results)) + "</b></u><br><br>"
            f = open(FILE_NAME,"a")
            f.write(str(track.name + " by " + track.artist + "\t" + track.mood + "\t" + ', '.join(ibm_results) + "\n"))
            f.close()
            print("Completed classifying " + str(i+1) + " tracks");
        except AttributeError :
            pass

    return render_template("musixmatch.html", k=k, result=result)

# Main Function
if __name__ == "__main__":
    # Run the Flask Server
    parser = ArgumentParser()
    parser.add_argument("-f",
                        "--file",
                        type = str, 
                        help = "File name", 
                        dest = "filename")

    args = parser.parse_args()
    FILE_NAME = args.filename if args.filename else "watson.csv"
    app.run()
