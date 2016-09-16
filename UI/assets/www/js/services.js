angular.module('starter.services', [])

.factory('Anatomies', function($http, $ionicPopup) {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var anatomies = [];

  return {
    all: function() {
      return anatomies;
    },

    getDataBeginner: function() {
      return $http.get('http://therapy.cfapps.io/main/children/folder/1/').
                                      success(function(data) {
                                          anatomies = data;
                                          return data;
                                      })
                                      .error(function(data)
                                      {
                                      var alertPopup = $ionicPopup.alert({
                                           title: 'Try again later!',
                                           template: 'No Connection Found.'
                                         });
                                         return null;
                                      });
    },
    getDataAdvanced: function() {
          return $http.get('http://therapy.cfapps.io/main/children/folder/2/').
                                          success(function(data) {
                                              anatomies = data;
                                              return data;
                                          })
                                          .error(function(data)
                                          {
                                          var alertPopup = $ionicPopup.alert({
                                               title: 'Try again later!',
                                               template: 'No Connection Found.'
                                             });
                                             return null;
                                          });
        },

        getDataExpert: function() {
              return $http.get('http://therapy.cfapps.io/main/children/folder/3/').
                                              success(function(data) {
                                                  anatomies = data;
                                                  return data;
                                              })
                                              .error(function(data)
                                              {
                                              var alertPopup = $ionicPopup.alert({
                                                   title: 'Try again later!',
                                                   template: 'No Connection Found.'
                                                 });
                                                 return null;
                                              });
            }
  };
})

.factory('SubAnatomies', function($http, $ionicPopup){
    var subanatomies = [];

       return {
          all: function() {
            return subanatomies;
          },

          getData: function(folder_id) {
          return $http.get('http://therapy.cfapps.io/main/children/folder/'+folder_id).
                                          success(function(data) {
                                              subanatomies = data;
                                              return data;
                                          })
                                          .error(function(data)
                                          {
                                          var alertPopup = $ionicPopup.alert({
                                               title: 'Try again later!',
                                               template: 'No Connection Found.'
                                             });
                                             return null;
                                          });
          }
        };
})

.factory('Exercises', function($http, $ionicPopup)
{
    var exercises=[];


    return {
              all: function() {
                return exercises;
              },

              getData: function(folder_id)
              {
                return $http.get('http://therapy.cfapps.io/main/children/video/'+folder_id).
                                success(function(data) {
                                    exercises = data;
                                    return data;
                                })
                                .error(function(data)
                                {
                                var alertPopup = $ionicPopup.alert({
                                     title: 'Try again later!',
                                     template: 'No Connection Found.'
                                   });
                                   return null;
                                });

              }
            };



});
