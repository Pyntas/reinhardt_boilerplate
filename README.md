Reinhardt boilerplate
=============================

This project is the seed for a customed Django boilerplate.

![django reinhard](https://dl.dropbox.com/s/htjjza0toqoho2x/reinhard.jpg)


## Installing:

1. Download the repo and cd into it:

    `git clone <repo:url>` and `cd reinhardt_boilerplate`

2. Virtualenv ([virtualenv](http://rukbottoland.com/blog/tutorial-de-python-virtualenv/))

    Create environment to isolate the project dependecies 

    `virtualenv env #create the virtualenv in the git root project`

    Activate the virtualenv:
    `source <env_name>/bin/activate`

    Install dependencies** for **local or production** environment:

     `pip install -r requirements/local.txt`

     `pip install -r requirements/production.txt`


3. Front-end dependencies:
    To be able to run the frontend dependencies you must have installed the following packages:

    > In `src` folder 
        
    0. Node [official site](http://nodejs.org/)
    1. Node Package Manager [official site](https://www.npmjs.org/doc/cli/npm-install.html)
    2. Bower [official site](http://bower.io/)

    `npm install bower -g`

    **Grunt** and other packages:

    `npm install`

    **Bower** packages like: jquery, fontawesome, bootstrap...

    `bower install`

    >install packages described in bower.json in the bowerrc specified directory)



4. Django:

    `python manage.py runserver [port]` or `./serve.sh`

5. Utils:

    - Sync Database: Little script to delete and syncdb sqlite database

        `chmod +x syncdb.sh`

        `./syncdb.sh # Give permissions chmod +x`

    - Start development server in broadcast for local network listening in port 8000:

        `./serve.sh# Give permissions chmod +x`

## Structure: understanding the organization.

- **core** Package with utils for your project
    - Templatetags

- **web** contains the code related to the web application

- **static** Contains the static files for the main apps.
    3rd party static files are stored in *vendor* folder (bower packages)

- **media** contains mainly images or other files uploaded.

- **templates** Contains the templates related to each app. Directory specified in base settings.

- **vendor** contains 3rd party libraries. i.e.: facebook.

- **tests** contains the tests for you projects. Check tests section to follow great TDD philosophy.

Other important configuration files:

- **settings** This package contains the specific settings for the different
develop stages. `local.py` for development and `production.py` for production. Both take some base configuraton from `base.py`.


## Code conventions:

There is a file located in the root folder called `.editorconfig` which contains the main settings to write code in your text editor following basic conventions


Install the plugin for your editor, and make sure this file is in your project.

EditorConfig [official site](http://editorconfig.org/)
