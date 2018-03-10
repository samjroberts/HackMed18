(function () {
  'use strict';

  angular.module('genomesequencecheck.demo')
    .directive('genomePlaceholder', GenomeDirective);

    function GenomeDirective() {
      return {
        templateUrl: '/static/genomesequencecheck/genome.html',
        restrict: 'E'
      };
    }
})();
