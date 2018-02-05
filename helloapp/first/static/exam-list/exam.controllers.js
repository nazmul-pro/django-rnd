(function ()
{
    'use strict';

    angular
    .module('app')
    .controller('ExamListCtrl', ExamListCtrl);

    /** @ngInject */
    function ExamListCtrl($scope)
    {
        var vm = this;
        $scope.name = "Ha-meem Group";

        init();
        function init() {
           

        }

    }
})();
