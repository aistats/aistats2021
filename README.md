# aistats.github.io

The AISTATS current webpage.

This repository contains the current AISTATS conference page. Once the year has past it can be archived to aistats20XX and modified to form the next year's page.



## Archiving Last Year's Page

Each year the main web page needs to be archived to store as a previous year's conference. To do this, the first thing you need to do is duplicate this repository. 

**These steps need to be done by someone with admin access to the aistats github organization**

1. Create the new repo in github by going to <https://github.com/organizations/aistats/repositories/new>, use the name coding `aistatsXXXX` where `XXXX` is the year of the archived conference. 

2. Give the conference a description, "April 9 - 11, Playa Blanca, Lanzarote, Canary Islands"

3. Do *not* create an initial README for the conference. 

4. Create the Repo.

**This step can be done with an account that has write access to the aistats.github.io.git**

5. Go to a suitable directory on your machine and type:

```
git clone --bare https://github.com/aistats/aistats.github.io.git
mv aistats.github.io.git aistatsXXXX
cd aistatsXXXX
git branch -m gh-pages
git push --mirror https://github.com/aistats/aistatsXXXX.git
```
6. Edit the `_config.yml` file in the new repo to set `baseurl` to `/aistatsXXXX`

7. Check that the archived page appears online at http://aistats.org/aistatsXXXX/

8. Update the original main repository at [https://github.com/aistats/aistats.github.io](https://github.com/aistats/aistats.github.io) for the current conference.
This will be used to host the current AISTATS.

9. Add the team `aistatsXXXX` to the admin rights for the repo `aistatsXXXX`

10. Create a new admin team for this year's page, `aistatsYYYY`, where `YYYY=XXXX+1` and assign it to admin `aistats.github.io` 

## More information

* See
  a list of repositories of past web sites [here](https://github.com/aistats/).

* This link gives [Github help about project
pages](https://help.github.com/articles/user-organization-and-project-pages/)
(at the bottom), if we put the Jekyll files in **gh-pages** branch, the repository
will be served under http://aistats.github.io/aistats20xx. Note that the main
repository uses master branch, not gh-pages.

* When archiving to aistats20xx, it is necessary to modify the ``baseurl``
  entry of ``_config.yml`` from ``baseurl: ""`` to ``baseurl: "/aistats20xx"``
so that internal links in the web site are generated correctly.  

* ``baseurl:
""`` is used only in the current AISTATS site because its files are at the root
of aistats.github.io.

* Repository set up by Neil Lawrence and conversion of the old javascript pages by Wittawat. Pages then arcived for the 2016 and 2017 editions of the conference. 


