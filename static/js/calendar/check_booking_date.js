$(function () {
    const datepicker = $("#datepicker");
    const timeBtn = $('.choose-time input');
    const serviceBtn = $('.booking-btn label input');

    Array.from(serviceBtn).forEach(elem => elem.addEventListener('click', getBdDate))

    function getCheckedBtn() {
        for (let i = 0; i < serviceBtn.length; i++) {
            if (serviceBtn[i].checked) {
                return serviceBtn[i].dataset.name
            }
        }
    }

    function getBdDate() {
        let data = {
            btnData: datepicker.val(),
            btnService: getCheckedBtn()
        }
        $.ajax({
            type: 'GET',
            url: 'check_booking_date',
            data: data,
            dataType: 'json',
            success: function (data) {
                if (data.data !== false) {
                    timeBtn.each(function (index, value) {
                        value.removeAttribute('disabled')
                    })
                    data.data.map(elem => {
                        timeBtn.each(function (index, value) {
                            if (value.parentElement.lastElementChild.innerHTML === elem) {
                                return value.setAttribute('disabled', true)
                            }
                        })
                    })
                } else {
                    timeBtn.each(function (index, value) {
                        value.removeAttribute('disabled')
                    })

                }
                timeBtn.each(function (index, value) {
                    if (!value.disabled) {
                        value.checked = true
                        return false
                    }
                })
            },
        })
    }

    datepicker.change(getBdDate);

    datepicker.before(getBdDate);
})
