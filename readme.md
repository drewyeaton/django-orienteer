#Orienteer

Orienteer is simple Compass integration for Django projects. It is the easiest 
way to give Compass/Sass projects first class status inside your Django 
project. Once you define the settings below and add template tags to your
template, fire up the development server. If a CSS file seems to be 
out-of-date, Orienteer will run Compass to generate your CSS for you. That's
all there is to it. Be sure to *carefully read the instructions* below for 
settings specifics.


##Usage

In your Django settings.py file, define the path to your source files. Your 
'src' folder should be inside the directory you define here.

    COMPASS_PROJECT_DIR = MEDIA_ROOT + 'css/'
    
Then, define the output directory. **This is relative to the project directory.**

    COMPASS_OUTPUT_DIR = './'

Also, set the URL where your output files will be accessed.

    COMPASS_OUTPUT_URL = MEDIA_URL + 'css/'

Finally, define where the compass binary is and how you want your CSS generated.

    COMPASS_BIN = '/usr/bin/compass'
    COMPASS_STYLE = 'compact'

Next, in your template file you can reference your Sass file along with which media type(s) it is and the appropriate
style tag will be generated.

    {% load orienteer %}
    {% compass 'my_style' 'screen, print' %}

This will check your Compass project's 'src' directory for the 'my_style.sass' 
file, compile it if necessary, and then output the following HTML tag:

    <link href='/media/css/my_style.css?1273972058.0' rel='stylesheet' type='text/css' />

That's it!


##Documentation

View [Sass documentation](http://sass-lang.com/docs.html) and 
[Compass documentation](http://compass-style.org/docs/) for details on syntax.
Also, be sure to visit the [Compass Google Group](http://groups.google.com/group/compass-users)
for help with Compass related issues. 


##Requirements

- [Python](http://python.org/) (2.5 or greater, but not 3.x)
- [Django](http://www.djangoproject.com/) (1.0 or greater)


##Acknowledgements

Special thanks to Ash Christopher (ash@newthink.net) for providing the clever 
Django Sass app which was the inspiration for this one.