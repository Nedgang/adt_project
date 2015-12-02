## Requirement

* Python3
* nltk package

Optional :

* nltk stopwords data use `sudo python3 -m nltk.downloader -d /usr/share/nltk_data stopwords`

## Run exemple

First you need generate a database with create_db tools :

```python
./create_db.py -i data/corpus_mail -o output/
```

Second you can use analysis for list all keyword refrence in database, with :

```python
./analysi.py -i output/tag2terms -p
```

After you can use analysis for list terms associated with some tag :

```python
./analysis.py -i output/tag2terms -[a,b,s] -t 1.0 -q genomic génomiqu protéin protéiqu
```

You need chose in a, b or s methode read help message for more information about
