miapp=angular.module('MyApp.controllers', []);

miapp.controller('controlador', function ($scope) {
         $scope.mensaje="deiner";
  });

miapp.controller('json', function($scope, $http) {
    $http.get("http://www.w3schools.com/angular/customers.php")
    .success(function(response) {
            $scope.names = response.records;
        });
});

miapp.controller('json1', function($scope, $http) {
    $http.get("https://restcountries.eu/rest/v1/all")
    .success(function(response) {
            $scope.name = response;
        });
});

miapp.controller('DRF', function($scope, $http) {
    var url="https://reinarbackend.herokuapp.com";
    $http.get(url+"/api/colegio/")
    .success(function(response) {
            $scope.name = response;
        });

   $scope.getitem=function(){

       $http.get("http://calm-refuge-6071.herokuapp.com/api/296")
           .success(function(response){
               $scope.codigo =response.id;
               $scope.nombre =response.description;
               $scope.telefono =response.done;
            alert($scope.codigo + $scope.nombre + $scope.telefono)
           });

   };

    $scope.eliminar=function(item){

    }
});

miapp.controller('alerta', function($scope) {
    $scope.mensaje="hola deiner"
        $scope.Show=function(){
            alert($scope.mensaje);
        };

});

miapp.controller('AddEmployeeController', function ($scope, SinglePageCRUDService) {
    $scope.EmpNo = 0;
    //The Save scope method used to define the Employee object and
    //post the Employee information to the server by making call to the Service
    $scope.save = function () {
        var Employee = {
            EmpNo: $scope.EmpNo,
            EmpName: $scope.EmpName,
            Salary: $scope.Salary,
            DeptName: $scope.DeptName,
            Designation: $scope.Designation
        };

        var promisePost = SinglePageCRUDService.post(Employee);


        promisePost.then(function (pl) {
            $scope.EmpNo = pl.data.EmpNo;
            alert("EmpNo " + pl.data.EmpNo);
        },
              function (errorPl) {
                  $scope.error = 'failure loading Employee', errorPl;
              });

    };
});