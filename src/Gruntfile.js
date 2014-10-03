module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    config: grunt.file.readJSON('package.json').config,
    bower: grunt.file.readJSON('.bowerrc'),

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

    // Concat JS files from the app and the vendor libraries used
    concat: {
      app: {
        src: '<%= config.scriptsDevDir %>/app/**/*.js',
        dest: '<%= config.scriptsBuildDir %>/<%= pkg.name %>.js'
      },

      reduced_vendor: {
        src: ['<%= bower.directory %>/jquery/dist/jquery.js',
              '<%= bower.directory %>/bootstrap/js/bootstrap.js',
        ],
        dest: '<%= config.scriptsBuildDir %>/reduced_vendor.js'
      }
    },

    // Uglify and minified concatenated files
    uglify: {
      options: {
        sourceMap: true,
        sourceMapIncludeSources: true,
        banner: '/*! <%= pkg.name %>  */\n'
      },
      dist: {
        files: {
          '<%= config.scriptsBuildDir %>/<%= pkg.name %>.min.js': ['<%= concat.app.dest %>'],
          '<%= config.scriptsBuildDir %>/reduced_vendor.min.js': ['<%= concat.reduced_vendor.dest %>'],
        }
      }
    },

    // Minify css and generated css files
    cssmin: {
      combine: {
        files: {
          '<%= config.stylesDir %>/<%= pkg.name %>.css': [
            '<%= config.stylesDir %>/css/**/*.css'
          ],
        }
      },
      minify: {
        expand: true,
        cwd: '<%= config.stylesDir %>/',
        src: ['<%= pkg.name %>.css',],
        dest: '<%= config.stylesDir %>/',
        ext: '.min.css'
      }
    },

    // Watch file changes to execute the task
    watch: {
      compass: {
        files: '<%= config.stylesDir %>/**/*.{scss,sass}',
        tasks: ['compass']
      },

      scripts: {
        files: ['<%= config.scriptsDevDir %>/app/**/*.js',

        ],
        tasks: ['concat:app', ],
        options: {
          interrupt: true,
        }
      }
    }

  });



  grunt.registerTask('css', ['compass', 'cssmin']);

  grunt.registerTask('js', ['concat', 'uglify']);

  // Prepare for production
  grunt.registerTask('build',
    ['compass', 'cssmin', 'concat', 'uglify']);


  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-requirejs');


  grunt.registerTask('default',['watch']); // task by running just `grunt` command.
};

