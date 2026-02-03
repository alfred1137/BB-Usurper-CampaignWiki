Description: Source code of Jekyll theme used in this project.

Directory structure:
└── drassil-git-wiki-theme/
    ├── README.md
    ├── _config.yml
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── docker-compose.yml
    ├── LICENSE
    ├── PULL_REQUEST_TEMPLATE.md
    ├── sync-wiki.sh
    ├── _includes/
    │   ├── .gitkeep
    │   └── git-wiki/
    │       ├── components/
    │       │   ├── action_btn/
    │       │   │   ├── downloads.html
    │       │   │   └── page_actions.html
    │       │   ├── copyrights/
    │       │   │   └── copyrights.html
    │       │   ├── lists/
    │       │   │   ├── page-list.html
    │       │   │   └── post-list.html
    │       │   ├── logo/
    │       │   │   └── logo.html
    │       │   ├── search/
    │       │   │   ├── index.html
    │       │   │   ├── se_github.html
    │       │   │   ├── se_google.html
    │       │   │   ├── se_js.html
    │       │   │   └── se_js_rss.html
    │       │   └── toc/
    │       │       ├── toc-lib.html
    │       │       └── toc.html
    │       ├── defines/
    │       │   └── defines.html
    │       └── sections/
    │           ├── content/
    │           │   ├── body.html
    │           │   ├── content.html
    │           │   └── wrapper.html
    │           ├── footer/
    │           │   └── footer.html
    │           ├── head/
    │           │   ├── head.html
    │           │   ├── meta.html
    │           │   ├── scripts.html
    │           │   └── styles.html
    │           ├── header/
    │           │   └── header.html
    │           ├── tail/
    │           │   └── tail.html
    │           └── tools/
    │               └── tools.html
    ├── _layouts/
    │   ├── default.html
    │   ├── git-wiki-404.html
    │   ├── git-wiki-blog.html
    │   ├── git-wiki-bs-github.html
    │   ├── git-wiki-bs-lux.html
    │   ├── git-wiki-bs-united.html
    │   ├── git-wiki-default.html
    │   └── git-wiki-post.html
    ├── _posts/
    │   └── .gitkeep
    ├── _sass/
    │   ├── fonts.scss
    │   ├── git-wiki-style.scss
    │   ├── rouge-github.scss
    │   └── w3.scss
    ├── assets/
    │   ├── 404.html
    │   ├── sitemap_full.xml
    │   ├── blog/
    │   │   └── index.html
    │   ├── css/
    │   │   ├── git-wiki-style.scss
    │   │   └── github.css
    │   ├── fonts/
    │   │   ├── Noto-Sans-700/
    │   │   │   ├── Noto-Sans-700.eot
    │   │   │   ├── Noto-Sans-700.ttf
    │   │   │   ├── Noto-Sans-700.woff
    │   │   │   └── Noto-Sans-700.woff2
    │   │   ├── Noto-Sans-700italic/
    │   │   │   ├── Noto-Sans-700italic.eot
    │   │   │   ├── Noto-Sans-700italic.ttf
    │   │   │   ├── Noto-Sans-700italic.woff
    │   │   │   └── Noto-Sans-700italic.woff2
    │   │   ├── Noto-Sans-italic/
    │   │   │   ├── Noto-Sans-italic.eot
    │   │   │   ├── Noto-Sans-italic.ttf
    │   │   │   ├── Noto-Sans-italic.woff
    │   │   │   └── Noto-Sans-italic.woff2
    │   │   └── Noto-Sans-regular/
    │   │       ├── Noto-Sans-regular.eot
    │   │       ├── Noto-Sans-regular.ttf
    │   │       ├── Noto-Sans-regular.woff
    │   │       └── Noto-Sans-regular.woff2
    │   ├── images/
    │   │   └── .gitkeep
    │   └── js/
    │       ├── checkLinks.js
    │       ├── scale.fix.js
    │       └── searchdata.js
    ├── wiki/
    │   ├── main_page.md
    │   └── .gitkeep
    ├── .env-files/
    │   ├── Dockerfile.github
    │   ├── Dockerfile.gitlab
    │   ├── Gemfile.github
    │   └── Gemfile.gitlab
    └── .github/
        └── ISSUE_TEMPLATE/
            ├── bug_report.md
            ├── config.yml
            ├── feature_request.md
            └── general.md

================================================
FILE: README.md
================================================
# git-wiki

