# -*- coding: utf-8 -*-
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


#class NotFoundPageHandler(TvStalkerHandler):
    #def get(self):
        #path = os.path.join(os.path.dirname(__file__),
            #"templates/page404.html")
        #self.response.out.write(template.render(path, {}))


class MainPage(webapp.RequestHandler):

    def get(self):
        data = {'home_selected': 'class="selected"'}
        path = os.path.join(os.path.dirname(__file__),
            "templates/index.html")
        self.response.out.write(template.render(path, data))


class AboutPage(webapp.RequestHandler):

    def get(self):
        data = {'about_selected': 'class="selected"'}
        path = os.path.join(os.path.dirname(__file__),
            "templates/about.html")
        self.response.out.write(template.render(path, data))


class ProjectsPage(webapp.RequestHandler):

    def get(self):
        data = {'projects_selected': 'class="selected"'}
        path = os.path.join(os.path.dirname(__file__),
            "templates/projects.html")
        self.response.out.write(template.render(path, data))


class ContactPage(webapp.RequestHandler):

    def get(self):
        data = {'contact_selected': 'class="selected"'}
        path = os.path.join(os.path.dirname(__file__),
            "templates/contact.html")
        self.response.out.write(template.render(path, data))


class UMediaPage(webapp.RequestHandler):

    def get(self):
        path = os.path.join(os.path.dirname(__file__),
            "templates/umedia.html")
        self.response.out.write(template.render(path, {}))


def main():
    application = webapp.WSGIApplication([
        ('/', MainPage),
        ('/about', AboutPage),
        ('/projects', ProjectsPage),
        ('/contact', ContactPage),
        ('/umedia', UMediaPage),
        #('/.*', NotFoundPageHandler),
        ], debug=True)
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
