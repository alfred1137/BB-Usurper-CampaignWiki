Directory structure:
└── drassil-git-wiki/
    ├── README.md
    ├── _config.yml
    ├── docker-compose.yml
    ├── Dockerfile
    ├── google5fc4ee7c715c55f5.html
    ├── LICENSE
    ├── PULL_REQUEST_TEMPLATE.md
    ├── _includes/
    │   └── drassil/
    │       ├── comments.html
    │       ├── head.html
    │       └── sidebar.html
    ├── _posts/
    │   ├── 2018-12-17-blog-refactoring-v2.1.0.md
    │   ├── 2018-12-17-first-post.md
    │   ├── 2020-1-7-version-2-5.md
    │   └── .gitkeep
    ├── assets/
    │   └── images/
    │       └── .gitkeep
    ├── wiki/
    │   ├── changelogs.md
    │   ├── customize.md
    │   ├── Demo.md
    │   ├── examples.md
    │   ├── extensionless
    │   ├── main_page.md
    │   ├── press.md
    │   ├── theme-default.md
    │   ├── theme-github.md
    │   ├── theme-lux.md
    │   ├── theme-united.md
    │   └── .gitkeep
    └── .env-files/
        ├── Dockerfile.github
        ├── Dockerfile.gitlab
        ├── Gemfile.github
        └── Gemfile.gitlab

================================================
FILE: README.md
================================================
# git-wiki

