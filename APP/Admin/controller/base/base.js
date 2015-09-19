var yumiAdmin = angular.module('yumiAdmin', ['ngRoute',
//    'ngStorage',
//    'cfp.hotkeys',
//    'ngSanitize'
]);
yumiAdmin.config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when("/", {
            templateUrl: 'view/template/inicio.html',
        }).when('/cadastro/usuario', {
            templateUrl: 'view/template/cadastro/usuario/lista.html',
            controller: 'controle_usuario'
        }).when('/cadastro/usuario/novo', {
            templateUrl: 'view/template/cadastro/usuario/form.html',
            controller: 'controle_usuario'
        }).otherwise({
            redirectTo: '/'
        });
    }]);