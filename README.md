# aistats.github.io
The AISTATS current webpage.

This repository contains the current AISTATS conference page. Once the year has past it can be archived to aistats20XX and modified to form the next year's page.

Repository set up by Neil and conversion of the old javascript pages by Wittawat. Pages moved for the 2016 edition of the conference. 


## Administration

* We have the main repository at
  [https://github.com/aistats/aistats.github.io](https://github.com/aistats/aistats.github.io).
This will be used to host the current AISTATS.
* We will make one repository with name aistats20xx for each past web site. See
  a list repositories of past web sites [here](https://github.com/aistats/).
According to this [Github help about project
pages](https://help.github.com/articles/user-organization-and-project-pages/)
(at the bottom), if we put the Jekyll files in **gh-pages** branch, the repository
will be served under http://aistats.github.io/aistats20xx. Note that the main
repository uses master branch, not gh-pages.
* When archiving to aistats20xx, it is necessary to modify the ``baseurl``
  entry of ``_config.yml`` from 

    baseurl: ""

to 

    baseurl: "/aistats20xx"

so that internal links in the web site are generated correctly.
``baseurl: ""`` is used only in the current AISTATS site because its files are 
at the root of aistats.github.io.


