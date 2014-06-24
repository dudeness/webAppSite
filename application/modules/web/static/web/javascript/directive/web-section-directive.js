'use strict';

angular.module('.web.directive.section', [
    '.web.directive.section.toggle'
    ])
    .directive('webSection', ['$rootScope',
        function() {

            return {
                restrict: 'A',
                controller: ['$scope',
                    function($scope) {
                        $scope.init = function(module, element) {
                            $scope.section = {
                                element: $(element),
                                name: module,
                                toggleClass: environment.sections[module].toggleClass
                            };
                            $scope.section.toggled = $scope.section.element.hasClass($scope.section.toggleClass);
                        };
                    }],
                link: function(scope, element, attr) {
                    scope.init(attr.webSection, element);
                    console.log(scope.section);
                }
            };
        }]);