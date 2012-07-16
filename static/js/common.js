jQuery(document).ready(function($){
	/*---------------------------------
		FORM AJAX Handlers
	-----------------------------------*/
	var options = {
        dataType:      'json',          // dataType identifies the expected content type of the server response 
        target:        '#flashmessage', // target element(s) to be updated with server response 
        beforeSubmit:  showRequest,     // pre-submit callback 
        success:       showResponse,    // post-submit callback
        clearForm:     true,            // clear all form fields after successful submit 
        resetForm:     true             // reset the form after successful submit

	};
	
    // bind form using 'ajaxForm' 
    $('#AddNews').ajaxForm(options);

});
// pre-submit callback 
function showRequest(formData, jqForm, options) { 
    // formData is an array; here we use $.param to convert it to a string to display it 
    // but the form plugin does this for you automatically when it submits the data 
    var queryString = $.param(formData); 
 
    // jqForm is a jQuery object encapsulating the form element.  To access the 
    // DOM element for the form do this: 
    // var formElement = jqForm[0]; 
 
    alert('About to submit: \n\n' + queryString); 
 
    // here we could return false to prevent the form from being submitted; 
    // returning anything other than false will allow the form submit to continue 
    return true; 
} 
 
// post-submit callback 
function showResponse(responseText, statusText, xhr, $form)  { 
    // for normal html responses, the first argument to the success callback 
    // is the XMLHttpRequest object's responseText property 
 
    // if the ajaxForm method was passed an Options Object with the dataType 
    // property set to 'xml' then the first argument to the success callback 
    // is the XMLHttpRequest object's responseXML property 
 
    // if the ajaxForm method was passed an Options Object with the dataType 
    // property set to 'json' then the first argument to the success callback 
    // is the json data object returned by the server 
    VK.api('wall.post', {
      message: responseText.message,
      attachments: "photo-442_131166821,http://vk.com/app3025017"
    }, function(data) { alert(data.response) } );


    alert('status: ' + statusText + '\n\nresponseText: \n' + responseText + 
        '\n\nThe output div should have already been updated with the responseText.'); 
}