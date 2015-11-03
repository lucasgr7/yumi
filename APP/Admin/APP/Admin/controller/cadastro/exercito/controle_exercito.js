yumiAdmin.service('exercito_service', function ($http, $rootScope) {
    return {
        get: function (scope) {
            return $http.get($rootScope.servidor_url + "/exercito/list/?format=json", {});
        }
    };
});
yumiAdmin.controller('controle_exercito', function ($rootScope, $scope, $routeParams, $http, $location, $translate, usuario_service, exercito_service) {

    $scope.init = function () {
        try {
            if ($rootScope.exercito !== undefined) {
                $scope.exercito = $rootScope.exercito;
                $rootScope.exercito = undefined;
            } else {
                $scope.usuario = {};
            }
            $scope.optionsRandom = {
                randomColors: 30,
                total: 50
            }
            usuario_service.getUsuarios().success(function (data, status) {
                $scope.usuarios = data;
                if ($scope.exercito !== undefined) {
                    for (var i = 0; i < $scope.usuarios.length; i++) {
                        var usuario = $scope.usuarios[i];
                        if ($scope.exercito.usuario === usuario.id) {
                            $scope.exercito.usuario = usuario;
                        }
                    }
                }
            });
        } catch (e) {
            alert(e);
        }
    }

    $scope.salvar = function () {
        try {
            $http.post($rootScope.servidor_url + "/exercito/inserir/", $scope.exercito).success(function (data, status) {
                alert($translate.instant("SUCCESS_UPDATE_MESSAGE"));
                $location.path('/cadastro/exercito').replace();
            });
        } catch (e) {
            alert(e);
        }
    };

    $scope.listarExercitos = function () {
        try {
            exercito_service.get().success(function (data, status) {
                if (data !== undefined) {
                    $scope.exercitos = data;
                }
            });
        } catch (e) {
            alert(e);
        }
    };

    $scope.editar = function (exercito) {
        try {
            $rootScope.exercito = exercito;
            $location.path('/cadastro/exercito/editar').replace();
        } catch (e) {
            alert(e);
        }
    }

    $scope.excluir = function (exercito) {
        try {
            if (confirm($translate.instant("CONFIRM_DELETE_MESSAGE"))) {
                $http.get($rootScope.servidor_url + "/exercito/delete/" + exercito.id).success(function (data, status) {
                    alert("Excluido com sucesso!");
                    $scope.listarExercitos();
                });
            }
        }
        catch (e) {
            alert(e);
        }
    }
    $scope.cor_mudou = function () {
        $rootScope.cor_painel = $scope.exercito.cor;
    }
});