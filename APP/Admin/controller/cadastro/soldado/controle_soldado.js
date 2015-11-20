yumiAdmin.service('soldado_service', function ($http, $rootScope) {
    return {
        getUsuarios: function (scope) {
            return $http.get($rootScope.servidor_url + "/soldado/list/?format=json", {});
        }
    };
});
yumiAdmin.controller('controle_usuario', function ($rootScope, $scope, $http, $location, $translate, usuario_service) {
    
    $scope.init = function () {
        try {
            if ($rootScope.soldado !== undefined) {
                $scope.soldado = $rootScope.soldado;
                $rootScope.soldado = undefined;
            } else {
                $scope.soldado = {};
            }
        } catch (e) {
            alert(e);
        }
    }
    
    
});