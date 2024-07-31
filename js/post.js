$(function(){
	if ($("#selectArtist").length > 0){
		$("#selectArtist").change(function(){
			var value=$(this).val();
			$.ajax({
				url:"/getvideo",
				data:{
					artist: value
				},
				success:function(data){
					currentTime.value=data.time;
					currentDate.value=data.date;
					myvid.innerHTML=data.title;
					myvideo.src="/uploads/"+data.filename;
					myvideo.play();
				}
			})
		});
	}
//$('.carousel').carousel();
$('form').on('submit', function () {
  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
return false;
  }
  $.ajax({
    // Your server script to process the upload
    url: $(this).attr("action"),
    type: $(this).attr("method"),

    // Form data
    data: new FormData($(this)[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    console.log("HEY")
	    console.log(JSON.stringify(data))
	    console.log(JSON.stringify(data.redirect))
window.location=data.redirect ? data.redirect : "/";
},
	  beforeSend: function(){
		         $('.loader').show()
		     },
	  complete: function(){
		         $('.loader').hide();
		    },
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
  });



  
});
