var flag = 0;

function openCalender() {
    if (!flag) {
        $("#datepicker-1").datepicker("show");
        flag = 1;
    } else {
        $("#datepicker-1").datepicker("hide");
        flag = 0;
    }
    //$("#datepicker-1").datepicker();
}
$(function() {
    $("#datepicker-1").datepicker().datepicker("setDate", new Date());
    dateFormat: 'YYYY-MM-DD'
});