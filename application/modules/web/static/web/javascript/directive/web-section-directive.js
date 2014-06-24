'use strict';

angular.module('.web.directive.section', [])
    .directive('webSection', ['$rootScope',
        function() {

            return {
                restrict: 'A',
                controller: ['$scope',
                    function() {

                    }],
                link: function(scope, element, attr) {
                    console.log('webSection', attr);
                }
            };
        }]);