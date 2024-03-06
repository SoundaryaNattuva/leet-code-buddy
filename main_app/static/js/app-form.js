const dateInput = document.getElementById('id_app_date')

const picker = MCDatepicker.create({
  el: '#id_app_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", () => {
  picker.open()
})