$(function(){
    $('#captcha-img').click(function (event) {
        var self = $(this);
        var src = self.attr('src');
        var newsrc = zlparam.setParam(src, 'xx', Math.random());
        self.attr('src', newsrc);
    });
});

$(function () {
    $("#sms-captcha-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        // 获取手机号码
        var telephone = $("input[name='telephone']").val();
        if(!(/^1[3456789]\d{9}$/.test(telephone))){
            zlalert.alertInfoToast('请输入正确的手机号码！');
            return;
        }
        zlajax.get({
            'url': '/c/sms_captcha?telephone='+telephone,
            'success': function (data) {
                console.log(data);
            }
        });
    });
});