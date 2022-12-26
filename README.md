# Tweets Profanity
This repository contains the code for finding degree of profranity for sentences based on a provided list of bad words (racial slurs).

## Table of content
*   [Assumptions made for this task](#assumptions-made-for-this-task)
*   [Requirements](#requirements)
*   [Files](#files)
*   [How to use it ](#how-to-use-it)
*   [Sample output](#sample-output)

## Assumptions made for this task
*   Tweets are provided in a text file, with 1 sentence per line
*   Offensive words are also provided in text file with 1 word per line
*   Required output is in csv file
*   Only important column in outfile is `degree_of_profanity` and `tweet`

## Requirements
*   `pandas` ( to ouput in csv format)

## Files
*   `tweets.txt` : This file contains tweets by user, one sentence per line.
*   `bad_words.txt` : This file contains the profanity word (racial slurs), one word per line.
*   `generate_degree_of_profanity.py` : This file contains the code which ouput a csv file with tweet and its degree of profanity based on the words provided in `bad_words.txt` file.

## How to use it   
To calculate the degree of profanity for sentence, add all the sentence into file `tweets.txt` and the profant words in `bad_words.txt`. By default those files are populated with some sample data. Then run the below command.
``` python
python gereate_degree_of_profanity.py
```

## Sample output
Output will be a `.csv` file, below is an sample to get an idean on the columns in output file.
| tweet | degree_of_profanity |
|--------|---------------------|
| I want to visit paris next year | 0.0000 |
| you stupid | 0.5000 |
