angular

  .module('SIBAdmin', ['restangular', 'ngTagsInput', 'ngFileUpload', 'ui.sortable'])

  .config(function (RestangularProvider) {
    RestangularProvider.setRequestSuffix('/');
  })

  .config(['$httpProvider', function($httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);
