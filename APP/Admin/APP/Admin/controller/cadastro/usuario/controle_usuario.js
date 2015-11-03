yumiAdmin.service('usuario_service', function ($http, $rootScope) {
    return {
        getUsuarios: function (scope) {
            return $http.get($rootScope.servidor_url + "/usuario/list/?format=json", {});
        }
    };
});
yumiAdmin.controller('controle_usuario', function ($rootScope, $scope, $routeParams, $http, $location, $translate, usuario_service) {

    $scope.init = function () {
        try {
            if ($rootScope.usuario !== undefined) {
                $scope.usuario = $rootScope.usuario;
                $rootScope.usuario = undefined;
            } else {
                $scope.usuario = {};
            }
        } catch (e) {
            alert(e);
        }
    }

    $scope.salvarUsuario = function () {
        try {
            if ($scope.usuario.senha === $scope.usuario.confirma_senha) {
                $http.post($rootScope.servidor_url + "/usuario/inserir/", $scope.usuario).success(function (data, status) {
                    alert("inserido com sucesso!");
                    $location.path('/cadastro/usuario').replace();
                });
            } else {
                alert("Erro senhas não são identicas!");
            }
        } catch (e) {
            alert(e);
        }
    }

    $scope.listarUsuarios = function () {
        try {
            usuario_service.getUsuarios().success(function (data, status) {
                if (data !== undefined) {
                    $scope.usuarios = data;
                }
            });
        } catch (e) {
            alert(e);
        }
    };

    $scope.editarUsuario = function (usuario) {
        try {
            $rootScope.usuario = usuario;
            $location.path('/cadastro/usuario/editar').replace();
        } catch (e) {
            alert(e);
        }
    }

    $scope.excluirUsuario = function (usuario) {
        try {
            if (confirm($translate.instant("CONFIRM_DELETE_MESSAGE"))) {
                $http.get($rootScope.servidor_url + "/usuario/delete/" + usuario.id).success(function (data, status) {
                    alert("Excluido com sucesso!");
                    $scope.listarUsuarios();
                });
            }
        } catch (e) {
            alert(e);
        }
    }
});