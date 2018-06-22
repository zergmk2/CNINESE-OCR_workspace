var url = 'http://127.0.0.1:8001/json';  


var http = require('http');
var querystring = require('querystring');
var options = {
        host: '127.0.0.1', // 请求地址 域名，google.com等..
        port:8001,
        path:'/json', // 具体路径eg:/upload
        method: 'GET', // 请求方式, 这里以post为例
        headers: { // 必选信息,  可以抓包工看一下
            'Content-Type': 'application/json'
        }
    };
    http.get(options, function(res) {
        var resData = "";
        res.on("data",function(data){
            resData += data;
	    console.log(resData);
        });
        
    })
