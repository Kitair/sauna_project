$(function(){
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

    // $(window).resize(function () {
    //     console.log('resize')
    // })

    const showFeedbackForm = $('#show-feedback-form')
    const popupForm = $('.popup-form')
    const feedbackForm = $('.feedback-form')

    popupForm.hide()

    showFeedbackForm.click(function () {
        popupForm.show()
    })

    popupForm.click(function () {
        popupForm.hide()

    })

    feedbackForm.click(function (e) {
        e.stopPropagation()
        popupForm.show()
    })
});

