(function () {
  'use strict';

  angular.module('genomesequencecheck.demo').run(['$http', run])
        .config(['$routeProvider', config])
        .run(['$http', run]);

  function config($routeProvider) {

    $routeProvider
      .when('/', {
        templateUrl: '/static/html/genomesequencecheck.html',
        controller: 'GenomeSequenceCheckController',
      })
      .otherwise('/');
  }

  function run($http){
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
