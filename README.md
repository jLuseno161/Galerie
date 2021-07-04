# GALERIA

## Author

[Joy Kolia](https://github.com/jLuseno161)

## Description

A photo gallery web application made using Django.

## Live Link

[View Site](https://galeria0.herokuapp.com)

## User Story

* User can view all photos on index page ordered by the date they were posted
* Hovering on an image will reveal more information about it; the title, description, location and time posted.
* User can click on the copy button on an image to copy its url for sharing purposes
* Clicking an image will toggle a lightbox with an expanded view of the image
* User can navigate to other images while on the lightbox view.
* User can search photos based on their categories
* User can browse photos based on the location they were taken

## Prerequisites

You need the following to start working on this project: On your local system; 

1. Python3.8
2. Django
3. Pip
4. Virtual Environment(virtual)
5. A text editor

## Development Installation

To get the code..

1. Clone the repository:
 `git clone  https://github.com/jLuseno161/Galerie.git`

2. Move to the folder and install requirements
 ` cd Galeria`

3. In the projects root directory, install the virtualenv library using pip and create a virtual environment. Run the following commands respectively:
    - **`pip install virtualenv`**
    - **`virtualenv virtual`**
    - **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
4. Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
5. Launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    - To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.

## Technology used

* [Python3.8](https://www.python.org/)
* [Django](https://docs.djangoproject.com)
* [Heroku](https://heroku.com)
* Git
* Javascript
* Bootstrap 4.3.1

## Known Bugs

* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [joyluseno0@gmail.com]

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright © 2021  [JOY L. KOLIA](https://github.com/jLuseno161)
