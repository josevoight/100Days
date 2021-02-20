var gulp = require('gulp');
var autoprefixer = require('gulp-autoprofixer');

gulp.task('styles', function() {
    gulp.src('css/styles.css')
    .pipe(autoprefixer())
    .pipe(gulp.dest('build'))

}};