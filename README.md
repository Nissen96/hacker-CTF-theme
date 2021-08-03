# The Hacker CTF theme

Hacker CTF is a Jekyll theme for GitHub Pages based on [The Hacker Plus Theme](https://github.com/CaptainIRS/hacker-plus-theme), which itself is based on [The Hacker Theme](https://pages-themes.github.io/hacker). The Hacker Plus Theme was optimized for writing CTF writeups, solutions, and blog posts, and I encourage you to take a look at that and all the features it adds on top of The Hacker Theme.

As I needed a theme for exclusively writing CTF writeups, the Hacker CTF theme focuses only on this. It removes the functionality for Codechef Problem solutions, blog posts, and comments to reduce clutter and unneeded functionality. Adding new writeups is very simple with the included script.

*Run the script -> Write in markdown -> Push commit -> The site is generated automatically*

*You can [preview the theme to see what it looks like](https://Nissen96.github.io/hacker-ctf-theme), and start [using it immediately](#usage).*
*You can also visit my [personal site](https://Nissen96.github.io) to see the theme used in an actual website*

*The theme is optimized for easy use in VS Code with some useful snippets to reduce the burden*

## Features Kept From The Hacker Plus Theme

* UI improvements with mobile compatibility
* Scripts for automatic generation of boilerplate templates for each writeup
* Social media links
* Easy google site verification, google analytics integration
* Post share buttons (Facebook, Twitter and LinkedIn)
* Automatic sitemap generation for improved SEO
* Search by tag functionality
* Anchors for subheadings
* Code markdown using Prism.js
  * Line number support
  * Code copy and download support
  * Syntax highlighting for numerous languages
  * Support for font ligatures in code like that for `=>`, `!=`, etc.
* Optimisations for CTF Writeups:
  * Automatically generate the top level writeups.html page, grouping CTFs by year
  * Automatically add side nav bar to show other writeups in the same CTF
  * Automatically generate beautiful headers for each writeup

*Some useful snippets for markdown included in the template project:*

| Prefix       | Description                                        |
|:-------------|:---------------------------------------------------|
| cmdbashdown  | To add a code block with bash prompt and download  |
| cmdbash      | To add a code block with bash prompt               |
| cmdotherdown | To add a code block with other prompt and download |
| cmdother     | To add a code block with other prompt              |
| down         | Downloadable code                                  |
| linenum      | Code block with line numbers                       |
| linenumdown  | Downloadable code with line numbers                |

## Features added by The Hacker CTF Theme

* Top level writeups page is made the front page
* Search by CTF title, challenge title, and tag
* Allow multiword tags and make all tags clickable
* Markdown in challenge descriptions
* UI/UX improvements


## Usage

To use the Hacker CTF theme:

*(Assuming that you have VS Code and python already installed)*

1. Go to [Nissen96/hacker-ctf-template](https://github.com/Nissen96/hacker-ctf-template) and click on 'Use this template'. Then fill in the asked details. This repo contains the basic structure, useful snippets for markdown in VS Code and a Gemfile in case you want to build and test the site locally
2. Enable GitHub Pages in your repository
3. Clone the repo locally
4. Fill in in the desired fields the `_config.yml` file and push the commits to have a working site
5. To get started, follow the instructions below (in VS Code):

Writing CTF Writeups:

1. Open a new terminal window in VS Code
2. Run `python scripts/writeup_gen.py` and fill in the details. The script generates the required writeup files and asset directory for the CTF
3. Write the writeups in markdown and push the commits to your repo

## Customizing

### Stylesheet

If you'd like to add your own custom styles:

1. Create a file called `/assets/css/style.scss` in your site
2. Add the following content to the top of the file, exactly as shown:
    ```scss
    ---
    ---

    @import "{{ site.theme }}";
    ```
3. Add any custom CSS (or Sass, including imports) you'd like immediately after the `@import` line

## Roadmap

See the [open issues](https://github.com/Nissen96/hacler-ctf-theme/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are welcome! If you'd like a feature to be added, submit an issue or make a pull request

### Previewing the theme locally

If you'd like to preview the theme locally (for example, in the process of proposing a change):

1. Clone down the theme's repository (`git clone https://github.com/Nissen96/hacker-ctf-theme`)
2. `cd` into the theme's directory
3. Run `gem install bundler` and `bundle install` to install the necessary dependencies
4. Run `bundle exec jekyll serve` to start the preview server
5. Visit [`localhost:4000`](http://localhost:4000) in your browser to preview the theme

## License

The theme is licensed under MIT License
