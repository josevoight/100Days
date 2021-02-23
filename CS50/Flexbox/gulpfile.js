var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');

gulp.task('styles', async function(){
    return gulp.src('css/style.css')
   .pipe(autoprefixer('last 2 versions'))
   .pipe(gulp.dest ('build'));
});

gulp.task('watch',  function(){
    gulp.watch('css/style.css', gulp.series(['styles']));
});