'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function () {
  return gulp.src('./src/odfauthors/theme/theme/scss/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./src/odfaufthors/theme/theme/styles'));
});

gulp.task('default', function () {
  gulp.watch('./src/odfauthors/theme/theme/**/*.scss', ['sass']);
});
