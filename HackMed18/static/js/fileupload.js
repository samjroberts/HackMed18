var myApp = angular.module('genomesequencecheckpage', ['ngRoute'])
    .directive('ngFiles', ['$parse', function ($parse) {

    function fn_link(scope, element, attrs) {
        var onChange = $parse(attrs.ngFiles);
        element.on('change', function (event) {
            onChange(scope, { $files: event.target.files });
        });
    };

    return {
        link: fn_link
    }
} ]);

myApp.controller('FileUploadController', ['$scope', '$http',

    function($scope, $http) {
      $scope.uploadFile = function(encodedFile) {
        var fileupload = {
          encodedFile: encodedFile,
        };

        var formdata = new FormData();
        $scope.getTheFiles = function ($files) {
            angular.forEach($files, function (value, key) {
                formdata.append(key, value);
            });
        };

        $scope.uploadFiles = function () {

            var request = {
                method: 'POST',
                url: '/genomesequencecheck/files/',
                data: formdata,
                headers: {
                    'Content-Type': undefined
                }
            };

            $http(request)
                .success(function (d) {
                    alert(d);
                })
                .error(function () {
                });
    }
  }
}
]);
