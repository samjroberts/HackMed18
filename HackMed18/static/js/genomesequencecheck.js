(function(){
  'use strict';

  angular.module('genomesequencecheck.demo', ['ngRoute'])
      .controller('GenomeSequenceCheckController',
      ['$scope', '$http', GenomeSequenceCheckController]);

  function GenomeSequenceCheckController($scope, $http) {

    $scope.add =  function(bacteria, sequence){
      var genome = {
        sequence: sequence,
      };
      bacteria.genomes.push(genome);
    };

    $scope.data = [];
    $http.get('/genomesequencecheck/bacteria').then(function(response) {
      $scope.data = response.data;
    });
  }
}());
