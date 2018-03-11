(function () {
  'use strict';

  angular.module('genomesequencecheckpage')
    .directive('genomePlaceholder', GenomeDirective);

    function GenomeDirective() {
      return {
        templateUrl: 'static/html/genome.html',
        restrict: 'E'
      };
    }
})();
