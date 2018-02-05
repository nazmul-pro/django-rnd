
  angular
    .module('app')
    .controller('MainCtrl', MainCtrl);

    function MainCtrl ($scope, $http) {
        $http.get('http://127.0.0.1:8000/families/')
        .then(function (response) {
            $scope.items = response.data;
            console.log(response);
        }, function (reason) {
            console.log(reason);
        });
        // $scope.items = [{
        //   name: 'Scuba Diving Kit',
        //   id: 7297510
        // }];
      }
      