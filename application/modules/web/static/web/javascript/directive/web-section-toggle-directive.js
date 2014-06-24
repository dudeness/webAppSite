'use strict';

angular.module('.web.directive.section.toggle', [])
    .directive('webSectionToggle', ['$rootScope',
        function() {

            return {
                restrict: 'A',
                link: function(scope, element, attr) {
                    console.log('webSectionToggle', attr);
                }
            };
        }
        ]);