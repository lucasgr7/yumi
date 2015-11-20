yumiAdmin.service('tatic_service', function ($http, $rootScope) {
    return {
        get: function (scope) {
            return $http.get($rootScope.servidor_url + "/tatic/list/?format=json", {});
        }
    };
});
yumiAdmin.controller('controle_tatic', function ($rootScope, $scope, $http, $location, $translate, tatic_service) {

    $scope.init = function () {
        try {
            if ($rootScope.tatic !== undefined) {
                $scope.tatic = $rootScope.tatic;
                $rootScope.tatic = undefined;
            } else {
                $scope.tatic = {
                    foto : 'http://www.jeaconf.org/UploadedFiles/Images/NoImage.jpg',
                    required_defesa : 5,
                    required_ofensa : 5,
                    required_estrategia : 5
                };
            }
        } catch (e) {
            alert(e);
        }
    }

    $scope.salvar = function () {
        try {
            $http.post($rootScope.servidor_url + "/tatic/inserir/", $scope.tatic).success(function (data, status) {
                alert($translate.instant("SUCCESS_UPDATE_MESSAGE"));
                $location.path('/cadastro/tatic').replace();
            });
        }
        catch (e) {
            alert(e);
        }
    }
    
    $scope.listar = function(){
        try{
            tatic_service.get().then(function(retorno){
               if(retorno !== undefined){
                   $scope.tatics = retorno.data;
               } 
            });
        }
        catch(e){
            alert(e);
        }
    }


});