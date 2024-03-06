const dateInput = document.getElementById('id_cl_date')

const picker = MCDatepicker.create({
  el: '#id_cl_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", () => {
  picker.open()
})