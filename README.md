# Group webpage

This is the source code of the [group webpage](https://mcgill-nlp.github.io/), which was built using [Jekyll](https://github.com/jekyll/jekyll) and [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes).

## Steps to contribute

For any type of contribution, please follow these steps:
1. [Fork](./fork) the repository.
2. Add your contribution by editing the desired files.
3. Create a pull request: Click on the [Pull Request](https://github.com/McGill-NLP/group-webpage/pulls) tab and select "New pull request". Select the repository you forked and modified.
4. Wait for a team member to review and merge your pull request.

## Add new member

Navigate to [_data/authors.yml](./_data/authors.yml) and add the desired information at the end of the file. It has to follow the following template:

```yaml
<username>:
  name: # Full Name
  role: # One of: "Faculty", "Postdoc", "PhD", "Master", "Undergraduate", "Intern"
  date: "Jan 2042" # When the new member joined the group. Must be in the "MMM YYYY" format, or "Fall"/"Winter" instead of month.
  alumni: false # Whether the new member is an alumni
  avatar: "/assets/images/bio/default.jpg"  # Path to your image
  bio: # Describe about the new member (optional)
  links:  # optional
    - name: "Website"
      url: # Link to the new member's website
    - name: "GitHub"
      url: # Link to the new member's GitHub profile
    - name: "LinkedIn"
      url: # Link to the new member's LinkedIn profile
    - name: "Twitter"
      url: # Link to the new member's Twitter profile
    - name: "Scholar"
      url: # Link to the new member's Google Scholar profile
      icon: "fas fa-fw fa-graduation-cap"  # A custom icon is needed here
```

Replace `<username>` with your firstname or nickname. If someone already has the same name, you can append your lastname and/or start date, to your preference. This will be what you will use when writing a blog post or a publication abstract.

## Front matters and YAML

For any type of page or post (publication, blog post, course description), we use something called ["Front Matters"](https://jekyllrb.com/docs/front-matter/) to tell Jekyll about the purpose of the file. This is a block of YAML text at the beginning of the file. The rest of the file is regular [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

## Modifying a page

To modify a page, navigate to [_pages](_pages/) and update the desired file. If you add a new file, you will also need to edit the [_data/navigation.yml](./_data/navigation.yml) file with the correct relative URL.

## Creating a post

### Publication link

To add a link to a publication, create a new file called `<YYYY>-<MM>-<DD>-<shorthand>.md` in the [`_posts/papers` directory](https://github.com/McGill-NLP/group-webpage/tree/master/_posts/papers). Note that `<shorthand>` will determine the URL of the file, so choose carefully.

Every file should start with the following:
```yaml
---
title: "My cool paper" # Add official title
author: <username> # Add name to show profile in sidebar
categories: Publications # Used to list all posts about publications in /publications/
names: "Firstname lastname, Firstname lastname, ..." # names of all authors
link: https://arxiv.org/abs/1234.5678 # link to paper
code: https://github.com/McGill-NLP/example  # link to code (optional)
webpage: https://mcgill-nlp.github.io/project  # link to project (optional)
video: https://youtube.com  # link to video (optional)
twitter: https://twitter.com/username  # link to twitter thread (optional)
demo: https://project-demo.com  # link to interactive demo (optional)
thumbnail: /assets/images/papers/figure.jpg  # link to a thumbnail (optional)
venue: ACL 2022  # venue and year of the paper
tags: ACL # tag of the paper (exclude year, use shorthand)
---
```

Then, it should be followed with the content in markdown:

```markdown

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract
<!-- Your abstract here -->
```

Note that `include display-publication-links.html` will display the icons and links to code, webpage, tweets, etc. `pub=page` refers to the page object, which is handled by Jekyll.


### Blog post

To write a blog post, create a new file called `<YYYY>-<MM>-<DD>-<shorthand>.md` in the [`_posts/blog` directory](_posts/blog). Note that `<shorthand>` will determine the URL of the file, so choose carefully.

Every file should start with the following:
```yaml
---
title: "My cool blog post" # Add title
author: <username> # Add your name (see above)
categories: # Used to list all blog posts in /blog/
  - Blog
tags: # Choose tag(s) not clashing with a conference name (optional)
  - Pytorch
excerpt_separator: "<!--more-->"  # Separate the excerpt from the body (optional)
last_modified_at: "2016-03-09" # Add modification date if relevant (optional)
---
```

Followed by the content in markdown:

```markdown
*Your summary here will be previewed on `/publications/`*

<!--more-->

Some starting statement

## Section in the paper

More content.
```

### Course description

```markdown
---
title: "COMP XYZ - Semester YYYY"  # Add course code, followed by the semester it's taught
author: siva  # Name of the instructor
categories:
  - Teaching  # Used to list all posts describing a course in /teaching/
tags:
  - Winter 2022  # Semester
link: "https://docs.google.com/document/d/..." # Link to an external course description
---

*Name of the course*
```

## Advanced

### Editing CSS

If you need to modify some CSS attributes directly, you need to use sass. You can create a new file in [_sass/custom](_sass/custom) and import it inside [_sass/main.scss](_sass/main.scss).

### Troubleshooting

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.
