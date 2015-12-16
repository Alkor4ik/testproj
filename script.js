	form_logon = $('<form name="logon" id="logon_form"><p>Login <input type="text" name="login"></p><p>Password <input type="text" name="password"></p><p><input type="submit" name="login_send" value="Login"></p>');
	$('section > a').on('click', function(){
  	var sections = $('section'),
    		parent = $(this).parent(),
    		body = $('ul', parent);
    // reset all
    sections.removeClass('active');
    $('ul', sections).hide();
    $('form', sections).remove();
    
    // show section
    body.show(300);    
    parent.toggleClass('active');
    $(body).append(form_logon);
  });

