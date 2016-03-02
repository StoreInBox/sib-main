angular.module('SIBAdmin').controller('CategoriesController', function($rootScope, $scope, Restangular) {
  var vm = this,
      url = 'api/products/categories',
      baseCategories = Restangular.all(url);

  baseCategories.getList().then(function(categories) {
    vm.topCategories = [];
    for (var i = 0; i < categories.length; i++) {
      if (!categories[i].parent) {
        categories[i].showChildren = false;
        vm.topCategories.push(categories[i]);
      }
    };
  });

  vm.sortableOptions = {
    start: function(event, ui) {
      $(ui.item).find('.action-container').css('display', 'none');
      $(ui.item).find('.child-action-container').css('display', 'none');
    },
    stop: function(event, ui) {
      $(ui.item).find('.action-container').css('display', 'block');
      $(ui.item).find('.child-action-container').css('display', 'block');
    },
    update: function(event, ui) {
      vm.disableOrderSave = false;
    }
  }

  vm.deleteCategory = function(category) {
    baseCategories.customDELETE(category.id);
    vm.topCategories = _.without(vm.topCategories, category);
  }

  vm.deleteChildCategory = function(topCategory, childCategory) {
    baseCategories.customDELETE(childCategory.id);
    topCategory.children = _.without(topCategory.children, childCategory);
  }

  vm.showCategoryChildren = function(category) {
    category.showChildren = !category.showChildren;
  }

  vm.addCategory = function() {
    $rootScope.$broadcast('editCategory', null, {});
  }

  vm.editCategory = function(category) {
    $rootScope.$broadcast('editCategory', null, category);
  }

  vm.addChildCategory = function(parent) {
    $rootScope.$broadcast('editCategory', parent, {});
  }

  vm.editChildCategory = function(parent, category) {
    $rootScope.$broadcast('editCategory', parent, category);
  }

  vm.disableOrderSave = true;
  vm.orderingSaveInProcess = false;
  vm.saveCategoriesOrder = function() {
    if (vm.disableOrderSave) return;
    vm.orderingSaveInProcess = true;
    ordering = {};
    for (var i = 0; i < vm.topCategories.length; i++) {
      topCategory = vm.topCategories[i];
      ordering[topCategory.id] = i + 1;
      for (var j = 0; j < topCategory.children.length; j++) {
        childCategory = topCategory.children[j];
        ordering[childCategory.id] = j + 1;
      }
    }
    baseCategories.customPOST(ordering, 'update_ordering').then(function () {
      vm.orderingSaveInProcess = false;
      vm.disableOrderSave = true;
      $.notify({message: 'Categories ordering has been saved successfully.'});
    });
  }

  $scope.$on('categoryAdded', function(event, parent, category) {
    if (!parent) {
      vm.topCategories.push(category);
    } else {
      parent.children.push(category);
    }
    $.notify({message: 'Category "' + category.name + '" has been added successfully.'});
  });

  $scope.$on('categoryUpdated', function(event, parent, oldCategory, newCategory) {
    oldCategory.image = newCategory.image;
    $.notify({message: 'Category "' + newCategory.name + '" has been updated successfully.'});
  });

});