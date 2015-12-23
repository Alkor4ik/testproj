jQuery(document).ready(function() {
	$('#reg_submit').click(function(){
		console.log('run main script');
		var name = $('#name').val(),
			phone = $('#phone').val(),
			email = $('#email').val(),
			massage = $('#massage').html(),
			delivery = false,
			fail = false;
		if (name == ""){
			fail = 'Вы не ввели имя'
		}
		else if(phone == ""){
			fail = 'Вы не ввели телефон'
		}
		else if(email == ""){
			fail = 'Вы не ввели email'
		}
		else if($("#trust").is(":not(:checked)")){
			fail = 'Вы не доверяете нам?'
		}
		else if ($("#delivery").is(":checked")){
			delivery = true
		}
		if (fail){alert(fail)}
		else{
			sessionStorage.setItem('name',name);
			sessionStorage.setItem('phone',phone);
			sessionStorage.setItem('email',email);
			sessionStorage.setItem('massage',massage);
			sessionStorage.setItem('delivery',delivery);
			window.location.replace('form.html');
		}
	});
});