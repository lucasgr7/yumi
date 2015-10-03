yumiAdmin.controller('controle_usuario', function ($rootScope, $scope, $routeParams, $http) {
    $scope.salvarUsuario = function () {
        if ($scope.usuario.senha === $scope.usuario.confirma_senha) {
            $http.post("localhost:90/usuario/inserir",$scope.usuario).success(function (data, status) {
                alert("inserido com sucesso!");
            });
        } else {
            alert("Erro senhas não são identicas!");
        }
    }
});