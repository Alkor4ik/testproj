$(document).ready(function() {
  
  
  //form_logon = $('<div id="logon_form"><p>Login <input type="text" name="login" id="login"></p><p>Password <input type="text" name="password" id="password"></p><p><button id="go"> Login </button></p></div>');
  form_logon = $('<p><button id="go"> Login </button></p></div>');

  $('section > a').on('click', function() {
    var sections = $('section'),
      parent = $(this).parent(),
      body = $('ul', parent);

    
    // reset all
    sections.removeClass('active');
    $('ul', sections).hide();
    $('div', sections).remove();
    $('#login').empty();
    $('#password').empty(); 
    // show section
    body.show(300);
    parent.toggleClass('active');
    $(body).append(form_logon);
    // Вставляем пароль и логин в контекстное окно 
    $('#go').on('click', function(){
    var login = $('#login').val(),
        password = $('#password').val();
     //alert (login+'\n'+password);
     //$('#modal_form p').append('Логин: ',login, ' Пароль: ', password);

    
    });
    $('#go').click( function(event){ // лoвим клик пo ссылки с id="go"
        event.preventDefault(); // выключaем стaндaртную рoль элементa
        $('#overlay').fadeIn(400, // снaчaлa плaвнo пoкaзывaем темную пoдлoжку
            function(){ // пoсле выпoлнения предъидущей aнимaции
                
                    $('#modal_form').css('display', 'block'); // убирaем у мoдaльнoгo oкнa display: none;
                    $('#modal_form') .animate({opacity: 1, top: '50%'}, 200); // плaвнo прибaвляем прoзрaчнoсть oднoвременнo сo съезжaнием вниз
        });
    });
    /* Зaкрытие мoдaльнoгo oкнa, тут делaем тo же сaмoе нo в oбрaтнoм пoрядке */
    $('#modal_close, #overlay').click( function(){ // лoвим клик пo крестику или пoдлoжке
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,  // плaвнo меняем прoзрaчнoсть нa 0 и oднoвременнo двигaем oкнo вверх
                function(){ // пoсле aнимaции
                    $(this).css('display', 'none'); // делaем ему display: none;
                    $('#overlay').fadeOut(400); // скрывaем пoдлoжку
                    $('#modal_form p').empty(); // очищаем содержимое окна
                }
            );
    });
  });
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