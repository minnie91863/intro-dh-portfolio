---
layout: page
title: Analyzing Documents with TF-IDF
description: Programming Historian Lesson on the many uses and varations of TF-IDF in NLP
---

# Analyzing Documents with TF-IDF

## Source

[https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf#tf-idf-and-common-alternatives](https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf#tf-idf-and-common-alternatives)

## Reflection

In this Programming Historian Lesson, the basic functionality of Term Frequency - Inverse Document Frequency (tf-idf) is introduced through a short example in Python, some variations of how it can be utilized, and some other NLP alternatives to using tf-idf. I learned that, unlike other methods of nlp frequency analysis, tf-idf is largely algorithmic in how it determines similarities and trends within a text corpus. There are many different methods of implementing tf-idf. One implementation called Scikit-Learn’s idf transformation mathematically defines the inverse document frequency (idf) of a text as

idf_i = ln[(N+1) / df_i] + 1

and therefore the total tf-idf  as

tf-idf_i = tf_i × idf_i

Since this process is largely quantitative, discrete parameters can be applied to this process, such as defining stopwords, minimum and maximum values, and certain min/max creatures and ranges. Thus, the resulting data can be more useful in other applications, such as machine learning and algorithmic searches. 

Compared to the other Programming Historian Lessons I completed, this one included minimal, but dense, coding that walked through the process of storing, sorting, and converting the text from a .txt file to a workable .csv file. The only issues I had with the tutorial was that one function, get_feature_names(), gave me a warning with the type, so I changed it to get_feature_names_out(). I also ran into an issue where instead of outputting the converted .csv files to the new directory we made in the lesson, they instead were outputted into the same file. I couldn’t figure out what was causing this issue, since the code seemed to be changing the file output directory.

Otherwise, the lesson stepping through the coding process was well-explained and highly technical. The reading in the second half was informative and served as a good introduction to the many ways data can be organized to be analyzed, and great examples of some issues that may arise based on the dataset’s qualities. 


## Code


```python
from pathlib import Path

all_txt_files =[]
for file in Path("txt").rglob("*.txt"):
     all_txt_files.append(file.parent / file.name)
# counts the length of the list
n_files = len(all_txt_files)
print(n_files)
```


```python
all_txt_files.sort()
all_txt_files[0]
```


```python
all_docs = []
for txt_file in all_txt_files:
    with open(txt_file) as f:
        txt_file_as_string = f.read()
    all_docs.append(txt_file_as_string)
```


```python
#import the TfidfVectorizer from Scikit-Learn.  
from sklearn.feature_extraction.text import TfidfVectorizer
 
vectorizer = TfidfVectorizer(max_df=.65, min_df=1, stop_words=None, use_idf=True, norm=None)
transformed_documents = vectorizer.fit_transform(all_docs)
```


```python
transformed_documents_as_array = transformed_documents.toarray()
# use this line of code to verify that the numpy array represents the same number of documents that we have in the file list
len(transformed_documents_as_array)
```


```python
import pandas as pd

# make the output folder if it doesn't already exist
Path("./tf_idf_output").mkdir(parents=True, exist_ok=True)
```


```python
# construct a list of output file paths using the previous list of text files the relative path for tf_idf_output
output_filenames = [(str(txt_file).replace(".txt", ".csv")).replace("txt/", "tf_idf_output/") for txt_file in all_txt_files]

# loop each item in transformed_documents_as_array, using enumerate to keep track of the current position
for counter, doc in enumerate(transformed_documents_as_array):
    # construct a dataframe
    tf_idf_tuples = list(zip(vectorizer.get_feature_names_out(), doc))
    one_doc_as_df = pd.DataFrame.from_records(tf_idf_tuples, columns=['term', 'score']).sort_values(by='score', ascending=False).reset_index(drop=True)

    # output to a csv using the enumerated value for the filename
    one_doc_as_df.to_csv(output_filenames[counter])
```
