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
    $scope.Colegio = {}; //Objeto Actual
    var url="https://reinarbackend.herokuapp.com/api/colegio/";

    $http.get(url)
    .success(function(response) {
            $scope.name = response;
        });
   
   $scope.getitem=function(item){
       $http.get(url+item)
           
           .success(function(response){
              
               $scope.Colegio.codigo =response.codigo;
               $scope.Colegio.nombre =response.nombre;
               $scope.Colegio.telefono =response.telefono;
               $scope.Colegio.direccion=response.direccion;
               $scope.Colegio.estado=response.estado;
               $('#detalleModal').modal('show');
           
           });

   };
  
      $scope.add=function(){ 
        $('#formModal').modal('show');  
       $scope.Colegio.codigo ="c3";
        $scope.Colegio.nombre ="hola";
        $scope.Colegio.telefono =565656;
        $scope.Colegio.direccion="calle falsa 123";
        $scope.Colegio.estado="Moroso";
        $http.post(url,$scope.Colegio);

   };

 
});

miapp.controller('alerta', function($scope) {
    $scope.mensaje="hola deiner"
        $scope.Show=function(){
            alert($scope.mensaje);
        };

});
