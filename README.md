# ODFAuthors.org

This is the repository used to create and configure the improved website ODFAuthors.org.

The purpose of the updated ODFAuthors site is to create an up to date environment to work on documentation files.

# Development notes

## Theme development

There is a Gulp worflow in the theme package in order to watch and compile the
SCSS stylesheet to CSS. To proceed it is required:

```
  $ cd src/odfauthors.theme
  $ npm install
  $ npm start
```

Then you can modify the SCSS file in
```
  src/odfauthors.theme/src/odfauthors/theme/theme/scss/main.scss
```
and it will be compiled to the corresponding CSS in

```
  src/odfauthors.theme/src/odfauthors/theme/theme/styles/main.css
```
