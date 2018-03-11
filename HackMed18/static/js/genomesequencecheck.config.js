(function () {
  'use strict';

  angular.module('genomesequencecheckpage', ['ngRoute'])
        .config(['$routeProvider', config])
        .run(['$http', run]);

  function config($routeProvider) {
    $routeProvider
      .when('/genomes', {
        templateUrl: '/static/html/genomesequencecheck.html',
        controller: 'GenomeSequenceCheckController',
      })
      .otherwise('/', {
        templateUrl: '/static/html/fileupload.html',
        controller: 'FileUploadController',
      });
  }

  function run($http){
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
