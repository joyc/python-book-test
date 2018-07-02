// jquery 封装好的 ajax
// 原生的XMLHTTPrequest 相对麻烦
// console.log('coming...')
// 整个文档都加载完成后才执行以下函数
$(function() {
    $('#submit').click(function (event) {
        //阻止默认的提交表单的行为
        event.preventDefault();
        //提交数据前需要先获取表单数据
        var email = $('input[name=email]').val();
        var password = $('input[name=password]').val();
        var csrftoken = $('meta[name=csrf_token]').val();

        $.post({
            'url': '/login/',
            'data': {
                'email': email,
                'password': password,
                'csrf_token': csrftoken
            },
            'success': function (data) {
                console.log(data);
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
});