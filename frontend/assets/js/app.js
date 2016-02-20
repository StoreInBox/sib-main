angular

  .module('SIBAdmin', ['restangular', 'ngTagsInput', 'ngFileUpload'])

  .config(function (RestangularProvider) {
      RestangularProvider.setRequestSuffix('/');
  });
