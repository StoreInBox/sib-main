angular.module('SIBAdmin').controller('CategoryEditController', function($scope, Restangular) {
  var vm = this;
  var baseCategories = Restangular.all('api/products/categories');

  vm.category = {};
  tags = ['test1', 'test2'];
  $scope.file = null;

  $scope.$watch('file', function () {
    console.log($scope.file);
  });

  $scope.$on('addCategory', function() {
    vm.category = {};
    $('#category-edit').modal('toggle');
  });

  $scope.$on('editCategory', function(event, category) {
    vm.category = category;
    $('#category-edit').modal('toggle');
  });

  $scope.$on('addChildCategory', function(event, parent) {
    vm.category = {parent: parent};
    $('#category-edit').modal('toggle');
  });

  $scope.$on('editChildCategory', function(event, parent, category) {
    vm.category = category
    vm.category.parent = parent;
    $('#category-edit').modal('toggle');
  });

});



// app.controller('MyCtrl', ['$scope', 'Upload', '$timeout', function ($scope, Upload, $timeout) {
//     $scope.$watch('files', function () {
//         $scope.upload($scope.files);
//     });
//     $scope.$watch('file', function () {
//         if ($scope.file != null) {
//             $scope.files = [$scope.file];
//         }
//     });
//     $scope.log = '';

//     $scope.upload = function (files) {
//         if (files && files.length) {
//             for (var i = 0; i < files.length; i++) {
//               var file = files[i];
//               if (!file.$error) {
//                 Upload.upload({
//                     url: 'https://angular-file-upload-cors-srv.appspot.com/upload',
//                     data: {
//                       username: $scope.username,
//                       file: file
//                     }
//                 }).then(function (resp) {
//                     $timeout(function() {
//                         $scope.log = 'file: ' +
//                         resp.config.data.file.name +
//                         ', Response: ' + JSON.stringify(resp.data) +
//                         '\n' + $scope.log;
//                     });
//                 }, null, function (evt) {
//                     var progressPercentage = parseInt(100.0 *
//                         evt.loaded / evt.total);
//                     $scope.log = 'progress: ' + progressPercentage +
//                       '% ' + evt.config.data.file.name + '\n' +
//                       $scope.log;
//                 });
//               }
//             }
//         }
//     };
// }]);