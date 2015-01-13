angular.module("app.services",[])
	.factory("metaService",function($http){
			
			var metadatas = {};

			metadatas.getData = function(){
				return $http({
					method: 'GET',
					url: 'http://localhost:8081/metaview/json/'
			});
		}
		return metadatas;
	});