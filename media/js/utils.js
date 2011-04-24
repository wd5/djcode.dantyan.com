(function(w){
	var utils = {
		log:function(){
			if( typeof(context) == 'undefined' )
			{
				window.console && console.log && console.log(item);
			}
			else
			{
				window.console && console.log && console.log(context, item);
			}
		},
		rand:function(min, max){
			var argc = arguments.length;
			if (argc === 0) {
				min = 0;
				max = 2147483647;
			} else if (argc === 1) {
				throw new Error('Warning: mt_rand() expects exactly 2 parameters, 1 given');
			}
			return Math.floor(Math.random() * (max - min + 1)) + min;
		}
	};
	
	w.utils = utils;
})(window);
