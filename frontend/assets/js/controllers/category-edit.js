angular.module('SIBAdmin').controller('CategoryEditController', function($rootScope, $scope, Upload, Restangular) {
  var vm = this,
      baseURL = 'api/products/categories';

  vm.category = {};

  $scope.$on('editCategory', function(event, parent, category) {
    vm.isUpdate = category.hasOwnProperty('id')
    $scope.file = null;
    vm.parent = parent;
    vm.category = category;
    $('#category-edit').modal('toggle');
  });

  vm.saveInProgress = false;
  vm.save = function() {
    vm.isUpdate = vm.category.hasOwnProperty('id');
    image = $scope.file;

    vm.validationErrors = {}
    if (!vm.category.name) vm.validationErrors.emptyName = true;
    if (!image && !vm.isUpdate) vm.validationErrors.emptyImage = true;

    vm.isError = !$.isEmptyObject(vm.validationErrors)
    if (vm.isError) {
      vm.saveInProgress = false;
      return
    }
    vm.saveInProgress = true;

    url = baseURL + '/';
    if (vm.isUpdate) url += vm.category.id + '/';

    data = {name: vm.category.name, characteristics: JSON.stringify(vm.category.characteristics)}
    if (vm.parent) {
      data.parent = vm.parent.id
    } else {
      data.parent = null;
    }
    if (image) data.image = image;
    method = 'POST';
    if (vm.isUpdate) method = 'PATCH';

    console.log(data.toSource());
    Upload.upload({
      url: url,
      data: data,
      method: method
    }).then(function(response) {
      newCategory = response.data;
      vm.saveInProgress = false;
      $('#category-edit').modal('hide');
      if (!vm.isUpdate) {
        $rootScope.$broadcast('categoryAdded', vm.parent, newCategory);
      } else {
        $rootScope.$broadcast('categoryUpdated', vm.parent, vm.category, newCategory);
      }
      $scope.file = null;
    });
  }

});
