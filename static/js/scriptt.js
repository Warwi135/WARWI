$(document).ready(function () {
    'use strict';

    var usernameError = true,
        emailError = true,
        passwordError = true,
        passConfirm = true;

    // Label animation
    $('input').focus(function () {
        $(this).siblings('label').addClass('active');
    });


    $('input').blur(function () {
        if ($(this).hasClass('name')) {
            if ($(this).val().length === 0) {
                $(this).siblings('span.error').text('Please type your full name').fadeIn().parent('.form-group').addClass('hasError');
                usernameError = true;
            } else if ($(this).val().length <= 6) {
                $(this).siblings('span.error').text('Please type at least 6 characters').fadeIn().parent('.form-group').addClass('hasError');
                usernameError = true;
            } else {
                $(this).siblings('.error').fadeOut().parent('.form-group').removeClass('hasError');
                usernameError = false;
            }
        }

        if ($(this).hasClass('email')) {
            if ($(this).val().length === 0) {
                $(this).siblings('span.error').text('Please type your email address').fadeIn().parent('.form-group').addClass('hasError');
                emailError = true;
            } else {
                $(this).siblings('.error').fadeOut().parent('.form-group').removeClass('hasError');
                emailError = false;
            }
        }

        if ($(this).hasClass('pass')) {
            if ($(this).val().length < 8) {
                $(this).siblings('span.error').text('Please type at least 8 characters').fadeIn().parent('.form-group').addClass('hasError');
                passwordError = true;
            } else {
                $(this).siblings('.error').fadeOut().parent('.form-group').removeClass('hasError');
                passwordError = false;
            }
        }

        if ($('.pass').val() !== $('.passConfirm').val()) {
            $('.passConfirm').siblings('.error').text("Passwords don't match").fadeIn().parent('.form-group').addClass('hasError');
            passConfirm = true;
        } else {
            $('.passConfirm').siblings('.error').fadeOut().parent('.form-group').removeClass('hasError');
            passConfirm = false;
        }

        if ($(this).val().length > 0) {
            $(this).siblings('label').addClass('active');
        } else {
            $(this).siblings('label').removeClass('active');
        }
    });

    $('a.switch').click(function (e) {
        e.preventDefault();
        $(this).toggleClass('active');

        if ($(this).hasClass('active')) {
            $(this).parents('.form-peice').addClass('switched').siblings('.form-peice').removeClass('switched');
        } else {
            $(this).parents('.form-peice').removeClass('switched').siblings('.form-peice').addClass('switched');
        }
    });

    // ✅ Form submit yang benar (kirim ke Flask jika valid)
    $('form.signup-form').on('submit', function (event) {
    $('.name, .email, .pass, .passConfirm').blur();

    if (usernameError || emailError || passwordError || passConfirm) {
        event.preventDefault();
        return false;
    }

    // Gunakan AJAX agar bisa munculkan alert tanpa reload
    event.preventDefault();
    var form = $(this);
    $.post(form.attr('action'), form.serialize())
        .done(function () {
            alert('Terima Kasih sudah register!');

            // Tampilkan pesan sukses jika kamu mau
            $('.success-msg').fadeIn();

            // Reset form dan pindah ke login
            form[0].reset();
            $('.signup').removeClass('switched');
            $('.login').addClass('switched');
        })
        .fail(function (xhr) {
            alert(xhr.responseText || 'Gagal mendaftar. Coba lagi.');
        });
});

});