Git-wiki is a **modular and full featured wiki** powered by Git, [GitHub](https://pages.github.com/)/[Gitlab](https://about.gitlab.com/product/pages/) Pages and pull requests!

The git-wiki project is composed by 3 different repository:

- [git-wiki-theme](https://github.com/Drassil/git-wiki-theme): This is the repository of the theme that implements the wiki functionalities. You would have not fork it unless you need to send a Pull Request or create your wiki project from scratch.

- [git-wiki-skeleton](https://github.com/Drassil/git-wiki-skeleton): This is the repo that you should fork or use as a template. It uses the [jekyll remote theme](https://github.com/benbalter/jekyll-remote-theme) functionality that allows you to create your own wiki based on git-wiki-theme. By using the remote functionality you can automatically keep your wiki always updated with latest features from the **git-wiki-theme**, but you can also fully customize it. 

- [git-wiki](https://github.com/Drassil/git-wiki): This is the documentation repository and website of the **git-wiki-theme** project. You would have not fork it unless you want to contribute to the git-wiki project documentation.

## Getting started

The easier and faster way to use git-wiki is the "skeleton" method.

**You don't need to install anything locally!**

1. Simply fork/clone [skeleton repo](https://github.com/Drassil/git-wiki-skeleton) or click on the "Use this template" button to create your copy of the skeleton project.

2. Edit _config.yml and other pages as you need and then deploy it on GitHub/Gitlab Pages.

**Done**! Now wait that your page will be published and you're ready **_to wiki_**!

## Features 

* Improvements in the **cooperative** aspect: forks, pull requests and roles.
* You can **customize your wiki** as you want with stylesheets and even changing the layout (see customization section below).
* **No databases!** Only static files that can be downloaded in a few seconds.
* **Blazing fast** and free thankfully to GitHub/Gitlab Pages and Jekyll Server Side Generation process!
* **Markdown and HTML** mixed together!
* **Multiple free search engines!** on a static site!
* **History, revision comparison** and everything you need from a wiki platform.
* You can **edit your pages** with the standard git editor, prose.io (integrated) or any kind of editor you prefer.
* Non-existent wiki page links are "[red](red.md)", you can **click on them to automatically create a new page**!
* [External links](http://example.com) get the right icon automatically.
* **Component system with hooks** that allows you to completely customize your wiki UI (see customization section below).
* Some **nice internal themes** to change your entire wiki UI with 1 simple configuration (see customization section below).
* Integrated **Blogging** feature thanks to Jekyll!
* Automatically generated **TOC**!
* You can download the entire wiki for **offline** usage and even navigate directly using a Markdown reader!


You can use it with the Jekyll ["remote_theme"](https://github.com/benbalter/jekyll-remote-theme) feature or fork/copy the master branch and start your wiki in just 1 minute.



Instructions and full documentation: [http://drassil.github.io/git-wiki](http://drassil.github.io/git-wiki)





================================================
FILE: _config.yml
================================================
# (string) Title of your wiki
title: 
# (string) Description of your wiki
description: 
# (boolean) disable edit functionalities (edit/delete/add pages)
disable_edit: false
# (boolean) Enable/disable wiki page list in sidebar
show_wiki_pages: true
# (integer) Maximum number of wiki page to shown in sidebar
show_wiki_pages_limit: 10
# (boolean) Enable/disable blog feature
blog_feature: true
# (boolean) Enable/disable wiki posts list in sidebar (needs blog_feature enabled)
show_wiki_posts: true
# (integer) Maximum number of wiki posts to shown in sidebar
show_wiki_posts_limit: 10
# from jekyll (read jekyll doc)
paginate: 5
paginate_path: "/assets/blog/page:num"
permalink: "/assets/blog/posts/:year/:month/:day/:title:output_ext"
# (boolean) Enable/disable download buttons in sidebar
show_downloads: true
# (string) Specify branch rendered by gitpages allowing wiki tool buttons to work
git_branch: "master"
# (string) Url of logo image, it can be full, absolute or relative.
logo_url: 
# (string) The UA-XXXXX-Y code from google analytic to enable GA on your wiki
google_analytics: 
# (string) folder where wiki pages are stored, it's needed for tool buttons
wiki_folder: "wiki"
# (boolean) if you're using github wiki as submodule then this config
# must be enabled to allow tool buttons to work properly
use_github_wiki: false
# (boolean) Enable "Edit with Prose.io" button in tools, it's a 3rd party
# service to edit github markdown pages easily
use_prose_io: true
# Select search_engine component from:
# - js: it uses a built in javascript component that uses generated js object
# - js_rss: it uses a built in javascript component that uses generated  sitemap_full.xml to search inside your wiki with lunr library (slow and experimental)
# - github : it uses internal github repository search
# - google : it uses cse search bar, you need to configure google_cse_token
#
search_engine : "js"
# Setting google custom search engine for google
# cse search bar (https://cse.google.it/cse/)
google_cse_token: 

# (string) path of site root. Normally it's must be empty because _config.yml resides in the root of your repository.
# If you have _config.yml and your site in a subfolder, then change this config accordly 
site_root: 

#
# Jekyll configurations
#

# You can customize it changing default layout for all pages
# More info: https://jekyllrb.com/docs/configuration/
#
# git-wiki includes some internal themes that you can choose
# check _layouts folder
#
markdown: kramdown
highlighter: rouge
kramdown:
  input: GFM
  syntax_highlighter: rouge

defaults:
 - 
    scope:
      path: "wiki"
    values:
      permalink: /:basename
 -
    scope:
      path: "" # an empty string here means all files in the project
    values:
      layout: "git-wiki-default"
 -
    scope:
      path: ""
      type: "pages"
    values:
      layout: "git-wiki-default"
 -
    scope:
      path: ""
      type: "posts"
    values:
      layout: "git-wiki-post"
 -
    scope:
      path: assets/blog
    values:
      layout: "git-wiki-blog"
sass:
    style: compressed
plugins:
  - jekyll-avatar
  - jekyll-coffeescript
  - jekyll-default-layout
  - jekyll-feed
  - jekyll-gist
  - jekyll-paginate
  - jekyll-mentions
  - jekyll-optional-front-matter
  - jekyll-readme-index
  - jekyll-redirect-from
  - jekyll-remote-theme
  - jekyll-relative-links
  - jekyll-seo-tag
  - jekyll-sitemap
  - jekyll-titles-from-headings
  - jemoji


#
# INCLUDING HOOKS
# They are optional, change them only if you need
# Check wiki documentation to learn how they work
#

inc_before_toc : 
inc_after_toc : 
inc_before_content : 
inc_after_content : 
inc_before_footer : 
inc_after_footer : 
inc_before_head : 
inc_after_head : 
inc_before_meta : 
inc_after_meta : 
inc_before_scripts : 
inc_after_scripts : 
inc_before_styles : 
inc_after_styles : 
inc_before_header : 
inc_after_header : 
inc_before_tail : 
inc_after_tail : 
inc_before_tools : 
inc_after_tools : 

inc_before_page_list :
inc_after_page_list :
inc_before_post_list :
inc_after_post_list :



================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at staff-drassil@googlegroups.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq



================================================
FILE: CONTRIBUTING.md
================================================
If you want to send a pull request to our project and github editor is not enough, then you can:

1. Fork or copy this repository

2. clone on your local environment and run your git-wiki installation following [this guide](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/)

3. do your changes, push on your fork and create a Pull Request for us



================================================
FILE: docker-compose.yml
================================================
version: '3.7'
services:
  github-wiki-theme:
    build:
      context: .
      dockerfile: .env-files/Dockerfile.github
    ports:
      - 4000:4000
      - 35729:35729
    environment:
      - BUNDLE_GEMFILE=.env-files/Gemfile.github
    volumes:
      - .:/srv/jekyll
      - github_site:/srv/jekyll/_site
    command: bundle exec jekyll serve --host 0.0.0.0 --force_polling --livereload
  gitlab-wiki-theme:
    build:
      context: .
      dockerfile: .env-files/Dockerfile.gitlab
    ports:
      - 4000:4000
      - 35729:35729
    environment:
      - BUNDLE_GEMFILE=.env-files/Gemfile.gitlab
    volumes:
      - .:/srv/jekyll
      - gitlab_site:/srv/jekyll/_site
    command: 'bundle exec jekyll serve --host 0.0.0.0 --force_polling --livereload'
    profiles:
      - gitlab
volumes:
  github_site:
  gitlab_site:



================================================
FILE: LICENSE
================================================
The MIT License (MIT)

Copyright (c) 2017 Drassil.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.



================================================
FILE: PULL_REQUEST_TEMPLATE.md
================================================
<!--- Provide a general summary of your changes in the Title above -->

## Description
<!--- Describe your changes in detail -->

## Related Issue
<!--- This project only accepts pull requests related to open issues -->
<!--- If suggesting a new feature or change, please discuss it in an issue first -->
<!--- If fixing a bug, there should be an issue describing it with steps to reproduce -->
<!--- Please link to the issue here: -->

## Motivation and Context
<!--- Why is this change required? What problem does it solve? -->
<!--- If it fixes an open issue, please link to the issue here. -->

## How Has This Been Tested?
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->

## Screenshots (if appropriate):



================================================
FILE: sync-wiki.sh
================================================
#!/usr/bin/env bash
#
# This script can be used to sync the wiki submodule
# in case you're using github internal wiki option
#

git pull origin master
cd wiki
git pull origin master
cd ..
git commit -a -m "updated wiki"
git push origin master



================================================
FILE: _includes/.gitkeep
================================================




================================================
FILE: _includes/git-wiki/components/action_btn/downloads.html
================================================
<ul class="git-wiki-downloads">
    <li><a href="{{ site.github.zip_url }}">Download <strong>ZIP File</strong></a></li>
    <li><a href="{{ site.github.tar_url }}">Download <strong>TAR Ball</strong></a></li>
    <li><a href="{{ site.github.repository_url }}">View On <strong>{% if site.github.hostname == "gitlab.com" %} Gitlab {% else %} Github {% endif %} </strong></a></li>
</ul>



================================================
FILE: _includes/git-wiki/components/action_btn/page_actions.html
================================================
<div class="git-wiki-tools">
    {% if site.use_github_wiki %}

    {% if site.disable_edit != true %}
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/wiki/_new">Add new</a></span>
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/wiki/{{url | remove: '.html' | append: ''}}/_edit">Edit</a></span>
    {% endif %}

    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/wiki/{{url | remove: '.html' | append: ''}}/_history">History</a></span>

    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/wiki/{{url | remove: '.html' | append: '.md'}}/">Source</a></span>
    {% else %}

    {% if site.disable_edit != true %}
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/new/{{site.git_branch | escape}}{{ site.site_root | default: '/' }}{{ site.wiki_folder }}?filename=">Add
            new</a></span>
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/edit/{{site.git_branch | escape}}/{{ site.site_root | default: '/' }}{{page.path | escape}}">Edit</a></span>

    {% if site.github.hostname == "gitlab.com" %}
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/blob/{{site.git_branch | escape}}/{{ site.site_root | default: '/' }}{{page.path | escape}}">Delete</a></span>
    {% else %}
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/delete/{{site.git_branch | escape}}/{{ site.site_root | default: '/' }}{{page.path | escape}}">Delete</a></span>
    {% endif %}

    {% endif %}

    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/commits/{{site.git_branch | escape}}/{{ site.site_root | default: '/' }}{{page.path | escape}}">History</a></span>
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/blob/{{site.git_branch | escape}}/{{ site.site_root | default: '/' }}{{page.path | escape}}">Source</a></span>
    {% if site.blog_feature %}
    <span class="tools-element"><a target="_blank" href="{{ site.github.repository_url }}/new/{{site.git_branch | escape}}{{ site.site_root | default: '/' }}_posts?filename=">Add
            new post</a></span>
    {% endif %}
    {% if site.use_prose_io and site.github.hostname != "gitlab.com" %}
    <br>
    Prose.io:
    <span class="tools-element"><a target="_blank" href="http://prose.io/#{{site.github.repository_nwo}}/new/{{site.git_branch | escape}}{{ site.site_root | default: '/' }}{{ site.wiki_folder }}">Add
            new</a></span>
    <span class="tools-element"><a target="_blank" href="http://prose.io/#{{site.github.repository_nwo}}/edit/{{site.git_branch | escape}}{{ site.site_root | default: '/' }}{{page.path | escape}}">Edit</a></span>
    {% if site.blog_feature %}
    <span class="tools-element"><a target="_blank" href="http://prose.io/#{{site.github.repository_nwo}}/new/{{site.git_branch | escape}}{{ site.site_root | default: '/' }}_posts/">Add
            new post</a></span>
    {% endif %}
    {% endif %}
    {% endif %}
</div>



================================================
FILE: _includes/git-wiki/components/copyrights/copyrights.html
================================================
{% if site.github.is_project_page %}
<div class="git-wiki-copyrights">
    <p>This project is maintained by <a href="{{ site.github.owner_url }}">{{ site.github.owner_name }}</a></p>
    {% endif %}
    <p><small>Hosted on GitHub Pages &mdash; Powered by <a href="https://github.com/Drassil/git-wiki-theme">Git-Wiki v{{
                version }}</a> </p>

    {% if site.github.is_project_page %}
    <p class="view"><a href="{{ site.github.repository_url }}">View the Project on {% if site.github.hostname == "gitlab.com" %} Gitlab {% else %} Github {% endif %} <small>{{ github_name }}</small></a></p>
</div>
{% endif %}



================================================
FILE: _includes/git-wiki/components/lists/page-list.html
================================================
<div class="git-wiki-page-list">
    {% if site.inc_before_page_list %}
    {% include {{ site.inc_before_page_list }} %}
    {% endif %}

    <span class="page-list-title">Pages {% if (site.show_wiki_pages_limit >= 1 %} (Latest {{site.show_wiki_pages_limit
        }} updated) {% endif %}:</span>
    <ul class="page-list">
        {% assign numPages=0 %}
        {% assign items = site.html_pages | sort: 'date' | reverse %}
        {% for page in items %}
        {% if numPages >= site.show_wiki_pages_limit %}
        {% break %}
        {% endif %}
        {% if page.is_wiki_page != false and page.sitemap != false %}
        <li class="page-list-item">
            {% assign title = page.title | default: page.name %}
            <a href="{{ page.url | relative_url }}">{{title | escape}}</a>
        </li>
        {% assign numPages = numPages | plus: 1 %}
        {% endif %}

        {% endfor %}
    </ul>

    {% if site.inc_after_page_list %}
    {% include {{ site.inc_after_page_list }} %}
    {% endif %}
</div>


================================================
FILE: _includes/git-wiki/components/lists/post-list.html
================================================
<div class="git-wiki-page-list">
    {% if site.inc_before_post_list %}
    {% include {{ site.inc_before_post_list }} %}
    {% endif %}

    <span class="post-list-title">Posts {% if (site.show_wiki_posts_limit >= 1 %} (Latest {{site.show_wiki_posts_limit
        }} updated) {% endif %}:</span>
    <ul class="post-list">
        {% assign numPages=0 %}
        {% assign items = site.posts | sort: 'date' | reverse %}
        {% for post in items %}
        {% if numPages >= site.show_wiki_posts_limit %}
        {% break %}
        {% endif %}

        {% if post.layout != "null" and post.sitemap != false and post.title %}
        <li class="post-list-item">
            <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
        </li>
        {% assign numPages = numPages | plus: 1 %}
        {% endif %}

        {% endfor %}
    </ul>

    <span class="post-list read-all"><a href="{{ '/assets/blog/' | relative_url}}">Read all</a></span>

    {% if site.inc_after_post_list %}
    {% include {{ site.inc_after_post_list }} %}
    {% endif %}
</div>


================================================
FILE: _includes/git-wiki/components/logo/logo.html
================================================
<div class="git-wiki-main-logo">
<a href="{{ '/' | relative_url }}"><img src="{{ site.logo_url | relative_url }}">
        <h1>{{ site.title | default: site.github.repository_name | escape }}</h1>
    </a>
    <p>{{ site.description | default: site.github.project_tagline }}</p>
</div>


================================================
FILE: _includes/git-wiki/components/search/index.html
================================================
<div class="git-wiki-search">
    {% comment %}
    This component just select your preferred search engine based on _config.yml value
    {% endcomment %}

    {% assign se = site.search_engine | default: "github" %}
    {% assign file = "git-wiki/components/search/se_" | append: se | append: ".html" %}
    {% include {{file}} %}
</div>


================================================
FILE: _includes/git-wiki/components/search/se_github.html
================================================
<div class="git-wiki-search-github">
    <form method="GET" action="{{ site.github.repository_url }}/search">
        <input type="text" name="q[]" placeholder="Text to search">
        {% if site.use_github_wiki %}
        <input type="hidden" name="type" value="Wikis">
        {% else %}
        <!-- <input type="hidden" name="l" value="Markdown"> -->
        <input type="hidden" name="q[]" value="path:/{{ site.wiki_folder }}">
        {% endif %}
        <input type="submit" value="Search">
    </form>
</div>


================================================
FILE: _includes/git-wiki/components/search/se_google.html
================================================
<div class="git-wiki-search-google">
    <script>
        (function () {
            var cx = "{{site.google_cse_token}}";
            var gcse = document.createElement('script');
            gcse.type = 'text/javascript';
            gcse.async = true;
            gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(gcse, s);
        })();
    </script>
    <gcse:search></gcse:search>
</div>


================================================
FILE: _includes/git-wiki/components/search/se_js.html
================================================
<div class="git-wiki-search-js">
	<input type="text" id="search-input" placeholder="Search..">
	<ul id="results-container"></ul>
</div>
<!-- script pointing to jekyll-search.js -->
<script src="{{ '/assets/js/simple-jekyll-search.min.js' | relative_url }}"></script>
<script async src="{{ 'assets/js/searchdata.js' | relative_url }}"></script>



================================================
FILE: _includes/git-wiki/components/search/se_js_rss.html
================================================
<div class="git-wiki-search-js">
	<div class="container">
		<div class="well" id="searchbox">
			<input id="search-field" placeholder="Search the Site" />
			<ul id="results"></ul>
		</div>
	</div>
</div>
<script type="text/javascript">
	$.ajax({
		url: "{{ '/assets/js/jquery.camelhunter.min.js' | relative_url }}",
		dataType: "script",
		success: function () {
			setTimeout($("#search-field").camelHunter({
				onKeyUp: true,
				rss: "{{ '/sitemap_full.xml' | relative_url }}",
				results: "#results"
			}), 0);
		}
	});
</script>


================================================
FILE: _includes/git-wiki/components/toc/toc-lib.html
================================================
{% capture tocWorkspace %}
    {% comment %}
        Version 1.0.9
          https://github.com/allejo/jekyll-toc

        "...like all things liquid - where there's a will, and ~36 hours to spare, there's usually a/some way" ~jaybe

        Usage:
            {% include toc.html html=content sanitize=true class="inline_toc" id="my_toc" h_min=2 h_max=3 %}

        Parameters:
            * html         (string) - the HTML of compiled markdown generated by kramdown in Jekyll

        Optional Parameters:
            * title        (string) : Contents:  - title for the TOC
            * minHeaders   (int)    : 1          - minimum number of headers required to show the TOC
            * sanitize     (bool)   : false      - when set to true, the headers will be stripped of any HTML in the TOC
            * class        (string) :   ''       - a CSS class assigned to the TOC
            * id           (string) :   ''       - an ID to assigned to the TOC
            * h_min        (int)    :   1        - the minimum TOC header level to use; any header lower than this value will be ignored
            * h_max        (int)    :   6        - the maximum TOC header level to use; any header greater than this value will be ignored
            * ordered      (bool)   : false      - when set to true, an ordered list will be outputted instead of an unordered list
            * item_class   (string) :   ''       - add custom class(es) for each list item; has support for '%level%' placeholder, which is the current heading level
            * baseurl      (string) :   ''       - add a base url to the TOC links for when your TOC is on another page than the actual content
            * anchor_class (string) :   ''       - add custom class(es) for each anchor element

        Output:
            An ordered or unordered list representing the table of contents of a markdown block. This snippet will only
            generate the table of contents and will NOT output the markdown given to it
    {% endcomment %}

    {% capture my_toc %}{% endcapture %}
    {% assign title = include.title | default: "Contents:" %}
    {% assign minHeaders = include.minHeaders | default: 1 %}
    {% assign orderedList = include.ordered | default: false %}
    {% assign minHeader = include.h_min | default: 1 %}
    {% assign maxHeader = include.h_max | default: 6 %}
    {% assign nodes = include.html | split: '<h' %}
    {% assign firstHeader = true %}

    {% capture listModifier %}{% if orderedList %}1.{% else %}-{% endif %}{% endcapture %}

    {% assign hCount = 0 %}

    {% for node in nodes %}
        {% if node == "" %}
            {% continue %}
        {% endif %}

        {% assign headerLevel = node | replace: '"', '' | slice: 0, 1 | times: 1 %}

        {% if headerLevel < minHeader or headerLevel > maxHeader %}
            {% continue %}
        {% endif %}

        {% if firstHeader %}
            {% assign firstHeader = false %}
            {% assign minHeader = headerLevel %}
        {% endif %}

        {% assign indentAmount = headerLevel | minus: minHeader %}
        {% assign _workspace = node | split: '</h' %}

        {% assign _idWorkspace = _workspace[0] | split: 'id="' %}
        {% assign _idWorkspace = _idWorkspace[1] | split: '"' %}
        {% assign html_id = _idWorkspace[0] %}

        {% assign _classWorkspace = _workspace[0] | split: 'class="' %}
        {% assign _classWorkspace = _classWorkspace[1] | split: '"' %}
        {% assign html_class = _classWorkspace[0] %}

        {% if html_class contains "no_toc" %}
            {% continue %}
        {% endif %}

        {% capture _hAttrToStrip %}{{ _workspace[0] | split: '>' | first }}>{% endcapture %}
        {% assign header = _workspace[0] | replace: _hAttrToStrip, '' %}

        {% assign space = '' %}
        {% for i in (1..indentAmount) %}
            {% assign space = space | prepend: '    ' %}
        {% endfor %}

        {% if include.item_class and include.item_class != blank %}
            {% capture listItemClass %}{:.{{ include.item_class | replace: '%level%', headerLevel }}}{% endcapture %}
        {% endif %}

        {% assign hCount = hCount | plus: 1 %}

        {% capture heading_body %}{% if include.sanitize %}{{ header | strip_html }}{% else %}{{ header }}{% endif %}{% endcapture %}
        {% capture my_toc %}{{ my_toc }}
{{ space }}{{ listModifier }} {{ listItemClass }} [{{ heading_body | replace: "|", "\|" }}]({% if include.baseurl %}{{ include.baseurl }}{% endif %}#{{ html_id }}){% if include.anchor_class %}{:.{{ include.anchor_class }}}{% endif %}{% endcapture %}
    {% endfor %}

    {% if include.class and include.item_class != blank %}
        {% capture my_toc %}{:.{{ include.class }}}
{{ my_toc | lstrip }}{% endcapture %}
    {% endif %}

    {% if include.id %}
        {% capture my_toc %}{: #{{ include.id }}}
{{ my_toc | lstrip }}{% endcapture %}
    {% endif %}
{% endcapture %}{% assign tocWorkspace = '' %}

{% if hCount >= minHeaders %}
    {{ title }}
    {{ my_toc | markdownify | strip }}
{% endif %}


================================================
FILE: _includes/git-wiki/components/toc/toc.html
================================================
{% if site.inc_before_toc %}
{% include {{ site.inc_before_toc }} %}
{% endif %}

{% include git-wiki/components/toc/toc-lib.html title="Contents:" minHeaders=1 html=content sanitize=true class="inline_toc" id="git-wiki-toc" h_min=1 h_max=3 ordered=1 %}

{% if site.inc_after_toc %}
{% include {{ site.inc_after_toc }} %}
{% endif %}



================================================
FILE: _includes/git-wiki/defines/defines.html
================================================
{% assign version = "2.8.6" %}
{% capture lchar %}{{page.url | slice: -1, 1}}{% endcapture %}
{% capture url %}
{% if lchar == "/" %}{{page.url}}index.html{% else %}{{ page.url | default: 'index.html' }}{% endif%}
{% endcapture %}


================================================
FILE: _includes/git-wiki/sections/content/body.html
================================================
<body style="background-color: black;" onload="darkModeSetBodyBg()">
    <!-- dark mode -->
    <script>
        darkModeSetBodyBg()
    </script>
    
    {% include git-wiki/sections/content/wrapper.html %}

    {% include git-wiki/sections/tail/tail.html %}
</body>


================================================
FILE: _includes/git-wiki/sections/content/content.html
================================================
<div class="git-wiki-page">
  <section>

    {% include git-wiki/sections/tools/tools.html %}

    {% include git-wiki/components/toc/toc.html %}

    {% if site.inc_before_content %}
    {% include {{ site.inc_before_content }} %}
    {% endif %}

    <div id="git-wiki-content">
      {{ content }}
    </div>

    {% if site.inc_after_content %}
    {% include {{ site.inc_after_content }} %}
    {% endif %}
  </section>
</div>


================================================
FILE: _includes/git-wiki/sections/content/wrapper.html
================================================
<div class="wrapper">
    {% include git-wiki/sections/header/header.html %}
    {% include git-wiki/sections/content/content.html %}
    {% include git-wiki/sections/footer/footer.html %}
</div>


================================================
FILE: _includes/git-wiki/sections/footer/footer.html
================================================
<footer>
    {% if site.inc_before_footer %}
    {% include {{ site.inc_before_footer }} %}
    {% endif %}

    {% include git-wiki/components/copyrights/copyrights.html %}

    {% if site.inc_after_footer %}
    {% include {{ site.inc_after_footer }} %}
    {% endif %}
</footer>


================================================
FILE: _includes/git-wiki/sections/head/head.html
================================================
<head>
  {% if site.inc_before_head %}
  {% include {{ site.inc_before_head }} %}
  {% endif %}
 
  {% include git-wiki/sections/head/meta.html %}
  {% include git-wiki/sections/head/scripts.html %}
  {% include git-wiki/sections/head/styles.html %}

  {% if site.inc_after_head %}
  {% include {{ site.inc_after_head }} %}
  {% endif %}
</head>


================================================
FILE: _includes/git-wiki/sections/head/meta.html
================================================
{% if site.inc_before_meta %}
{% include {{ site.inc_before_meta }} %}
{% endif %}

<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="chrome=1">
<meta name="viewport" content="width=device-width">

{% seo %}

{% assign pagetitle = page.name | replace: ".md", "" %}
{% assign title = pagetitle | append: " - " | append: site.title  | strip_html %}

<title>{{ title | strip_html | strip_newlines | truncate: 160 }}</title>

<meta property="og:title" content="{{ title | strip_html | strip_newlines | truncate: 160 }}">

<meta property="og:description" content="{% if page.excerpt %}
        {{ page.excerpt | strip_html | strip_newlines | truncate: 160 }}
      {% else %}
        {{ site.description }}
      {% endif %}">


<meta property="og:url"
  content="{{ page.url | replace:'index.html','' | prepend: site.baseurl | prepend: site.url }}" />

{% if page.image %}
<meta property="og:image" content="{{page.image}}" />
<meta name="twitter:image" content="{{page.image}}" />
{% elsif site.logo_url %}
<meta property="og:image" content="{{ site.logo_url | relative_url }}" />
<meta name="twitter:image" content="{{ site.logo_url | relative_url }}" />
{% endif %}


{% if site.inc_after_meta %}
{% include {{ site.inc_after_meta }} %}
{% endif %}


================================================
FILE: _includes/git-wiki/sections/head/scripts.html
================================================
{% if site.inc_before_scripts %}
{% include {{ site.inc_before_scripts }} %}
{% endif %}

<script src="https://cdn.jsdelivr.net/npm/darkmode-js@1.5.7/lib/darkmode-js.min.js"></script>


<script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
<script src="{{ '/assets/js/checkLinks.js' | relative_url }}"></script>
<!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

<!-- dark mode -->
<style>
  body {
    visibility: hidden;
    opacity: 0;
  }
</style>
<noscript>
  <style>
    body {
      visibility: visible;
      opacity: 1;
    }
  </style>
</noscript>
<script>
  function darkModeSetBodyBg() {
    if (localStorage.getItem('darkmode')==="true") {
      console.log("darkmode activated");
      document.body.style.backgroundColor = "black !important";
    } else {
      document.body.style.backgroundColor = ""; // reset background color
    }
  }

  function addDarkmodeWidget() {

    const options = {
        label: '🌓', // default: ''
        time: '0s'
    }

    new Darkmode(options).showWidget();

    document.body.style.visibility = 'visible';
    document.body.style.opacity = 1;
  }

  $(document).ready(addDarkmodeWidget);
</script>

{% if site.inc_after_scripts %}
{% include {{ site.inc_after_scripts }} %}
{% endif %}


================================================
FILE: _includes/git-wiki/sections/head/styles.html
================================================
{% if site.inc_before_styles %}
{% include {{ site.inc_before_styles }} %}
{% endif %}

<link rel="stylesheet" href="{{ '/assets/css/git-wiki-style.css?v=' | append: site.github.build_revision | relative_url }}">

{% if site.inc_after_styles %}
{% include {{ site.inc_after_styles }} %}
{% endif %}


================================================
FILE: _includes/git-wiki/sections/header/header.html
================================================
<div class=" w3-xlarge w3-hide-large" id="git-wiki-mobile-header">
  <button class="w3-button w3-teal" onclick="sidebar_toggle()">&#9776;</button>
  <a href="{{ '/' | relative_url }}">
    {% if site.logo_url %}
    <img src="{{ site.logo_url | relative_url }}" width="20px">
    {% endif %}
    {{ site.title | escape }}
  </a>
</div>
<header class="w3-sidebar w3-bar-block w3-collapse" id="git-wiki-sidebar">
  <div>
    <button class="w3-bar-item w3-button w3-large w3-hide-large" onclick="sidebar_toggle()">Close &times;</button>
    {% if site.inc_before_header %}
    {% include {{ site.inc_before_header }} %}
    {% endif %}

    <div class="w3-hide-medium w3-hide-small">
      {% if site.logo_url %}
      {% include git-wiki/components/logo/logo.html %}
      {% else %}
      <h1>{{ site.title | escape }}</h1>
      {% endif %}
    </div>


    {% if site.github.is_user_page %}
    <p class="view"><a href="{{ site.github.owner_url }}">View My GitHub Profile</a></p>
    {% endif %}

    {% if site.show_downloads %}
    {% include git-wiki/components/action_btn/downloads.html %}
    {% endif %}

    {% if site.show_wiki_pages %}
    {% include git-wiki/components/lists/page-list.html %}
    {% endif %}

    {% if site.blog_feature and site.show_wiki_posts %}
    {% include git-wiki/components/lists/post-list.html %}
    {% endif %}

    {% if site.inc_after_header %}
    {% include {{ site.inc_after_header }} %}
    {% endif %}
  </div>
</header>
<script>
  function sidebar_toggle() {
    var sidebar = document.getElementById("git-wiki-sidebar");
    if (sidebar.style.display == "block") {
      sidebar.style.display = "none";
      sidebar.style.position = "inherit";
    } else {
      $(sidebar).attr('style', 'display: block;');
    }
  }
</script>



================================================
FILE: _includes/git-wiki/sections/tail/tail.html
================================================
{% if site.inc_before_tail %}
{% include {{ site.inc_before_tail }} %}
{% endif %}

<script src="{{ '/assets/js/scale.fix.js' | relative_url }}"></script>

{% if site.google_analytics %}
<script>
    (function (i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date(); a = s.createElement(o),
        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', '{{ site.google_analytics }}', 'auto');
    ga('send', 'pageview');
</script>
{% endif %}

{% assign items = site.html_pages %}
{% for page in items %}
{% assign url = page.url | relative_url %}
{% assign urls = urls | append: url | append: "," %}
{% endfor %}

<script type="text/javascript">
    $(document).ready(function () {
        $(document.body).checkLinks("{{ urls }}".split(","));
    });
</script>

{% if site.inc_after_tail %}
{% include {{ site.inc_after_tail }} %}
{% endif %}



================================================
FILE: _includes/git-wiki/sections/tools/tools.html
================================================
<div id="tools-buttons" style="width: 100%; text-align: right">
    {% if site.inc_before_tools %}
    {% include {{ site.inc_before_tools }} %}
    {% endif %}

    {% include git-wiki/components/action_btn/page_actions.html %}

    {% include git-wiki/components/search/index.html %}

    {% if site.inc_after_tools %}
    {% include {{ site.inc_after_tools }} %}
    {% endif %}
</div>


================================================
FILE: _layouts/default.html
================================================
---
title: Default
layout: git-wiki-default
---


================================================
FILE: _layouts/git-wiki-404.html
================================================
---
title: Not Found
permalink: /404.html
is_wiki_page: false
---

<!-- redirect to page creator if not exists -->
{% if site.disable_edit != true %}
<script type="text/javascript">
    var filename = window.location.pathname.split('/').pop();
    if (!filename.endsWith(".md"))
        filename+=".md";

    var url = '{{ site.github.repository_url }}/new/{{site.git_branch | escape}}?filename={{ site.wiki_folder | default: 'wiki' }}/'+filename;
    window.location=url;
</script>
{% else %}

Page Not Found

{% endif %}


================================================
FILE: _layouts/git-wiki-blog.html
================================================
---
title: Blog
layout: git-wiki-default
---

<!-- This loops through the paginated posts -->
{% for post in paginator.posts %}
    <div class="post-item">
        <p class="author">
            <span class="date">{{ post.date | date: "%-d %B %Y"}}</span>
        </p>
        <div class="git-wiki-content">
            {{ post.excerpt }}

            <a href="{{ post.url | relative_url }}">...Read all</a>
        </div>
    </div>
    <hr>
{% endfor %}

<!-- Pagination links -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | relative_url }}" class="previous">
      Previous
    </a>
  {% else %}
    <span class="previous">Previous</span>
  {% endif %}
  <span class="page_number ">
    Page: {{ paginator.page }} of {{ paginator.total_pages }}
  </span>
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | relative_url }}" class="next">Next</a>
  {% else %}
    <span class="next ">Next</span>
  {% endif %}
</div>


================================================
FILE: _layouts/git-wiki-bs-github.html
================================================
{% comment %}
#
# This layout uses bootstrap with united theme
#
{% endcomment %}

{% include git-wiki/defines/defines.html %}

<!doctype html>
<html>

<head>
    {% if site.inc_before_head %}
    {% include {{ site.inc_before_head }} %}
    {% endif %}

    {% include git-wiki/sections/head/meta.html %}
    {% include git-wiki/sections/head/scripts.html %}
    {% include git-wiki/sections/head/styles.html %}

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.1.3/united/bootstrap.min.css">
    <link rel="stylesheet" href="{{ '/assets/css/github.css?v=' | append: site.github.build_revision | relative_url }}">

    {% if site.inc_after_head %}
    {% include {{ site.inc_after_head }} %}
    {% endif %}
</head>

<body>
    <div class="wrapper">
        <div class="row">
            <div class="col-lg-9">
                <div class="git-wiki-page">
                    {% include git-wiki/sections/tools/tools.html %}

                    {% include git-wiki/components/toc/toc.html %}

                    {% if site.inc_before_content %}
                    {% include {{ site.inc_before_content }} %}
                    {% endif %}

                    <div id="git-wiki-content">
                        {{ content }}
                    </div>

                    {% if site.inc_after_content %}
                    {% include {{ site.inc_after_content }} %}
                    {% endif %}
                </div>
            </div>
            <div class="col-lg-3">
                {% include git-wiki/sections/header/header.html %}
            </div>
        </div>
        <div class="row">
            <div class="col">
                {% include git-wiki/sections/footer/footer.html %}
            </div>
        </div>
    </div>

    {% include git-wiki/sections/tail/tail.html %}
</body>

</html>


================================================
FILE: _layouts/git-wiki-bs-lux.html
================================================
{% comment %}
#
# This layout uses bootstrap with lux theme
#
{% endcomment %}

{% include git-wiki/defines/defines.html %}

<!doctype html>
<html>

<head>
    {% if site.inc_before_head %}
    {% include {{ site.inc_before_head }} %}
    {% endif %}

    {% include git-wiki/sections/head/meta.html %}
    {% include git-wiki/sections/head/scripts.html %}
    {% include git-wiki/sections/head/styles.html %}

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.1.3/lux/bootstrap.min.css">
    
    {% comment %} Hacky-Fix for lux theme {% endcomment %}
    <style>
        .git-wiki-page {
            padding-left: 0;   
        }
        
        .wrapper .col-lg-3 {
            max-width: 300px;
        }
    </style>

    {% if site.inc_after_head %}
    {% include {{ site.inc_after_head }} %}
    {% endif %}
</head>

<body>
    <div class="wrapper">
        <div class="row">
            <div class="col-lg-3">
                {% include git-wiki/sections/header/header.html %}
            </div>
            <div class="col-lg-9">
                <div class="git-wiki-page">
                    {% include git-wiki/sections/tools/tools.html %}

                    {% include git-wiki/components/toc/toc.html %}

                    {% if site.inc_before_content %}
                    {% include {{ site.inc_before_content }} %}
                    {% endif %}

                    <div id="git-wiki-content">
                        {{ content }}
                    </div>

                    {% if site.inc_after_content %}
                    {% include {{ site.inc_after_content }} %}
                    {% endif %}
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col">
                {% include git-wiki/sections/footer/footer.html %}
            </div>
        </div>
    </div>

    {% include git-wiki/sections/tail/tail.html %}
</body>

</html>



================================================
FILE: _layouts/git-wiki-bs-united.html
================================================
{% comment %}
#
# This layout uses bootstrap with united theme
#
{% endcomment %}

{% include git-wiki/defines/defines.html %}

<!doctype html>
<html>

<head>
    {% if site.inc_before_head %}
    {% include {{ site.inc_before_head }} %}
    {% endif %}

    {% include git-wiki/sections/head/meta.html %}
    {% include git-wiki/sections/head/scripts.html %}
    {% include git-wiki/sections/head/styles.html %}

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.1.3/united/bootstrap.min.css">

    {% if site.inc_after_head %}
    {% include {{ site.inc_after_head }} %}
    {% endif %}
</head>

<body>
    <div class="wrapper">
        <div class="row">
            <div class="col-lg-9">
                <div class="git-wiki-page">
                    {% include git-wiki/sections/tools/tools.html %}

                    {% include git-wiki/components/toc/toc.html %}

                    {% if site.inc_before_content %}
                    {% include {{ site.inc_before_content }} %}
                    {% endif %}

                    <div id="git-wiki-content">
                        {{ content }}
                    </div>

                    {% if site.inc_after_content %}
                    {% include {{ site.inc_after_content }} %}
                    {% endif %}
                </div>
            </div>
            <div class="col-lg-3">
                {% include git-wiki/sections/header/header.html %}
            </div>
        </div>
        <div class="row">
            <div class="col">
                {% include git-wiki/sections/footer/footer.html %}
            </div>
        </div>
    </div>

    {% include git-wiki/sections/tail/tail.html %}
</body>

</html>


================================================
FILE: _layouts/git-wiki-default.html
================================================
{% include git-wiki/defines/defines.html %}

<!doctype html>
<html>
{% include git-wiki/sections/head/head.html %}

{% include git-wiki/sections/content/body.html %}

</html>


================================================
FILE: _layouts/git-wiki-post.html
================================================
---
layout: git-wiki-default
---

<small>{{ page.date | date: "%-d %B %Y" }}</small>
{% if page.author or site.author %}
<p class="view">by {{ page.author | default: site.author }}</p>
{% endif %}

{{content}}


{% if page.tags.size > 0 %}
  <small>tags: <em>{{ page.tags | join: "</em> - <em>" }}</em></small>
{% endif %}


================================================
FILE: _posts/.gitkeep
================================================




================================================
FILE: _sass/fonts.scss
================================================
@font-face {
  font-family: 'Noto Sans';
  font-weight: 400;
  font-style: normal;
  src: url('../fonts/Noto-Sans-regular/Noto-Sans-regular.eot');
  src: url('../fonts/Noto-Sans-regular/Noto-Sans-regular.eot?#iefix') format('embedded-opentype'),
       local('Noto Sans'),
       local('Noto-Sans-regular'),
       url('../fonts/Noto-Sans-regular/Noto-Sans-regular.woff2') format('woff2'),
       url('../fonts/Noto-Sans-regular/Noto-Sans-regular.woff') format('woff'),
       url('../fonts/Noto-Sans-regular/Noto-Sans-regular.ttf') format('truetype'),
       url('../fonts/Noto-Sans-regular/Noto-Sans-regular.svg#NotoSans') format('svg');
}

@font-face {
  font-family: 'Noto Sans';
  font-weight: 700;
  font-style: normal;
  src: url('../fonts/Noto-Sans-700/Noto-Sans-700.eot');
  src: url('../fonts/Noto-Sans-700/Noto-Sans-700.eot?#iefix') format('embedded-opentype'),
       local('Noto Sans Bold'),
       local('Noto-Sans-700'),
       url('../fonts/Noto-Sans-700/Noto-Sans-700.woff2') format('woff2'),
       url('../fonts/Noto-Sans-700/Noto-Sans-700.woff') format('woff'),
       url('../fonts/Noto-Sans-700/Noto-Sans-700.ttf') format('truetype'),
       url('../fonts/Noto-Sans-700/Noto-Sans-700.svg#NotoSans') format('svg');
}

@font-face {
  font-family: 'Noto Sans';
  font-weight: 400;
  font-style: italic;
  src: url('../fonts/Noto-Sans-italic/Noto-Sans-italic.eot');
  src: url('../fonts/Noto-Sans-italic/Noto-Sans-italic.eot?#iefix') format('embedded-opentype'),
       local('Noto Sans Italic'),
       local('Noto-Sans-italic'),
       url('../fonts/Noto-Sans-italic/Noto-Sans-italic.woff2') format('woff2'),
       url('../fonts/Noto-Sans-italic/Noto-Sans-italic.woff') format('woff'),
       url('../fonts/Noto-Sans-italic/Noto-Sans-italic.ttf') format('truetype'),
       url('../fonts/Noto-Sans-italic/Noto-Sans-italic.svg#NotoSans') format('svg');
}

@font-face {
  font-family: 'Noto Sans';
  font-weight: 700;
  font-style: italic;
  src: url('../fonts/Noto-Sans-700italic/Noto-Sans-700italic.eot');
  src: url('../fonts/Noto-Sans-700italic/Noto-Sans-700italic.eot?#iefix') format('embedded-opentype'),
       local('Noto Sans Bold Italic'),
       local('Noto-Sans-700italic'),
       url('../fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff2') format('woff2'),
       url('../fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff') format('woff'),
       url('../fonts/Noto-Sans-700italic/Noto-Sans-700italic.ttf') format('truetype'),
       url('../fonts/Noto-Sans-700italic/Noto-Sans-700italic.svg#NotoSans') format('svg');
}



================================================
FILE: _sass/git-wiki-style.scss
================================================
@import "fonts";
@import "rouge-github";
@import "w3.scss";

body {
  /* background-color: #fff; */
  padding: 50px;
  font: 14px/1.5 "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: #727272;
  font-weight: 400;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  color: #222;
  margin: 0 0 20px;
}

p,
ul,
ol,
table,
pre,
dl {
  margin: 0 0 20px;
}

h1,
h2,
h3 {
  line-height: 1.1;
}

h1 {
  font-size: 28px;
}

h2 {
  color: #393939;
}

h3,
h4,
h5,
h6 {
  color: #494949;
}

a {
  color: #39c;
  text-decoration: none;
}

a:hover {
  color: #069;
}

a small {
  font-size: 11px;
  color: #777;
  margin-top: -0.3em;
  display: block;
}

a:hover small {
  color: #777;
}

.wrapper {
  /*width:860px;*/
  margin: 0 auto;
}

blockquote {
  border-left: 1px solid #e5e5e5;
  margin: 0;
  padding: 0 0 0 20px;
  font-style: italic;
}

code,
pre {
  font-family: Monaco, Bitstream Vera Sans Mono, Lucida Console, Terminal, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
  color: #333;
  font-size: 12px;
}

pre {
  padding: 8px 15px;
  background: #f8f8f8;
  border-radius: 5px;
  border: 1px solid #e5e5e5;
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  text-align: left;
  padding: 5px 10px;
  border-bottom: 1px solid #e5e5e5;
}

dt {
  color: #444;
  font-weight: 700;
}

th {
  color: #444;
}

img {
  max-width: 100%;
}

.w3-teal {
  color: #000 !important;
  background-color: inherit !important;
}

#git-wiki-mobile-header {
  position: fixed;
  top: 0;
  height: 55px;
  background-color: white;
  width: 100%;
  border-bottom: 1px solid;
  border-radius: 10px;
  // z-index: 999; // it breaks the dark mode
}

#git-wiki-sidebar {
  width: 280px !important;
  float: left;
  position: relative !important;
  -webkit-font-smoothing: subpixel-antialiased;
  /*overflow-y: auto;
  overflow-x: auto;*/
  max-height: 100%;
  padding-bottom: 55px !important;
}

@media print,
screen and (max-width: 992px) {
  #git-wiki-sidebar {
    position: fixed !important;
    top: 50px;
    border-right: 1px solid;
    border-bottom: 1px solid;
    border-radius: 10px;
  }

  .git-wiki-page {
    margin-top: 60px;
  }
}

.git-wiki-main-logo {
  max-width: 270px;
}

#git-wiki-sidebar .git-wiki-downloads {
  list-style: none;
  height: 40px;
  padding: 0;
  background: #f4f4f4;
  border-radius: 5px;
  border: 1px solid #e0e0e0;
  width: 270px;
}

#git-wiki-sidebar .git-wiki-downloads li {
  width: 89px;
  float: left;
  border-right: 1px solid #e0e0e0;
  height: 40px;
}

#git-wiki-sidebar .git-wiki-downloads li:first-child a {
  border-radius: 5px 0 0 5px;
}

#git-wiki-sidebar .git-wiki-downloads li:last-child a {
  border-radius: 0 5px 5px 0;
}

#git-wiki-sidebar .git-wiki-downloads a {
  line-height: 1;
  font-size: 11px;
  color: #999;
  display: block;
  text-align: center;
  padding-top: 6px;
  height: 34px;
}

#git-wiki-sidebar .git-wiki-downloads a:hover {
  color: #999;
}

#git-wiki-sidebar .git-wiki-downloads a:active {
  background-color: #f0f0f0;
}

