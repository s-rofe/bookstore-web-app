# Book Store


## Description

The "Book Store" Flask application renders the content of a Book object instance from the domain model on various HTML pages.
The application provides the following functionality that allows users to:
- browse all Book objects,
- Book objects with a specific Author, Publisher, release year, or title.
- User registration, login, and logout. 

When logged in, Users can write reviews of Books and add to, remove from, and view a personal reading list. Users can add Books to their reading list when browsing books and remove Books from their reading list page.

The repository contains unit tests and integration tests which can be run through pytest

This application was developed as part of the [Compsci 235 Software Development Methodologies](https://courseoutline.auckland.ac.nz/dco/course/COMPSCI/235/1215) coursework based on the grading requirements. The application was created in collaboration with [@Ubaidd](https://github.com/Ubaidd). The development of this application was split across two assignments, each of which was rewarded an A+ grade.


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


Ensure `TESTING = True` in `.env`.

## Execution of the web application

**Running the Flask application**

From the project directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 


Ensure `TESTING = False` in `.env`.
## Data sources 

The data in the excerpt files were downloaded from (Comic & Graphic):
https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home

On this webpage, you can find more books and authors in the same file format as in our excerpt, for example for different book genres. 
These might be useful to extend your web application with more functionality.

We would like to acknowledge the authors of these papers for collecting the datasets by extracting them from Goodreads:

*Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18.*

*Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19.*
