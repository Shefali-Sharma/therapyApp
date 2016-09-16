angular.module('starter.controllers', [])


.controller('anatomyBeginnerCtrl', function($scope, Anatomies, $ionicModal, $ionicLoading) {
  $ionicLoading.show({
        template: 'Loading...'
      });
   Anatomies.getDataBeginner().then(function(response){
    $scope.anatomies=Anatomies.all();
    $ionicLoading.hide();
    }, function(){
    $ionicLoading.hide();
    });

})


.controller('anatomyAdvancedCtrl', function($scope, Anatomies, $ionicModal,$ionicLoading) {
     $ionicLoading.show({
            template: 'Loading...'
          });
    Anatomies.getDataAdvanced().then(function(response){
    $scope.anatomies=Anatomies.all();
    $ionicLoading.hide();
    }, function(){
         $ionicLoading.hide();
         });
})

.controller('anatomyExpertCtrl', function($scope, Anatomies, $ionicModal,$ionicLoading) {
    $ionicLoading.show({
                template: 'Loading...'
              });
    Anatomies.getDataExpert().then(function(response){
    $scope.anatomies=Anatomies.all();
    $ionicLoading.hide();
    }, function(){
         $ionicLoading.hide();
         });
})


.controller('subAnatomyCtrl', function($scope,$stateParams, SubAnatomies,$ionicLoading) {
     $ionicLoading.show({
                    template: 'Loading...'
                  });
      SubAnatomies.getData($stateParams.folder_id).then(function(response){
      $scope.subanatomies=SubAnatomies.all();
      $ionicLoading.hide();
      }, function(){
           $ionicLoading.hide();
           });
})


.controller('exercisesCtrl',function($scope, $cordovaFile, $http, $ionicPopup,$ionicModal,$ionicLoading,$stateParams,$ionicPlatform,Exercises){
  $ionicLoading.show({
                      template: 'Loading...'
                    });
  Exercises.getData($stateParams.folder_id).then(function(response){
  $scope.values=Exercises.all();
  $ionicLoading.hide();
  }, function(){
       $ionicLoading.hide();
       });

  $scope.showModal = function(templateUrl) {
  		$ionicModal.fromTemplateUrl(templateUrl, {
  			scope: $scope,
  			animation: 'slide-in-up'
  		}).then(function(modal) {
  			$scope.modal = modal;
  			$scope.modal.show();
  		});
  	}

	$scope.closeModal = function() {
		$scope.modal.hide();
		$scope.modal.remove();
	};

	$scope.clipSrc = '';

  $scope.playVideo = function() {
  	$scope.showModal('templates/video-popover.html');
  	var deregister = $ionicPlatform.registerBackButtonAction(function(){
            $scope.closeModal();
            deregister();
          },600);
  };


$scope.download = function(path,filename) {
    $ionicLoading.show({
      template: 'Downloading...'
    });
    var deregister = $ionicPlatform.registerBackButtonAction(function(){
        $ionicLoading.hide();
        deregister();
      },600);
    window.requestFileSystem(LocalFileSystem.PERSISTENT, 0, function(fs) {
        fs.root.getDirectory(
            "PhysioGuide",
            {
                create: true
            },
            function(dirEntry) {
                dirEntry.getFile(
                    filename,
                    {
                        create: true,
                        exclusive: false
                    },
                    function gotFileEntry(fe) {
                        var p = fe.toURL();
                        fe.remove();
                        ft = new FileTransfer();
                        ft.download(
                            encodeURI(path),
                            p,
                            function(entry) {
                                $ionicLoading.hide();
                                $scope.clipSrc = entry.toURL();
                            },
                            function(error) {
                                $ionicLoading.hide();
                                alert("Download Error Source -> " + error.source);
                            },
                            false,
                            null
                        );
                    },
                    function() {
                        $ionicLoading.hide();
                        console.log("Get file failed");
                    }
                );
            }
        );
    },
    function() {
        $ionicLoading.hide();
        console.log("Request for filesystem failed");
    });
}

$scope.load = function(filename) {
    $ionicLoading.show({
      template: 'Loading...'
    });
//$cordovaFile.checkFile(cordova.file.applicationStorageDirectory,"PhysioGuide/"+filename).then(function(result){

            window.requestFileSystem(LocalFileSystem.PERSISTENT, 0, function(fs) {
                fs.root.getDirectory(
                    "PhysioGuide",
                    {
                        create: false
                    },
                    function(dirEntry) {
                        dirEntry.getFile(
                            filename,
                            {
                                create: false,
                                exclusive: false
                            },
                            function gotFileEntry(fe) {
                                $ionicLoading.hide();
                                $scope.clipSrc = fe.toURL();
                                $scope.playVideo();
                            },
                            function(error) {
                                $ionicLoading.hide();
                                console.log("Error getting file");
                                //alert("Error Loading Source -> " + error.source);
                                var alertPopup = $ionicPopup.alert({
                                                                       title: 'File not found!',
                                                                       template: 'Swipe left to download!'
                                                                     });
                            }) ;
                    });
            },
            function() {
                $ionicLoading.hide();
                console.log("Error requesting filesystem");
            });
/*
},function(err){
  $ionicLoading.hide();
  var alertPopup = $ionicPopup.alert({
                                       title: 'File not found!',
                                       template: 'Swipe left to download!'
                                     });
});
*/




}

});


