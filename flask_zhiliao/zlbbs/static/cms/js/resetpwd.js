/**
 * Created by hynev on 2017/11/25.
 */

$(function () {
    $("#submit").click(function (event) {
        // event.preventDefault 阻止按钮默认的提交表单事件
        event.preventDefault();
        // 获取表单元素
        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwd2E = $("input[name=newpwd2]");
        // 获取表单元素数据
        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        // 1. 需在模板meta中渲染csrf-token
        // 2. 在ajax请求头中设置X-CSRFtoken (zlcsrf.js)
        zlajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                // code ==  200
                // code != 200
                if (data['code'] == 200){
                    zlalert.alertSuccessToast("密码修改成功！")
                    // 成功后清楚数据
                    oldpwdE.val("");
                    newpwdE.val("");
                    newpwd2E.val("");
                } else {
                    var message = data['message'];
                    zlalert.alertInfo(message)
                }
            },
            'fail': function (error) {
                zlalert.alertNetworkError();
            }
        });
    });
});