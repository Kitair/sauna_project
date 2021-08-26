$(function () {
    const datepicker = $("#datepicker")
    const booking = $("#booking")
    const checkbox = $('.checkbox-btn input')

    let a
    datepicker.datepicker({
        minDate: 0,
        // onSelect: function (dateText, inst) {
        //     return a = inst
        // }
    });

    datepicker.change(function () {
        console.log(datepicker.val())
    })

    // let b
    //
    // let getCheckedCheckbox = () => {
    //     for (let i = 0; i < checkbox.length; i++) {
    //         if (checkbox[i].checked) {
    //             b = checkbox[i].nextElementSibling.innerHTML
    //         }
    //     }
    // }
    //
    // booking.click(function () {
    //     getCheckedCheckbox()
    //     a.time = b
    //     console.log(a)
    // })
})