/**
 * Created by Lgpan on 2017/7/1.
 */
$(function () {
    var clickele = localStorage.getItem('clickEle');
    $('.' + clickele +' a').click();
    var temp = localStorage.getItem('jsonobj1');
    var jsonobj = JSON.parse(temp);
    var question_index = 1;
    $('.glyphicon-home').click(function () {//返回搜索页面
        window.location.href="home";
    });

    search();
    function search() {
        for (var key in jsonobj) {
            for (var i=0; i<jsonobj[key].length;i++) {
                    $('#'+key).append(//为每个问题创建列表框
                        '<a href="#" class="list-group-item" id="question-'+question_index+'">'+jsonobj[key][i].question+'</a>'
                    );
                    $('body').append(//每个问题对应的模态框
                        '<div class="modal fade" id ="modal_question-'+question_index+'"'+ 'tabindex="-1" role="dialog" aria-labelledby="myModalLabel">'+
                        '<div class="modal-dialog modal-lg" role="document">'+
                        '<div class="modal-content">'+
                        '<div class="modal-header">'+
                        '<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>'+
                        '<h4 class="modal-title" id="myModalLabel">'+jsonobj[key][i].question+'</h4>'+
                        '</div>'+
                        '<div class="modal-body">'+
                        '</div>'+
                        '<div class="modal-footer">'+
                        '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>'+
                        '</div>'+
                        '</div>'+
                        '</div>'+
                        '</div>'
                    );
                if(key =="csdn"){//没description的网站
                    for(var j=0;j<jsonobj[key][i].answer.length;j++){
                        var answer_list = jsonobj[key][i].answer;
                        $('#modal_question-'+question_index+' .modal-body').append(
                            '<div class="answer">'+
                            '<div class="wrap">'+
                            '<div class="author">'+answer_list[j].author +'</div>'+
                            '<div class="time">'+ answer_list[j].time+'</div>'+
                            '</div>'+
                            '<br>'+
                            '<div class="content">'+ answer_list[j].content+'</div>'+
                            '</div>'
                        )
                    }
                }
                else{//含description的网站
                    for(var j=0;j<jsonobj[key][i].answer.length;j++){
                        var answer_list = jsonobj[key][i].answer;
                        $('#modal_question-'+question_index+' .modal-body').append(
                            '<div class="answer">'+
                            '<div class="wrap">'+
                            '<div class="author">'+answer_list[j].author +'</div>'+
                            '<div class="time">'+ answer_list[j].time+'</div>'+
                            '</div>'+
                            '<br>'+
                            '<div class="description">'+ jsonobj[key][i].description+'</div>'+
                            '<br>'+
                            '<div class="content">'+ answer_list[j].content+'</div>'+
                            '</div>'
                        )
                    }
                }
                    question_index++;
            }
        }
    }
    $('.list-group-item').click(function () {//点击问题模态框出现
        var que_id = this.id;
        $('#modal_'+que_id).modal('show');
    });

});