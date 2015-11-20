var yumiAdmin = angular.module('yumiAdmin', ['ngRoute', 'pascalprecht.translate', 'ngjsColorPicker'
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
        }).when('/cadastro/usuario/editar', {
            templateUrl: 'view/template/cadastro/usuario/form.html',
            controller: 'controle_usuario'
        }).when('/cadastro/exercito/', {
            templateUrl: 'view/template/cadastro/exercito/lista.html',
            controller: 'controle_exercito'
        }).when('/cadastro/exercito/novo', {
            templateUrl: 'view/template/cadastro/exercito/form.html',
            controller: 'controle_exercito'
        }).when('/cadastro/exercito/editar', {
            templateUrl: 'view/template/cadastro/exercito/form.html',
            controller: 'controle_exercito'
        }).when('/cadastro/tatic', {
            templateUrl: 'view/template/cadastro/tatic/form.html',
            controller: 'controle_exercito'
        }).when('/cadastro/soldado/', {
            templateUrl: 'view/template/cadastro/soldado/lista.html',
            controller: 'controle_soldato'
        }).otherwise({
            redirectTo: '/'
        });
    }]);

yumiAdmin.config(['$translateProvider', function ($translateProvider) {

        // Simply register translation table as object hash
        $translateProvider.useStaticFilesLoader({
            prefix: 'view/language/locale-',
            suffix: '.json'
        });
        $translateProvider.preferredLanguage('pt-BR');
    }]);

yumiAdmin.run(function($rootScope){
    $rootScope.servidor_url = 'http://127.0.0.1:90';
    $rootScope.cor_painel = "#3f51b5";
})