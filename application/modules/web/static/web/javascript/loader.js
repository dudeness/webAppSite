'use strict';

var dependencies = [
    'ngResource',
    'ngAnimate',

    '.web.controller',
    '.web.directive.section'
];

_.forEach(environment.modules, function(name) {
    if (name !== 'web') {
        dependencies.push('#' + name);
    }

});

angular.module('#', dependencies);