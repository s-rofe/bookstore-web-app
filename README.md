# COMPSCI 235 Assignment 2 by srof384 & udea631


## Description

This repository contains an implementation of the domain model from Assignment 1. 
It contains unit tests and integration tests which can be run through pytest. 
It also contains a Flask application that renders content of a Book object instance from our domain model on various html pages.
The Flask application allows users to browse all Book objects, Book objects with a specific Author, Publisher, release year or title.

The Flask application allows users to register, login and logout of the application.
When logged-in users can write reviews of Books, as well as view their personal reading list. User's can add Books to their reading list when browsing books
and remove Books from their reading list page.


## Python version

Please use Python version 3.6 or newer versions for development. Some of the depending libraries of our web application do not support Python versions below 3.6!


## Installation

**Installation via requirements.txt**

```shell
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm for requirements installation, set the virtual environment using 'File'->'Settings' and select your project from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 


## Testing with the pytest unit tests

After you have configured pytest as the testing tool for PyCharm (File - Settings - Tools - Python Integrated Tools - Testing), you can then run tests from within PyCharm by right-clicking the tests folder and selecting "Run pytest in tests".

Alternatively, from a terminal in the root folder of the project, you can also call 'python -m pytest tests' to run all the tests. PyCharm also provides a built-in terminal, which uses the configured virtual environment. 


## Execution of the web application

**Running the Flask application**

From the project directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 

## Data sources 

The data in the excerpt files were downloaded from (Comic & Graphic):
https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home

On this webpage, you can find more books and authors in the same file format as in our excerpt, for example for different book genres. 
These might be useful to extend your web application with more functionality.

We would like to acknowledge the authors of these papers for collecting the datasets by extracting them from Goodreads:

*Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18.*

*Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19.*
