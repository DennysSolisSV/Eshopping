/*=============================================
TEMPLATE
=============================================*/

$.ajax({

	url:"/ajax/",
	success:function(response){
		var data = JSON.parse(response)[0]['fields']; /*getting the fields */
		var colorBackground = data.color_background;
		var colorText = data.color_text;
		var topBar = data['top_bar'];
		var topText = data.top_text;
		
		$(".backColor, .backColor a").css({"background": colorBackground,
											"color": colorText})

		$(".topBar, .topBar a").css({"background": topBar, 
			                                       "color": topText})

	}


})