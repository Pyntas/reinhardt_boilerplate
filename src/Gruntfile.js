module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    compass: {
      dist: {
        options: {
          sassDir: 'static/stylesheets/sass',
          cssDir: 'static/stylesheets/css'
        }
      }
    },
    watch: {
      css: {
        files: 'static/stylesheets/**/*.{scss,sass}',
        tasks: ['compass']
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.registerTask('default',['watch']);
};
