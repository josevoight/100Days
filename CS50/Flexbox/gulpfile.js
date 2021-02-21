var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');

gulp.task('style', async function() {
    gulp.src('css/style.css')
    .pipe(autoprefixer())
    .pipe(gulp.dest('build'))

}); 