strong {
  color: #222;
  font-weight: 700;
}

#git-wiki-sidebar .git-wiki-downloads li+li+li {
  border-right: none;
  width: 89px;
}

#git-wiki-sidebar .git-wiki-downloads a strong {
  font-size: 14px;
  display: block;
  color: #222;
}

.git-wiki-page {
  /*width:500px;
  float:right;*/
  padding-left: 320px;
  padding-bottom: 50px;
}

small {
  font-size: 11px;
}

hr {
  border: 0;
  background: #e5e5e5;
  height: 1px;
  margin: 0 0 20px;
}

footer {
  padding-left: 320px;
  float: left;
  bottom: 50px;
  -webkit-font-smoothing: subpixel-antialiased;
}

.tools-element {
  border-left: aqua;
  border-left-style: solid;
  padding-left: 10px;
  padding-right: 10px;
}

@media print,
screen and (max-width: 960px) {

  div.wrapper {
    width: auto;
    margin: 0;
  }

  #git-wiki-sidebar,
  .git-wiki-page,
  footer {
    float: none;
    position: static;
    width: auto;
  }

  #git-wiki-sidebar {
    padding-right: 320px;
  }

  .git-wiki-page,
  footer {
    border: 1px solid #e5e5e5;
    border-width: 1px 0;
    padding: 20px 0;
    margin: 60px 0 20px;
  }

  #git-wiki-sidebara small {
    display: inline;
  }

  /*#git-wiki-sidebar .git-wiki-downloads {
    position:absolute;
    right:50px;
    top:52px;
  }*/
}


