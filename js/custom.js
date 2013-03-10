
$(document).ready(function(){

	var width = $(window).width();
	if (width < 1000) {
	$('#Container .workerChair').animate({'right':'8%'},500, function(){	
		$('#Container .workerChair span').animate({'top':'80px','opacity':'1'},800, function(){
			$('#Container .bossChair').animate({'left':'8%'},1200,function(){
				$('#Container .bossChair span').animate({'top':'73px','opacity':'1'},1000, function(){
					$('#Container .textContainer').animate({'bottom':'350px'},800);
				});
			});
		});
	});
		
	}
	else {
	$('#Container .workerChair').animate({'right':'30%'},500, function(){	
		$('#Container .workerChair span').animate({'top':'80px','opacity':'1'},800, function(){
			$('#Container .bossChair').animate({'left':'30%'},1200,function(){
				$('#Container .bossChair span').animate({'top':'73px','opacity':'1'},1000, function(){
					$('#Container .textContainer').animate({'bottom':'350px'},800);
				});
			});
		});
	});
	}
	
	var height = $(window).height();
	if (height < 800){
		$('p').css({'margin':'0'})
		$('#Container .textContainer').addClass('lowHeight');
	}

});
