angular.module("app.controllers",[])
	.controller("metaController", function($scope,metaService){
		$scope.json_data = [];
		$scope.val = 10;
		metaService.getData().success(function(response){
			$scope.json_data = response;
		});
	}
);