@media print,
screen and (max-width: 720px) {
  body {
    word-wrap: break-word;
  }

  #git-wiki-sidebar {
    padding: 0;
  }

  #git-wiki-sidebar .git-wiki-downloads,
  #git-wiki-sidebarp.view {
    position: static;
  }

  pre,
  code {
    word-wrap: normal;
  }
}

@media print,
screen and (max-width: 480px) {
  body {
    padding: 15px;
  }

  #git-wiki-sidebar .git-wiki-downloads {
    width: 99%;
  }

  #git-wiki-sidebarli,
  #git-wiki-sidebar .git-wiki-downloads li+li+li {
    width: 33%;
  }
}

@media print {
  body {
    padding: 0.4in;
    font-size: 12pt;
    color: #444;
  }
}

/*
  Pagination rules
*/

.pagination a,
.pagination span {
  padding: 7px 18px;
  border: 1px solid #eee;
  margin-left: -2px;
  margin-right: -2px;
  background-color: #ffffff;
  display: inline-block;
}

.pagination a {
  &:hover {
    background-color: #f1f1f1;
    color: #333;
  }
}

.pagination {
  text-align: center;
}

.post-item {
  margin-bottom: 50px;
}

#results-container li {
  list-style-type: none;
}

.external-link {
  background-position: center right;
  background-repeat: no-repeat;
  background-image: url("../images/external-link-ltr-icon.png");
  background-image: linear-gradient(transparent, transparent), url("../images/external.svg");
  padding-right: 13px;
}


/* 
  dark mode
  https://darkmodejs.learn.uno/#debug 
*/
.darkmode-layer, .darkmode-toggle {
  z-index: 500;
}

/* disable dark mode on images */
body.darkmode--activated img, body.darkmode--activated .darkmode-ignore {
  mix-blend-mode: difference;
}


================================================
FILE: _sass/rouge-github.scss
================================================
.highlight table td { padding: 5px; }
.highlight table pre { margin: 0; }
.highlight .cm {
  color: #999988;
  font-style: italic;
}
.highlight .cp {
  color: #999999;
  font-weight: bold;
}
.highlight .c1 {
  color: #999988;
  font-style: italic;
}
.highlight .cs {
  color: #999999;
  font-weight: bold;
  font-style: italic;
}
.highlight .c, .highlight .cd {
  color: #999988;
  font-style: italic;
}
.highlight .err {
  color: #a61717;
  background-color: #e3d2d2;
}
.highlight .gd {
  color: #000000;
  background-color: #ffdddd;
}
.highlight .ge {
  color: #000000;
  font-style: italic;
}
.highlight .gr {
  color: #aa0000;
}
.highlight .gh {
  color: #999999;
}
.highlight .gi {
  color: #000000;
  background-color: #ddffdd;
}
.highlight .go {
  color: #888888;
}
.highlight .gp {
  color: #555555;
}
.highlight .gs {
  font-weight: bold;
}
.highlight .gu {
  color: #aaaaaa;
}
.highlight .gt {
  color: #aa0000;
}
.highlight .kc {
  color: #000000;
  font-weight: bold;
}
.highlight .kd {
  color: #000000;
  font-weight: bold;
}
.highlight .kn {
  color: #000000;
  font-weight: bold;
}
.highlight .kp {
  color: #000000;
  font-weight: bold;
}
.highlight .kr {
  color: #000000;
  font-weight: bold;
}
.highlight .kt {
  color: #445588;
  font-weight: bold;
}
.highlight .k, .highlight .kv {
  color: #000000;
  font-weight: bold;
}
.highlight .mf {
  color: #009999;
}
.highlight .mh {
  color: #009999;
}
.highlight .il {
  color: #009999;
}
.highlight .mi {
  color: #009999;
}
.highlight .mo {
  color: #009999;
}
.highlight .m, .highlight .mb, .highlight .mx {
  color: #009999;
}
.highlight .sb {
  color: #d14;
}
.highlight .sc {
  color: #d14;
}
.highlight .sd {
  color: #d14;
}
.highlight .s2 {
  color: #d14;
}
.highlight .se {
  color: #d14;
}
.highlight .sh {
  color: #d14;
}
.highlight .si {
  color: #d14;
}
.highlight .sx {
  color: #d14;
}
.highlight .sr {
  color: #009926;
}
.highlight .s1 {
  color: #d14;
}
.highlight .ss {
  color: #990073;
}
.highlight .s {
  color: #d14;
}
.highlight .na {
  color: #008080;
}
.highlight .bp {
  color: #999999;
}
.highlight .nb {
  color: #0086B3;
}
.highlight .nc {
  color: #445588;
  font-weight: bold;
}
.highlight .no {
  color: #008080;
}
.highlight .nd {
  color: #3c5d5d;
  font-weight: bold;
}
.highlight .ni {
  color: #800080;
}
.highlight .ne {
  color: #990000;
  font-weight: bold;
}
.highlight .nf {
  color: #990000;
  font-weight: bold;
}
.highlight .nl {
  color: #990000;
  font-weight: bold;
}
.highlight .nn {
  color: #555555;
}
.highlight .nt {
  color: #000080;
}
.highlight .vc {
  color: #008080;
}
.highlight .vg {
  color: #008080;
}
.highlight .vi {
  color: #008080;
}
.highlight .nv {
  color: #008080;
}
.highlight .ow {
  color: #000000;
  font-weight: bold;
}
.highlight .o {
  color: #000000;
  font-weight: bold;
}
.highlight .w {
  color: #bbbbbb;
}
.highlight {
  background-color: #f8f8f8;
}