[Demo and documentation](https://github.com/Drassil/git-wiki) for [git-wiki-theme](https://github.com/Drassil/git-wiki-theme)



================================================
FILE: _config.yml
================================================
# (string) Title of your wiki
title: git-wiki
demo_ver: 1.0.24
remote_theme: Drassil/git-wiki-theme@master
description: Git-Wiki demo and documentation
show_downloads: true
show_wiki_pages: true
show_wiki_pages_limit: 10
paginate: 2
paginate_path: "/assets/blog/page:num"
permalink: "/assets/blog/posts/:year/:month/:day/:title:output_ext"
blog_feature: true
show_wiki_posts: true
show_wiki_posts_limit: 5
logo_url: assets/images/1200px-Wikipedia-logo-v2.svg_.png
google_analytics:
git_branch: gh-pages
use_github_wiki: false
use_prose_io: true
service: github
search_engine: "js"
google_cse_token: 007197903287787072094:8rbvkeqo6qw
wiki_folder: "wiki"
site_root:

#
# Jekyll
#

defaults:
  - scope:
      path: "wiki"
    values:
      permalink: /:basename
  - scope:
      path: "" # an empty string here means all files in the project
    values:
      layout: "git-wiki-default"
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "git-wiki-default"
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "git-wiki-post"
  - scope:
      path: assets/blog
    values:
      layout: "git-wiki-blog"

plugins:
  - jekyll-feed
  - jekyll-redirect-from
  - jekyll-seo-tag
  - jekyll-sitemap
  - jekyll-avatar
  - jemoji
  - jekyll-mentions

#
# INCLUDING HOOKS
# They are optional, change them only if you need
# Check wiki documentation to learn how they work
#

inc_after_content: "drassil/comments.html"
inc_after_head: "drassil/head.html"
inc_before_page_list: "drassil/sidebar.html"



================================================
FILE: docker-compose.yml
================================================
version: '3.7'
services:
  github-wiki:
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
  gitlab-wiki:
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
FILE: Dockerfile
================================================
FROM jekyll/jekyll:pages

COPY Gemfile* /srv/jekyll/

WORKDIR /srv/jekyll

RUN apk update && \
	apk add ruby-dev gcc make curl build-base libc-dev libffi-dev zlib-dev libxml2-dev libgcrypt-dev libxslt-dev python

RUN bundle config build.nokogiri --use-system-libraries && \
	bundle install

EXPOSE 4000


================================================
FILE: google5fc4ee7c715c55f5.html
================================================
google-site-verification: google5fc4ee7c715c55f5.html


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





================================================
FILE: _includes/drassil/comments.html
================================================
<div id="disqus_thread"></div>
<script>

    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
    /*
    var disqus_config = function () {
    this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function () { // DON'T EDIT BELOW THIS LINE
        var d = document, s = d.createElement('script');
        s.src = 'https://git-wiki.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>


================================================
FILE: _includes/drassil/head.html
================================================
<link rel="shortcut icon" type="image/png"  href="{{ 'assets/images/1200px-Wikipedia-logo-v2.svg_.png' | relative_url }}" >


================================================
FILE: _includes/drassil/sidebar.html
================================================
Menu (<a href="{{ site.github.repository_url }}/edit/{{site.git_branch | escape}}/_includes/drassil/sidebar.html">Edit</a>):

<ul>
  <li><a href="https://github.com/Drassil/git-wiki-theme">Theme Repository</a>
  <li><a href="{{ '/' | relative_url }}">Home</a></li>
  <li><a href="{{ '/examples.html' | relative_url }}">Made with Git-Wiki</a>
  <li><a href="{{ '/changelogs.html' | relative_url }}">Changelogs</a>
  <li><a href="{{ '/customize.html' | relative_url }}">Customize</a>
  <li><a href="{{ '/press.html' | relative_url }}">Press & Contacts</a>
</ul>



================================================
FILE: _posts/2018-12-17-blog-refactoring-v2.1.0.md
================================================
---
published: true
---

# Blog Refactoring v2.1.0

Version 2.1.0 of git-wiki includes with following features:

* Complete Blog solution
* New search engine based on javascript
* Buttons to add new Wiki page and post
* Configurable Page and post list in sidebar
* other minor fixes

Configurations added (modify your _config.yml):

```
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
paginate_path: "/blog/page:num"
# Select search_engine component from:
# - js: it uses a built in javascript component that uses generated sitemap_full.xml to search inside your wiki
# - github : it uses internal github repository search
# - google : it uses cse search bar, you need to configure google_cse_token
#
search_engine : "js"

defaults:
 -
    scope:
      path: ""
      type: "posts"
    values:
      layout: "git-wiki-post"
      
plugins:
 - jekyll-feed
 - jekyll-redirect-from
 - jekyll-seo-tag
 - jekyll-sitemap
 - jekyll-avatar
 - jemoji
 - jekyll-mentions
 - jekyll-include-cache
 
inc_before_page_list :
inc_after_page_list :
inc_before_post_list :
inc_after_post_list :
```



================================================
FILE: _posts/2018-12-17-first-post.md
================================================
---
published: true
---
# First post - An example of blogging

Welcome to Git Wiki first post!

it's a post example and nothing more

you can use Add or Edit buttons to create or edit posts the same way you create pages!



================================================
FILE: _posts/2020-1-7-version-2-5.md
================================================
# GIT WIKI 2.5.0 - REMOTE THEME

This new version of git-wiki introduces a new installation method that allows to run git-wiki as a remote theme using this plugin: https://github.com/benbalter/jekyll-remote-theme

Such plugin is included in github pages by default so you can use it without any effort.

[RELEASE](https://github.com/Drassil/git-wiki-theme/releases/tag/v2.5.0)



================================================
FILE: _posts/.gitkeep
================================================




================================================
FILE: assets/images/.gitkeep
================================================




================================================
FILE: wiki/changelogs.md
================================================
# Changelogs

## 2.7.4

* Dark mode implemented

## 2.5.1

* refactoring the project to be supported by [remote_theme](https://github.com/benbalter/jekyll-remote-theme). No you can avoid to import all sources files into your project
* improved support for gitlab
* improved support for docker
* implemented static TOC (removed the javascript method) 

## 2.3.0

Changed #toc div, now it's called #git-wiki-toc. You've to change it too if you are using a totally custom theme.

New theme: github

Various fixes

## 2.2 - External Links

* Implemented external links icon (wikipedia style)

## 2.1.16 - Search with steroids

* Improved search engine with new async js data loading
* fixed page list

## 2.1.12 - Mobile Header
* Implemented collapsible responsive header

## 2.1.11 - Blog fixes

* various critical fixes to new blog system
* added "permalink" in config dist 

## 2.1.0 - Blog Refactoring

* Blog
* New search engine
* Button to add wiki page and post
* Page and post list in sidebar
* other minor fixes
* Improved SEO

See the list of changes here: [Article](../_posts/2018-12-17-blog-refactoring-v2.1.0.md)

## 2.0.3

* fixed bug on logo visualization
* fixed united and lux theme unwanted character

## 2.0.1 - Themed Wiki

* Created new themes from "united" and "lux" bootstrap styles
* minor fix to 404 page, fixed build warning

## 2.0.0 - Wiki Modules

* Splitted default layout in reusable partial files and modular architecture
* Created configurable including hooks to extend git-wiki theme
* Fixed some deprecation
* Crated Gemfile for local installations
* removed not used configurations
* compress css
* minor fixes


### How to upgrade from 1.0.5

you must upgrade your _config.xml changing following configurations:

```
# to add comments now you can include a file using inc_after_content configuration
# it's exactly the position where old comments.html file was placed i 1.0.5
comments : true -> inc_after_content : "path_of_comments_file.html"

# to add custom elements in <head> now you can use inc_after_head or inc_before_head to add
# your code
custom_head: true ->  inc_after_head : "path_of_head_file.html"

# custom sidebar can be added directly in <header> 
# via a custom file using inc_after_header
custom_sidebar: true -> inc_after_header : "path_of_sidebar_file.html" 

# if you need custom footer elements you can use inc_before_footer configuration now
custom_footer: true -> inc_before_footer : "path_of_footer_file.html"

# in new jekyll versions gems has been deprecated in favour of plugins
gems -> plugins
```

then you've to add following new configurations:

```
# change default layouts if you want to totally customize your wiki
defaults:
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
```

## 1.0.5 - ToC

* Improved ToC performances and fixed minor bugs

## 1.0.4 - Red

* Implemented red links for non-existing pages
* various style fixes

## 1.0.2

First public version of git-wiki with following features:

* Action buttons to edit page, see the history and search in wiki
* You can customize your wiki as you want with style sheets and even changing the layout.
* Improvements in the cooperative aspect: forks, pull-requests and roles.
* No databases! Only static files that can be downloaded in a few seconds.
* Markdown and html mixed together!
* History, revision comparison and everything you need from a wiki platform.
* You can edit your pages with the standard git editor, prose.io (integrated) or any kind of editor you prefer.






================================================
FILE: wiki/customize.md
================================================
# Customize git-wiki


From version 2.x Git-Wiki uses a **modular** architecture based on **components** and **"including hooks".**
This will allow you to **totally costumize** your wiki **adding new code** and/or **create your layout from scratch reusing every single piece** of git-wiki.

There are various methods to costumize and extends git-wiki, starting from the easiest one we will list them here:

## Configuration changes

First thing to do during git-wiki installation is and changing values in _config.yml.

If you like our theme as is you just need to set following configurations:

```
title
description
logo_url
```

It will allow you to define your brand.
Of course there are also other internal configurations to enable/disable features (you can see the complete list at bottom of this page)

## Internal themes

by default git-wiki includes some internal layout that you can set in your _config.yml to change your UI:

* [default theme](theme-default) (w3css)
* [lux theme](theme-lux) (bootstrap)
* [united theme](theme-united) (bootstrap)
* [github theme](theme-github) (bootstrap)

## Including hooks

If you need to extend git-wiki adding or replacing css rules, adding scripts or html elements you
can use the "including hooks" feature. It allows you to dynamically include a custom html code using the jekyll partials.
**NOTE**: Your file must be added inside the _include folder

### Style changes (head)

If you need a simple style change the easiest way to do it is including a custom css file that is able to add/overwrite default css rules.
  
To do it you can add in your _config.yml the following configuration:

```
inc_after_styles : "path/to/your/style.html" 
```
  
then in your _include folder you must add file defined above. It must be an html with
the <link> elements inside.
  
For example: 

```HTML
<link rel="stylesheet" href="{{ 'assets/css/mystyle.css' | relative_url }}">
```
  
**NOTE**: as you can see we're using relative_url jekyll function allowing us to include the css file of our assets folder.


  
### Add your components
  
With the same method used to include styles file you are able to use our "including hooks" to add your code everywhere you want.

You can find the list of all hooks at the bottom of this page


#### Sidebar
  
If you need to add content inside sidebar of our default layout you can use following hook:

`inc_after_header: "my_sidebar_file.html"`

#### Comments
  
If you need to add a comment component (for example disqus) you can use following hook:
  
`inc_after_content: "my_comments_file.html"`


## Layout refactoring

Before working with layout refactoring you should learn:

* how to work with Jekyll: [https://jekyllrb.com/docs/](https://jekyllrb.com/docs/)
* which are the components of git-wiki, you can find them here: <https://github.com/Drassil/git-wiki-theme/tree/master/_includes>
* Take a look at git-wiki default layouts to understand how to build your: <https://github.com/Drassil/git-wiki-theme/tree/master/_layouts>

If you need to totally change the layout of your wiki you can create a custom file in _layout folder and reuse only components that you need in the place that you want.
  
You've just to change following config:

```
defaults:
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
```
  
replacing **layout: "git-wiki-default"** with name of your custom layout.

## Configuration keys:
  
Read _config.yml file of your git-wiki installation for detailed list of configuration values (commented)



================================================
FILE: wiki/Demo.md
================================================
# Demo (example wiki page)

Within the computer subculture known as the demoscene, a non-interactive multimedia presentation is called a demo (or demonstration). Demogroups create demos to demonstrate their abilities in programming, music, drawing, and 3D modeling. The key difference between a classical animation and a demo is that the display of a demo is computed in real time, making computing power considerations the biggest challenge. Demos are mostly composed of 3D animations mixed with 2D effects and full screen effects.

The boot block demos of the 1980s, demos that were created to fit within the small (generally 512 to 4096 bytes) first block of the floppy disk that was to be loaded into RAM,[1] were typically created so that software crackers could boast of their accomplishment prior to the loading of the game. What began as a type of electronic graffiti on cracked software became an art form unto itself. The demoscene both produced and inspired many techniques used by video games and 3D rendering applications today - for instance, light bloom, among others.

![Demo Pic](Beyond_-_Conspiracy_-_2004_-_64k_intro.jpg)



================================================
FILE: wiki/examples.md
================================================
# Made with Git-Wiki

If you have built a wiki with git-wiki, please edit this file and add your wiki link

* [aZerothCore](http://www.azerothcore.org/wiki/home)

* [River Architect](https://riverarchitect.github.io/RA_wiki/)

* [HW-Core JS Class](https://hw-core.github.io/js-lib-class/)

* [NestJS Yalc](https://www.drassil.org/nestjs-yalc/)

* [Agora Wiki](https://agoranomic.github.io/wiki/)

* [ClearlyDefined doc](https://docs.clearlydefined.io/)

* [ifbctag](https://ifbctag.github.io/labwiki)

* [sonbuildmeahouse](https://sonbuildmeahouse.github.io/)

* [lacroix](https://gihad.github.io/lacroix/)

* [NCSA Genomics](http://priyab2.github.io/git-wiki)

* [WoWGaming](https://wowgaming.github.io/wiki-en)

* [Talon Wiki](https://talon.wiki/)

* [Ornia](https://ornia.arcinas.info/)

* [Anoduck's Das Wiki](https://anoduck.github.io/wiki/)

* [JaxPlays](https://jaxplays.com)




================================================
FILE: wiki/extensionless
================================================
## test markdown

* test1 

* test2



================================================
FILE: wiki/main_page.md
================================================
---
redirect_from: /
published: true
---

# Welcome to git-wiki demo!

This is both documentation and [demo](Demo.md) of [git-wiki theme](https://github.com/Drassil/git-wiki-theme) project.

it's a **modular and full featured wiki** powered by git, [github](https://pages.github.com/)/[gitlab](https://about.gitlab.com/product/pages/) pages and pull-requests!

The git-wiki project is composed by 3 different repository:

- [git-wiki-theme](https://github.com/Drassil/git-wiki-theme): This is the repository of the theme that implements the wiki functionalities. You would have not fork it unless you need to send a Pull Request or create your wiki project from scratch.

- [git-wiki-skeleton](https://github.com/Drassil/git-wiki-skeleton): This is the repo that you should fork or use as a template. It uses the [jekyll remote theme](https://github.com/benbalter/jekyll-remote-theme) functionality that allows you to create your own wiki based on git-wiki-theme. By using the remote functionality you can automatically keep your wiki always updated with latest features from the **git-wiki-theme**, but you can also fully customize it. 

- [git-wiki](https://github.com/Drassil/git-wiki): This is the documentation repository and website of the **git-wiki-theme** project. You would have not fork it unless you want to contribute to the git-wiki project documentation.

## Getting started

The easier and faster way to use git-wiki is the "skeleton" method.

**You don't need to install anything locally!**

1. Simply fork/clone [skeleton repo](https://github.com/Drassil/git-wiki-skeleton) or click on "Use this template" button to create your copy of the skeleton project.

2. Edit _config.yml and other pages as you need and then deploy it on github/gitlab pages.

**Done**! now wait that your page will be published and you're ready **_to wiki_**!

For more installation options see the [Installation instructions](#installation-instructions)

## Features 

* Improvements in the **cooperative** aspect: forks, pull-requests and roles.
* You can **customize your wiki** as you want with style sheets and even changing the layout. (see customization section below) 
* **No databases!** Only static files that can be downloaded in a few seconds.
* **Blazing fast** and free thankfully to Github/Gitlab Pages and Jekyll Server Side Generation process!
* **Markdown and html** mixed together!
* **Multiple free search engines!** on a static site!
* **History, revision comparison** and everything you need from a wiki platform.
* You can **edit your pages** with the standard git editor, prose.io (integrated) or any kind of editor you prefer.
* Non-existent wiki page links are "[red](red.md)", you can **click on them to automatically create a new page**!
* [External links](http://www.google.com) get the right icon automatically
* **Component system with hooks** that allows you to totally customize your wiki UI. (see customization section below) 
* Some **nice internal themes** to change your entire wiki UI with 1 simple configuration (see customization section below)
* Integrated **Blogging** feature thanks to jekyll!
* Automatic generated **TOC**
* You can download the entire wiki for **offline** usage and even navigate directly using a markdown reader


You can use it with jekyll ["remote_theme"](https://github.com/benbalter/jekyll-remote-theme) feature or fork/copy the master branch  and start your wiki in just 1 minute*.

Git-wiki can be used as [theme for jekyll](https://jekyll-themes.com/git-wiki/)

 *Github/Gitlab pages takes about 10 minutes to show up the first time you configure it

**Note:**
You can even include the [official github wiki](https://help.github.com/articles/about-github-wikis/) as a submodule and enable the option in our conf file to use github wiki pages in git-wiki system, but it's an experimental feature and it implies less advantages and greater disadvantages for now.

## Who is using git-wiki

[List of git-wiki installations](examples.md)

[List of forked repository](https://github.com/Drassil/git-wiki-theme/network/members)


### [Share your wiki with us!](examples) and keep the "Powered by Git-Wiki" footer link please. It will help both of us!


## Installation instructions

### Remote theme method

1. Fork, Clone [the skeleton repository](https://github.com/Drassil/git-wiki-skeleton) or click on "Use this template" button to create your copy.

2. Edit _config.yml and other pages as you need and then deploy it on github/gitlab pages.

**Description**: This method will allow you to create a wiki based on our skeleton repository and that extends git-wiki-theme. 

**Direct installation comparison**:

 + **pros**: This will allow you to avoid upgrading process pulling files from git-wiki-theme and eventually merge them.

 - **cons**: To edit/fix git-wiki-theme core files you need to configure a second repository forked by git-wiki-theme repo. However, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)

**GITLAB SUPPORT**: if you want to fork the skeleton from gitlab, you can use [this repo](https://gitlab.com/drassil/git-wiki-skeleton)

**Without skeleton**: you can avoid to use the skeleton repository if you want start from scratch, however it's important to use at leaset the configuration variables needed by the theme: [_config.yml](https://github.com/Drassil/git-wiki-skeleton/blob/master/_config.yml)

### Direct installation method

1. Fork, Clone [git-wiki-theme repository](https://github.com/drassil/git-wiki-theme) or click on "Use this template"

2. Edit _config.yml and push your changes in your repository, then configure the github/gitlab pages in your repository settings

**Description**: This method will allow you to create a wiki using git-wiki-theme directly. You can create your theme from scratch. It's for advanced users and people who want directly collaborate to git-wiki-theme project.

**Remote installation comparison**:

 + **pros**: You can build your wiki and collaborate with git-wiki-theme project by PR at the same time.

 - **cons**: Upgrading your wiki to the latest version need a merge with git-wiki-theme repo.


### Notes:
In both cases please is preferred to use **Fork** instead of **Template** and **Template** instead of **Clone** (Fork > Template > Clone).
Fork will allow you to make pull request to/from original repository to keep your files updated (for skeleton too). Please, keep everything open and collaborative!


### Local development

If you need to work on git-wiki locally before publish, then clone your wiki repo and follow this instructions 
from official github article: <https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/>
Git wiki already contains the Gemfile for local installations.

You can also use our **docker files** to run git-wiki under **docker**, 
the easiest method is to run `docker-compose up` command in this folder

## Configuration and customization

* [How to customize your wiki](customize.md)

* [How to setup the search feature](search-feature.md)

## Current known limitations

* You can't use the wiki internal link format: [[example]]. Please, use gh-pages links instead: \[example\](example) . It's a known jekyll limitation: <https://jekyllrb.com/docs/templates/>


## Support & Collaboration

You can open a public issue on [github](https://github.com/Drassil/git-wiki/issues) , 
send a private <a href="mailto:staff-drassil@googlegroups.com">email</a>  or create a PR to improve it.

Thank you!

## Components used

- [jekyll-toc](https://github.com/allejo/jekyll-toc)

- [jQuery](https://jquery.com/) for DOM manipulation

[MIT LICENSE](LICENSE)



================================================
FILE: wiki/press.md
================================================
# Press

feel free to add references or articles that talks about us:

* (add here!)

## Contacts

if you want to add your article here please edit this page or <a href="mailto:staff-drassil@googlegroups.com">contact us</a>



================================================
FILE: wiki/theme-default.md
================================================
# Theme: Git-Wiki Default


This is an example of layout built using default git-wiki theme


To use it as your default theme you've to change layout configuration in your _config.yml, for example:

```
defaults:
 -
    scope:
      path: ""
    values:
      layout: "git-wiki-default"
 -
    scope:
      path: ""
      type: "pages"
    values:
      layout: "git-wiki-default"
```

**NOTE:** it's the default configuration available in _config.yml




================================================
FILE: wiki/theme-github.md
================================================
---
layout: "git-wiki-bs-github"
---

# Theme: Github


This is an example of layout built using github css file


To use it as your default theme you've to change layout configuration in your _config.yml, for example:

```
defaults:
 -
    scope:
      path: ""
    values:
      layout: "git-wiki-bs-github"
 -
    scope:
      path: ""
      type: "pages"
    values:
      layout: "git-wiki-bs-github"
```




================================================
FILE: wiki/theme-lux.md
================================================
---
layout: "git-wiki-bs-lux"
---

# Theme: Lux


This is an example of layout built using [bootstrap lux](https://bootswatch.com/lux/)


To use it as your default theme you've to change layout configuration in your _config.yml, for example:

```
defaults:
 -
    scope:
      path: ""
    values:
      layout: "git-wiki-bs-lux"
 -
    scope:
      path: ""
      type: "pages"
    values:
      layout: "git-wiki-bs-lux"
```




================================================
FILE: wiki/theme-united.md
================================================
---
layout: "git-wiki-bs-united"
---

# Theme: United


This is an example of layout built using [bootstrap united theme](https://bootswatch.com/united/)


To use it as your default theme you've to change layout configuration in your _config.yml, for example:

```
defaults:
 -
    scope:
      path: ""
    values:
      layout: "git-wiki-bs-united"
 -
    scope:
      path: ""
      type: "pages"
    values:
      layout: "git-wiki-bs-united"
```




================================================
FILE: wiki/.gitkeep
================================================
[Empty file]


================================================
FILE: .env-files/Dockerfile.github
================================================
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

