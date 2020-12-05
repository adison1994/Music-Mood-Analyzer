# Music-Mood
Heroku Link: https://music-mood-analyzer.herokuapp.com/

Video Link: https://www.youtube.com/watch?v=za_l-5WSPoM



## Screenshot

![](https://lh4.googleusercontent.com/PztgFo8l2eemofz8_EbuZCCq1XR5CjiIxMdquwyuSrMcEZrLE1ALCatVj7ygubR3DcwLgymnUv537DXHJ0o7e-1vX39rfHZjg-iGMmyw3CAwpTfgPYdR8szXDPlTmJDDlepqa8FGub7YPMQ2yicZdHQUIKTLexh08cvSwzpw1Pfn7vl9)

## Usage

Install requirements
```bash
pip install -r requirements.txt
```

Run Server
```bash
python app.py
```

## Classifier Information - V1
* Model : **Support Vector Machine**
  * Training F1 : 0.997
  * Validation F1 : 0.712

* Method : TFIDF - Vectorizer 
  * Stopwords : English
  * N-Gram Range : (1,5)


## Codelabs

https://codelabs-preview.appspot.com/?file_id=1GLGXp5jniPDrvBAQd1ffC1ApWlR60HM7WkQWlVrU6w8#0

## Built With

- [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) - Code editor used for python.
- [IBM Watson Tone Analyzer](<https://www.ibm.com/watson/services/tone-analyzer/>)-API used for analyzing mood of the songs.
- [Musixmatch Developer](https://developer.musixmatch.com/)- API used to fetch lyrics for the songs in top charts.
- [Heroku](https://www.heroku.com/) :Cloud Application Platform used to host the website.
- [Flask](http://flask.pocoo.org/) :Microframework in python used to deploy the front end