================================================
FILE: _sass/w3.scss
================================================
﻿/* W3.CSS 4.12 Novemberr 2018 by Jan Egil and Borge Refsnes */
html{box-sizing:border-box}*,*:before,*:after{box-sizing:inherit}
/* Extract from normalize.css by Nicolas Gallagher and Jonathan Neal git.io/normalize */
html{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}
article,aside,details,figcaption,figure,footer,header,main,menu,nav,section,summary{display:block}
audio,canvas,progress,video{display:inline-block}progress{vertical-align:baseline}
audio:not([controls]){display:none;height:0}[hidden],template{display:none}
a{background-color:transparent;-webkit-text-decoration-skip:objects}
a:active,a:hover{outline-width:0}abbr[title]{border-bottom:none;text-decoration:underline;text-decoration:underline dotted}
dfn{font-style:italic}mark{background:#ff0;color:#000}
small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}
sub{bottom:-0.25em}sup{top:-0.5em}figure{margin:1em 40px}img{border-style:none}svg:not(:root){overflow:hidden}
code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}hr{box-sizing:content-box;height:0;overflow:visible}
button,input,select,textarea{font:inherit;margin:0}optgroup{font-weight:bold}
button,input{overflow:visible}button,select{text-transform:none}
button,html [type=button],[type=reset],[type=submit]{-webkit-appearance:button}
button::-moz-focus-inner, [type=button]::-moz-focus-inner, [type=reset]::-moz-focus-inner, [type=submit]::-moz-focus-inner{border-style:none;padding:0}
button:-moz-focusring, [type=button]:-moz-focusring, [type=reset]:-moz-focusring, [type=submit]:-moz-focusring{outline:1px dotted ButtonText}
fieldset{border:1px solid #c0c0c0;margin:0 2px;padding:.35em .625em .75em}
legend{color:inherit;display:table;max-width:100%;padding:0;white-space:normal}textarea{overflow:auto}
[type=checkbox],[type=radio]{padding:0}
[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}
[type=search]{-webkit-appearance:textfield;outline-offset:-2px}
[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}
::-webkit-input-placeholder{color:inherit;opacity:0.54}
::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}
/* End extract */
html,body{font-family:Verdana,sans-serif;font-size:15px;line-height:1.5}html{overflow-x:hidden}
h1{font-size:36px}h2{font-size:30px}h3{font-size:24px}h4{font-size:20px}h5{font-size:18px}h6{font-size:16px}.w3-serif{font-family:serif}
h1,h2,h3,h4,h5,h6{font-family:"Segoe UI",Arial,sans-serif;font-weight:400;margin:10px 0}.w3-wide{letter-spacing:4px}
hr{border:0;border-top:1px solid #eee;margin:20px 0}
.w3-image{max-width:100%;height:auto}img{vertical-align:middle}a{color:inherit}
.w3-table,.w3-table-all{border-collapse:collapse;border-spacing:0;width:100%;display:table}.w3-table-all{border:1px solid #ccc}
.w3-bordered tr,.w3-table-all tr{border-bottom:1px solid #ddd}.w3-striped tbody tr:nth-child(even){background-color:#f1f1f1}
.w3-table-all tr:nth-child(odd){background-color:#fff}.w3-table-all tr:nth-child(even){background-color:#f1f1f1}
.w3-hoverable tbody tr:hover,.w3-ul.w3-hoverable li:hover{background-color:#ccc}.w3-centered tr th,.w3-centered tr td{text-align:center}
.w3-table td,.w3-table th,.w3-table-all td,.w3-table-all th{padding:8px 8px;display:table-cell;text-align:left;vertical-align:top}
.w3-table th:first-child,.w3-table td:first-child,.w3-table-all th:first-child,.w3-table-all td:first-child{padding-left:16px}
.w3-btn,.w3-button{border:none;display:inline-block;padding:8px 16px;vertical-align:middle;overflow:hidden;text-decoration:none;color:inherit;background-color:inherit;text-align:center;cursor:pointer;white-space:nowrap}
.w3-btn:hover{box-shadow:0 8px 16px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19)}
.w3-btn,.w3-button{-webkit-touch-callout:none;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}   
.w3-disabled,.w3-btn:disabled,.w3-button:disabled{cursor:not-allowed;opacity:0.3}.w3-disabled *,:disabled *{pointer-events:none}
.w3-btn.w3-disabled:hover,.w3-btn:disabled:hover{box-shadow:none}
.w3-badge,.w3-tag{background-color:#000;color:#fff;display:inline-block;padding-left:8px;padding-right:8px;text-align:center}.w3-badge{border-radius:50%}
.w3-ul{list-style-type:none;padding:0;margin:0}.w3-ul li{padding:8px 16px;border-bottom:1px solid #ddd}.w3-ul li:last-child{border-bottom:none}
.w3-tooltip,.w3-display-container{position:relative}.w3-tooltip .w3-text{display:none}.w3-tooltip:hover .w3-text{display:inline-block}
.w3-ripple:active{opacity:0.5}.w3-ripple{transition:opacity 0s}
.w3-input{padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:100%}
.w3-select{padding:9px 0;width:100%;border:none;border-bottom:1px solid #ccc}
.w3-dropdown-click,.w3-dropdown-hover{position:relative;display:inline-block;cursor:pointer}
.w3-dropdown-hover:hover .w3-dropdown-content{display:block}
.w3-dropdown-hover:first-child,.w3-dropdown-click:hover{background-color:#ccc;color:#000}
.w3-dropdown-hover:hover > .w3-button:first-child,.w3-dropdown-click:hover > .w3-button:first-child{background-color:#ccc;color:#000}
.w3-dropdown-content{cursor:auto;color:#000;background-color:#fff;display:none;position:absolute;min-width:160px;margin:0;padding:0;z-index:1}
.w3-check,.w3-radio{width:24px;height:24px;position:relative;top:6px}
.w3-sidebar{height:100%;width:200px;background-color:#fff;position:fixed!important;z-index:1;overflow:auto}
.w3-bar-block .w3-dropdown-hover,.w3-bar-block .w3-dropdown-click{width:100%}
.w3-bar-block .w3-dropdown-hover .w3-dropdown-content,.w3-bar-block .w3-dropdown-click .w3-dropdown-content{min-width:100%}
.w3-bar-block .w3-dropdown-hover .w3-button,.w3-bar-block .w3-dropdown-click .w3-button{width:100%;text-align:left;padding:8px 16px}
.w3-main,#main{transition:margin-left .4s}
.w3-modal{z-index:3;display:none;padding-top:100px;position:fixed;left:0;top:0;width:100%;height:100%;overflow:auto;background-color:rgb(0,0,0);background-color:rgba(0,0,0,0.4)}
.w3-modal-content{margin:auto;background-color:#fff;position:relative;padding:0;outline:0;width:600px}
.w3-bar{width:100%;overflow:hidden}.w3-center .w3-bar{display:inline-block;width:auto}
.w3-bar .w3-bar-item{padding:8px 16px;float:left;width:auto;border:none;display:block;outline:0}
.w3-bar .w3-dropdown-hover,.w3-bar .w3-dropdown-click{position:static;float:left}
.w3-bar .w3-button{white-space:normal}
.w3-bar-block .w3-bar-item{width:100%;display:block;padding:8px 16px;text-align:left;border:none;white-space:normal;float:none;outline:0}
.w3-bar-block.w3-center .w3-bar-item{text-align:center}.w3-block{display:block;width:100%}
.w3-responsive{display:block;overflow-x:auto}
.w3-container:after,.w3-container:before,.w3-panel:after,.w3-panel:before,.w3-row:after,.w3-row:before,.w3-row-padding:after,.w3-row-padding:before,
.w3-cell-row:before,.w3-cell-row:after,.w3-clear:after,.w3-clear:before,.w3-bar:before,.w3-bar:after{content:"";display:table;clear:both}
.w3-col,.w3-half,.w3-third,.w3-twothird,.w3-threequarter,.w3-quarter{float:left;width:100%}
.w3-col.s1{width:8.33333%}.w3-col.s2{width:16.66666%}.w3-col.s3{width:24.99999%}.w3-col.s4{width:33.33333%}
.w3-col.s5{width:41.66666%}.w3-col.s6{width:49.99999%}.w3-col.s7{width:58.33333%}.w3-col.s8{width:66.66666%}
.w3-col.s9{width:74.99999%}.w3-col.s10{width:83.33333%}.w3-col.s11{width:91.66666%}.w3-col.s12{width:99.99999%}
@media (min-width:601px){.w3-col.m1{width:8.33333%}.w3-col.m2{width:16.66666%}.w3-col.m3,.w3-quarter{width:24.99999%}.w3-col.m4,.w3-third{width:33.33333%}
.w3-col.m5{width:41.66666%}.w3-col.m6,.w3-half{width:49.99999%}.w3-col.m7{width:58.33333%}.w3-col.m8,.w3-twothird{width:66.66666%}
.w3-col.m9,.w3-threequarter{width:74.99999%}.w3-col.m10{width:83.33333%}.w3-col.m11{width:91.66666%}.w3-col.m12{width:99.99999%}}
@media (min-width:993px){.w3-col.l1{width:8.33333%}.w3-col.l2{width:16.66666%}.w3-col.l3{width:24.99999%}.w3-col.l4{width:33.33333%}
.w3-col.l5{width:41.66666%}.w3-col.l6{width:49.99999%}.w3-col.l7{width:58.33333%}.w3-col.l8{width:66.66666%}
.w3-col.l9{width:74.99999%}.w3-col.l10{width:83.33333%}.w3-col.l11{width:91.66666%}.w3-col.l12{width:99.99999%}}
.w3-rest{overflow:hidden}.w3-stretch{margin-left:-16px;margin-right:-16px}
.w3-content,.w3-auto{margin-left:auto;margin-right:auto}.w3-content{max-width:980px}.w3-auto{max-width:1140px}
.w3-cell-row{display:table;width:100%}.w3-cell{display:table-cell}
.w3-cell-top{vertical-align:top}.w3-cell-middle{vertical-align:middle}.w3-cell-bottom{vertical-align:bottom}
.w3-hide{display:none!important}.w3-show-block,.w3-show{display:block!important}.w3-show-inline-block{display:inline-block!important}
@media (max-width:1205px){.w3-auto{max-width:95%}}
@media (max-width:600px){.w3-modal-content{margin:0 10px;width:auto!important}.w3-modal{padding-top:30px}
.w3-dropdown-hover.w3-mobile .w3-dropdown-content,.w3-dropdown-click.w3-mobile .w3-dropdown-content{position:relative}	
.w3-hide-small{display:none!important}.w3-mobile{display:block;width:100%!important}.w3-bar-item.w3-mobile,.w3-dropdown-hover.w3-mobile,.w3-dropdown-click.w3-mobile{text-align:center}
.w3-dropdown-hover.w3-mobile,.w3-dropdown-hover.w3-mobile .w3-btn,.w3-dropdown-hover.w3-mobile .w3-button,.w3-dropdown-click.w3-mobile,.w3-dropdown-click.w3-mobile .w3-btn,.w3-dropdown-click.w3-mobile .w3-button{width:100%}}
@media (max-width:768px){.w3-modal-content{width:500px}.w3-modal{padding-top:50px}}
@media (min-width:993px){.w3-modal-content{width:900px}.w3-hide-large{display:none!important}.w3-sidebar.w3-collapse{display:block!important}}
@media (max-width:992px) and (min-width:601px){.w3-hide-medium{display:none!important}}
@media (max-width:992px){.w3-sidebar.w3-collapse{display:none}.w3-main{margin-left:0!important;margin-right:0!important}.w3-auto{max-width:100%}}
.w3-top,.w3-bottom{position:fixed;width:100%;z-index:1}.w3-top{top:0}.w3-bottom{bottom:0}
.w3-overlay{position:fixed;display:none;width:100%;height:100%;top:0;left:0;right:0;bottom:0;background-color:rgba(0,0,0,0.5);z-index:2}
.w3-display-topleft{position:absolute;left:0;top:0}.w3-display-topright{position:absolute;right:0;top:0}
.w3-display-bottomleft{position:absolute;left:0;bottom:0}.w3-display-bottomright{position:absolute;right:0;bottom:0}
.w3-display-middle{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);-ms-transform:translate(-50%,-50%)}
.w3-display-left{position:absolute;top:50%;left:0%;transform:translate(0%,-50%);-ms-transform:translate(-0%,-50%)}
.w3-display-right{position:absolute;top:50%;right:0%;transform:translate(0%,-50%);-ms-transform:translate(0%,-50%)}
.w3-display-topmiddle{position:absolute;left:50%;top:0;transform:translate(-50%,0%);-ms-transform:translate(-50%,0%)}
.w3-display-bottommiddle{position:absolute;left:50%;bottom:0;transform:translate(-50%,0%);-ms-transform:translate(-50%,0%)}
.w3-display-container:hover .w3-display-hover{display:block}.w3-display-container:hover span.w3-display-hover{display:inline-block}.w3-display-hover{display:none}
.w3-display-position{position:absolute}
.w3-circle{border-radius:50%}
.w3-round-small{border-radius:2px}.w3-round,.w3-round-medium{border-radius:4px}.w3-round-large{border-radius:8px}.w3-round-xlarge{border-radius:16px}.w3-round-xxlarge{border-radius:32px}
.w3-row-padding,.w3-row-padding>.w3-half,.w3-row-padding>.w3-third,.w3-row-padding>.w3-twothird,.w3-row-padding>.w3-threequarter,.w3-row-padding>.w3-quarter,.w3-row-padding>.w3-col{padding:0 8px}
.w3-container,.w3-panel{padding:0.01em 16px}.w3-panel{margin-top:16px;margin-bottom:16px}
.w3-code,.w3-codespan{font-family:Consolas,"courier new";font-size:16px}
.w3-code{width:auto;background-color:#fff;padding:8px 12px;border-left:4px solid #4CAF50;word-wrap:break-word}
.w3-codespan{color:crimson;background-color:#f1f1f1;padding-left:4px;padding-right:4px;font-size:110%}
.w3-card,.w3-card-2{box-shadow:0 2px 5px 0 rgba(0,0,0,0.16),0 2px 10px 0 rgba(0,0,0,0.12)}
.w3-card-4,.w3-hover-shadow:hover{box-shadow:0 4px 10px 0 rgba(0,0,0,0.2),0 4px 20px 0 rgba(0,0,0,0.19)}
.w3-spin{animation:w3-spin 2s infinite linear}@keyframes w3-spin{0%{transform:rotate(0deg)}100%{transform:rotate(359deg)}}
.w3-animate-fading{animation:fading 10s infinite}@keyframes fading{0%{opacity:0}50%{opacity:1}100%{opacity:0}}
.w3-animate-opacity{animation:opac 0.8s}@keyframes opac{from{opacity:0} to{opacity:1}}
.w3-animate-top{position:relative;animation:animatetop 0.4s}@keyframes animatetop{from{top:-300px;opacity:0} to{top:0;opacity:1}}
.w3-animate-left{position:relative;animation:animateleft 0.4s}@keyframes animateleft{from{left:-300px;opacity:0} to{left:0;opacity:1}}
.w3-animate-right{position:relative;animation:animateright 0.4s}@keyframes animateright{from{right:-300px;opacity:0} to{right:0;opacity:1}}
.w3-animate-bottom{position:relative;animation:animatebottom 0.4s}@keyframes animatebottom{from{bottom:-300px;opacity:0} to{bottom:0;opacity:1}}
.w3-animate-zoom {animation:animatezoom 0.6s}@keyframes animatezoom{from{transform:scale(0)} to{transform:scale(1)}}
.w3-animate-input{transition:width 0.4s ease-in-out}.w3-animate-input:focus{width:100%!important}
.w3-opacity,.w3-hover-opacity:hover{opacity:0.60}.w3-opacity-off,.w3-hover-opacity-off:hover{opacity:1}
.w3-opacity-max{opacity:0.25}.w3-opacity-min{opacity:0.75}
.w3-greyscale-max,.w3-grayscale-max,.w3-hover-greyscale:hover,.w3-hover-grayscale:hover{filter:grayscale(100%)}
.w3-greyscale,.w3-grayscale{filter:grayscale(75%)}.w3-greyscale-min,.w3-grayscale-min{filter:grayscale(50%)}
.w3-sepia{filter:sepia(75%)}.w3-sepia-max,.w3-hover-sepia:hover{filter:sepia(100%)}.w3-sepia-min{filter:sepia(50%)}
.w3-tiny{font-size:10px!important}.w3-small{font-size:12px!important}.w3-medium{font-size:15px!important}.w3-large{font-size:18px!important}
.w3-xlarge{font-size:24px!important}.w3-xxlarge{font-size:36px!important}.w3-xxxlarge{font-size:48px!important}.w3-jumbo{font-size:64px!important}
.w3-left-align{text-align:left!important}.w3-right-align{text-align:right!important}.w3-justify{text-align:justify!important}.w3-center{text-align:center!important}
.w3-border-0{border:0!important}.w3-border{border:1px solid #ccc!important}
.w3-border-top{border-top:1px solid #ccc!important}.w3-border-bottom{border-bottom:1px solid #ccc!important}
.w3-border-left{border-left:1px solid #ccc!important}.w3-border-right{border-right:1px solid #ccc!important}
.w3-topbar{border-top:6px solid #ccc!important}.w3-bottombar{border-bottom:6px solid #ccc!important}
.w3-leftbar{border-left:6px solid #ccc!important}.w3-rightbar{border-right:6px solid #ccc!important}
.w3-section,.w3-code{margin-top:16px!important;margin-bottom:16px!important}
.w3-margin{margin:16px!important}.w3-margin-top{margin-top:16px!important}.w3-margin-bottom{margin-bottom:16px!important}
.w3-margin-left{margin-left:16px!important}.w3-margin-right{margin-right:16px!important}
.w3-padding-small{padding:4px 8px!important}.w3-padding{padding:8px 16px!important}.w3-padding-large{padding:12px 24px!important}
.w3-padding-16{padding-top:16px!important;padding-bottom:16px!important}.w3-padding-24{padding-top:24px!important;padding-bottom:24px!important}
.w3-padding-32{padding-top:32px!important;padding-bottom:32px!important}.w3-padding-48{padding-top:48px!important;padding-bottom:48px!important}
.w3-padding-64{padding-top:64px!important;padding-bottom:64px!important}
.w3-left{float:left!important}.w3-right{float:right!important}
.w3-button:hover{color:#000!important;background-color:#ccc!important}
.w3-transparent,.w3-hover-none:hover{background-color:transparent!important}
.w3-hover-none:hover{box-shadow:none!important}
/* Colors */
.w3-amber,.w3-hover-amber:hover{color:#000!important;background-color:#ffc107!important}
.w3-aqua,.w3-hover-aqua:hover{color:#000!important;background-color:#00ffff!important}
.w3-blue,.w3-hover-blue:hover{color:#fff!important;background-color:#2196F3!important}
.w3-light-blue,.w3-hover-light-blue:hover{color:#000!important;background-color:#87CEEB!important}
.w3-brown,.w3-hover-brown:hover{color:#fff!important;background-color:#795548!important}
.w3-cyan,.w3-hover-cyan:hover{color:#000!important;background-color:#00bcd4!important}
.w3-blue-grey,.w3-hover-blue-grey:hover,.w3-blue-gray,.w3-hover-blue-gray:hover{color:#fff!important;background-color:#607d8b!important}
.w3-green,.w3-hover-green:hover{color:#fff!important;background-color:#4CAF50!important}
.w3-light-green,.w3-hover-light-green:hover{color:#000!important;background-color:#8bc34a!important}
.w3-indigo,.w3-hover-indigo:hover{color:#fff!important;background-color:#3f51b5!important}
.w3-khaki,.w3-hover-khaki:hover{color:#000!important;background-color:#f0e68c!important}
.w3-lime,.w3-hover-lime:hover{color:#000!important;background-color:#cddc39!important}
.w3-orange,.w3-hover-orange:hover{color:#000!important;background-color:#ff9800!important}
.w3-deep-orange,.w3-hover-deep-orange:hover{color:#fff!important;background-color:#ff5722!important}
.w3-pink,.w3-hover-pink:hover{color:#fff!important;background-color:#e91e63!important}
.w3-purple,.w3-hover-purple:hover{color:#fff!important;background-color:#9c27b0!important}
.w3-deep-purple,.w3-hover-deep-purple:hover{color:#fff!important;background-color:#673ab7!important}
.w3-red,.w3-hover-red:hover{color:#fff!important;background-color:#f44336!important}
.w3-sand,.w3-hover-sand:hover{color:#000!important;background-color:#fdf5e6!important}
.w3-teal,.w3-hover-teal:hover{color:#fff!important;background-color:#009688!important}
.w3-yellow,.w3-hover-yellow:hover{color:#000!important;background-color:#ffeb3b!important}
.w3-white,.w3-hover-white:hover{color:#000!important;background-color:#fff!important}
.w3-black,.w3-hover-black:hover{color:#fff!important;background-color:#000!important}
.w3-grey,.w3-hover-grey:hover,.w3-gray,.w3-hover-gray:hover{color:#000!important;background-color:#9e9e9e!important}
.w3-light-grey,.w3-hover-light-grey:hover,.w3-light-gray,.w3-hover-light-gray:hover{color:#000!important;background-color:#f1f1f1!important}
.w3-dark-grey,.w3-hover-dark-grey:hover,.w3-dark-gray,.w3-hover-dark-gray:hover{color:#fff!important;background-color:#616161!important}
.w3-pale-red,.w3-hover-pale-red:hover{color:#000!important;background-color:#ffdddd!important}
.w3-pale-green,.w3-hover-pale-green:hover{color:#000!important;background-color:#ddffdd!important}
.w3-pale-yellow,.w3-hover-pale-yellow:hover{color:#000!important;background-color:#ffffcc!important}
.w3-pale-blue,.w3-hover-pale-blue:hover{color:#000!important;background-color:#ddffff!important}
.w3-text-amber,.w3-hover-text-amber:hover{color:#ffc107!important}
.w3-text-aqua,.w3-hover-text-aqua:hover{color:#00ffff!important}
.w3-text-blue,.w3-hover-text-blue:hover{color:#2196F3!important}
.w3-text-light-blue,.w3-hover-text-light-blue:hover{color:#87CEEB!important}
.w3-text-brown,.w3-hover-text-brown:hover{color:#795548!important}
.w3-text-cyan,.w3-hover-text-cyan:hover{color:#00bcd4!important}
.w3-text-blue-grey,.w3-hover-text-blue-grey:hover,.w3-text-blue-gray,.w3-hover-text-blue-gray:hover{color:#607d8b!important}
.w3-text-green,.w3-hover-text-green:hover{color:#4CAF50!important}
.w3-text-light-green,.w3-hover-text-light-green:hover{color:#8bc34a!important}
.w3-text-indigo,.w3-hover-text-indigo:hover{color:#3f51b5!important}
.w3-text-khaki,.w3-hover-text-khaki:hover{color:#b4aa50!important}
.w3-text-lime,.w3-hover-text-lime:hover{color:#cddc39!important}
.w3-text-orange,.w3-hover-text-orange:hover{color:#ff9800!important}
.w3-text-deep-orange,.w3-hover-text-deep-orange:hover{color:#ff5722!important}
.w3-text-pink,.w3-hover-text-pink:hover{color:#e91e63!important}
.w3-text-purple,.w3-hover-text-purple:hover{color:#9c27b0!important}
.w3-text-deep-purple,.w3-hover-text-deep-purple:hover{color:#673ab7!important}
.w3-text-red,.w3-hover-text-red:hover{color:#f44336!important}
.w3-text-sand,.w3-hover-text-sand:hover{color:#fdf5e6!important}
.w3-text-teal,.w3-hover-text-teal:hover{color:#009688!important}
.w3-text-yellow,.w3-hover-text-yellow:hover{color:#d2be0e!important}
.w3-text-white,.w3-hover-text-white:hover{color:#fff!important}
.w3-text-black,.w3-hover-text-black:hover{color:#000!important}
.w3-text-grey,.w3-hover-text-grey:hover,.w3-text-gray,.w3-hover-text-gray:hover{color:#757575!important}
.w3-text-light-grey,.w3-hover-text-light-grey:hover,.w3-text-light-gray,.w3-hover-text-light-gray:hover{color:#f1f1f1!important}
.w3-text-dark-grey,.w3-hover-text-dark-grey:hover,.w3-text-dark-gray,.w3-hover-text-dark-gray:hover{color:#3a3a3a!important}
.w3-border-amber,.w3-hover-border-amber:hover{border-color:#ffc107!important}
.w3-border-aqua,.w3-hover-border-aqua:hover{border-color:#00ffff!important}
.w3-border-blue,.w3-hover-border-blue:hover{border-color:#2196F3!important}
.w3-border-light-blue,.w3-hover-border-light-blue:hover{border-color:#87CEEB!important}
.w3-border-brown,.w3-hover-border-brown:hover{border-color:#795548!important}
.w3-border-cyan,.w3-hover-border-cyan:hover{border-color:#00bcd4!important}
.w3-border-blue-grey,.w3-hover-border-blue-grey:hover,.w3-border-blue-gray,.w3-hover-border-blue-gray:hover{border-color:#607d8b!important}
.w3-border-green,.w3-hover-border-green:hover{border-color:#4CAF50!important}
.w3-border-light-green,.w3-hover-border-light-green:hover{border-color:#8bc34a!important}
.w3-border-indigo,.w3-hover-border-indigo:hover{border-color:#3f51b5!important}
.w3-border-khaki,.w3-hover-border-khaki:hover{border-color:#f0e68c!important}
.w3-border-lime,.w3-hover-border-lime:hover{border-color:#cddc39!important}
.w3-border-orange,.w3-hover-border-orange:hover{border-color:#ff9800!important}
.w3-border-deep-orange,.w3-hover-border-deep-orange:hover{border-color:#ff5722!important}
.w3-border-pink,.w3-hover-border-pink:hover{border-color:#e91e63!important}
.w3-border-purple,.w3-hover-border-purple:hover{border-color:#9c27b0!important}
.w3-border-deep-purple,.w3-hover-border-deep-purple:hover{border-color:#673ab7!important}
.w3-border-red,.w3-hover-border-red:hover{border-color:#f44336!important}
.w3-border-sand,.w3-hover-border-sand:hover{border-color:#fdf5e6!important}
.w3-border-teal,.w3-hover-border-teal:hover{border-color:#009688!important}
.w3-border-yellow,.w3-hover-border-yellow:hover{border-color:#ffeb3b!important}
.w3-border-white,.w3-hover-border-white:hover{border-color:#fff!important}
.w3-border-black,.w3-hover-border-black:hover{border-color:#000!important}
.w3-border-grey,.w3-hover-border-grey:hover,.w3-border-gray,.w3-hover-border-gray:hover{border-color:#9e9e9e!important}
.w3-border-light-grey,.w3-hover-border-light-grey:hover,.w3-border-light-gray,.w3-hover-border-light-gray:hover{border-color:#f1f1f1!important}
.w3-border-dark-grey,.w3-hover-border-dark-grey:hover,.w3-border-dark-gray,.w3-hover-border-dark-gray:hover{border-color:#616161!important}
.w3-border-pale-red,.w3-hover-border-pale-red:hover{border-color:#ffe7e7!important}.w3-border-pale-green,.w3-hover-border-pale-green:hover{border-color:#e7ffe7!important}
.w3-border-pale-yellow,.w3-hover-border-pale-yellow:hover{border-color:#ffffcc!important}.w3-border-pale-blue,.w3-hover-border-pale-blue:hover{border-color:#e7ffff!important}


================================================
FILE: assets/404.html
================================================
---
layout: git-wiki-404
permalink: /404.html
is_wiki_page: false
---

<!--- this file is needed for automatic creation of non existent pages --->



================================================
FILE: assets/sitemap_full.xml
================================================
---
layout: none
sitemap: false
is_wiki_page: false
permalink: /sitemap_full.xml
---
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
{% if site.search_engine == "js_rss" %}
	<title>{{ site.name | xml_escape }}</title>
	<description>{{ site.description | xml_escape }}</description>
	<link>{{ site.url }}</link>
	<atom:link href="{{ site.url }}/search.xml" rel="self" type="application/rss+xml" />
	{% for post in site.posts %}
		{% if post.published != false %}
		<item>
			<title>{{ post.title | xml_escape }}</title>
			<description>{{ post.content | xml_escape }}</description>
			<pubDate>{{ post.date | date: "%a, %d %b %Y %H:%M:%S %z" }}</pubDate>
			<link>{{site.url}}{{ post.url | relative_url }}</link>
			<guid isPermaLink="true">{{site.url}}{{ post.url | relative_url }}</guid>
		</item>
		{% endif %}
	{% endfor %}
	{% for post in site.pages %}
		{% if post.layout != "null" %}
			{% if post.sitemap != false %}
			<item>
				<title>{{ post.title | xml_escape }}</title>
				<description>{{ post.content | xml_escape }}</description>
				<pubDate>{{ post.date | date: "%a, %d %b %Y %H:%M:%S %z" }}</pubDate>
				<link>{{site.url}}{{ post.url | relative_url }}</link>
				<guid isPermaLink="true">{{site.url}}{{ post.url | relative_url }}</guid>
			</item>
			{% endif %}
		{% endif %}
	{% endfor %}
{% endif %}
</channel>
</rss>



================================================
FILE: assets/blog/index.html
================================================
---
is_wiki_page: false
---

<!--- this file is needed for automatic creation of blog page --->


================================================
FILE: assets/css/git-wiki-style.scss
================================================
---
layout: "null"
---

@import "git-wiki-style.scss";



================================================
FILE: assets/css/github.css
================================================
@font-face {
    font-family: octicons-link;
    src: url(data:font/woff;charset=utf-8;base64,d09GRgABAAAAAAZwABAAAAAACFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEU0lHAAAGaAAAAAgAAAAIAAAAAUdTVUIAAAZcAAAACgAAAAoAAQAAT1MvMgAAAyQAAABJAAAAYFYEU3RjbWFwAAADcAAAAEUAAACAAJThvmN2dCAAAATkAAAABAAAAAQAAAAAZnBnbQAAA7gAAACyAAABCUM+8IhnYXNwAAAGTAAAABAAAAAQABoAI2dseWYAAAFsAAABPAAAAZwcEq9taGVhZAAAAsgAAAA0AAAANgh4a91oaGVhAAADCAAAABoAAAAkCA8DRGhtdHgAAAL8AAAADAAAAAwGAACfbG9jYQAAAsAAAAAIAAAACABiATBtYXhwAAACqAAAABgAAAAgAA8ASm5hbWUAAAToAAABQgAAAlXu73sOcG9zdAAABiwAAAAeAAAAME3QpOBwcmVwAAAEbAAAAHYAAAB/aFGpk3jaTY6xa8JAGMW/O62BDi0tJLYQincXEypYIiGJjSgHniQ6umTsUEyLm5BV6NDBP8Tpts6F0v+k/0an2i+itHDw3v2+9+DBKTzsJNnWJNTgHEy4BgG3EMI9DCEDOGEXzDADU5hBKMIgNPZqoD3SilVaXZCER3/I7AtxEJLtzzuZfI+VVkprxTlXShWKb3TBecG11rwoNlmmn1P2WYcJczl32etSpKnziC7lQyWe1smVPy/Lt7Kc+0vWY/gAgIIEqAN9we0pwKXreiMasxvabDQMM4riO+qxM2ogwDGOZTXxwxDiycQIcoYFBLj5K3EIaSctAq2kTYiw+ymhce7vwM9jSqO8JyVd5RH9gyTt2+J/yUmYlIR0s04n6+7Vm1ozezUeLEaUjhaDSuXHwVRgvLJn1tQ7xiuVv/ocTRF42mNgZGBgYGbwZOBiAAFGJBIMAAizAFoAAABiAGIAznjaY2BkYGAA4in8zwXi+W2+MjCzMIDApSwvXzC97Z4Ig8N/BxYGZgcgl52BCSQKAA3jCV8CAABfAAAAAAQAAEB42mNgZGBg4f3vACQZQABIMjKgAmYAKEgBXgAAeNpjYGY6wTiBgZWBg2kmUxoDA4MPhGZMYzBi1AHygVLYQUCaawqDA4PChxhmh/8ODDEsvAwHgMKMIDnGL0x7gJQCAwMAJd4MFwAAAHjaY2BgYGaA4DAGRgYQkAHyGMF8NgYrIM3JIAGVYYDT+AEjAwuDFpBmA9KMDEwMCh9i/v8H8sH0/4dQc1iAmAkALaUKLgAAAHjaTY9LDsIgEIbtgqHUPpDi3gPoBVyRTmTddOmqTXThEXqrob2gQ1FjwpDvfwCBdmdXC5AVKFu3e5MfNFJ29KTQT48Ob9/lqYwOGZxeUelN2U2R6+cArgtCJpauW7UQBqnFkUsjAY/kOU1cP+DAgvxwn1chZDwUbd6CFimGXwzwF6tPbFIcjEl+vvmM/byA48e6tWrKArm4ZJlCbdsrxksL1AwWn/yBSJKpYbq8AXaaTb8AAHja28jAwOC00ZrBeQNDQOWO//sdBBgYGRiYWYAEELEwMTE4uzo5Zzo5b2BxdnFOcALxNjA6b2ByTswC8jYwg0VlNuoCTWAMqNzMzsoK1rEhNqByEyerg5PMJlYuVueETKcd/89uBpnpvIEVomeHLoMsAAe1Id4AAAAAAAB42oWQT07CQBTGv0JBhagk7HQzKxca2sJCE1hDt4QF+9JOS0nbaaYDCQfwCJ7Au3AHj+LO13FMmm6cl7785vven0kBjHCBhfpYuNa5Ph1c0e2Xu3jEvWG7UdPDLZ4N92nOm+EBXuAbHmIMSRMs+4aUEd4Nd3CHD8NdvOLTsA2GL8M9PODbcL+hD7C1xoaHeLJSEao0FEW14ckxC+TU8TxvsY6X0eLPmRhry2WVioLpkrbp84LLQPGI7c6sOiUzpWIWS5GzlSgUzzLBSikOPFTOXqly7rqx0Z1Q5BAIoZBSFihQYQOOBEdkCOgXTOHA07HAGjGWiIjaPZNW13/+lm6S9FT7rLHFJ6fQbkATOG1j2OFMucKJJsxIVfQORl+9Jyda6Sl1dUYhSCm1dyClfoeDve4qMYdLEbfqHf3O/AdDumsjAAB42mNgYoAAZQYjBmyAGYQZmdhL8zLdDEydARfoAqIAAAABAAMABwAKABMAB///AA8AAQAAAAAAAAAAAAAAAAABAAAAAA==) format('woff');
}

body>.wrapper .octicon {
    display: inline-block;
    fill: currentColor;
    vertical-align: text-bottom;
}

body>.wrapper .anchor {
    float: left;
    line-height: 1;
    margin-left: -20px;
    padding-right: 4px;
}

body>.wrapper .anchor:focus {
    outline: none;
}

body>.wrapper h1 .octicon-link,
body>.wrapper h2 .octicon-link,
body>.wrapper h3 .octicon-link,
body>.wrapper h4 .octicon-link,
body>.wrapper h5 .octicon-link,
body>.wrapper h6 .octicon-link {
    color: #1b1f23;
    vertical-align: middle;
    visibility: hidden;
}

body>.wrapper h1:hover .anchor,
body>.wrapper h2:hover .anchor,
body>.wrapper h3:hover .anchor,
body>.wrapper h4:hover .anchor,
body>.wrapper h5:hover .anchor,
body>.wrapper h6:hover .anchor {
    text-decoration: none;
}

body>.wrapper h1:hover .anchor .octicon-link,
body>.wrapper h2:hover .anchor .octicon-link,
body>.wrapper h3:hover .anchor .octicon-link,
body>.wrapper h4:hover .anchor .octicon-link,
body>.wrapper h5:hover .anchor .octicon-link,
body>.wrapper h6:hover .anchor .octicon-link {
    visibility: visible;
}

body>.wrapper {
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    color: #24292e;
    line-height: 1.5;
    font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol;
    font-size: 16px;
    line-height: 1.5;
    word-wrap: break-word;
}

body>.wrapper .pl-c {
    color: #6a737d;
}

body>.wrapper .pl-c1,
body>.wrapper .pl-s .pl-v {
    color: #005cc5;
}

body>.wrapper .pl-e,
body>.wrapper .pl-en {
    color: #6f42c1;
}

body>.wrapper .pl-s .pl-s1,
body>.wrapper .pl-smi {
    color: #24292e;
}

body>.wrapper .pl-ent {
    color: #22863a;
}

body>.wrapper .pl-k {
    color: #d73a49;
}

body>.wrapper .pl-pds,
body>.wrapper .pl-s,
body>.wrapper .pl-s .pl-pse .pl-s1,
body>.wrapper .pl-sr,
body>.wrapper .pl-sr .pl-cce,
body>.wrapper .pl-sr .pl-sra,
body>.wrapper .pl-sr .pl-sre {
    color: #032f62;
}

body>.wrapper .pl-smw,
body>.wrapper .pl-v {
    color: #e36209;
}

body>.wrapper .pl-bu {
    color: #b31d28;
}

body>.wrapper .pl-ii {
    background-color: #b31d28;
    color: #fafbfc;
}

body>.wrapper .pl-c2 {
    background-color: #d73a49;
    color: #fafbfc;
}

body>.wrapper .pl-c2:before {
    content: "^M";
}

body>.wrapper .pl-sr .pl-cce {
    color: #22863a;
    font-weight: 700;
}

body>.wrapper .pl-ml {
    color: #735c0f;
}

body>.wrapper .pl-mh,
body>.wrapper .pl-mh .pl-en,
body>.wrapper .pl-ms {
    color: #005cc5;
    font-weight: 700;
}

body>.wrapper .pl-mi {
    color: #24292e;
    font-style: italic;
}

body>.wrapper .pl-mb {
    color: #24292e;
    font-weight: 700;
}

body>.wrapper .pl-md {
    background-color: #ffeef0;
    color: #b31d28;
}

body>.wrapper .pl-mi1 {
    background-color: #f0fff4;
    color: #22863a;
}

body>.wrapper .pl-mc {
    background-color: #ffebda;
    color: #e36209;
}

body>.wrapper .pl-mi2 {
    background-color: #005cc5;
    color: #f6f8fa;
}

body>.wrapper .pl-mdr {
    color: #6f42c1;
    font-weight: 700;
}

body>.wrapper .pl-ba {
    color: #586069;
}

body>.wrapper .pl-sg {
    color: #959da5;
}

body>.wrapper .pl-corl {
    color: #032f62;
    text-decoration: underline;
}

body>.wrapper details {
    display: block;
}

body>.wrapper summary {
    display: list-item;
}

body>.wrapper a {
    background-color: transparent;
}

body>.wrapper a:active,
body>.wrapper a:hover {
    outline-width: 0;
}

body>.wrapper strong {
    font-weight: inherit;
    font-weight: bolder;
}

body>.wrapper h1 {
    font-size: 2em;
    margin: .67em 0;
}

body>.wrapper img {
    border-style: none;
}

body>.wrapper code,
body>.wrapper kbd,
body>.wrapper pre {
    font-family: monospace, monospace;
    font-size: 1em;
}

body>.wrapper hr {
    box-sizing: content-box;
    height: 0;
    overflow: visible;
}

body>.wrapper input {
    font: inherit;
    margin: 0;
}

body>.wrapper input {
    overflow: visible;
}

body>.wrapper [type=checkbox] {
    box-sizing: border-box;
    padding: 0;
}

body>.wrapper * {
    box-sizing: border-box;
}

body>.wrapper input {
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
}

body>.wrapper a {
    color: #0366d6;
    text-decoration: none;
}

body>.wrapper a:hover {
    text-decoration: underline;
}

body>.wrapper strong {
    font-weight: 600;
}

body>.wrapper hr {
    background: transparent;
    border: 0;
    border-bottom: 1px solid #dfe2e5;
    height: 0;
    margin: 15px 0;
    overflow: hidden;
}

body>.wrapper hr:before {
    content: "";
    display: table;
}

body>.wrapper hr:after {
    clear: both;
    content: "";
    display: table;
}

body>.wrapper table {
    border-collapse: collapse;
    border-spacing: 0;
}

body>.wrapper td,
body>.wrapper th {
    padding: 0;
}

body>.wrapper details summary {
    cursor: pointer;
}

body>.wrapper h1,
body>.wrapper h2,
body>.wrapper h3,
body>.wrapper h4,
body>.wrapper h5,
body>.wrapper h6 {
    margin-bottom: 0;
    margin-top: 0;
}

body>.wrapper h1 {
    font-size: 32px;
}

body>.wrapper h1,
body>.wrapper h2 {
    font-weight: 600;
}

body>.wrapper h2 {
    font-size: 24px;
}

body>.wrapper h3 {
    font-size: 20px;
}

body>.wrapper h3,
body>.wrapper h4 {
    font-weight: 600;
}

body>.wrapper h4 {
    font-size: 16px;
}

body>.wrapper h5 {
    font-size: 14px;
}

body>.wrapper h5,
body>.wrapper h6 {
    font-weight: 600;
}

body>.wrapper h6 {
    font-size: 12px;
}

body>.wrapper p {
    margin-bottom: 10px;
    margin-top: 0;
}

body>.wrapper blockquote {
    margin: 0;
}

body>.wrapper ol,
body>.wrapper ul {
    margin-bottom: 0;
    margin-top: 0;
    padding-left: 0;
}

body>.wrapper ol ol,
body>.wrapper ul ol {
    list-style-type: lower-roman;
}

body>.wrapper ol ol ol,
body>.wrapper ol ul ol,
body>.wrapper ul ol ol,
body>.wrapper ul ul ol {
    list-style-type: lower-alpha;
}

body>.wrapper dd {
    margin-left: 0;
}

body>.wrapper code,
body>.wrapper pre {
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;
    font-size: 12px;
}

body>.wrapper pre {
    margin-bottom: 0;
    margin-top: 0;
}

body>.wrapper input::-webkit-inner-spin-button,
body>.wrapper input::-webkit-outer-spin-button {
    -webkit-appearance: none;
    appearance: none;
    margin: 0;
}

body>.wrapper .border {
    border: 1px solid #e1e4e8 !important;
}

body>.wrapper .border-0 {
    border: 0 !important;
}

body>.wrapper .border-bottom {
    border-bottom: 1px solid #e1e4e8 !important;
}

body>.wrapper .rounded-1 {
    border-radius: 3px !important;
}

body>.wrapper .bg-white {
    background-color: #fff !important;
}

body>.wrapper .bg-gray-light {
    background-color: #fafbfc !important;
}

body>.wrapper .text-gray-light {
    color: #6a737d !important;
}

body>.wrapper .mb-0 {
    margin-bottom: 0 !important;
}

body>.wrapper .my-2 {
    margin-bottom: 8px !important;
    margin-top: 8px !important;
}

body>.wrapper .pl-0 {
    padding-left: 0 !important;
}

body>.wrapper .py-0 {
    padding-bottom: 0 !important;
    padding-top: 0 !important;
}

body>.wrapper .pl-1 {
    padding-left: 4px !important;
}

body>.wrapper .pl-2 {
    padding-left: 8px !important;
}

body>.wrapper .py-2 {
    padding-bottom: 8px !important;
    padding-top: 8px !important;
}

body>.wrapper .pl-3,
body>.wrapper .px-3 {
    padding-left: 16px !important;
}

body>.wrapper .px-3 {
    padding-right: 16px !important;
}

body>.wrapper .pl-4 {
    padding-left: 24px !important;
}

body>.wrapper .pl-5 {
    padding-left: 32px !important;
}

body>.wrapper .pl-6 {
    padding-left: 40px !important;
}

body>.wrapper .f6 {
    font-size: 12px !important;
}

body>.wrapper .lh-condensed {
    line-height: 1.25 !important;
}

body>.wrapper .text-bold {
    font-weight: 600 !important;
}

body>.wrapper:before {
    content: "";
    display: table;
}

body>.wrapper:after {
    clear: both;
    content: "";
    display: table;
}

body>.wrapper>:first-child {
    margin-top: 0 !important;
}

body>.wrapper>:last-child {
    margin-bottom: 0 !important;
}

body>.wrapper a:not([href]) {
    color: inherit;
    text-decoration: none;
}

body>.wrapper blockquote,
body>.wrapper dl,
body>.wrapper ol,
body>.wrapper p,
body>.wrapper pre,
body>.wrapper table,
body>.wrapper ul {
    margin-bottom: 16px;
    margin-top: 0;
}

body>.wrapper hr {
    background-color: #e1e4e8;
    border: 0;
    height: .25em;
    margin: 24px 0;
    padding: 0;
}

body>.wrapper blockquote {
    border-left: .25em solid #dfe2e5;
    color: #6a737d;
    padding: 0 1em;
}

body>.wrapper blockquote>:first-child {
    margin-top: 0;
}

body>.wrapper blockquote>:last-child {
    margin-bottom: 0;
}

body>.wrapper kbd {
    background-color: #fafbfc;
    border: 1px solid #c6cbd1;
    border-bottom-color: #959da5;
    border-radius: 3px;
    box-shadow: inset 0 -1px 0 #959da5;
    color: #444d56;
    display: inline-block;
    font-size: 11px;
    line-height: 10px;
    padding: 3px 5px;
    vertical-align: middle;
}

body>.wrapper h1,
body>.wrapper h2,
body>.wrapper h3,
body>.wrapper h4,
body>.wrapper h5,
body>.wrapper h6 {
    font-weight: 600;
    line-height: 1.25;
    margin-bottom: 16px;
    margin-top: 24px;
}

body>.wrapper h1 {
    font-size: 2em;
}

body>.wrapper h1,
body>.wrapper h2 {
    border-bottom: 1px solid #eaecef;
    padding-bottom: .3em;
}

body>.wrapper h2 {
    font-size: 1.5em;
}

body>.wrapper h3 {
    font-size: 1.25em;
}

body>.wrapper h4 {
    font-size: 1em;
}

body>.wrapper h5 {
    font-size: .875em;
}

body>.wrapper h6 {
    color: #6a737d;
    font-size: .85em;
}

body>.wrapper ol,
body>.wrapper ul {
    padding-left: 2em;
}

body>.wrapper ol ol,
body>.wrapper ol ul,
body>.wrapper ul ol,
body>.wrapper ul ul {
    margin-bottom: 0;
    margin-top: 0;
}

body>.wrapper li {
    word-wrap: break-all;
}

body>.wrapper li>p {
    margin-top: 16px;
}

body>.wrapper li+li {
    margin-top: .25em;
}

body>.wrapper dl {
    padding: 0;
}

body>.wrapper dl dt {
    font-size: 1em;
    font-style: italic;
    font-weight: 600;
    margin-top: 16px;
    padding: 0;
}

body>.wrapper dl dd {
    margin-bottom: 16px;
    padding: 0 16px;
}

body>.wrapper table {
    display: block;
    overflow: auto;
    width: 100%;
}

body>.wrapper table th {
    font-weight: 600;
}

body>.wrapper table td,
body>.wrapper table th {
    border: 1px solid #dfe2e5;
    padding: 6px 13px;
}

body>.wrapper table tr {
    background-color: #fff;
    border-top: 1px solid #c6cbd1;
}

body>.wrapper table tr:nth-child(2n) {
    background-color: #f6f8fa;
}

body>.wrapper img {
    background-color: #fff;
    box-sizing: content-box;
    max-width: 100%;
}

body>.wrapper img[align=right] {
    padding-left: 20px;
}

body>.wrapper img[align=left] {
    padding-right: 20px;
}

body>.wrapper code {
    background-color: rgba(27, 31, 35, .05);
    border-radius: 3px;
    font-size: 85%;
    margin: 0;
    padding: .2em .4em;
}

body>.wrapper pre {
    word-wrap: normal;
}

body>.wrapper pre>code {
    background: transparent;
    border: 0;
    font-size: 100%;
    margin: 0;
    padding: 0;
    white-space: pre;
    word-break: normal;
}

body>.wrapper .highlight {
    margin-bottom: 16px;
}

body>.wrapper .highlight pre {
    margin-bottom: 0;
    word-break: normal;
}

body>.wrapper .highlight pre,
body>.wrapper pre {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    overflow: auto;
    padding: 16px;
}

body>.wrapper pre code {
    background-color: transparent;
    border: 0;
    display: inline;
    line-height: inherit;
    margin: 0;
    max-width: auto;
    overflow: visible;
    padding: 0;
    word-wrap: normal;
}

body>.wrapper .commit-tease-sha {
    color: #444d56;
    display: inline-block;
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;
    font-size: 90%;
}

body>.wrapper .blob-wrapper {
    border-bottom-left-radius: 3px;
    border-bottom-right-radius: 3px;
    overflow-x: auto;
    overflow-y: hidden;
}

body>.wrapper .blob-wrapper-embedded {
    max-height: 240px;
    overflow-y: auto;
}

body>.wrapper .blob-num {
    -moz-user-select: none;
    -ms-user-select: none;
    -webkit-user-select: none;
    color: rgba(27, 31, 35, .3);
    cursor: pointer;
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;
    font-size: 12px;
    line-height: 20px;
    min-width: 50px;
    padding-left: 10px;
    padding-right: 10px;
    text-align: right;
    user-select: none;
    vertical-align: top;
    white-space: nowrap;
    width: 1%;
}

body>.wrapper .blob-num:hover {
    color: rgba(27, 31, 35, .6);
}

body>.wrapper .blob-num:before {
    content: attr(data-line-number);
}

body>.wrapper .blob-code {
    line-height: 20px;
    padding-left: 10px;
    padding-right: 10px;
    position: relative;
    vertical-align: top;
}

body>.wrapper .blob-code-inner {
    color: #24292e;
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;
    font-size: 12px;
    overflow: visible;
    white-space: pre;
    word-wrap: normal;
}

body>.wrapper .pl-token.active,
body>.wrapper .pl-token:hover {
    background: #ffea7f;
    cursor: pointer;
}

body>.wrapper kbd {
    background-color: #fafbfc;
    border: 1px solid #d1d5da;
    border-bottom-color: #c6cbd1;
    border-radius: 3px;
    box-shadow: inset 0 -1px 0 #c6cbd1;
    color: #444d56;
    display: inline-block;
    font: 11px SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;
    line-height: 10px;
    padding: 3px 5px;
    vertical-align: middle;
}

body>.wrapper :checked+.radio-label {
    border-color: #0366d6;
    position: relative;
    z-index: 1;
}

body>.wrapper .tab-size[data-tab-size="1"] {
    -moz-tab-size: 1;
    tab-size: 1;
}

body>.wrapper .tab-size[data-tab-size="2"] {
    -moz-tab-size: 2;
    tab-size: 2;
}

body>.wrapper .tab-size[data-tab-size="3"] {
    -moz-tab-size: 3;
    tab-size: 3;
}

body>.wrapper .tab-size[data-tab-size="4"] {
    -moz-tab-size: 4;
    tab-size: 4;
}

body>.wrapper .tab-size[data-tab-size="5"] {
    -moz-tab-size: 5;
    tab-size: 5;
}

body>.wrapper .tab-size[data-tab-size="6"] {
    -moz-tab-size: 6;
    tab-size: 6;
}

body>.wrapper .tab-size[data-tab-size="7"] {
    -moz-tab-size: 7;
    tab-size: 7;
}

body>.wrapper .tab-size[data-tab-size="8"] {
    -moz-tab-size: 8;
    tab-size: 8;
}

body>.wrapper .tab-size[data-tab-size="9"] {
    -moz-tab-size: 9;
    tab-size: 9;
}

body>.wrapper .tab-size[data-tab-size="10"] {
    -moz-tab-size: 10;
    tab-size: 10;
}

body>.wrapper .tab-size[data-tab-size="11"] {
    -moz-tab-size: 11;
    tab-size: 11;
}

body>.wrapper .tab-size[data-tab-size="12"] {
    -moz-tab-size: 12;
    tab-size: 12;
}

body>.wrapper .task-list-item {
    list-style-type: none;
}

body>.wrapper .task-list-item+.task-list-item {
    margin-top: 3px;
}

body>.wrapper .task-list-item input {
    margin: 0 .2em .25em -1.6em;
    vertical-align: middle;
}

body>.wrapper hr {
    border-bottom-color: #eee;
}

body>.wrapper .pl-0 {
    padding-left: 0 !important;
}

body>.wrapper .pl-1 {
    padding-left: 4px !important;
}

body>.wrapper .pl-2 {
    padding-left: 8px !important;
}

body>.wrapper .pl-3 {
    padding-left: 16px !important;
}

body>.wrapper .pl-4 {
    padding-left: 24px !important;
}

body>.wrapper .pl-5 {
    padding-left: 32px !important;
}

body>.wrapper .pl-6 {
    padding-left: 40px !important;
}

body>.wrapper .pl-7 {
    padding-left: 48px !important;
}

body>.wrapper .pl-8 {
    padding-left: 64px !important;
}

body>.wrapper .pl-9 {
    padding-left: 80px !important;
}

body>.wrapper .pl-10 {
    padding-left: 96px !important;
}

body>.wrapper .pl-11 {
    padding-left: 112px !important;
}

body>.wrapper .pl-12 {
    padding-left: 128px !important;
}

/* https://darkmodejs.learn.uno/#debug */
.darkmode-layer, .darkmode-toggle {
    z-index: 500;
}


================================================
FILE: assets/fonts/Noto-Sans-700/Noto-Sans-700.eot
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-700/Noto-Sans-700.ttf
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-700/Noto-Sans-700.woff
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-700/Noto-Sans-700.woff2
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-700italic/Noto-Sans-700italic.eot
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-700italic/Noto-Sans-700italic.ttf
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff2
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-italic/Noto-Sans-italic.eot
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-italic/Noto-Sans-italic.ttf
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-italic/Noto-Sans-italic.woff
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-italic/Noto-Sans-italic.woff2
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-regular/Noto-Sans-regular.eot
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-regular/Noto-Sans-regular.ttf
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-regular/Noto-Sans-regular.woff
================================================
[Binary file]


================================================
FILE: assets/fonts/Noto-Sans-regular/Noto-Sans-regular.woff2
================================================
[Binary file]


================================================
FILE: assets/images/.gitkeep
================================================




================================================
FILE: assets/js/checkLinks.js
================================================
(function ($) {
    //
    // RED LINK FEATURE (Hacky)
    $.fn.checkLinks = function (staticPages) {
        setTimeout(
            function () {
                $('a').each(function () {
                    // avoid red link for external urls
                    if (this.hostname != window.location.hostname) {
                        if ($(this).parents('#git-wiki-content').length > 0)
                            $(this).addClass("external-link");
                        return;
                    }

                    for (var k in staticPages) {
                        var page = staticPages[k];
                        var link = document.createElement("a");
                        link.href = page;

                        if (this.href === link.href) {
                            return;
                        }
                    }

                    var ext = this.pathname.split('.').pop().split(/\#|\?/)[0];

                    // pessimistic condition based on the fact that
                    // markdown files are automatically converted in html
                    // if they are part of the wiki (the real check is right below)
                    var lExt = ext && ext.toLowerCase();
                    var isRed = lExt == "md" || lExt == "markdown";

                    if (isRed)
                        $(this).css('color', 'red');

                    var that = this;
                    $.ajax({
                        type: 'HEAD',
                        url: this.href,
                        success: function () {
                            $(that).css('color', '');
                        },
                        error: function (xhr, ajaxOptions, thrownError) {
                            if (xhr.status == 404) {
                                $(that).css('color', 'red');
                            }
                        }
                    });
                });
            }, 0);
    };

})(jQuery);


================================================
FILE: assets/js/scale.fix.js
================================================
(function(document) {
    var metas = document.getElementsByTagName('meta'),
        changeViewportContent = function(content) {
            for (var i = 0; i < metas.length; i++) {
                if (metas[i].name == "viewport") {
                    metas[i].content = content;
                }
            }
        },
        initialize = function() {
            changeViewportContent("width=device-width, minimum-scale=1.0, maximum-scale=1.0");
        },
        gestureStart = function() {
            changeViewportContent("width=device-width, minimum-scale=0.25, maximum-scale=1.6");
        },
        gestureEnd = function() {
            initialize();
        };


    if (navigator.userAgent.match(/iPhone/i)) {
        initialize();

        document.addEventListener("touchstart", gestureStart, false);
        document.addEventListener("touchend", gestureEnd, false);
    }
})(document);



================================================
FILE: assets/js/searchdata.js
================================================
---
layout: null
is_wiki_page: false
---
{% if site.search_engine == "js" %}
var jsondata=[
  {% for post in site.posts %}
    {
      "title"    : "{{ post.title | escape }}",
      "category" : "{{ post.category }}",
      "tags"     : "{{ post.tags | join: ', ' }}",
      "url"      : "{{ site.baseurl }}{{ post.url }}",
      "date"     : "{{ post.date }}",
      "content"  : {{ page.content | jsonify }}
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
  ,
  {% for page in site.html_pages %}
   {
     {% assign title = page.title | default: page.name %}
     {% if title != nil %}
        "title"    : "{{ title | escape }}",
        "category" : "{{ page.category }}",
        "tags"     : "{{ page.tags | join: ', ' }}",
        "url"      : "{{ site.baseurl }}{{ page.url }}",
        "date"     : "{{ page.date }}",
        "content"  : {{ page.content | jsonify }}
     {% endif %}
   } {% unless forloop.last %},{% endunless %}
  {% endfor %}
];

var sjs = SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: jsondata,
    searchResultTemplate: '<li><a href="{url}" title="{desc}">{title}</a></li>',
    noResultsText: 'No results found',
    limit: 10,
    fuzzy: false,
    exclude: []
  })
{% endif %}




================================================
FILE: wiki/main_page.md
================================================
---
redirect_from: "/"
---

This is a sample of main page. You can edit it to start your wiki.

For documentation, installation guide and demo of [git-wiki-theme](git-wiki-theme) visit this [link](http://drassil.github.io/git-wiki/)




================================================
FILE: wiki/.gitkeep
================================================
[Empty file]


================================================
FILE: .env-files/Dockerfile.github
================================================
# The ruby version should be in sync with this: https://github.com/github/pages-gem/blob/master/Dockerfile#L1
FROM ruby:3.3
ENV LC_ALL=C.UTF-8=value

ADD . /srv/jekyll

WORKDIR /srv/jekyll

RUN bundle install --gemfile=.env-files/Gemfile.github

EXPOSE 4000


================================================
FILE: .env-files/Dockerfile.gitlab
================================================
FROM ruby:2.7.0

ENV LC_ALL=C.UTF-8=value

ADD . /srv/jekyll

WORKDIR /srv/jekyll

RUN bundle install --gemfile=.env-files/Gemfile.gitlab

EXPOSE 4000


================================================
FILE: .env-files/Gemfile.github
================================================
source 'http://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
gem "jekyll-gitlab-metadata" # for cross compatibility


================================================
FILE: .env-files/Gemfile.gitlab
================================================
source 'http://rubygems.org'
gem "jekyll-avatar"
gem "jekyll-coffeescript"
gem "jekyll-default-layout"
gem "jekyll-feed"
gem "jekyll-gist"
gem "jekyll-paginate"
gem "jekyll-mentions"
gem "jekyll-optional-front-matter"
gem "jekyll-readme-index"
gem "jekyll-redirect-from"
gem "jekyll-remote-theme"
gem "jekyll-relative-links"
gem "jekyll-seo-tag"
gem "jekyll-sitemap"
gem "jekyll-titles-from-headings"
gem "jemoji"
gem "jekyll-gitlab-metadata"


================================================
FILE: .github/ISSUE_TEMPLATE/bug_report.md
================================================
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. Windows 10]
 - Browser: [e.g. chrome, safari]
 - Version: [e.g. 22]

**Smartphone (please complete the following information):**
 - Device: [e.g. iPhone6]
 - OS: [e.g. iOS8.1]
 - Browser: [e.g. stock browser, safari]
 - Version: [e.g. 22]

**Additional context**
Add any other context about the problem here.



================================================
FILE: .github/ISSUE_TEMPLATE/config.yml
================================================
blank_issues_enabled: false
contact_links:
  - name: Git Wiki Documentation
    url: http://www.drassil.org/git-wiki/
    about: All information in our official wiki



================================================
FILE: .github/ISSUE_TEMPLATE/feature_request.md
================================================
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.



================================================
FILE: .github/ISSUE_TEMPLATE/general.md
================================================
---
name: General
about: Everything related with Git-Wiki that doesn't fit in other categories
title: "[GENERAL]"
labels: general
assignees: ''

---


