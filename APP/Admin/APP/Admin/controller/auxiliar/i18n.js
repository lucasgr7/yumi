yumiAdmin.controller('linguagemControle', function ($translate, $scope, $rootScope) {
    $scope.mudarLinguagem = function (linguagem, flag) {
        $rootScope.linguagem_selecionada = flag;
        $translate.use(linguagem);
    }
});