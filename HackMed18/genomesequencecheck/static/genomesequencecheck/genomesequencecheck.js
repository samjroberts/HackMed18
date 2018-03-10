(function(){
  'use strict';

  angular.module('genomesequencecheck.demo', [])
      .controller('GenomeSequenceCheckController',
      ['$scope', '$http', GenomeSequenceCheckController]);

  function GenomeSequenceCheckController($scope, $http) {

    $scope.add =  function(bacteria, sequence){
      var genomeindicator = {
        sequence: sequence,
      };
      bacteria.genomeindicators.push(genomeindicator);
    };

    $scope.data = [];
    $http.get('/genomesequencecheck/bacteria').then(function(response) {
      $scope.data = response.data;
    });
  }
}());
