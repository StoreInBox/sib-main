module.exports = function(grunt) {

    grunt.initConfig({

        copy: {
            main: {
                files: [
                    {
                        expand: true,
                        cwd: 'bower_components/admin-lte/dist',
                        src: ['*/*/*', '*/*'],
                        dest: 'static/admin/'
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/admin-lte/bootstrap',
                        src: ['*/*'],
                        dest: 'static/admin/bootstrap/',
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/admin-lte/plugins',
                        src: ['*/*'],
                        dest: 'static/admin/plugins/',
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/rowsorter/dist',
                        src: ['*'],
                        dest: 'static/admin/plugins/rowsorter',
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/ng-tags-input',
                        src: ['*.min.*'],
                        dest: 'static/admin/plugins/ng-tags-input',
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/ng-file-upload',
                        src: ['*.min.*'],
                        dest: 'static/admin/plugins/ng-file-upload',
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/angular-ui-sortable',
                        src: ['*.min.js'],
                        dest: 'static/admin/plugins/angular-ui-sortable',
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/remarkable-bootstrap-notify/dist',
                        src: ['*.min.js'],
                        dest: 'static/admin/plugins/remarkable-bootstrap-notify',
                    },
                    {
                        expand: true,
                        cwd: 'assets/js/',
                        src: ['*/*', '*'],
                        dest: 'static/js/',
                    }
                ],
            },
        },


        watch: {
            options: {
                livereload: true,
            },
            scripts: {
                files: ['assets/js/*/*.js','assets/js/*.js'],
                tasks: ['copy'],
                options: {
                    spawn: false,
                }
            },
        }

    });

    require('load-grunt-tasks')(grunt);

    grunt.registerTask('build', ['copy']);
    grunt.registerTask('run', ['build', 'watch']);
    grunt.registerTask('default', ['run']);

};
