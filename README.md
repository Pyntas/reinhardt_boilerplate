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
    - **images**: Where the images of your app are.
    - **scripts**: The javascript files divided in *dev* and *build*.
    - **stylesheets** The stylesheets divided in *css* and *sass*.
    - **vendor** 3rd party files downloaded by running `bower install` in the src folder.

- **media** contains mainly images or other files uploaded by users, like the admin user.

- **templates** Contains the templates related to each app. Directory specified in base settings.

- **vendor** contains 3rd party libraries not installed through `pip`.

- **tests** contains the tests for you projects. Check tests section to follow great TDD philosophy.

Other important configuration files:

- **settings** This package contains the specific settings for the different
develop stages. The file`local.py` for development and `production.py` for production. Both take some base configuraton from `base.py`.



## GRUNT

Once you installed the `bower` packages (`bower install`) and node packages used by **grunt** (`npm install`) you will be able to extend your Gruntfile as it comes with a basic configuration.
###Commands:

`grunt` will run *default* task specified in the Gruntfile.js

`grunt watch` on your files changes will run a serie of tasks. By default just for compass.

`grunt build` prepares the files for production. Combines, minifies, uglifies ...


## Translations

The folder `locale` contains the language folders with the `.po` files to translate.
This folder is specified in the settings with `LOCALE_PATH`.

Run `django-admin.py makemessages -l <lang>` to generate the strings from your code and then translate them. 

After that, you can compile the messages by running `django-amdin.py compilemessages`.


Compiles .po files created by makemessages to .mo files for use with the builtin gettext support.

You can use for example, a GUI tool like [POEDIT](http://www.poedit.net/download.php) to open and translate the files.


## Code conventions:

There is a file located in the root folder called `.editorconfig` which contains the main settings to write code in your text editor following basic conventions


Install the plugin for your editor, and make sure this file is in your project.

EditorConfig [official site](http://editorconfig.org/)
