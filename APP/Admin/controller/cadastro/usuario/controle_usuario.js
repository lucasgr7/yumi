yumiAdmin.controller('controle_usuario', function ($rootScope, $scope, $routeParams, $http){
    
    $scope.salvarUsuario = function(){
        if($scope.usuario.senha === $scope.usuario.confirma_senha){
            //Função enviar para WS objeto
        }else{
            alert("Erro senhas não são identicas!");
        }
    }
});