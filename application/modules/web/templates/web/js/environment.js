'use strict';

var environment = {
    installedModules: [{% for module in INSTALLED_MODULES %}'{{module}}', {% endfor %}],
    module: function(name) {
        return {
            template: {
                view: '/static/' + name + '/template/view/'
            }
        };
    }
};