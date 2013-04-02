
$(document).ready(function(){

	var wChair = $('#Container .workerChair');
	var wCItem = $('#Container .workerChair span');
	var bChair = $('#Container .bossChair');
	var bCItem = $('#Container .bossChair span');
	var textContainer = $('#Container .textContainer');

	var width = $(window).width();
	if (width < 1000) {
	wChair.animate({'right':'8%'},500, function(){	
		wCItem.animate({'top':'80px','opacity':'1'},800, function(){
			bChair.animate({'left':'8%'},1200,function(){
				bCItem.animate({'top':'73px','opacity':'1'},1000, function(){
					textContainer.animate({'bottom':'350px'},800);
				});
			});
		});
	});
		
	}
	else {
	wChair.animate({'right':'30%'},500, function(){	
		wCItem.animate({'top':'80px','opacity':'1'},800, function(){
			bChair.animate({'left':'30%'},1200,function(){
				bCItem.animate({'top':'73px','opacity':'1'},1000, function(){
					textContainer.animate({'bottom':'350px'},800);
				});
			});
		});
	});
	}
	
	var height = $(window).height();
	if (height < 800){
		$('p').css({'margin':'0'})
		textContainer.addClass('lowHeight');
	}

	$('#Container .letsText').click(function(){
		bChair.fadeOut(
			function(){
				wChair.fadeOut(
					function(){
						textContainer.animate({'bottom':'-500px'},function(){
							$(this).fadeOut(
								function(){
									$('#SendFormContainer').fadeIn(function(){
										$('#SendFormContainer').animate({'top':'5%'});
									});
								}
							);
						});
					}
				);	
			}
		);
	});



});
