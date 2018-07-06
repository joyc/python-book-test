$(function () {
    $("#submit").click(function (event) {
        // 阻止默认表单的提交事件
        event.preventDefault();
        // 获取表单元素
        var oldpwdElement = $("input[name=oldpwd]");
        var newpwdElement = $("input[name=newpwd]");
        var newpwd2Element = $("input[name=newpwd2]");
        // 获取表单元素数据
        var oldpwd = oldpwdElement.val();
        var newpwd = newpwdElement.val();
        var newpwd2 = newpwd2Element.val();
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
                console.log(data);
            },
            'fail': function(error){
                console.log(error);
            }
        });
    }); 
});