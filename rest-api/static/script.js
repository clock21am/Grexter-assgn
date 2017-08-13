var app = angular.module("myapp", []);

app.controller("myCtrl", function($scope) {
    $scope.query_name = "To display age and Name from the students table";
});

var appu = angular.module("appi", []);

appu.controller("myctrl", function($scope) {
    $scope.query_name = "To display age and Name from the students table";
});
