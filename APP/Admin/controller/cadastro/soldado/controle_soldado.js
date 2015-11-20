yumiAdmin.service('soldado_service', function ($http, $rootScope) {
    return {
        getSoldados: function (scope) {
            return $http.get($rootScope.servidor_url + "/soldado/list/?format=json", {});
        }
    };
});
yumiAdmin.controller('controle_soldato', function ($rootScope, $scope, $routeParams, $http, $location, $translate, soldado_service) {

    
    //$scope.init = function () {
    //    $scope.soldatos = {};
        //try {
        //    if ($rootScope.soldado !== undefined) {
        //        $scope.soldado = $rootScope.soldado;
        //        $rootScope.soldado = undefined;
        //    } else {
        //        $scope.soldado = {};
        //    }
        //} catch (e) {
        //    alert(e);
        //}
    //}
    
    $scope.listarSoldados = function () {
        try {
            soldado_service.getSoldados().success(function (data) {
                if (data !== undefined) {
                    $scope.soldados = data;
                }
            });
        } catch (e) {
            alert(e);
        }
    };

});