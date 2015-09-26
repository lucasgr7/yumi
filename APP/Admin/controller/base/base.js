var yumiAdmin = angular.module('yumiAdmin', ['ngRoute', 'pascalprecht.translate'
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

yumiAdmin.config(['$translateProvider', function ($translateProvider) {

        // Simply register translation table as object hash
        $translateProvider.useStaticFilesLoader({
            prefix: 'view/language/locale-',
            suffix: '.json'
        });
        $translateProvider.preferredLanguage('pt-BR');
    }]);