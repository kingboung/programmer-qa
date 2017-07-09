/**
 * Created by Lgpan on 2017/6/26.
 */
$(function(){
    $('html').on('keydown',function(e){//ENTER键搜索
        if(e.keyCode==13){
            $('.btn-default').click();
            e.preventDefault();
        }
    });
    $('.search').on('click',search);//点击按钮搜索

    function search(){
        $('.website').hide();
        var inputText= $.trim($('.form-control').val());
        var req_data= inputText;
        if(inputText!=""){//检测键盘输入的内容是否为空，为空就不发出请求
            $.ajax({
                type: 'POST',
                crossDomain:true,
                url: 'http://127.0.0.1:8000/search',
                cache:false,//不从浏览器缓存中加载请求信息
                data:{'question':req_data},//向服务器端发送的数据
                dataType: 'JSON',//服务器返回数据的类型为json
                success: function (res) {
                    localStorage.setItem('jsonobj1',JSON.stringify(res));
                    if (res.length != 0) {//检测返回的结果是否为空
                        $('.website').show();
                        for (var key in res ){//有结果就改变颜色
                            if (key=="oschina"){
                                $('#idx-oschina a img').attr('src','../static/image/oschina_active.png');
                            }
                            if (key=="zhihu"){
                                $('#idx-zhihu a img').attr('src','../static/image/zhihu_active.png');
                            }
                            if (key=="csdn"){
                                $('#idx-csdn a img').attr('src','../static/image/CSDN_active.png');
                            }
                            if (key=="v2ex"){
                                $('#idx-v2ex a img').attr('src','../static/image/v2ex_active.png');
                            }
                            if (key=="stackoverflow"){
                                $('#idx-stackoverflow a img').attr('src','../static/image/stackoverflow_active.png');
                            }
                        }

                    }
                },
                error:function (XMLHttpRequest, textStatus, errorThrown){
                    console.log(XMLHttpRequest.status + " "+XMLHttpRequest.readyState+" "+textStatus.toString())
                }
            });
        }else{
            alert("输入内容为空！")
        }
    }

        // localStorage.setItem('clickEle','');
        $('#idx-oschina').click(function () {
            localStorage.setItem('clickEle','oschina');
        });
        $('#idx-zhihu').click(function () {
            localStorage.setItem('clickEle','zhihu');
        });
        $('#idx-v2ex').click(function () {
            localStorage.setItem('clickEle','v2ex');
        });
        $('#idx-csdn').click(function () {
            localStorage.setItem('clickEle','csdn');
        });
        $('#idx-stackoverflow').click(function () {
            localStorage.setItem('clickEle','stackoverflow');
        });

});