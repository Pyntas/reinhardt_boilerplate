module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    config: grunt.file.readJSON('config.json'),
    compass: {
      dist: {
        options: {
          sassDir: '<%= config.stylesDir %>/sass',
          cssDir: '<%= config.stylesDir %>/css',
          imagesDir: '<%= config.staticDir %>/images',
          fontsDir: '<%= config.staticDir %>/fonts',

        }
      }
    },
    concat: {
      app: {
        src: ['<%= config.scriptsDevDir %>/**/*.js'],
        dest: '<%= config.scriptsBuildDir %>/<%= pkg.name %>.js'
      },
      vendor: {
        src: [
          '<%= config.staticDir %>/vendor/jquery/dist/jquery.min.js',
          '<%= config.staticDir %>/vendor/bootstrap/dist/js/bootstrap.min.js',
        ],
        dest: '<%= config.scriptsBuildDir %>/vendor.js'
      }
    },
    uglify: {
      options: {
        // sourceMap: true,
        // sourceMapIncludeSources: true,
        banner: '/*! <%= pkg.name %>  */\n'
      },
      dist: {
        files: {
          '<%= config.scriptsBuildDir %>/<%= pkg.name %>.min.js': ['<%= concat.app.dest %>'],
          '<%= config.scriptsBuildDir %>/vendor.min.js': ['<%= concat.vendor.dest %>'],
        }
      }
    },
    cssmin: {
      combine: {
        files: {
          '<%= config.stylesDir %>/<%= pkg.name %>.min.css': ['<%= config.stylesDir %>/**/*.css'],
        }
      },
    },
    watch: {
      compass: {
        files: '<%= config.stylesDir %>/**/*.{scss,sass}',
        tasks: ['compass']
      },
      // Add tasks here to run on every file saved change, as you would do for coffeescript,
    },
    shell: {
      runserver: {
          command: function(settings){
            if (settings){
              return 'echo running <%= pkg.name %> with settings'+settings+' && '+'python manage.py runserver --settings=settings.'+settings;
            } else {

              return 'echo running <%= pkg.name %> with settings local && python manage.py runserver --settings=settings.local';
            }
          },
          options: {
            stdout: true
          }
      }
    }
  });


  grunt.registerTask('build',
    ['compass', 'cssmin', 'concat', 'uglify']);


  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-shell');


  grunt.registerTask('default',['watch']); // task by  running just grunt.
  grunt.registerTask('serve', ['shell:runserver']); // run server
}
