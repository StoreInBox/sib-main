angular.module('SIBAdmin').controller('CategoriesController', function($rootScope, $scope, Restangular) {
  var vm = this;

  var baseCategories = Restangular.all('api/products/categories');

  // This will query /accounts and return a promise.
  baseCategories.getList().then(function(categories) {
    vm.topCategories = [];
    for (var i = categories.length - 1; i >= 0; i--) {
      if (!categories[i].parent) {
        categories[i].showChildren = false;
        vm.topCategories.push(categories[i]);
      }
    };
  });

  vm.disableOrderSave = true;

  function onDragStart(tbody, row, old_index) {
    $(row).addClass('info');
    $(row).css('cursor', 'all-scroll');
  };

  function onDragEnd(tbody, row, old_index) {
    $(row).removeClass('info');
    $(row).css('cursor', 'pointer');
  };

  function onDrop(tbody, row, new_index, old_index) {
    $(row).removeClass('info');
    $(row).css('cursor', 'pointer');
    if (new_index != old_index) {
      var button = $('[backend-id="save-categories-ordering"]');
      button.removeClass('disabled');
      button.removeClass('btn-default');
      button.addClass('btn-warning');
    }
  };

  new RowSorter(
    '#top-categories',
    options = {
      onDragStart: onDragStart,
      onDragEnd: onDragEnd,
      onDrop: onDrop
    }
  );

  vm.deleteCategory = function(category) {
    category.remove();
    vm.topCategories = _.without(vm.topCategories, category);
  }

  vm.showCategoryChildren = function(category) {
    category.showChildren = !category.showChildren;
    if (category.showChildren) {
      selector = '#child-categories-' + category.id;
      new RowSorter(
        selector,
        options = {
          onDragStart: onDragStart,
          onDragEnd: onDragEnd,
          onDrop: onDrop
        }
      );
    }
  }

  vm.addCategory = function() {
    $rootScope.$broadcast('addCategory');
  }

  vm.editCategory = function(category) {
    $rootScope.$broadcast('editCategory', category);
  }

  vm.addChildCategory = function(parent) {
    $rootScope.$broadcast('addChildCategory', parent);
  }

  vm.editChildCategory = function(parent, category) {
    $rootScope.$broadcast('editChildCategory', parent, category);
  }

});