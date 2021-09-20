$(function () {
    const showPopup = $('#show-popup');
    const hidePopup = $('#hide-popup');
    const galleryPopup = $('.gallery-popup')
    const img = $('#carouselExampleControlsNoTouching.carousel.slide .d-block.popup-img')
    const controlPrev = $('#carouselExampleControlsNoTouching.carousel.slide button.carousel-control-prev')
    const controlNext = $('#carouselExampleControlsNoTouching.carousel.slide button.carousel-control-next')

    galleryPopup.hide()

    showPopup.click(function () {
        $('.gallery-popup').show()
    })

    hidePopup.click(function () {
        $('.gallery-popup').hide()
    })

    galleryPopup.click(function () {
        $('.gallery-popup').hide()
    })

    img.click(function (e) {
        e.stopPropagation()
        $('.gallery-popup').show()
    })

    controlPrev.click(function (e) {
        e.stopPropagation()
        $('.gallery-popup').show()
    })

    controlNext.click(function (e) {
        e.stopPropagation()
        $('.gallery-popup').show()
    })

    $(window).click(function (e) {
        const showFeedbackForm = $('#show-feedback-form')
        const popupForm = $('.popup-form')
        const feedbackForm = $('.feedback-form')
        const booking = $('#booking')
        const chooseServices = $('.booking-btn input')
        const datepicker = $("#datepicker")
        const checkbox = $('.choose-time input')


        if (e.target === showFeedbackForm[0]) {
             popupForm.show()
        }

        if (e.target === popupForm[0]) {
            popupForm.hide()
        }

        if (e.target === booking[0]) {
             popupForm.show()
            const date = document.querySelector('.popup-form input[name=data_field]')
            const time = document.querySelector('.popup-form input[name=time_field]')
            const service = document.querySelector('.popup-form input[name=service_field]')

            console.log(service)

            date.value = datepicker.val()

            checkbox.each(function (index, value) {
                console.log(1)
                if(value.checked) {
                    time.value = value.nextElementSibling.innerHTML
                }
            })

            chooseServices.each(function (index, value) {

                if(value.checked) {
                    service.value = value.dataset.name
                }
            })

        }

    })



});

