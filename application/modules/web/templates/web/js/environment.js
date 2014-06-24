'use strict';

var environment = {
    modules: [{% for module in INSTALLED_MODULES %}'{{module}}', {% endfor %}],
    sections: {
        {% for module,config in SECTION_MODULES.items %}{{module}}: {
                toggleClass: '{{config.toggle_class}}'
            },
        {% endfor %}
    },
    module: function(name) {
        return {
            template: {
                view: '/static/' + name + '/template/view/'
            }
        };
    }
};